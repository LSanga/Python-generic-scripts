#This script convert .heic images into png or jp(e)g, using multithread as default (see line "with concurrent")
#JPEG and JPG are the same format but both input are accepted to avoid mistakes. In any case the resulting files will be saved as .jpg
#To use it, copy the script in the folder where you have all the heic file and run with:
#python3 convert-heic-images.py

from PIL import Image
import pyheif
import os
import concurrent.futures
from tqdm import tqdm

def convert_heic_to_image(heic_path, destination_folder, image_format):
    try:
        heif_file = pyheif.read(heic_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )

        image_filename = os.path.splitext(os.path.basename(heic_path))[0]
        if image_format == 'png':
            image_path = os.path.join(destination_folder, f"{image_filename}.png")
            image.save(image_path, format='PNG')
        elif image_format in ('jpeg', 'jpg'):  # Allow both 'jpeg' and 'jpg'
            image_path = os.path.join(destination_folder, f"{image_filename}.jpg")
            image.save(image_path, format='JPEG')
            
        return heic_path  # Return the path of the converted image
    except Exception as e:
        print(f"Error converting {heic_path}: {e}")
        return None

def main():
    source_folder = os.getcwd()  # Use the current working directory as the source folder
    destination_folder = os.path.join(source_folder, "converted_images")
    os.makedirs(destination_folder, exist_ok=True)

    heic_files = [filename for filename in os.listdir(source_folder) if filename.lower().endswith('.heic')]

    image_format = input("Enter the desired image format (png, jpeg, or jpg): ").lower()
    if image_format not in ('png', 'jpeg', 'jpg'):
        print("Invalid image format choice. Please choose 'png', 'jpeg', or 'jpg'.")
        return

    # Create a ThreadPoolExecutor and use a list comprehension to submit tasks
    #if you want to specify a fixed number of threads use the following:
    #with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(convert_heic_to_image, os.path.join(source_folder, heic_file), destination_folder, image_format) for heic_file in heic_files]

        # Create a progress bar using tqdm
        with tqdm(total=len(results), desc="Converting") as pbar:
            for future in concurrent.futures.as_completed(results):
                if future.result() is not None:
                    pbar.update(1)

if __name__ == "__main__":
    main()
