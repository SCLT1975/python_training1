from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


testdata = [
    Contact(name=random_string("name", 10), middle_name=random_string("middle_name", 10),
            last_name=random_string("last_name", 10), nick_name=random_string("nick_name", 10),
            title=random_string("title", 10), company=random_string("company", 10),
            address=random_string("address", 10), t_home=random_string("t_home", 10),
            t_mobile=random_string("t_mobile", 10), t_work=random_string("t_work", 10),
            t_fax=random_string("t_fax", 10),
            email1=random_string("email1", 10), email2=random_string("email2", 10), email3=random_string("email3", 10),
            homepage=random_string("homepage", 10), address2=random_string("address2", 10),
            home2=random_string("home2", 10),
            notes=random_string("notes", 10), b_year=random_string("b_year", 10), a_year=random_string("a_year", 10))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))