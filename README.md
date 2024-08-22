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

Additionally, here is the results of the figure/table caption extract sampling test, 100 random samples of 1000 papers from the dataset each time：

| INDEX | EXTRACTED captionS | NONE VALUE CAPTIONS |
| ----- | ------------------ | ------------------- |
| 1     | 6946               | 369                 |
| 2     | 6743               | 405                 |
| 3     | 6296               | 413                 |
| 4     | 6674               | 354                 |
| 5     | 7004               | 447                 |
| 6     | 6561               | 453                 |
| 7     | 6284               | 445                 |
| 8     | 6340               | 498                 |
| 9     | 7346               | 477                 |
| 10    | 6528               | 354                 |
| 11    | 6495               | 440                 |
| 12    | 6972               | 471                 |
| 13    | 6102               | 463                 |
| 14    | 6034               | 403                 |
| 15    | 6024               | 411                 |
| 16    | 6809               | 430                 |
| 17    | 6363               | 418                 |
| 18    | 6273               | 436                 |
| 19    | 5911               | 397                 |
| 20    | 6428               | 433                 |
| 21    | 6180               | 467                 |
| 22    | 6167               | 456                 |
| 23    | 6220               | 418                 |
| 24    | 6730               | 347                 |
| 25    | 6647               | 432                 |
| 26    | 6090               | 447                 |
| 27    | 6379               | 384                 |
| 28    | 6689               | 432                 |
| 29    | 6159               | 423                 |
| 30    | 6334               | 399                 |
| 31    | 6588               | 423                 |
| 32    | 6223               | 406                 |
| 33    | 6126               | 432                 |
| 34    | 7179               | 446                 |
| 35    | 6267               | 389                 |
| 36    | 6105               | 387                 |
| 37    | 6835               | 385                 |
| 38    | 6515               | 434                 |
| 39    | 6310               | 452                 |
| 40    | 5954               | 467                 |
| 41    | 6741               | 447                 |
| 42    | 7615               | 511                 |
| 43    | 6724               | 382                 |
| 44    | 5991               | 367                 |
| 45    | 7429               | 451                 |
| 46    | 6329               | 422                 |
| 47    | 6051               | 405                 |
| 48    | 6014               | 486                 |
| 49    | 6716               | 388                 |
| 50    | 6071               | 390                 |
| 51    | 6087               | 364                 |
| 52    | 6018               | 387                 |
| 53    | 6088               | 422                 |
| 54    | 6315               | 436                 |
| 55    | 6867               | 414                 |
| 56    | 6695               | 416                 |
| 57    | 7613               | 536                 |
| 58    | 5954               | 340                 |
| 59    | 6114               | 404                 |
| 60    | 6433               | 424                 |
| 61    | 6055               | 347                 |
| 62    | 6176               | 409                 |
| 63    | 6837               | 409                 |
| 64    | 6207               | 384                 |
| 65    | 6318               | 405                 |
| 66    | 6410               | 427                 |
| 67    | 6796               | 448                 |
| 68    | 6560               | 408                 |
| 69    | 7058               | 377                 |
| 70    | 6994               | 394                 |
| 71    | 6232               | 438                 |
| 72    | 6209               | 363                 |
| 73    | 6127               | 432                 |
| 74    | 6077               | 380                 |
| 75    | 6063               | 395                 |
| 76    | 6037               | 449                 |
| 77    | 7262               | 459                 |
| 78    | 6512               | 370                 |
| 79    | 6733               | 428                 |
| 80    | 6266               | 430                 |
| 81    | 5885               | 416                 |
| 82    | 6344               | 417                 |
| 83    | 6342               | 486                 |
| 84    | 6496               | 440                 |
| 85    | 6963               | 482                 |
| 86    | 7233               | 405                 |
| 87    | 6947               | 410                 |
| 88    | 6712               | 428                 |
| 89    | 6098               | 451                 |
| 90    | 8270               | 456                 |
| 91    | 6507               | 439                 |
| 92    | 6051               | 451                 |
| 93    | 6931               | 489                 |
| 94    | 6358               | 420                 |
| 95    | 6124               | 395                 |
| 96    | 5915               | 403                 |
| 97    | 6458               | 438                 |
| 98    | 6064               | 410                 |
| 99    | 6306               | 377                 |
| 100   | 6170               | 433                 |
