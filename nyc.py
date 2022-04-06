from hashlib import new
from types import new_class

from numpy import full
from nyc_trends import nyc_trends
from pathlib import Path
from wordcloud import WordCloud
import imageio
import matplotlib.pyplot as plt
import pandas as pd
from textblob import TextBlob
from operator import itemgetter

#1) Using this information, create a bar chart of the top 10 topics based on their corresponding
# tweet volume.
full_list = []
for i in nyc_trends:
  trends = i["trends"]
  for i in trends:
    name = i["name"]
    volume = i["tweet_volume"]
    if volume == None:
      volume = 0
    new_list = [name,volume]
    full_list.append(new_list)
  sorted_list = sorted(full_list, key=itemgetter(1),reverse=True)
  top_10 = sorted_list[:10]
  df = pd.DataFrame(top_10,columns = ['Name','Volume'])
  print(df)

df.plot.bar(x='Name', y='Volume', legend=False)

plt.gcf().tight_layout()
plt.show()

#2) Create a Word Cloud of all topics with over 20,000 tweet volume. The size of the word (topic)
#should be based on their tweet volume.