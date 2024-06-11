import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

listing_url = "https://appbrewery.github.io/Zillow-Clone/"
google_form = "https://forms.gle/82zM784zaxZDr4EL9"
google_form_address_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
google_form_price_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
google_form_url_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
google_form_submit_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'
google_form_another_xpath = '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'
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
#Initialize Selenium Webdriver Settings
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#Open Link
driver.get(google_form)

#Manipulate the form
for index in range(len(property_price_list)):
    driver.find_element(By.XPATH, value=google_form_address_xpath).send_keys(property_address_list[index])
    driver.find_element(By.XPATH, value=google_form_price_xpath).send_keys(property_price_list[index])
    driver.find_element(By.XPATH, value=google_form_url_xpath).send_keys(property_url_list[index])
    driver.find_element(By.XPATH, value=google_form_submit_xpath).click()
    elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, google_form_another_xpath)))
    driver.find_element(By.XPATH, value=google_form_another_xpath).click()


