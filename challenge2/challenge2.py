import unittest
import time
from selenium import webdriver

class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        self.driver.get("https://www.copart.com")
        elem = self.driver.find_element_by_id('input-search')
        elem.send_keys("exotic")
        self.driver.find_element_by_css_selector("[ng-click='search()']").click()
        time.sleep(5)
        por = self.driver.find_element_by_css_selector("[data-uname='lotsearchLotmake']").text
        print(por)
        self.assertEqual(por, 'PORSCHE', "Title is wrong")


if __name__ == '__main__':
    unittest.main()