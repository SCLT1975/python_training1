# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from fixture.group import GroupHelper


class Application:


#group_tests

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


        # low level functions



    def open_home_page(self):
            wd = self.wd
            wd.get("http://localhost/addressbook/")

    def destroy(self):
            wd = self.wd
            self.wd.quit()



#contact_tests






    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        wd = self.wd
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
