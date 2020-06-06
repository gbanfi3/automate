import re
regex = re.compile(r'(Ha){3}')
mo = regex.search(" j j ksa HaHaHa j kj kl Ha kjkj")
print(mo.group())