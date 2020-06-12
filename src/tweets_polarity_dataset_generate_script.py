states_list = [
  'Andhra Pradesh',
  'Arunachal Pradesh',
  'Assam',
  'Bihar',
  'Chhattisgarh',
  'Goa',
  'Gujarat',
  'Haryana',
  'Himachal Pradesh',
  'Jammu & Kashmir',
  'Jharkhand',
  'Karnataka',
  'Kerala',
  'Madhya Pradesh',
  'Maharashtra',
  'Manipur',
  'Meghalaya',
  'Mizoram',
  'Nagaland',
  'Odisha',
  'Punjab',
  'Rajasthan',
  'Sikkim',
  'Tamil Nadu',
  'Telangana',
  'Tripura',
  'Uttarakhand',
  'Uttar Pradesh',
  'West Bengal',
]


months_list = ['11', '12', '01', '02', '03', '04', '05']

from textblob import TextBlob
import pandas as pd
import re
def clean_data(string):
  return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", string).split())


for state in states_list:
  for month in months_list:
    file_name = f"data/{state}_{month}_tweets.csv"

    try:
      tweets = pd.read_csv(file_name)
    except:
      print(state, month)
      continue

    tweets['Tweets'] = tweets['Tweets'].apply(clean_data)
    
    lst = []
    
    for index in tweets.index:
      polarity = TextBlob(tweets['Tweets'][index]).sentiment.polarity
      lst.append(polarity)
    
    tweets['Polarity']=lst

    lst=[]
    for index in tweets.index:
      if tweets['Polarity'][index]>0:
        lst.append("Positive")
      elif tweets["Polarity"][index]<0:
        lst.append("Negative")
      else:
        lst.append("Neutral")

    tweets['Sentiments']=lst

    tweets.to_csv("output/" + file_name[5:-10] + "polarity.csv", index=False)

