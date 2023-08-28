#This script convert .heic images into png, using multithread as default (see line 37)
#To use it, copy the script in the folder where you have all the heic file and run with:
#python3 convert-heic-to-png.py


from PIL import Image
import pyheif
import os
import concurrent.futures

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

        image_filename = os.path.splitext(os.path.basename(heic_path))[0] + f'.{image_format}'
        image_path = os.path.join(destination_folder, image_filename)

        image.save(image_path, format=image_format)
        print(f"Converted {heic_path} to {image_path}")
    except Exception as e:
        print(f"Error converting {heic_path}: {e}")

def main():
    source_folder = os.getcwd()  # Use the current working directory as the source folder
    destination_folder = os.path.join(source_folder, "converted_images")
    os.makedirs(destination_folder, exist_ok=True)

    heic_files = [filename for filename in os.listdir(source_folder) if filename.lower().endswith('.heic')]

    image_format = input("Enter the desired image format (png or jpg): ").lower()
    if image_format not in ('png', 'jpg'):
        print("Invalid image format choice. Please choose 'png' or 'jpg'.")
        return
		
	#if you want to specify a fixed number of threads use the following:
    #with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for heic_file in heic_files:
            heic_path = os.path.join(source_folder, heic_file)
            executor.submit(convert_heic_to_image, heic_path, destination_folder, image_format)

if __name__ == "__main__":
    main()
