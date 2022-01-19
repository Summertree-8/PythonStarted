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
sleep(4)

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