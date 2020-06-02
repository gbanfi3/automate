myCat = {'size':'fat', 'color': 'gray', 'disposition':'loud'}
print(myCat['size'])

for a,b in myCat.items():
    print(a,b, sep=': ')

print("fatz" in myCat.values())

if 'size' in myCat:
    print(myCat['size'])

print(myCat.get('sizee', 'nincs ilyen'))