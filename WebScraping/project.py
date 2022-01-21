from selenium import webdriver
from time import sleep

# basic notes
# browser = webdriver.Chrome()
# browser.quit()
# browser.get('https://www.google.com/')

#access webpage, find login box and login
browser = webdriver.Chrome()
url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)
sleep(1)

elem_username = browser.find_element_by_id('username')
# print(elem_username)
elem_username.send_keys('imanishi')

elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')

sleep(1)
elem_login_btn = browser.find_element_by_id('login-btn')
# print(elem_login_btn)
elem_login_btn.click()

#headless mode(GUI->CUI)
#without launching the browser
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_argument('--headless')
# browser = webdriver.Chrome(options = options)
# url = 'https://scraping-for-beginner.herokuapp.com/login_page'
# browser.get(url)
# browser.quit()

#get data
elem = browser.find_element_by_id('name')
name = elem.text
print(name)
elem = browser.find_element_by_id('company')
company = elem.text
print(company)
elem = browser.find_element_by_id('birthday')
birthday = elem.text
print(birthday)
elem = browser.find_element_by_id('come_from')
come_from = elem.text
print(come_from)
elem = browser.find_element_by_id('hobby')
hobby = elem.text
hobby = hobby.replace('\n', ',')
print(hobby)

#get data from table
# elem_th = browser.find_element_by_tag_name('th')
# print(elem_th.text)

#th
keys = []
elems_th = browser.find_elements_by_tag_name('th')
for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)
    # print(elem_th.text)
    print(keys)

#td
values = []
elems_td = browser.find_elements_by_tag_name('td')
for elem_td in elems_td:
    value = elem_td.text
    values.append(value)
# print(values)

import pandas as pd
df = pd.DataFrame()
df['項目'] = keys
df['値'] = values
# print(df)
df.to_csv('teacher_info.csv', index=False)

import requests
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/udemy'
res = requests.get(url)

# print(res)

#create better html by BeautifulSoup