import os
import csv
def count_files():
    path = r"C:\Users\KIIT\Desktop\podhai\Btech Project\Stock_Prediction\ophl_dataset_creation\ophl_datasets"
    files_list = os.listdir(path)
    total_dataset_count = 0
    for files in files_list:
        csv_file = open(
            "C:\\Users\\KIIT\\Desktop\\podhai\\Btech Project\\Stock_Prediction\\ophl_dataset_creation\\ophl_datasets\\"+files)
        reader = csv.reader(csv_file)
        lines = len(list(reader)) - 1
        total_dataset_count = total_dataset_count + lines
    print("\nTotal OPHL data collected till now => ",total_dataset_count)
