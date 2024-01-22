import pytest
import json
from selenium import webdriver

@pytest.fixture(scope='session')
def configuration():
    config = open('config.json')
    return json.load(config)

@pytest.fixture()
def setup(request,configuration):
    browser = configuration['browser']
    url = configuration['url']
    headless_mode = configuration['headless_mode']

    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        if headless_mode == True:
            options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        
    if browser == 'firefox':
        options = webdriver.FirefoxOptions()
        if headless_mode == True:
            options.headless = True
        driver = webdriver.Firefox(options=options)
    
    request.cls.driver = driver
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(5)
    driver.get(url)

@pytest.fixture()
def tear_down(request):
    yield
    request.cls.driver.close()
    request.cls.driver.quit()