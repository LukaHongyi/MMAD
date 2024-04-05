import sys
import os
from pdf_to_image import pdf_to_image
from extract_figure import extract_figure
from extract_figures_info import extract_figure_info
import detect
import json
from pathlib import Path


# Function of processing one paper
def run_single_file(folder_path: str, filename: str):
    model_path = os.path.join(os.path.dirname(__file__), 'yolov5x_extract_figure.pt')   
    name_stem, name_suffix = os.path.splitext(filename)
    json_file_path = Path(os.path.join("output/json_dataset", f"{name_stem}.json"))
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
    if 'figures' in data and len(data["figures"]) > 0:
        data["figures"] = []
    
    with open(json_file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

    file_path = os.path.join(folder_path, filename)
    print(file_path)
    img_source_path, root_path = pdf_to_image(file_path)
    #recognize figures using yolov5 
    detect.run(weights=model_path, source=img_source_path, imgsz=(640, 640), save_txt=True, name=name_stem+"_detect_result", project=root_path)
    extract_figure(name_stem)            # extract figures
    result = extract_figure_info(name_stem, filename, file_path)            # extract figure related text in the pdf paper
    return result
