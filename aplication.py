import time
from selenium import webdriver
from userandpassword import USER, PASSWORD

class Linkedin:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        
    def site(self):
        #OPEN SITE
        self.driver.get("https://br.linkedin.com/")
        self.driver.find_element_by_xpath('/html/body/nav/div/a[2]').click()

        #USER AND PASSWORD
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(self.user)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        
        #CLICK THE BUTTON

        self.driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()

linkedin =  Linkedin(USER, PASSWORD)
linkedin.site()

