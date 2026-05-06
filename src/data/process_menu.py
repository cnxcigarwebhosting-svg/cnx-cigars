import os
import glob
import subprocess
import json
import re
from PIL import Image

menu_dir = "/Users/pnwemd/Desktop/Websites/cnx-cigars/menu"
ocr_bin = "/Users/pnwemd/Desktop/Websites/cnx-cigars/ocr"
out_dir = "/Users/pnwemd/Desktop/Websites/cnx-cigars/public/cigars"
json_path = "/Users/pnwemd/Desktop/Websites/cnx-cigars/src/data/cigars.json"

os.makedirs(out_dir, exist_ok=True)
images = sorted(glob.glob(os.path.join(menu_dir, "*.jpg")))

all_cigars = []

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

for img_idx, img_path in enumerate(images):
    print(f"Processing {os.path.basename(img_path)}...")
    
    # Run OCR
    result = subprocess.run([ocr_bin, img_path], capture_output=True, text=True)
    text = result.stdout
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    # Identify cigar blocks by finding "THB"
    thb_indices = [i for i, line in enumerate(lines) if "THB" in line]
    
    if not thb_indices:
        print(f"No THB found in {os.path.basename(img_path)}")
        continue
        
    page_cigars = []
    
    for i, thb_idx in enumerate(thb_indices):
        # Name is usually the line before THB
        if thb_idx > 0:
            name = lines[thb_idx - 1]
            if name == "CNX CIGAR®" or "CIGARS" in name or name == "*" or name == "H" or len(name) < 3:
                # Sometimes it misses, look one more up
                if thb_idx > 1:
                    name = lines[thb_idx - 2]
        else:
            name = f"Unknown Cigar {img_idx}_{i}"
            
        # Price is numbers from THB line
        price_match = re.search(r'(\d+)', lines[thb_idx])
        price = int(price_match.group(1)) if price_match else 0
        
        # End of this block is the next Name (which is next_thb_idx - 1), or end of lines
        if i + 1 < len(thb_indices):
            end_idx = thb_indices[i+1] - 1
        else:
            end_idx = len(lines)
            
        block_lines = lines[thb_idx+1:end_idx]
        block_text = " ".join(block_lines)
        
        # Avoid including footer text
        footer_markers = ["Prices exclude", "VAT", "Nimmana Haeminda", "Chiang Mai", "ONLINE SALE"]
        for marker in footer_markers:
            if marker in block_text:
                block_text = block_text.split(marker)[0]
                
        # Parse specs
        strength = "Medium"
        format_str = "Robusto"
        time_str = "45 mins"
        
        strength_match = re.search(r'Strength:\s*([^FSLR]+)', block_text, re.IGNORECASE)
        if strength_match:
            strength = strength_match.group(1).strip()
            
        format_match = re.search(r'(?:Format|Size):\s*([^LRS]+)', block_text, re.IGNORECASE)
        if format_match:
            format_str = format_match.group(1).strip()
            
        time_match = re.search(r'Smoking time:\s*([^\.]+)', block_text, re.IGNORECASE)
        if time_match:
            time_str = time_match.group(1).strip()
            
        # Notes is everything else roughly
        notes = block_text
        notes = re.sub(r'Strength:.*?(Format|Size):.*?(Length|Ring|Smoking).*?(mins?|min|m)', '', notes, flags=re.IGNORECASE)
        notes = re.sub(r'(Length|Ring).*?(mins?|min|m)', '', notes, flags=re.IGNORECASE)
        notes = notes.strip(".,;: ")
        if not notes:
            notes = "A premium hand-rolled cigar with exceptional flavor and construction."
            
        cigar_id = slugify(name)
        
        page_cigars.append({
            "id": cigar_id,
            "name": name,
            "category": "Cuban Classics", # Default
            "price": price,
            "strength": strength,
            "format": format_str,
            "smokingTime": time_str,
            "notes": notes,
            "featured": False
        })
        
        all_cigars.append(page_cigars[-1])
        
    # Crop images for this page
    try:
        img = Image.open(img_path)
        N = len(page_cigars)
        if N > 0:
            # Page is 1024h. Usable area ~200 to 900 -> 700px height.
            # Split 700px into N chunks
            start_y = 200
            end_y = 900
            chunk_h = (end_y - start_y) / N
            for i, cigar in enumerate(page_cigars):
                y1 = int(start_y + i * chunk_h)
                y2 = int(start_y + (i + 1) * chunk_h)
                # Ensure we only get the cigar, let's tightly crop the center
                # Cigars are usually around y_center of this chunk
                yc = (y1 + y2) // 2
                crop_y1 = max(start_y, yc - 45)
                crop_y2 = min(end_y, yc + 45)
                cigar_crop = img.crop((100, crop_y1, 624, crop_y2))
                cigar_crop.save(os.path.join(out_dir, f"{cigar['id']}.jpg"))
    except Exception as e:
        print(f"Failed to crop {img_path}: {e}")

# Try to merge with existing data
if os.path.exists(json_path):
    with open(json_path, 'r') as f:
        existing_data = json.load(f)
    
    # We will override with new ones to ensure we have all 26 pages, but maybe keep some featured flags
    existing_map = {c["id"]: c for c in existing_data}
    for c in all_cigars:
        if c["id"] in existing_map:
            c["featured"] = existing_map[c["id"]].get("featured", False)
            c["category"] = existing_map[c["id"]].get("category", c["category"])
            
with open(json_path, 'w') as f:
    json.dump(all_cigars, f, indent=2)

print(f"Successfully processed {len(all_cigars)} cigars from {len(images)} pages.")
