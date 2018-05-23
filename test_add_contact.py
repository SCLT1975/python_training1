# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from contact import Contact
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group_py(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def test_test_add_group_py(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_contacts_page(wd)
        self.create_contact(wd, Contact(name="qwerty", middle_name="123", last_name="wqertyu", nick_name='wer',
                                      title='brsf', company='ertw', address='qwer', t_home='dsaf', t_mobile='234', t_work='345',
                                      t_fax='345', email1='234', email2='534', email3='2134', homepage='5423', address2='3425', home2='gertgertg', notes='btertgwertgretg', b_year=2010, a_year='1987'))
        self.logout(wd)


    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()


    def create_contact(self, wd, contact):
        # Fill out сontacts' textfields
        self.fill_out_field(wd, 'firstname', contact.name)
        self.fill_out_field(wd, 'middlename', contact.middle_name)
        self.fill_out_field(wd, 'lastname', contact.last_name)
        self.fill_out_field(wd, 'nickname', contact.nick_name)
        self.fill_out_field(wd, 'title', contact.title)
        self.fill_out_field(wd, 'company', contact.company)
        self.fill_out_field(wd, 'address', contact.address)
        self.fill_out_field(wd, 'home', contact.t_home)
        self.fill_out_field(wd, 'mobile', contact.t_mobile)
        self.fill_out_field(wd, 'work', contact.t_work)
        self.fill_out_field(wd, 'fax', contact.t_fax)
        self.fill_out_field(wd, 'email', contact.email1)
        self.fill_out_field(wd, 'email2', contact.email2)
        self.fill_out_field(wd, 'email3', contact.email3)
        self.fill_out_field(wd, 'homepage', contact.homepage)
        self.fill_out_field(wd, 'address2', contact.address2)
        self.fill_out_field(wd, 'phone2', contact.home2)
        self.fill_out_field(wd, 'notes', contact.notes)
        # fill out contacts' datapickers
        wd.find_element_by_name('bday').click()
        wd.find_element_by_xpath("//select/option[7]").click()
        wd.find_element_by_name('bmonth').click()
        wd.find_element_by_xpath("//select/option[@value='January']").click()
        wd.find_element_by_name('aday').click()
        wd.find_element_by_xpath("//select[3]/option[20]").click()
        wd.find_element_by_name('amonth').click()
        wd.find_element_by_xpath("//select[4]/option[7]").click()
        self.fill_out_field(wd, 'byear', contact.b_year)
        self.fill_out_field(wd, 'ayear', contact.a_year)



        # submit group creation
        wd.find_element_by_name("submit").click()


    def fill_out_field(self, wd, elements_name, filled_data):
        wd.find_element_by_name(elements_name).click()
        wd.find_element_by_name(elements_name).clear()
        wd.find_element_by_name(elements_name).send_keys(filled_data)

    def open_contacts_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_name("MainForm").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
