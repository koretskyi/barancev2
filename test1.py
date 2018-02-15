from selenium import webdriver
import unittest
from group import Group
class test(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get('https://liebherr.com.ua')

    def login_buy(self, wd):
        wd.find_element_by_link_text("Холодильники").click()
        wd.find_element_by_css_selector("img.product-card-image").click()
        wd.find_element_by_xpath(
            "//section[@class='first-product-container']/div[2]/div[2]/div[4]/div[2]/button").click()
        wd.find_element_by_xpath("//div[@class='modal-footer']/button[1]").click()
        wd.find_element_by_id("send-order").click()

    def fill_form(self, wd, group):
        wd.find_element_by_id("contact-form-name").click()
        wd.find_element_by_id("contact-form-name").clear()
        wd.find_element_by_id("contact-form-name").send_keys(group.username)
        wd.find_element_by_id("contact-form-number").click()
        wd.find_element_by_id("contact-form-number").clear()
        wd.find_element_by_id("contact-form-number").send_keys(group.phone)
        wd.find_element_by_id("contact-form-email").click()
        wd.find_element_by_id("contact-form-email").clear()
        wd.find_element_by_id("contact-form-email").send_keys(group.mail)

    def test_test(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login_buy(wd)
        self.fill_form(wd, Group(username="test", phone="+380 (11) 111-11-11", mail="test@test.com"))

    def test_empty_test(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login_buy(wd)
        self.fill_form(wd, Group(username="", phone="", mail=""))

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()