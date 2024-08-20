# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
 
# Setting up the automation
service = Service(executable_path='./chromedriver.exe')

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 
chrome_browser = webdriver.Chrome(options = options, service=service)
chrome_browser.minimize_window()
# Selecting website of choice
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

# Filling in text box on website
user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('Here we are')

assert 'Show Message' in chrome_browser.page_source

# Giving time to not spam the website
time.sleep(2)

# Clicking submit button
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
show_message_button.click()

# Verifying if all went well
output_message = chrome_browser.find_element(By.ID, 'display')
assert 'Here we are' in output_message.text

# Closing the browser
chrome_browser.close()
chrome_browser.quit()