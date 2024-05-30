#importing necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
 
#setting up the automation
service = Service(executable_path='./chromedriver.exe')

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 
chrome_browser = webdriver.Chrome(options = options, service=service)
chrome_browser.minimize_window()
#selecting website of choice
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

#filling in text box on website
user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('Here we are')

assert 'Show Message' in chrome_browser.page_source

#giving time to not spam the website
time.sleep(2)

#clicking submit button
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
show_message_button.click()

#veifying if all went well
output_message = chrome_browser.find_element(By.ID, 'display')
assert 'Here we are' in output_message.text

#closing the browser
chrome_browser.close()
chrome_browser.quit()