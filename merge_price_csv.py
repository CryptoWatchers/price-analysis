# @Author: Varoon Pazhyanur <varoon>
# @Date:   Jan-03-2018
# @Filename: merge_price_csv.py
# @Last modified by:   varoon
# @Last modified time: Jan-03-2018
import pandas as pd
import glob

frames = []
for file in glob.glob("cryptocurrencypricehistory/*.csv"):
    frames.append(pd.read_csv(file))
    currency_name = file.split("/")[1].split("_")[0]

    #add constant col of currency name to each frame
    frames[len(frames)-1]["Currency"] = [currency_name] * len(frames[len(frames)-1])

res = pd.concat(frames, join = "outer")
res.to_csv("combined_prices.csv", sep = ",")
