import re

#szov = 'a@b.c'
#szov = 'a@b..'
#szov = 'a@b._'
szov = 'a@b.-9'

reg = re.compile(r'(([a-z]|[A-Z]|[0-9]|_|-|\.)+@([a-z]|[A-Z]|[0-9]|_|-)+\.([a-z]|[A-Z]|[0-9]|_|-|\.)+)')
mo = reg.search(szov)
print(mo.group())



