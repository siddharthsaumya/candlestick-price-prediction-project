from api import *
from data_count import *
create_folder()
count_files()
api_key = "c7df68iad3i911lpfnng"
try:
    generate_ophl_dataset(api_key, "BINANCE:BTCUSDT")
except KeyError:
    print("\nStopped due to some error. Starting again ASAP.")
    generate_ophl_dataset(api_key, "BINANCE:BTCUSDT")
