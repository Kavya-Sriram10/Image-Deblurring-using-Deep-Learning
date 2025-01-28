import cv2
import os
from tqdm import tqdm

src_dir = 'C:/Users/srira/Downloads/Image blur/Image Deblurring App/test_data'
images = os.listdir(src_dir)
dst_dir = 'C:/Users/srira/Downloads/Image blur/Image Deblurring App/test_data/gaussian_blurred'

for image_name in tqdm(images, total=len(images)):
    img_path = os.path.join(src_dir, image_name)
    # Load the image
    img = cv2.imread(img_path)
    
    # Check if image is loaded successfully
    if img is None:
        print(f"Error: Unable to load image {image_name}")
        continue

    # add gaussian blurring
    blur = cv2.GaussianBlur(img, (51, 51), 0)
    
    # Write the blurred image to the destination directory
    cv2.imwrite(os.path.join(dst_dir, image_name), blur)

print('DONE')