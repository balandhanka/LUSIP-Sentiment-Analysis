!pip install GetOldTweets3

query_list = ['corona', 'COVID', 'COVID-19',]


location_list = [
    ['Andhra Pradesh',140],
    ['Arunachal Pradesh',101],
    ['Assam',98],
    ['Bihar',111],
    ['Chhattisgarh',129],
    ['Goa',21],
    ['Gujarat',155],
    ['Haryana',74],
    ['Himachal Pradesh',83],
    ['Jammu & Kashmir',165],
    ['Jharkhand',99],
    ['Karnataka',154],
    ['Kerala',69],
    ['Madhya Pradesh',195],
    ['Maharashtra',195],
    ['Manipur',52],
    ['Meghalaya',53],
    ['Mizoram',51],
    ['Nagaland',43],
    ['Odisha',138],
    ['Punjab',79],
    ['Rajasthan',205],
    ['Sikkim',30],
    ['Tamil Nadu',127],
    ['Telangana',117],
    ['Tripura',36],
    ['Uttarakhand',81],
    ['Uttar Pradesh',173],
    ['West Bengal',104]
]

location_list = [(location + ', India', within) for location, within in location_list]


date_list = [
    ("2019-11-01", "2019-11-30"), # Nov, 2019
    ("2019-12-01", "2019-12-31"), # Dec, 2019
    ("2020-01-01", "2020-01-31"), # Jan, 2020
    ("2020-02-01", "2020-02-29"), # Feb, 2020
    ("2020-03-01", "2020-03-31"), # Mar, 2020
    ("2020-04-01", "2020-04-30"), # Apr, 2020
    ("2020-05-01", "2020-05-30"), # May, 2020  
]


import time
import GetOldTweets3 as got
import pandas as pd


for location, within in location_list:
  for since_date, until_date in date_list:
    text_tweets = []

    for i in range(len(query_list)):
      query_text = query_list[i]
      tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query_text).setNear(location).setSince(since_date).setUntil(until_date).setLang("en").setWithin(f"{within}mi")
      
      try:
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
      except:
        print("Error at", i)
        time.sleep(3)
        i -= 1
        continue

      text_tweets.extend( [tweet.text for tweet in tweets] )

    df = pd.DataFrame({"Tweets": text_tweets}, columns=['Tweets',])
    df = df.drop_duplicates().reset_index(drop=True)

    df.to_csv(f"{location[:-7]}_{since_date[5:7]}_tweets.csv", index=False)

  print(location, "done")


