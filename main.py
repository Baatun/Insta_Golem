from selenium import webdriver
import os
import time

class InstagramBot:

    #CONSTRUCTOR
    def __init__(self, username, password): 
        #/////////////////////////////////////////////////////////////////////////////////////////////////////
        """
        Initializes an instance of the InstagramBot class.
        Call the login method to authenticate a user with Instagram.

        Args:
            username:str: The Instagram username for a user
            password:str: The Instagram password for a user    

        Atributes:
            driver:Selenium.webdriver.Chrome: The Chromedriver that is used to automate browser actions
        """
        #/////////////////////////////////////////////////////////////////////////////////////////////////////
        self.username = username
        self.password = password
        self.base_url = "https://www.instagram.com"
        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.login()

    
        
    #LOGIN
    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        self.driver.implicitly_wait(5) #wait 5 second after loading the page, there was a problem when driven.find was faster and never found the element
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(self.username) #finds element in html by Xpath and paste there username
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()

    #NAVIGATE TO WEBSITE
    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))


#MAIN
if __name__ == '__main__':
    ig_bot = InstagramBot('temp_username', 'temp_password') #creating class InstagramBot with username and password parameters

    ig_bot.nav_user('samuel_stolicny')

    print('SUCCESS')