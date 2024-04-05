import requests
from pathlib import Path
import re
import json
import os
import shutil

# Function of deleting a folder and its inside contents
def delete_folder(path):
    try:
        shutil.rmtree(path)
        print(f"Folder '{path}' and its contents have been deleted.")
    except OSError as e:
        print(f"Error deleting '{path}': {e}")

# Function of extracting the figure related text in a pdf paper
def extract_figure_info(paper_name: str, file_name: str, file_path: str):
    url = 'http://Grobid_docker_server'  # This is the Grobid docker server, replace with your URL
    folder_path = os.path.join("yolov5_master/data/path", paper_name) # Replace with your temporary folder path for yolo processing
    json_file_path = Path(os.path.join("output/json_dataset", f"{paper_name}.json")) # Replace with your json folder path
    with open(file_path, 'rb') as file:
        files = {'file': file}

        response = requests.post(url, files=files)


    try:
        text_data = json.loads(response.text)

        text_paragraphs = text_data["pdf_parse"]["body_text"] # Extract text from pdf paper using Grobid


        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)


        for index, figure in enumerate(data["figures"]): #Iterate figure captions from the current json file
            cur_text = figure["figure{}_caption".format(index+1)]  # You can modify this based on your data structure
            if cur_text != "":
                match = re.search(r'(\b\w+)\s*\.?\s*(\d+)(?=\D|$)', cur_text) # For each figure caption, set the regular expression rule

                if match:
                    figure_type, figure_index = match.group(1), match.group(2)
                    # Set the regular expression for potential cases
                    if figure_type.lower().startswith("fig"):
                        pattern = rf"(Figure|Fig\.?\s*)\s*\.?\s*({figure_index})(?=\D|$)"
                    else:
                        pattern = rf"({figure_type}s?)\s*\.?\s*({figure_index})(?=\D|$)"
                    count = 0
                    cur_figure_info = {}
                    # Save the figure related text in the json file
                    for item in text_paragraphs:
                        text_match = re.search(pattern, item["text"], re.IGNORECASE)
                        if text_match:
                            count += 1
                            cur_figure_info["figure{}_info_{}".format(index+1, count)] = item["text"]
                            
                    figure["figure{}_info".format(index+1)].append(cur_figure_info)
        # Update the json file
        with open(json_file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        # Delete the temporary folder
        delete_folder(folder_path)    
        return "success"
    except Exception as e:
        print(f"An error occurred while processing an article: {str(e)}") 
        return "error"         
