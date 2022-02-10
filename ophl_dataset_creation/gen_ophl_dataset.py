from api import *
from data_count import *
create_folder()
count_files()

# Ener you API Key here
api_key = ""

# This is your data symbol
data_symbol = "BINANCE:BTCUSDT"

generate_ophl_dataset(api_key, data_symbol)
