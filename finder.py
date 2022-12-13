# selenium 4
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def find(word):
    chrom_options = Options()
    chrom_options.add_argument('--headless')
    ch_options = Options()
    ch_options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), chrome_options= ch_options)#
    driver.maximize_window()
    driver.get("https://www.google.com/?hl=uk")
    cookie_btn = driver.find_element(By.XPATH, '//*[@id="L2AGLb"]')
    cookie_btn.click()
    elem = driver.find_element("name","q")
    elem.send_keys(word)
    elem.send_keys(Keys.RETURN)
    link = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/div/cite')
    link.click()
    url = driver.current_url
    assert "No results found." not in driver.page_source 
    driver.quit()
    return url



