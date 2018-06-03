

class GroupHelper():



    def __init__(self, app):
        self.app = app

    def return_to_groups(self):
            wd = self.app.wd
            wd.find_element_by_link_text("group page").click()

    def create(self, group):
            wd = self.app.wd
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

    def delete(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_xpath("//span[@class='group'][1]").click()
        wd.find_element_by_name("delete").click()



    def modify(self, group):
            wd = self.app.wd
            # start group modification
            self.open_groups_page()
            wd.find_element_by_xpath("//span[@class='group'][1]").click()
            wd.find_element_by_name("edit").click()
            # Fill out edited groups' form
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
            wd.find_element_by_name("update").click()
            self.return_to_groups()


    def open_groups_page(self):
            wd = self.app.wd
            wd.find_element_by_link_text("groups").click()
