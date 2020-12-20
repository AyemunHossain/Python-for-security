import re 

print(re.findall(r'quant[ia]tative','will find either quantitative, or quantatative.'))

exampleString = '''Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather. (do did done)
'''

ages = re.findall(r'\d{1,2}',exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)
print(ages)
print(names)

# everything except abc,\n
print(re.findall(r'[^abc(^\n)]',exampleString))

#word after d 
print(re.findall(r'(d)(\w+)',exampleString))

#dxxxxxxxxx
#dxxxxxxxxd
print(re.findall(r'(d)(\w+)(d)',exampleString))

print(re.search(r'(d)(\w+)(d)',exampleString)) #returns the re object
print(re.search(r'(d)(\w+)(d)',exampleString).group()) # returns the matches
