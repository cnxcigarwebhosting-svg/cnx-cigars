import cv2
import numpy as np
import os
import glob

out_dir = "/Users/pnwemd/Desktop/Websites/cnx-cigars/public/cigars"
crops = glob.glob(os.path.join(out_dir, "*.jpg"))
crops = [c for c in crops if not c.endswith("_test.jpg")]

processed = 0
for img_path in crops:
    img = cv2.imread(img_path)
    if img is None: continue
    
    # Create an alpha channel (all opaque initially)
    b_channel, g_channel, r_channel = cv2.split(img)
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255
    
    # We will make any black-ish pixel transparent
    # Black is roughly R<30, G<30, B<30
    black_mask = (r_channel < 40) & (g_channel < 40) & (b_channel < 40)
    alpha_channel[black_mask] = 0
    
    # Also remove any white/grey text noise
    white_mask = (r_channel > 200) & (g_channel > 200) & (b_channel > 200)
    alpha_channel[white_mask] = 0
    
    # Merge into BGRA
    img_bgra = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
    
    png_path = img_path.replace(".jpg", ".png")
    cv2.imwrite(png_path, img_bgra)
    
    # Delete the old jpg
    os.remove(img_path)
    processed += 1

print(f"Processed and converted {processed} images to transparent PNGs.")
