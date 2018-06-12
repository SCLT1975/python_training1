
class ContactHelper():

    #primary methods

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
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

    def modify(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//tr[@name][1]/td[8]").click()
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




    def delete(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//tr[@name][1]/td[8]").click()
        wd.find_element_by_xpath("// input[ @ name = 'update'][1]").click()




    #secondary methods

    def fill_out_field(self, elements_name, filled_data):
        wd = self.app.wd
        if filled_data is not None:
            wd.find_element_by_name(elements_name).click()
            wd.find_element_by_name(elements_name).clear()
            wd.find_element_by_name(elements_name).send_keys(filled_data)







    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
