__author__ = 'Shankar'

import unittest
import sys
from appium import webdriver
import json
import logging
from time import sleep
from pprint import pprint

"""Step1: Start Appium instance using the command from Appium Directory
                    node /lib/server/main.js -U <Device UDID>
            Step2: Run the ios-webkit-debug-proxy listening on port 27753
                    ios_webkit_debug_proxy -c <Device UDID>

   Make sure you followed the setup configuration from Readme Link"""

class safariTest(unittest.TestCase):

    def setUp(self):

        with open('config.json') as config_file:
            config = json.load(config_file)

        desired_caps = config['safariIphone']
        '''pprint(desired_caps) For checking Desired capability'''
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(2)

    def tearDown(self):
        sleep(3)
        self.driver.quit()

    def test_login(self):

        try:
            self.driver.get("http://beta.housejoy.in/promotions/plumbing")
            sleep(6)
            usrname = self.driver.find_element_by_id('userName')
            usrname.click()
            sleep(1)
            usrname.send_keys('shankar')
            mobile = self.driver.find_element_by_id('mobileNumber')
            mobile.click()
            mobile.send_keys('9448083238')
            sleep(1)
            mailid = self.driver.find_element_by_id('userEmailid')
            mailid.send_keys('shanky@hotmail.com')
            sleep(10)
            button = self.driver.find_element_by_xpath("//span[1][contains(text(),'Book a Plumber No')]")
            button.click()
            sleep (8)
            self.driver.back()
        except:
            print("failed to Execute the Command")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(safariTest)
    unittest.TextTestRunner(verbosity=2).run(suite)