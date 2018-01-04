import praw
from reddit_instance import *

search_terms = ["crypto", "bitcoin", "crypto currency", "ethereum", "crypto trade", "altcoin"]
subreddits = []
text_file = open("subreddits.txt","w")

for search in search_terms:
    for sub in reddit.subreddits.search(search):
        if sub not in subreddits:
            subreddits.append(sub.display_name)
            text_file.write(sub.display_name + '\n')

print("Final subreddits list:")
print(subreddits)
