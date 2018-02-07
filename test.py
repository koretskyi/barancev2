# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test(self):
        success = True
        wd = self.wd
        wd.get("https://liebherr.com.ua/")
        wd.find_element_by_link_text("Холодильники").click()
        wd.find_element_by_css_selector("img.product-card-image").click()
        wd.find_element_by_xpath("//section[@class='first-product-container']/div[2]/div[2]/div[4]/div[2]/button").click()
        wd.find_element_by_xpath("//div[@class='modal-footer']/button[1]").click()
        wd.find_element_by_id("send-order").click()
        wd.find_element_by_id("contact-form-name").click()
        wd.find_element_by_id("contact-form-name").clear()
        wd.find_element_by_id("contact-form-name").send_keys("test")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys("\\9")
        wd.find_element_by_id("contact-form-number").click()
        wd.find_element_by_id("contact-form-number").clear()
        wd.find_element_by_id("contact-form-number").send_keys("+380 (11) 111-11-11")
        wd.find_element_by_id("contact-form-email").click()
        wd.find_element_by_id("contact-form-email").clear()
        wd.find_element_by_id("contact-form-email").send_keys("test@test.com")
        wd.find_element_by_xpath("//div[4]/div").click()
        wd.find_element_by_id("send-order").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
