# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver


class Application:


#group_tests

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

        # low level functions

    def logout(self):
            wd = self.wd
            wd.find_element_by_link_text("Logout").click()

    def return_to_groups(self):
            wd = self.wd
            wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
            wd = self.wd
            # start group creation
            self.open_groups_page()
            wd.find_element_by_xpath("//div[@id='content']/form/input[4]").click()
            # Fill out groups' form
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name)
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)
            # submit group creation
            wd.find_element_by_name("submit").click()
            self.return_to_groups()

    def open_groups_page(self):
            wd = self.wd
            wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
            wd = self.wd
            self.open_home_page()
            wd.find_element_by_name("user").click()
            wd.find_element_by_name("user").clear()
            wd.find_element_by_name("user").send_keys(username)
            wd.find_element_by_name("pass").click()
            wd.find_element_by_name("pass").clear()
            wd.find_element_by_name("pass").send_keys(password)
            wd.find_element_by_id("LoginForm").click()
            wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
            wd.find_element_by_name("MainForm").click()

    def open_home_page(self):
            wd = self.wd
            wd.get("http://localhost/addressbook/")

    def destroy(self):
            wd = self.wd
            self.wd.quit()



#contact_tests

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


    def create_contact(self, contact):
        wd = self.wd
        self.open_contacts_page()
        # Fill out сontacts' textfields
        self.fill_out_field('firstname', contact.name)
        self.fill_out_field('middlename', contact.middle_name)
        self.fill_out_field('lastname', contact.last_name)
        self.fill_out_field('nickname', contact.nick_name)
        self.fill_out_field('title', contact.title)
        self.fill_out_field('company', contact.company)
        self.fill_out_field('address', contact.address)
        self.fill_out_field('home', contact.t_home)
        self.fill_out_field('mobile', contact.t_mobile)
        self.fill_out_field('work', contact.t_work)
        self.fill_out_field('fax', contact.t_fax)
        self.fill_out_field('email', contact.email1)
        self.fill_out_field('email2', contact.email2)
        self.fill_out_field('email3', contact.email3)
        self.fill_out_field('homepage', contact.homepage)
        self.fill_out_field('address2', contact.address2)
        self.fill_out_field('phone2', contact.home2)
        self.fill_out_field('notes', contact.notes)
        # fill out contacts' datapickers
        wd.find_element_by_name('bday').click()
        wd.find_element_by_xpath("//select/option[7]").click()
        wd.find_element_by_name('bmonth').click()
        wd.find_element_by_xpath("//select/option[@value='January']").click()
        wd.find_element_by_name('aday').click()
        wd.find_element_by_xpath("//select[3]/option[20]").click()
        wd.find_element_by_name('amonth').click()
        wd.find_element_by_xpath("//select[4]/option[7]").click()
        self.fill_out_field('byear', contact.b_year)
        self.fill_out_field('ayear', contact.a_year)
        # submit group creation
        wd.find_element_by_name("submit").click()


    def fill_out_field(self,elements_name, filled_data):
        wd = self.wd
        wd.find_element_by_name(elements_name).click()
        wd.find_element_by_name(elements_name).clear()
        wd.find_element_by_name(elements_name).send_keys(filled_data)

    def open_contacts_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_name("MainForm").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        wd = self.wd
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
