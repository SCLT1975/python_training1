
from sys import maxsize

class Contact:

    def __init__(self, name=None, middle_name=None, last_name=None, nick_name=None, title=None, company=None,
                 address=None, t_home=None, t_mobile=None, t_work=None, t_fax=None, email1=None, email2=None,
                 email3=None, homepage=None, address2=None, home2=None, notes=None, b_year=None, a_year=None,
                 id=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.name = name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.title = title
        self.company = company
        self.address = address
        self.t_home = t_home
        self.t_mobile = t_mobile
        self.t_work = t_work
        self.t_fax = t_fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.home2 = home2
        self.notes = notes
        self.b_year = b_year
        self.a_year = a_year
        self.id = id
        self.all_phones_from_home_page=all_phones_from_home_page
        self.all_emails_from_home_page=all_emails_from_home_page


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name,self.last_name)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id), self.name == other.name, self.last_name == other.last_name

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize
