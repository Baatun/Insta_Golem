from selenium import webdriver
import os
import time
import random


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
        time.sleep(5)

    #NAVIGATE TO USER
    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))

    #NAVIGATE TO HASHTAG
    def nav_hashtag(self, hashtag):
        self.driver.get('{}/explore/tags/{}/'.format(self.base_url, hashtag))

    #FOLLOW USER
    def follow_user(self, user):
        self.nav_user(user) 
        time.sleep(3)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        follow_button.click()

    #LIKE HASHTAG 
    #-- like "count" images of hashtag
    def like_hashtag(self, hashtag, count):
        self.nav_hashtag(hashtag)
        
        self.driver.find_elements_by_class_name('_9AhH0')[9].click()

        for x in range(count):
            time.sleep(random.randrange(3,10))
            self.driver.find_element_by_xpath("//*[@aria-label='{}']".format('Like')).click() #click on the like button
            self.driver.find_element_by_xpath("//a[contains(text(), 'Next')]").click()
        



#MAIN
if __name__ == '__main__':

    username = 'username'
    password = 'pass'

    ig_bot = InstagramBot(username, password) #creating class InstagramBot with username and password parameters

    #ig_bot.nav_user('samuel_stolicny')
    #ig_bot.nav_hashtag('dnescestujem')
    ig_bot.like_hashtag('dnescestujem', 3)
    #ig_bot.follow_user('adobe')


    print('SUCCESS')