

from model.contact import Contact
import re


class ContactHelper():

    #primary methods

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_for_creation()
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
        self.contact_cache = None


    def modify(self):
        self.modify_by_index(0)

    def modify_by_index(self, contact, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
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
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modify_by_id(self, contact, id):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
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
        wd.find_element_by_name("update").click()
        self.contact_cache = None




    def delete(self):
        self.delete_by_index(0)


    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        wd.find_element_by_xpath("//input[ @ value = 'Delete']").click()
        self.contact_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        wd.find_element_by_xpath("//input[ @ value = 'Delete']").click()
        self.open_contacts_page()
        self.contact_cache = None




    #secondary methods


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name('entry')[index]
        row.find_element_by_xpath("./td[8]/a").click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath("//a[contains(@href, %s) and contains(@href, 'edit.php?id=')]" % id).click()


    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name('entry')[index]
        row.find_element_by_xpath("./td[7]/a").click()


    def fill_out_field(self, elements_name, filled_data):
        wd = self.app.wd
        if filled_data is not None:
            wd.find_element_by_name(elements_name).click()
            wd.find_element_by_name(elements_name).clear()
            wd.find_element_by_name(elements_name).send_keys(filled_data)


    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))




    def open_for_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/addressbook') and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()


    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                elements = element.find_elements_by_xpath("./td")
                name = elements[2].text
                sirname = elements[1].text
                id = elements[0].find_element_by_name("selected[]").get_attribute("value")
                all_phones = elements[5].text
                all_emeils = elements[4].text
                self.contact_cache.append(Contact(name=name, last_name=sirname, id=id, all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emeils))
        return list(self.contact_cache)



    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        t_home = wd.find_element_by_name('home').get_attribute('value')
        t_work = wd.find_element_by_name('work').get_attribute('value')
        mobilephone = wd.find_element_by_name('mobile').get_attribute('value')
        home2 = wd.find_element_by_name('phone2').get_attribute('value')
        email1 = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        return Contact(name=firstname, last_name=lastname, id=id, t_home=t_home, t_work=t_work, t_mobile=mobilephone,
                       home2=home2, email1=email1, email2=email2,email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        t_home = re.search("H: (.*)", text).group(1)
        t_work = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        home2 = re.search("P: (.*)", text).group(1)
        return Contact(t_home=t_home, t_work=t_work, t_mobile=mobilephone,
                       home2=home2)