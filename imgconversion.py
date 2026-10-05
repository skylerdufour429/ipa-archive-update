from PIL import Image
import os
import logging

# Set up logging
logging.basicConfig(filename='conversion_errors.log', level=logging.ERROR)

# Path to the root folder containing subfolders with PNG files
root_folder_path = 'C:/Users/kiren/Desktop/Documents/testing script/data'

# Traverse all directories and subdirectories
for root, dirs, files in os.walk(root_folder_path):
    # Process each PNG file
    for file_name in files:
        if file_name.lower().endswith('.png'):
            file_path = os.path.join(root, file_name)
            try:
                # Open PNG file
                with Image.open(file_path) as img:
                    # Convert to JPG
                    jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
                    jpg_file_path = os.path.join(root, jpg_file_name)
                    img.convert('RGB').save(jpg_file_path, 'JPEG')
                    # Log successful conversion
                    logging.info(f'Converted {file_path} to {jpg_file_path}')
                    
                    # Optionally delete the original PNG file
                    os.remove(file_path)
                    
            except Exception as e:
                # Log the error
                logging.error(f'Error converting {file_path}: {e}')

print('Conversion completed. Errors logged in conversion_errors.log.')
