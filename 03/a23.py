#! python3

import re

reg = re.compile(r'(((\(\d\d\d\) |\d\d\d-)?'    # area
                 r'\d\d\d-\d\d\d\d)?'           # tel
                 r'( ext\.? \d{2,5}|x\d{2,5})?)') #extension
szoveg = "123-123-0000, 555-0000, (415) 555-0000, 555-0001 ext. 1234, ext 12345, x12345"
lista = reg.findall(szoveg)
print(lista)
for i in range(len(lista)):
    if lista[i][0].strip():
        print(lista[i][0].strip())

# TODO: create regex for email addresses



# TODO: create regex for phone numbers



# TODO: create regex for phone numbers



# TODO: create regex for phone numbers



# TODO: create regex for phone numbers



# TODO: create regex for phone numbers



# TODO: create regex for phone numbers



