# a : 0=(o>c) | 1=(o<c) | 2=(o=c)
# b : 0=(h=l) | 1=(h>l)
# c : 0 = 0 to .25 | 1 = .25 to .5 | 2 = .5 to .75 | 3 = .75 to 1 | 4 = High=Low        candle to body ratio
# d : 0 = 0 to .333 | 1 = .334 to .666 | 2 = .667 to 1 | 3 = min(Open,Close) = Low      upper shadow to lower shadow ratio
# e : 0 = mean[n] - mean[n-1] = 0 | 1 = mean[n] - mean[n-1] > 0 | 2 = mean[n] - mean[n-1] < 0

import pandas as pd
import os
import glob

df = pd.read_csv("Merged.csv")

df["Name"] = ""

# df["CTB Ratio"] = 1
# for i in df.index:
#     df.at[i,"CTB Ratio"] =  float(abs((df["Open"][i]-df["Close"][i]))/(df["High"][i]-df["Low"][i]))

for i in df.index:
    curr_name = str(df["Name"][i])
    if df["Open"][i] > df["Close"][i]:
        curr_name+= "a0"
        df.at[i,"Name"] = curr_name
    elif df["Open"][i] < df["Close"][i]:
        curr_name+= "a1"
        df.at[i,"Name"] = curr_name
    else :
        curr_name+= "a2"
        df.at[i,"Name"] = curr_name

for i in df.index:
    curr_name = str(df["Name"][i])
    if df["High"][i] == df["Low"][i]:
        curr_name+= "b0"
        df.at[i,"Name"] = curr_name
    else:
        curr_name+= "b1"
        df.at[i,"Name"] = curr_name

for i in df.index:
    curr_name = str(df["Name"][i])
    if df["High"][i] == df["Low"][i]:
        curr_name+= "c4"
        df.at[i,"Name"] = curr_name
    else :
        if float(abs((df["Open"][i]-df["Close"][i]))/(df["High"][i]-df["Low"][i])) <= 0.25:
            curr_name+= "c0"
            df.at[i,"Name"] = curr_name
        elif float(abs((df["Open"][i]-df["Close"][i]))/(df["High"][i]-df["Low"][i])) > 0.25 and float(abs((df["Open"][i]-df["Close"][i]))/(df["High"][i]-df["Low"][i])) <= 0.5:
            curr_name+= "c1"
            df.at[i,"Name"] = curr_name
        elif float(abs((df["Open"][i]-df["Close"][i]))/(df["High"][i]-df["Low"][i])) > 0.5 and float(abs((df["Open"][i]-df["Close"][i]))/(df["High"][i]-df["Low"][i])) <= 0.75:
            curr_name+= "c2"
            df.at[i,"Name"] = curr_name
        else :
            curr_name+= "c3"
            df.at[i,"Name"] = curr_name

for i in df.index:
    curr_name = str(df["Name"][i])
    if min(df["Open"][i],df["Close"][i]) == df["Low"][i]:
        curr_name+= "d3"
        df.at[i,"Name"] = curr_name
    else :
        if float(df["High"][i]-max(df["Open"][i],df["Close"][i])/(min(df["Open"][i],df["Close"][i])-df["Low"][i])) <= 0.333:
            curr_name+= "d0"
            df.at[i,"Name"] = curr_name
        elif float(df["High"][i]-max(df["Open"][i],df["Close"][i])/(min(df["Open"][i],df["Close"][i])-df["Low"][i])) > 0.333 and float(df["High"][i]-max(df["Open"][i],df["Close"][i])/(min(df["Open"][i],df["Close"][i])-df["Low"][i])) < 0.667:
            curr_name+= "d1"
            df.at[i,"Name"] = curr_name
        else :
            curr_name+= "d2"
            df.at[i,"Name"] = curr_name

for i in df.index:
    curr_name = str(df["Name"][i])
    if i == 0:
        curr_name+= "e0"
        df.at[i,"Name"] = curr_name
    else:
        diff_mean = (df["Open"][i]+df["Close"][i])/2 - (df["Open"][i-1]+df["Close"][i-1])/2
        if diff_mean == 0:
            curr_name+= "e0"
            df.at[i,"Name"] = curr_name
        elif diff_mean > 0:
            curr_name+= "e1"
            df.at[i,"Name"] = curr_name
        else:
            curr_name+= "e2"
            df.at[i,"Name"] = curr_name

df.to_csv("Merged_and_named.csv")
