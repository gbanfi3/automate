#! python3
import re

reg = re.compile(r'(((\(\d\d\d\) |\d\d\d-)?'    # area
                 r'\d\d\d-\d\d\d\d)?'           # tel
                 r'( ext\.? \d{2,5}|x\d{2,5})?)') #extension
szoveg = "123-123-0000, 555-0000, (415) 555-0000, 555-0001 ext. 1234, ext 12345, x12345"
lista = reg.findall(szoveg)
tels = []
for i in range(len(lista)):
    if lista[i][0]:
        tels.append(lista[i][0])
print(tels)

# TODO: create regex for email addresses
szoveg = "a.b@c.d a_+_.B.c@d_+.e_+ a,b@.."
reg = re.compile(r""
                 r"[a-zA-Z0-9.+_]+"
                 r"@"
                 r"[a-zA-Z0-9.+_]+"
                 r"\."
                 r"[a-zA-Z0-9.+_]+"
                 r"")
lista = reg.findall(szoveg)
emails = []
for i in range(len(lista)):
    if lista[i]:
        emails.append(lista[i])
print(emails)



# TODO: create regex for phone numbers



# TODO: create regex for phone numbers



# TODO: create regex for phone numbers



# TODO: create regex for phone numbers



# TODO: create regex for phone numbers



# TODO: create regex for phone numbers



