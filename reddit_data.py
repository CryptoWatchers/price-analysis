# @Author: Varoon Pazhyanur <varoon>
# @Date:   Jan-02-2018
# @Filename: reddit_data.py
# @Last modified by:   varoon
# @Last modified time: Jan-02-2018

import praw
import pandas as pd
import csv
from reddit_instance import * #Reddit instance is declared as "reddit"

search_terms = ["cryptocurrency",
                "cryptocurrencies",
                "cryptocurrency exchange",
                "cryptocurrency market",
                "crypto",
                "cryptocurrency value",
                "cryptocurrency news",
                "new cryptocurrency",
                "mining cryptocurrency",
                "bitcoin",
                "cryptocurrency",
                 "ethereum",
                 "crypto trade",
                 "altcoin",
                 "btc",
                 "eth",
                 "ether"]

subreddits = []
for search in search_terms:
    for sub in reddit.subreddits.search(search):
        if sub not in subreddits:
            subreddits.append(sub)

cols =['title','gilded','author','selftext','url','subreddit', 'created_utc', 'score', 'num_comments', 'view_count', 'ups', 'downs', 'link_flair_css_class']
rows = []

for subreddit in subreddits:
    print(subreddit.display_name)
    try:    
        for sub in subreddit.submissions(start=1356998400, end=1514764799):
            rows.append([str(sub.title),
                        str(sub.gilded),
                        str(sub.author),
                        str(sub.selftext),
                        str(sub.url),
                        str(sub.subreddit),
                        str(sub.created_utc),
                        str(sub.score),
                        str(sub.num_comments),
                        str(sub.view_count),
                        str(sub.ups),
                        str(sub.downs),
                        str(sub.link_flair_css_class)])
    except:
        print("Error getting submisison")
        pass

res2 = pd.DataFrame(rows, columns = cols) 
res2.to_csv("jan1_2013-dec31_2017_subreddits.csv", sep = ",")
