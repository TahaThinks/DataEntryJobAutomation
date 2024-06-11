import requests
from bs4 import BeautifulSoup

listing_url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url=listing_url)

soup = BeautifulSoup(response.text, 'html.parser')
properties = soup.find_all(name="div", attrs={'class':"StyledPropertyCardDataWrapper"})
print(properties)
property_price_list = []
property_url_list = []
property_address_list = []

for property in properties:
    property_price_list.append(property.find("span").text)

# print(property_price_lists)