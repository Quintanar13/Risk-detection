# Import necessary libraries
import cv2
import os

#--------------------------------------------------------------------
# Dataset preprocessing

# Specify the source and destination paths
source_folder = 'Dataset_cd/test/dogs'
destination_folder = 'Dataset_post/test/dogs_post'

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Define the desired size
desired_size = (512, 512)

# Iterate through each file in the source folder
for filename in os.listdir(source_folder):
    # Ensure the file is an image
    if filename.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        # Construct the full file path
        filepath = os.path.join(source_folder, filename)

        # Read the image
        image = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Resize the image to the desired size
        resized_image = cv2.resize(gray_image, desired_size)

        # Save the resized grayscale image to the destination folder
        dest_path = os.path.join(destination_folder, filename)
        cv2.imwrite(dest_path, resized_image)