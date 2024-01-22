from Main.home_page import HomePage
from Main.base import Base

class TestHome(Base):

    TITLE = 'Google'
    TEXT = 'phanison'

    def test_website_title(self):
        self.home_page = HomePage(self.driver)
        assert self.home_page.get_page_title() == self.TITLE  
    
    def test_search_functionality(self):
        self.home_page = HomePage(self.driver)
        output = self.home_page.search_something(self.TEXT)
        assert self.TEXT in output
    
