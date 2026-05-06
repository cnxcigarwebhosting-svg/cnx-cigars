import cv2
import numpy as np
import os
import glob

out_dir = "/Users/pnwemd/Desktop/Websites/cnx-cigars/public/cigars"
crops = glob.glob(os.path.join(out_dir, "*.jpg"))
# Ignore any _test.jpg
crops = [c for c in crops if not c.endswith("_test.jpg")]

processed = 0
for img_path in crops:
    img = cv2.imread(img_path)
    if img is None: continue
    
    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Range for brown/orange/yellow (cigar colors)
    lower_brown = np.array([0, 40, 20])
    upper_brown = np.array([40, 255, 255])
    
    mask = cv2.inRange(hsv, lower_brown, upper_brown)
    
    # Clean up noise
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Find the largest contour (presumably the cigar)
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        
        # Only crop if it's reasonably cigar-sized
        if w > 50 and h > 10:
            # We can add a margin
            margin = 5
            x1 = max(0, x - margin)
            y1 = max(0, y - margin)
            x2 = min(img.shape[1], x + w + margin)
            y2 = min(img.shape[0], y + h + margin)
            
            cropped = img[y1:y2, x1:x2]
            cv2.imwrite(img_path, cropped) # Overwrite
            processed += 1

print(f"Processed and tightly cropped {processed} out of {len(crops)} images.")
