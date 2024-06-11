import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

listing_url = "https://appbrewery.github.io/Zillow-Clone/"
google_form = "https://forms.gle/82zM784zaxZDr4EL9"
response = requests.get(url=listing_url)

soup = BeautifulSoup(response.text, 'html.parser')
properties = soup.find_all(name="div", attrs={'class':"StyledPropertyCardDataWrapper"})
# print(properties)
property_price_list = []
property_url_list = []
property_address_list = []

for property in properties:
    property_price_list.append(property.find("span").text)
    property_url_list.append(property.find("a").get('href'))
    property_address_list.append(property.find("address").text.strip())

# print(property_price_list)
# print(property_url_list)
# print(property_address_list)

properties_dict = {}

for index in range(len(property_price_list)):
    properties_dict[index] = {
        "Address": property_address_list[index],
        "Price": property_price_list[index],
        "URL": property_url_list[index]
    }

# print(properties_dict)