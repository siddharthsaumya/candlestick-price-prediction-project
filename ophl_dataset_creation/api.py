import subprocess
import time
from csv import writer
import csv
import os

def install(name):
    try:
        subprocess.call(['pip', 'install', name],stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print("Package "+str(name)+" installed successfully :)")
    except ImportError:
        print("Faced some error while installing "+str(name)+" package :(")

file_name = open("requirements.txt", "r")
Content = file_name.read()
PackagesList = Content.split("\n")
for i in PackagesList:
    install(i)

import datetime
import finnhub

def generate_ophl_dataset(apiKey,dataSymbol):
    finnhub_client = finnhub.Client(apiKey)

    fields = ['time', 'open', 'close', 'high','low']

    current_time = datetime.datetime.now()
    ts = int(current_time.timestamp())
    data_symbol = dataSymbol
    data_symbol = data_symbol.replace(":", "-")

    csv_name = "ophl_datasets//"+str(ts)+"_"+data_symbol+".csv"

    with open(csv_name, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
    
    print("\nStarting data collection process...\n")
    i = 0
    while True:
        
        hloc_data = finnhub_client.crypto_candles(dataSymbol, '1', ts-60, ts)

        close_price = hloc_data['c'][0]
        open_price = hloc_data['o'][0]
        high_price = hloc_data['h'][0]
        low_price = hloc_data['l'][0]
        current_timestamp = ts+19740

        price_data_list = [current_timestamp,open_price, close_price, high_price, low_price]

        with open(csv_name, 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(price_data_list)
        print("Entry "+str(i+1)+" for " + str(current_timestamp) + " is updated in CSV file successfully!!")
        i+=1
        time.sleep(60)
        current_time = datetime.datetime.now()
        ts = int(current_time.timestamp())
