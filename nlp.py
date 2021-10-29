# -*- coding: utf-8 -*-

import requests
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# 1. Scrit that pulls 50 companies and purposes

names = []
purposes = []

for i in range(0, 50):
    get_resp = requests.get("http://3.85.131.173:8000/random_company")

    y=(get_resp.text.partition("Name:")[2])
    name=(y.partition("<")[0])
    names.append(name)

    x=(get_resp.text.partition("Purpose:")[2])
    purpose=(x.partition("<")[0])
    purposes.append(purpose)
    



data = pd.DataFrame(data = {'Names': names, 'Purpose': purposes})
print(data)

data.to_csv (r'luke_50cos.csv', index = False, header=True)

# 2. Combining various outputs into 1 (with a theoretical txt import)

anton=pd.read_csv('anton.csv')
neil=pd.read_csv('web_scrape_output.csv')
anton = anton.iloc[: , 1:]
neil = neil.iloc[: , 1:]
anton1=pd.read_csv('anton.txt')
anton1 = anton1.iloc[: , 1:]

anton = anton.rename({'Company': 'Names', 'Purpose': 'Purpose'}, axis='columns')
neil = neil.rename({'Name': 'Names', 'Purpose': 'Purpose'}, axis='columns')


combined= [data,anton,neil]
result=pd.concat(combined)


# 3. 

analyzer = SentimentIntensityAnalyzer()
x = []

for col in result.Purpose:    
    
    x.append(analyzer.polarity_scores(col)["compound"])

result['Sentiment']=x

result.sort_values('Sentiment')