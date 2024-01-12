from django.db import models
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


client = MongoClient('mongodb+srv://srishtikashyap1234:<F8Cn6jOkP6lsBqvd>@cluster0.6somnkm.mongodb.net/?retryWrites=true&w=majority')
db = client['job_listings']


from lxml import etree as et


from csv import writer


import time


from time import sleep


import pandas as pd


from random import randint


import selenium



from selenium import webdriver


from selenium.webdriver.chrome.service import Service as ChromeService


from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import WebDriverWait



from selenium.common.exceptions import NoSuchElementException

option= webdriver.ChromeOptions()


option.add_argument("--incognito")


driver = webdriver.Chrome() 

job_search_keyword = ['Data+Scientist', 'Business+Analyst', 'Data+Engineer', 
                      'Python+Developer', 'Full+Stack+Developer', 
                      'Machine+Learning+Engineer']


location_search_keyword = ['New+York', 'California', 'Washington']


paginaton_url_ = 'https://in.indeed.com/jobs?q={}&l={}'



start = time.time()


job_='python+developer'
location='jaipur'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                         options=option)



driver.get(paginaton_url_.format(job_, location))


sleep(randint(2, 6))


p = driver.find_element(By.CLASS_NAME, 'jobsearch-JobCountAndSortPane-jobCount').text
print(p)

max_iter_pgs = int(p.split(' ')[0]) // 15

driver.quit() 

end = time.time()

print(end - start, 'seconds to complete action!')
print('-----------------------')
print('Max Iterable Pages for this search:', max_iter_pgs)



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
