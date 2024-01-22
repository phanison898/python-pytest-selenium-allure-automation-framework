from Utils.web_utils import WebUtils
from selenium.webdriver.common.by import By

class HomePage(WebUtils):

    def __init__(self,driver):
        super().__init__(driver)

    INPUT_BOX = (By.NAME,'q')
    SUBMIT_BTN = (By.NAME,'btnK')

    def get_page_title(self):
        return self.driver.title
    
    def search_something(self, text):
        self.send_keys(self.INPUT_BOX,text)
        self.click(self.SUBMIT_BTN)
        return self.driver.title

