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
for trend in nyc_trends:
  trends = trend["trends"]
  df = pd.DataFrame(trends)
  #sorted_nyc = sorted(df)
  sorted_nyc = sorted(df, reverse=True)
  print(sorted_nyc)

#2) Create a Word Cloud of all topics with over 20,000 tweet volume. The size of the word (topic)
#should be based on their tweet volume.