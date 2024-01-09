from django.db import models
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


client = MongoClient('mongodb+srv://srishtikashyap1234:<F8Cn6jOkP6lsBqvd>@cluster0.6somnkm.mongodb.net/?retryWrites=true&w=majority')
db = client['job_listings']

# Parsing and creating xml data
from lxml import etree as et

# Store data as a csv file written out
from csv import writer

# In general to use with timing our function calls to Indeed
import time

# Assist with creating incremental timing for our scraping to seem more human
from time import sleep

# Dataframe stuff
import pandas as pd

# Random integer for more realistic timing for clicks, buttons and searches during scraping
from random import randint


import selenium

# Selenium 4:

from selenium import webdriver

# Starting/Stopping Driver: can specify ports or location but not remote access
from selenium.webdriver.chrome.service import Service as ChromeService

# Manages Binaries needed for WebDriver without installing anything directly
from webdriver_manager.chrome import ChromeDriverManager

# Allows searchs similar to beautiful soup: find_all
from selenium.webdriver.common.by import By

# Try to establish wait times for the page to load
from selenium.webdriver.support.ui import WebDriverWait


# Locate elements on page and throw error if they do not exist
from selenium.common.exceptions import NoSuchElementException

# Allows you to cusotmize: ingonito mode, maximize window size, headless browser, disable certain features, etc
option= webdriver.ChromeOptions()

# Going undercover:
option.add_argument("--incognito")


# # Consider this if the application works and you know how it works for speed ups and rendering!

# option.add_argument('--headless=chrome')

driver = webdriver.Chrome() 
# Define job and location search keywords
job_search_keyword = ['Data+Scientist', 'Business+Analyst', 'Data+Engineer', 
                      'Python+Developer', 'Full+Stack+Developer', 
                      'Machine+Learning+Engineer']

# Define Locations of Interest
location_search_keyword = ['New+York', 'California', 'Washington']

# Finding location, position, radius=35 miles, sort by date and starting page
paginaton_url_ = 'https://in.indeed.com/jobs?q={}&l={}'

# print(paginaton_url)

start = time.time()


job_='python+developer'
location='jaipur'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                         options=option)


# ... (previous code remains unchanged)

driver.get(paginaton_url_.format(job_, location))

# t = ScrapeThread(url_)
# t.start()

sleep(randint(2, 6))

# Corrected class name for finding job count
p = driver.find_element(By.CLASS_NAME, 'jobsearch-JobCountAndSortPane-jobCount').text
print(p)

max_iter_pgs = int(p.split(' ')[0]) // 15

driver.quit()  # Closing the browser we opened

end = time.time()

print(end - start, 'seconds to complete action!')
print('-----------------------')
print('Max Iterable Pages for this search:', max_iter_pgs)

# ... (previous code remains unchanged)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
p_ = []
salary_list_ = []

for i in range(0, 3):
    driver.get(paginaton_url_.format(job_, location))
    sleep(randint(2, 3))

    job_page = driver.find_element(By.ID, "mosaic-jobResults")
    jobs = job_page.find_elements(By.CLASS_NAME, "job_seen_beacon")  # return a list

    for jj in jobs:
        job_title = jj.find_element(By.CLASS_NAME, "jobTitle")
        print(job_title.text)
        p_.append(job_title.text)
        # sleep(randint(3, 5))

        try:
            salary_list_.append(jj.find_element(By.CLASS_NAME, "salary-snippet-container").text)
            print(jj.find_element(By.CLASS_NAME, "salary-snippet-container").text)
        except NoSuchElementException:
            try:
                # Corrected variable name for appending salary information
                salary_list_.append(jj.find_element(By.CLASS_NAME, "estimated-salary").text)
                print(jj.find_element(By.CLASS_NAME, "estimated-salary").text)
            except NoSuchElementException:
                print('None')

driver.quit()