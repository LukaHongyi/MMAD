# MMAD

MMAD is a multi-modal dataset which for academic data processing. It contains open access paper's meta-data and visual information. This repository contains the datasets generation tool. 

If you want to process one paper, then you can run the **run.py** in the **yolov5_master** with the command:

```shell
python3 run.py [your_paper_folder_path]
```

It can automatically extract all the figures and tables in the paper and extract those visual information's  surrounding descriptive text extracted from the article’s paragraphs.

To get the meta-data of one paper, you can utilize the **get_details_from_doi** function in  **doi_api_update_data.py** in the **utl**.

The figure and table extract modal uses YOLOv5, the weight file is uploaded to the dropbox:

https://www.dropbox.com/scl/fo/3eap70fy3hjf06xi2zob6/ACCvny-AWIEogr0_Sg4jDiw?rlkey=pghkksshy55lugbqtcn4oypyu&st=tvvqhvm6&dl=0

The YOLO model weight refers to the weight in the following link:

https://github.com/hshindo/extract_tables_figures.git
