import pandas as pd
import requests
from bs4 import BeautifulSoup
"""
OPEN THIS IS ANY ID TO USE THIS :-)
scraping is taking date from web using python
pip install beautifulsoup4
pip install requests
pip install pandas
"""

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=26.01067000000006&lon=-80.16025999999994#.YE5MmJ0zZPY')
soup = BeautifulSoup(page.content,'html.parser')
#print(soup.find_all('a'))
week = soup.find(id='seven-day-forecast-body')
#print(week)

items = week.find_all(class_='tombstone-container')
#print(items[0])

"""
print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())
"""

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
tempratures = [item.find(class_='temp').get_text() for item in items]

"""
print(period_names)
print(short_descriptions)
print(tempratures)
"""

weather_stuff = pd.DataFrame(
    {'period': period_names,
    'short_descriptions': short_descriptions,
    'tempretures': tempratures,
    })

print(weather_stuff)

weather_stuff.to_csv('weather.csv')

#04:32:00