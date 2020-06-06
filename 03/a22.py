import re
szoveg = """
<h1>Dies ist eine Überschrift ersten Grades1</h1>
<h2>Dies ist eine Überschrift zweiten Grades</h2>
<p>Dies ist einfach nur ein ganz normaler Abschnitt.</p>
<p>Dies ist einfach nur ein ganz normaler ffff.</p>
<h1>Dies ist noch eine Überschrift ersten Grades2</h1> 
"""

# reg = re.compile(r'<h1>(.+)</h1>')
# # reg = re.compile(r'<h1>\w+')
# lista = reg.findall(szoveg)
# print(lista)
# for i in range(len(lista)):
#     print(lista[i])

# reg = re.compile(r'Dies')
# lista = reg.sub('das', szoveg)
# print(lista)

reg = re.compile(r'<h1(>.+</)h1>')
lista = reg.sub(r'<u\1u>',szoveg)
print(lista)