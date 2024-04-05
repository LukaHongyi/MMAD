import sys
import json
from dataclasses import dataclass
from pathlib import Path
from PIL import Image
import fitz
import os
import pytesseract
from PIL import Image


@dataclass
class TextBlock:
    x1: float
    y1: float
    x2: float
    y2: float
    text: str


def extract_figure(paper_name: str):
    figure_index = 1
    detect_result_folder = paper_name + "_detect_result"
    path = os.path.join("yolov5_master/data/path", paper_name)
    path = Path(path)
    out_path = Path(os.path.join("output/image_files", paper_name))
    json_file_path = Path(os.path.join("output/json_dataset", f"{paper_name}.json"))
    if not out_path.exists():
        out_path.mkdir()
    for text_file in (path / detect_result_folder / "labels").glob("*.txt"):
        image_file = path / f"images/{text_file.name[:-3]}png"
        image = Image.open(str(image_file))
        pdf_file = Path(path / text_file.name[:-8])
        page_index = int(text_file.name[-7:-4])
        #Using fitz package to extracting text blocks from a paper
        pdf_doc = fitz.open(str(pdf_file))
        pdf_page = pdf_doc[page_index]
        text_blocks = pdf_page.get_text('blocks') 
        fig_blocks = [TextBlock(b[0], b[1], b[2], b[3], b[4]) for b in text_blocks if (b[4].lower().startswith("fig") or b[4].lower().startswith("tab"))]

        with open(str(text_file), encoding="utf-8") as f:
            lines = f.readlines()
        count = 0
        for line in lines:
            items = line.strip().split(" ")
            x, y, w, h = float(items[1]), float(items[2]), float(items[3]), float(items[4])
            x1 = x - w / 2
            y1 = y - h / 2
            x2 = x + w / 2
            y2 = y + h / 2
            if items[0] == "1" or items[0] == "0":  # label: "table": 0, "figure": 1
                out_image_file = f"{out_path}/{image_file.name[:-4]}_{count:02}.png"

                with open(json_file_path, "r") as json_file:
                    data = json.load(json_file)

                # Extracted figures data (modify this based on your extraction results)
                extracted_figures = [
                    {
                        "figure{}_url".format(figure_index): f"{image_file.name[:-4]}_{count:02}.png",
                        "figure{}_caption".format(figure_index): "",
                        "figure{}_info".format(figure_index): [
                        ]
                    },
                    # Add more extracted figures as needed...
                ]

                w, h = image.width, image.height
                image_bbox = x1 * w, y1 * h, x2 * w + 10, y2 * h

                w, h = pdf_page.rect.width, pdf_page.rect.height
                pdf_bbox = x1 * w, y1 * h, x2 * w, y2 * h
                caption = find_caption(fig_blocks, pdf_bbox)
                croped_image = image.crop(image_bbox)
                croped_image.save(out_image_file)  
                # Process the rotated tables
                if items[0] == "0":
                    k = pytesseract.image_to_osd(croped_image, output_type='dict')
                    if(k["rotate"] == 0):
                        croped_image.save(out_image_file)  
                    else:
                        rotated_croped_image = croped_image.rotate(-90, expand=True)
                        rotated_croped_image.save(out_image_file)  
                else:
                    croped_image.save(out_image_file)             
                if caption is not None:
                    extracted_figures[0]["figure{}_caption".format(figure_index)] = caption.text.encode("utf-8", "replace").decode().replace("\n", "")
            
            # Create the "figures" attribute if not already present
            if "figures" not in data:
                data["figures"] = []
                
            # Add the extracted figures data to the existing "figures" list
            data["figures"].extend(extracted_figures)
            # Save the modified JSON back to the file
            with open(json_file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
            count += 1
            figure_index+=1

    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
    if 'figures' not in data:
        data["figures"] = []
    with open(json_file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

# Function of locating the captions near figures
def find_caption(blocks: list[TextBlock], bbox: tuple):
    x1, y1, x2, y2 = bbox
    nearest_block = None
    for b in blocks:
        gap_y2 = abs(b.y1 - y2)  # text block bbox
        gap_y1 = abs(b.y2 - y1)
        gap_x2 = abs(b.x1 - x2)
        gap_x1 = abs(b.x2 - x1)
        cx = (b.x1 + b.x2) / 2
        cy = (b.y1 + b.y2) / 2
        # gap: 50 change it as we need
        if ((0 < gap_y1 < 50 or 0 < gap_y2 < 50) and x1 <= cx <= x2) or ((0 < gap_x1 < 50 or 0 < gap_x2 < 50) and y1 <= cy <= y2):
            if nearest_block:
                min_nearest_block = min(abs(nearest_block.y1 - y2), abs(nearest_block.y2 - y1), abs(nearest_block.x1 - x2), abs(nearest_block.x2 - x1))
            min_cur_block = min(abs(b.y1 - y2), abs(b.y2 - y1), abs(b.x1 - x2), abs(b.x2 - x1))
            if nearest_block is None or min_nearest_block > min_cur_block:
                nearest_block = b    
           
    return nearest_block