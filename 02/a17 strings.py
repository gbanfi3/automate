import pyperclip
spam = "hello world"
print(spam.upper())
spam = spam.lower()
print(spam)

a= '.'.join(['jj', 'oo', 'bb'])
print(a)

b = 'hello alma kkk itt mi ez'
b2 = '-'.join(b.split())
b3 = '='.join(b2.split('-'))
print(b3)

c= "alma".rjust(10)
c= "alma".ljust(10, 'h').rjust(22, 'x')
print(c)
c= c.strip('hx')
print(c)

pyperclip.copy = 'hello'
# d= pyperclip.paste
# print(d)