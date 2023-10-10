# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Youtube homepage
driver.get("https://www.youtube.com")
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
#search_bar = driver.find_element("id","search")
#search_bar.send_keys("hello adele")

search_bar = driver.find_element(by = 'name', value = 'search_query')  # You can change this to the appropriate locator
search_bar.clear()  # Clear any existing text in the search bar
#search_bar.send_keys('hello')


#search_bar = driver.find_element(by='Xpath',value = '//*[@id="search-input"]')
search_bar.send_keys("hello adele")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "hello adele" in driver.title


song_link = driver.find_element(by='xpath', value= '//*[@id="video-title"]/yt-formatted-string')
song_link.click()
time.sleep(50)

driver.close()
