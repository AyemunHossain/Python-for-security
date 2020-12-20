import re

statement = "Please contact us at: support@DataCamp.com, xyz@DATACAMP.com"

pattern = re.compile(r"""
[\w\.-]+@[\w\.-]+
""", re.X | re.I)

addresses = re.findall(pattern, statement)                       
for address in addresses:
    print("Address: ", address)