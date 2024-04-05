import sys
import os
from pdf_to_image import pdf_to_image
from extract_figure import extract_figure
from extract_figures_info import extract_figure_info
import detect

def main(folder_path: str):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # list all files in the folder
        for filename in os.listdir(folder_path):
            name_stem, name_suffix = os.path.splitext(filename)
            file_path = os.path.join(folder_path, filename)
            img_source_path, root_path = pdf_to_image(file_path)
            #recognize figures using yolov5 
            detect.run(weights="yolov5x_extract_figure.pt", source=img_source_path, imgsz=(800, 640), save_txt=True, name=name_stem+"_detect_result", project=root_path)
            #extract figures
            extract_figure(name_stem)
            #extract figure information
            extract_figure_info(name_stem, filename)
            
    else:
        print(f'{folder_path} does not exist or is not a folder.')    


if __name__ == "__main__":
    folder_path = sys.argv[1]
    print(folder_path)
    main(folder_path)
