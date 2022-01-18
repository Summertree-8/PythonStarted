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
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options = options)
url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)
browser.quit()