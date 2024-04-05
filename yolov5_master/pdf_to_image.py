from pathlib import Path
from pdf2image import convert_from_path
import os
import shutil

# Function of converting a pdf file into images
def pdf_to_image(pdf_path: str):
    images = convert_from_path(pdf_path)
    cur_file_name = os.path.basename(pdf_path)
    name_stem, name_suffix = os.path.splitext(cur_file_name)
    out_path = os.path.join("yolov5_master/data/path", name_stem)
    image_out_path = out_path + "/images"
    delete_files_in_folder(image_out_path)
    os.makedirs(image_out_path, exist_ok=True)
    #for testing, can delete it later
    shutil.copy(pdf_path, os.path.join(out_path, cur_file_name))
    for i, image in enumerate(images):
        image_path = os.path.join(image_out_path, f'{cur_file_name}_{i:03}.png')
        image.save(image_path, 'PNG')
    
    return image_out_path, out_path


def delete_files_in_folder(folder_path):
    # ensure the folder exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # list all files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            # if it's a file, delete it
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                print(f'{file_path} is not a file.')
    else:
        print(f'{folder_path} does not exist or is not a folder.')
