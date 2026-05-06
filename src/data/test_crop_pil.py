from PIL import Image
import os

img_path = "/Users/pnwemd/Desktop/Websites/cnx-cigars/menu/Cigar menu_page-0001.jpg"
img = Image.open(img_path).convert('RGB')
pixels = img.load()
width, height = img.size

cigars = []
# Scan rows
in_cigar = False
cigar_start = 0

for y in range(height):
    brown_pixels = 0
    for x in range(width):
        r, g, b = pixels[x, y]
        # Check if pixel is "cigar colored" (brown/orange)
        # and NOT white (warning labels) or gray
        if r > g > b and r > 40 and (r - g) > 15:
            brown_pixels += 1
            
    if brown_pixels > 50:
        if not in_cigar:
            in_cigar = True
            cigar_start = y
    else:
        if in_cigar:
            in_cigar = False
            cigar_end = y
            # If the segment is tall enough
            if cigar_end - cigar_start > 20:
                cigars.append((cigar_start, cigar_end))

print(f"Found {len(cigars)} potential cigars.")
for y1, y2 in cigars:
    print(f"y1: {y1}, y2: {y2}")

