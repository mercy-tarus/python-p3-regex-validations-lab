import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r""
name_regex = re.compile(name)
name_regex = re.compile(r"^[A-Z][a-zA-Z]*([ '-][A-Z][a-zA-Z]*)*$")

phone_number = r""
phone_regex = re.compile(phone_number)
phone_regex = re.compile(r"^(\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$")

email_address = r""
email_regex = re.compile(email_address)
email_regex = re.compile(r"^[a-zA-Z][a-zA-Z0-9.]*@[a-zA-Z]+\.[a-zA-Z]{2,}$")
