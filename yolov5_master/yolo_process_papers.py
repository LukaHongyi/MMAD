import os
import sys


yolo_master_path = '/katana/xhy/fetch_papers/yolov5_master'  # Update this with the actual path
folder_path = "/katana/xhy/fetch_papers/output/pdf_files"
# Get an iterator of directory entries (files and directories)
count = 0
error_count = 0
sys.path.append(yolo_master_path)

from run_single_file import run_single_file

# Process a file and count the success returns
def process_file(args):
    global count
    global error_count
    count += 1
    folder_path, file_name = args
    print(f"Processing {file_name}")
    print(f"Processing {count}")
    result = run_single_file(folder_path, file_name)
    if result == "error":
        error_count += 1
        print(f"error: {error_count}/{count}")
    print(f"{file_name} finished")
    print(f"finished {count}")

def main():
    start_num, end_num= sys.argv

    with os.scandir(folder_path) as entries:
        # Filter out only the files from the iterator
        file_names = [(folder_path, entry.name) for entry in entries if entry.is_file()][int(start_num):int(end_num)]
    print(len(file_names))
    # Process all papers
    for file_name in file_names:
        process_file(file_name)

    print("finished")


if __name__ == "__main__":
    main()
    
