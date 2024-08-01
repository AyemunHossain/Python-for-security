import re


statement = 'Please contact us at: support@datacamp.com'
match = re.search(r'([\w-]+)@([\w-]+)', statement)
if statement:
  print("Email address:", match.group())
  print("Username:", match.group(1))
  print("Host:", match.group(2)) 


# you can also create named 

statement = 'Please contact us at: support@datacamp.com'
match2 = re.search(r'(?P<email>(?P<username>[\w-]+)@(?P<host>[\w-]+))', statement)
if statement:
  print("Email address:", match2.group("email"))
  print("Username:", match2.group("username"))
  print("Host:", match2.group("host")) 


# compliling demo match string into regular expression object

pattern = re.compile(r'(?P<email>(?P<username>[\w-]+)@(?P<host>[\w-]+))')

match3 = pattern.search(statement)

if statement:
  print("Email address:", match3.group("email"))
  print("Username:", match3.group("username"))
  print("Host:", match3.group("host")) 


#findall in re

statement = "Please contact us at: support@datacamp.com, xyz@datacamp.com"

emails = re.findall(r'[\w\.-]+@[\w\.-]+', statement)

# Finds all the possible matches in the entire sequence and returns them 
# as a list of strings. Each returned string represents one match.
for email in emails:
    print(email)



pattern = re.compile('COOKIE', re.IGNORECASE)
match = pattern.search("I am not a cookie monster")

print("Start index:", match.start())
print("End index:", match.end())
print("Tuple:", match.span())