import pandas as pd
import os
import glob

pwd = os.path.abspath(os.getcwd())
dest = pwd+"\\candle_train_dataset"

if os.path.isdir(dest):
    print("\nFolder already present...\nProceeding...\n\n")
else :
    os.mkdir(dest, mode=0o666)
    print(f"\nCreated the folder : '{dest}'\n\n")


csv_list = glob.glob("./*.csv")
print(f"Total of {len(csv_list)} csv files found ....\nBegining Conversion ....\n")
c = 1
for file in csv_list:
    df = pd.read_csv(file)
    name_df = df["Name"]
    name_list = []
    l = len(name_df.index) -3
    for i in range(l):
        temp = []
        temp.append(name_df[i])
        temp.append(name_df[i+1])
        temp.append(name_df[i+2])
        temp.append(name_df[i+3])
        name_list.append(temp)
    new_df = pd.DataFrame(name_list, columns = ['tm2', 'tm1', 't', 'tp1'])
    new_df.to_csv(os.path.join(dest,file),index = False)
    print(f"{c} files created!")
    c+=1
print("All Done!!!")
