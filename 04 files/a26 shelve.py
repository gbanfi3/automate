import shelve
shelveFile = shelve.open("shelveFile")
shelveFile['nóra'] = ['a','b', 'ccccc']
shelveFile.close()
shelveFile = shelve.open("shelveFile")
shelveFile['kati'] = "valami"
shelveFile.close()

shelveFile = shelve.open("shelveFile")
a = shelveFile['nóra']
shelveFile.close()
print(a)