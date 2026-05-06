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

# Helper to find cigar blobs in image
def find_cigar_blobs(img):
    # Convert to RGB
    img = img.convert('RGB')
    width, height = img.size
    pixels = img.load()
    
    # We will scan rows and find segments with brown pixels
    segments = []
    in_segment = False
    start_y = 0
    
    for y in range(height):
        brown_count = 0
        min_x = width
        max_x = 0
        for x in range(width):
            r, g, b = pixels[x, y]
            # Brown/Orange heuristic: R > G > B, and not too dark or too white
            # Warnings are white (r,g,b > 200) or red (r>150, g,b<50)
            if r > g + 10 and g > b and r > 30 and r < 230:
                brown_count += 1
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                
        if brown_count > 30: # Need a solid line of brown pixels
            if not in_segment:
                in_segment = True
                start_y = y
                seg_min_x = min_x
                seg_max_x = max_x
            else:
                seg_min_x = min(seg_min_x, min_x)
                seg_max_x = max(seg_max_x, max_x)
        else:
            if in_segment:
                in_segment = False
                end_y = y
                if end_y - start_y > 30: # Must be at least 30px tall
                    segments.append({
                        "y1": start_y, "y2": end_y, 
                        "x1": seg_min_x, "x2": seg_max_x,
                        "yc": (start_y + end_y) / 2
                    })
    return segments

for img_idx, img_path in enumerate(images):
    print(f"Processing {os.path.basename(img_path)}...")
    
    # Run OCR
    result = subprocess.run([ocr_bin, img_path], capture_output=True, text=True)
    text = result.stdout
    
    # Parse lines: "Y|Text"
    parsed_lines = []
    for line in text.split('\n'):
        if not line.strip(): continue
        parts = line.split('|', 1)
        if len(parts) == 2:
            try:
                y_norm = float(parts[0])
                # CoreGraphics Y is 0 at bottom, 1 at top. We want 0 at top to match image.
                y_norm = 1.0 - y_norm
                parsed_lines.append((y_norm, parts[1].strip()))
            except:
                pass
                
    # Sort top to bottom
    parsed_lines.sort(key=lambda x: x[0])
    
    # Identify cigar blocks by finding "THB"
    thb_items = [(i, item) for i, item in enumerate(parsed_lines) if "THB" in item[1] or "BAHT" in item[1]]
    
    if not thb_items:
        print(f"No price found in {os.path.basename(img_path)}")
        continue
        
    page_cigars = []
    img = Image.open(img_path)
    img_h = img.size[1]
    
    for i, (thb_idx, thb_item) in enumerate(thb_items):
        y_thb = thb_item[0]
        
        # Name is usually right above THB
        name = "Unknown"
        if thb_idx > 0:
            name = parsed_lines[thb_idx - 1][1]
            if name == "CNX CIGAR®" or "CIGARS" in name or len(name) < 4:
                if thb_idx > 1:
                    name = parsed_lines[thb_idx - 2][1]
                    
        # Clean bad names
        if "warning" in name.lower() or "smoking" in name.lower() or "health" in name.lower():
            continue
            
        # Price is numbers from THB line
        price_match = re.search(r'(\d+)', thb_item[1])
        price = int(price_match.group(1)) if price_match else 0
        
        # Determine block boundaries
        block_start_idx = thb_idx + 1
        if i + 1 < len(thb_items):
            block_end_idx = thb_items[i+1][0] - 1
            # But the next cigar's name is right before it, so end before that name
            block_end_idx -= 1
        else:
            block_end_idx = len(parsed_lines)
            
        block_lines = []
        for j in range(block_start_idx, block_end_idx):
            if j < len(parsed_lines):
                # Ignore warning labels at the bottom (usually very low Y)
                if parsed_lines[j][0] > 0.9: continue
                block_lines.append(parsed_lines[j][1])
                
        block_text = " ".join(block_lines)
        
        # Ignore footer/warning blocks
        if "Rauchen" in block_text or "stop smoking" in block_text.lower():
            continue
            
        strength = "Medium"
        format_str = "Robusto"
        time_str = "45 mins"
        
        strength_match = re.search(r'Strength:\s*([^FSLR]+)', block_text, re.IGNORECASE)
        if strength_match: strength = strength_match.group(1).strip()
            
        format_match = re.search(r'(?:Format|Size):\s*([^LRS]+)', block_text, re.IGNORECASE)
        if format_match: format_str = format_match.group(1).strip()
            
        time_match = re.search(r'Smoking time:\s*([^\.]+)', block_text, re.IGNORECASE)
        if time_match: time_str = time_match.group(1).strip()
            
        notes = block_text
        notes = re.sub(r'Strength:.*?(Format|Size):.*?(Length|Ring|Smoking).*?(mins?|min|m)', '', notes, flags=re.IGNORECASE)
        notes = re.sub(r'(Length|Ring).*?(mins?|min|m)', '', notes, flags=re.IGNORECASE)
        notes = notes.strip(".,;: ")
        if not notes: notes = "A premium hand-rolled cigar."
            
        cigar_id = slugify(name)
        
        # We know the Y coordinate of the text. Let's convert to pixel space
        pixel_y = y_thb * img_h
        
        page_cigars.append({
            "id": cigar_id,
            "name": name,
            "category": "Premium", # Temp, will run categorize.py later
            "price": price,
            "strength": strength,
            "format": format_str,
            "smokingTime": time_str,
            "notes": notes,
            "featured": False,
            "pixel_y": pixel_y
        })
        
    # Now map the text blocks to the image blobs!
    blobs = find_cigar_blobs(img)
    
    for cigar in page_cigars:
        # Find closest blob in Y coordinate
        closest_blob = None
        min_dist = float('inf')
        for blob in blobs:
            dist = abs(blob["yc"] - cigar["pixel_y"])
            if dist < min_dist:
                min_dist = dist
                closest_blob = blob
                
        if closest_blob and min_dist < 200: # Within 200 pixels
            # Tightly crop the blob!
            # Give a 10px margin
            cy1 = max(0, closest_blob["y1"] - 10)
            cy2 = min(img_h, closest_blob["y2"] + 10)
            cx1 = max(0, closest_blob["x1"] - 20)
            cx2 = min(img.size[0], closest_blob["x2"] + 20)
            
            cigar_crop = img.crop((cx1, cy1, cx2, cy2))
            cigar_crop.save(os.path.join(out_dir, f"{cigar['id']}.jpg"))
        else:
            print(f"Could not find matching crop for {cigar['name']} (Y={cigar['pixel_y']})")
            
        # Clean up the pixel_y before saving to JSON
        del cigar["pixel_y"]
        all_cigars.append(cigar)
        
with open(json_path, 'w') as f:
    json.dump(all_cigars, f, indent=2)

print(f"Successfully fully rebuilt database: {len(all_cigars)} cigars.")
