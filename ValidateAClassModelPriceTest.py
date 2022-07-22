from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import unittest
from time import sleep


class ValidatePrice(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_openBrowser(self):
        url = "https://www.mercedes-benz.co.uk/"
        self.driver.get(url)
        sleep(5)
        self.driver.execute_script('''return document.querySelector('[settings-id="fph8XBqir"]').shadowRoot.querySelector('[data-test="handle-accept-all-button"]')''').click()
        
        #Filter by Hatchback
        self.driver.execute_script('''return document.querySelector('[component-id="c74290488f750c48e27ac0dbce1833df"]').firstChild.shadowRoot.querySelector('div > div > div > div > div > div > div:nth-child(4) > div > section > div > div > section:nth-child(2) > button:nth-child(2)')''').click()
        self.driver.execute_script('''return document.querySelector('[component-id="c74290488f750c48e27ac0dbce1833df"]').firstChild.shadowRoot.querySelector('.dh-io-vmos_jQyeG').focus()''')
        self.driver.execute_script('''return document.querySelector('body > div.root.responsivegrid > div > div > div > dh-io-vmos > div').shadowRoot.querySelector('div > div > div > div > div > div > div:nth-child(4) > section > div > div > div:nth-child(1) > div > wb-popover > ul > li:nth-child(2) > a')''').click()
        
        #Scroll the results to view
        self.driver.execute_script('''return document.querySelector('[component-id="8f90efb9b25acd626539281bf797a113"]').shadowRoot.querySelector('#cc-app-container-main > div.cc-app-container__main-frame.cc-grid-container > div.cc-grid-container.ng-star-inserted > div > div.cc-app-container__content-selectables-container > cc-motorization > cc-motorization-filters > div').scrollIntoView()''')
        sleep(5)
        self.driver.get_screenshot_as_file(".\\screenshot.png") 
        
        #Check Prices
        prices = self.driver.execute_script(''' return document.querySelector('[component-id="8f90efb9b25acd626539281bf797a113"]').shadowRoot.querySelectorAll('.cc-motorization-header__price')''')
        lowest = self.driver.execute_script(''' return document.querySelector('[component-id="8f90efb9b25acd626539281bf797a113"]').shadowRoot.querySelector('.cc-motorization-header__price').textContent''')
        highest = self.driver.execute_script(''' return document.querySelector('[component-id="8f90efb9b25acd626539281bf797a113"]').shadowRoot.querySelector('#cc-app-container-main > div.cc-app-container__main-frame.cc-grid-container > div.cc-grid-container.ng-star-inserted > div > div.cc-app-container__content-selectables-container > cc-motorization > cc-motorization-comparison > div > div > div:nth-child(23) > wb-card > div.cc-motorization-comparison-header-wrapper > cc-motorization-header > div > div > div:nth-child(4) > span').textContent''')

        with open('carPrices.txt', 'w') as f:
            f.write('Lowest price: ' + lowest + '\n')
            f.write('Highest price: ' + highest)
            f.close()

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
