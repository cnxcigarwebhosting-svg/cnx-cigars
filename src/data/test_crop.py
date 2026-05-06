import cv2
import numpy as np
import os

img_path = "/Users/pnwemd/Desktop/Websites/cnx-cigars/menu/Cigar menu_page-0001.jpg"
img = cv2.imread(img_path)

if img is None:
    print("Could not read image.")
    exit()

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define range for brown/orange colors (the cigar)
# Brown/Orange is typically: Hue 0-30, Saturation > 50, Value > 20
lower_brown = np.array([0, 40, 20])
upper_brown = np.array([40, 255, 255])

mask = cv2.inRange(hsv, lower_brown, upper_brown)

# Find contours
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"Found {len(contours)} contours")
for i, cnt in enumerate(contours):
    x, y, w, h = cv2.boundingRect(cnt)
    # Cigars are long and thin. Width > 100, Height < 200
    if w > 100 and h > 20 and w > h * 2:
        print(f"Possible cigar at: x={x}, y={y}, w={w}, h={h}")
        
