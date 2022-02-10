import os
import csv

current_location = os.path.abspath(os.getcwd())
def count_files():
    path = current_location+"\\ophl_datasets"
    files_list = os.listdir(path)
    total_dataset_count = 0
    for files in files_list:
        csv_file = open(
            current_location+"\\ophl_datasets\\"+ files)
        reader = csv.reader(csv_file)
        lines = len(list(reader)) - 1
        total_dataset_count = total_dataset_count + lines
    print("\nTotal OPHL data collected till now => ",total_dataset_count)

def create_folder():
    
    directory = "ophl_datasets"
    parent_dir = current_location
    isExist = os.path.exists(parent_dir+"\\"+directory)
    if isExist == False:
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
