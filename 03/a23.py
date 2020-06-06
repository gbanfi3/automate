#! python3

import re

# TODO: create regex for phone numbers

reg2 = re.compile(r'((\(\d\d\d\) |\d\d\d-)?'  # area code
                 r'\d\d\d-\d\d\d\d'  # tel num
                 r' ext\.? \d\d(\d){0,3}|x\d\d(\d){0,3})')    #extension
reg = re.compile(r'(((\(\d\d\d\) |\d\d\d-)?\d\d\d-\d\d\d\d)?( ext\.? \d\d\d{0,3})?)')
szoveg = "123-123-0000, 555-0000, (415) 555-0000, 555-0001 ext. 1234, ext 12345, x12345"
lista = reg.findall(szoveg)
print(lista)
for i in range(len(lista)):
    print(lista[i][0])


# TODO: create regex for email addresses



# TODO: create regex for phone numbers



# TODO: create regex for phone numbers



# TODO: create regex for phone numbers



# TODO: create regex for phone numbers



# TODO: create regex for phone numbers



# TODO: create regex for phone numbers



