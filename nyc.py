from nyc_trends import nyc_trends
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
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

full1_dict = {}
for i in nyc_trends:
  trends1 = i["trends"]
  for i in trends1:
    name1 = i["name"]
    volume1 = i["tweet_volume"]
    if volume1 == None:
      volume1 = 0
    full1_dict[name1] = volume1
    pairs = full1_dict.items()
  filtered_dict = {key: value for key, value in pairs if value > 20000}  
print(filtered_dict)

wordcloud = WordCloud(colormap='prism',background_color='white')

wordcloud = wordcloud.generate_from_frequencies(filtered_dict)

plt.imshow(wordcloud)
plt.show()
print("Done")