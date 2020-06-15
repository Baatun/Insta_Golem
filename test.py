from selenium import webdriver
import os
import time
import random
import configparser
import ast
import datetime

#MAIN
if __name__ == '__main__':


    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome('./chromedriver.exe',chrome_options=options)
    
    driver.get("https://www.reddit.com/")
    driver.close()
    print('SUCCESS')