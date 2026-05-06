import os
import glob
from PIL import Image

brain_dir = "/Users/pnwemd/.gemini/antigravity/brain/c7dd2792-ed6c-4990-accf-6af43eceb2a2/"
images = glob.glob(os.path.join(brain_dir, "*.jpg"))
for img_path in images:
    with Image.open(img_path) as img:
        print(f"{os.path.basename(img_path)}: {img.size}")
