import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from create_xlsx import create_xlsx
from create_json import export_json
from create_csv import export_csv

class SearchMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\chrome-driver\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://mercadolibre.com/')

    def test_search(self):
        driver = self.driver
        driver.find_element(By.ID, 'AR').click()
        
        time.sleep(10)
        # Accpet cookies
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div[2]/button[1]')))
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/button[1]').click()
        

        # Skip select postal code
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div[2]/button[2]/span')))
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div[2]/button[2]/span').click()
        
        # Locate search bar and search 'Play Station 5'
        search_field = driver.find_element(By.XPATH, '/html/body/header/div/div[2]/form/input')
        search_field.clear()
        search_field.send_keys('Play Station 5')
        search_field.submit()

        #filter new ones        
        new = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/aside/section/div[7]/ul/li[1]/a/span[1]')
        new.click()

        #filter for CABA
        caba = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/aside/section[2]/div[10]/ul/li[1]/a/span[1]')
        caba.click()
        time.sleep(10)
        
        # order by cheapest price
        expected_options = ['Más relevantes', 'Menor precio', 'Mayor precio']
        active_option = []

        select_filter_price = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/div[2]/div/div/div/div[2]/div/div/button')
        select_filter_price.click()
        
        driver.find_element(By.XPATH, '//*[@id="andes-dropdown-más-relevantes-list-option-price_asc"]/div/div/span').click()
        time.sleep(10)

        #create a list with the item names and prices
        titles = []
        prices = []
        for title_price in range(5):
            title = driver.find_element(By.XPATH, f'/html/body/main/div/div[2]/section/ol/li[{title_price + 1}]/div/div/div[2]/div[1]/a/h2')
            titles.append(title.text)
            price = driver.find_element(By.XPATH, f'/html/body/main/div/div[2]/section/ol/li[{title_price + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]')
            prices.append(price.text)

        #export date to an excel file  
        create_xlsx(titles, prices)
        export_json(titles,prices)
        export_csv(titles, prices)
        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity = 2)