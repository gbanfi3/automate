import re
# szoveg = " itt vagyok én Agent Banfi, szolgálatára Agent 140"
#
# regex = re.compile(r'Agent \D+')
# lista = regex.findall(szoveg)
# print(lista)

szoveg1 = " 1000 9999 1234"
szoveg2 = " 0456 0000 1234 aaaa a1234 123 12345"
reg = re.compile(r'\D[1-9]\d{3}\D')
a1 = reg.findall(szoveg1)
print(a1)
a2 = reg.findall(szoveg2)
print(a2)