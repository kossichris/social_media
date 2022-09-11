import os
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

########## Step 1 Loading Linkedin home page #########
# Get the webdriver path
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "/usr/local/bin/chromedriver")

# Linkedin Url
url = "https://www.linkedin.com/home"

# Open Linkedin &  pause at this step for 3 secs
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

########### Step-2 Signing in #########
email = driver.find_element("xpath", "//input[@name = 'session_key']")
password = driver.find_element("xpath", "//input[@name = 'session_password']")


with open("/Users/christiankossi/Documents/login.txt") as userEmail:
    username = userEmail.read().replace('\n', '')
    email.send_keys(username)

with open("/Users/christiankossi/Documents/pass.txt") as userPass:
    userPassword = userPass.read().replace('\n', '')
    password.send_keys(userPassword)

time.sleep(2)

submit = driver.find_element(
    "xpath", "//button[@type = 'submit']").click()

time.sleep(2)


####### POsting a content #######

box_post = driver.find_element(
    "xpath", '//*[@id ="ember28"]')
box_post.click()

time.sleep(2)

# box_post_img = driver.find_element(
#    "xpath", '//*[@id ="ember582"]')
# box_post_img.click()

post_input = driver.find_element("name", "ql-blank")

post_input.send_keys("Test data from selenium")
