from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

class WebUtils:

    def __init__(self,driver):
        self.driver = driver
        config_file = open('config.json')
        config = json.load(config_file)
        self.EX_WAIT = config['explicit_wait']

    def click(self,by_locator):
        WebDriverWait(self.driver,self.EX_WAIT).until(EC.element_to_be_clickable(by_locator)).click()

    def send_keys(self,by_locator,text):
        element=WebDriverWait(self.driver,self.EX_WAIT).until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def get_text(self,by_locator):
       return WebDriverWait(self.driver,self.EX_WAIT).until(EC.visibility_of_element_located(by_locator)).text