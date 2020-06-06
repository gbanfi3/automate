import re
import pprint

# szoveg = " itt vagyok én Agent Banfi, szolgálatára Agent 140"
#
# regex = re.compile(r'Agent \D+')
# lista = regex.findall(szoveg)
# print(lista)

# reg = re.compile(r'\D([1-9]\d{3})\D')
# reg = re.compile(r'\s([1-9]\d{3})\s')
# szoveg1 = " 1000  9999  1234 "
# a1 = reg.findall(szoveg1)
# print(a1)
#
# szoveg2 = " 0456 0000 aaaa a1235 123 12375"
# a2 = reg.findall(szoveg2)
# print(a2)
"""
Zahlen gibt es in den unterschiedlichsten Formaten. Betrachten wir folgende Zahlen:
* nur positive ganze Zahlen
* Tausender-Apostroph zur Abtrennung von 1000 Bereichen
* zum Beispiel 1, 42, 486, 9’386, 719’528, 783’748’894’846
Auch hier hat jemand von einen Anfang gemacht: Der Ausdruck \d{1,3}'\d{3} erkennt immerhin
schon die Zahlen 1’000 bis 999’999. 
"""

reg = re.compile(r"((\d{1,3}\')*\d{3}|\d{1,3})")
# reg = re.compile(r"(\d{1,3})")
reg = re.compile(r"([1-9]\d{0,2}(\'\d{3}){4}" \
                 r"|[1-9]\d{0,2}(\'\d{3}){3}" \
                 r"|[1-9]\d{0,2}(\'\d{3}){2}" \
                 r"|[1-9]\d{0,2}(\'\d{3}){1}" \
                 r"|[1-9]\d{0,2})")

szamok1 = "'0 01 012" \
          "1 12 '323 1''234 123'4 123'45 123'456 123'456' 123'456'7 0987654321 '456'7 "
szamok2 = "1 21 321 4'321 54'321 654'321 7'654'321 87'654'321 987'654'321 0'987'654'321 " \
          "90'987'654'321 890'987'654'321 7'890'987'654'321 67'890'987'654'321 567'890'987'654'321 " \
          "4'567'890'987'654'321 34'567'890'987'654'321 234'567'890'987'654'321 1'234'567'890'987'654'321 "
lista = reg.findall(szamok2)
print(lista)
for i in range(len(lista)):
    pprint.pprint(lista[i][0])
