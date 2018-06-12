

class GroupHelper():

    #primary methods

    def __init__(self, app):
        self.app = app



    def create(self, group):
            wd = self.app.wd
            # start group creation
            self.open_groups_page()
            wd.find_element_by_xpath("//div[@id='content']/form/input[4]").click()
            self.fill_group_form(group)
            # submit group creation
            wd.find_element_by_name("submit").click()
            self.return_to_groups()

    def delete(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()

    def modify(self, group):
            wd = self.app.wd
            # start group modification
            self.open_groups_page()
            self.select_first_group()
            wd.find_element_by_name("edit").click()
            self.fill_group_form(group)
            # submit group creation
            wd.find_element_by_name("update").click()
            self.return_to_groups()


    #secondary methods

    def return_to_groups(self):
            wd = self.app.wd
            wd.find_element_by_link_text("group page").click()

    def fill_group_form(self, group):
        self.type("group_name", group.name)
        self.type("group_header", group.header)
        self.type("group_footer", group.footer)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name("group_name").send_keys(text)


    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[@class='group'][1]").click()



    def open_groups_page(self):
            wd = self.app.wd
            if not (wd.current_url.endswith('/group.php') and len(wd.find_elements_by_name("new")) > 0):
                wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
