from PIL import Image
import os
import glob

brain_dir = "/Users/pnwemd/.gemini/antigravity/brain/c7dd2792-ed6c-4990-accf-6af43eceb2a2/"
images = sorted(glob.glob(os.path.join(brain_dir, "*.jpg")))

out_dir = "/Users/pnwemd/Desktop/Websites/cnx-cigars/public/cigars"
os.makedirs(out_dir, exist_ok=True)

# 1. Extract Logo from the first image
img0 = Image.open(images[0])
logo = img0.crop((362 - 80, 50, 362 + 80, 210))
logo.save("/Users/pnwemd/Desktop/Websites/cnx-cigars/public/logo.png")

# 2. Extract Cigars (we will just take 3 slices from each page)
# Page width is 724, let's crop from x=100 to x=624 (width 524)
# Cigars are roughly at y=220-300, y=460-530, y=700-780.
y_crops = [(220, 300), (450, 530), (700, 780)]

cigar_idx = 0
for idx, img_path in enumerate(images):
    img = Image.open(img_path)
    for i, (y1, y2) in enumerate(y_crops):
        cigar_crop = img.crop((100, y1, 624, y2))
        cigar_crop.save(os.path.join(out_dir, f"cigar_{idx}_{i}.jpg"))
