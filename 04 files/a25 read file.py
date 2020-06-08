import os

# hellofile = open("./aldir/file01_orig.txt")
# # a = hellofile.read()
# b = hellofile.readlines()
# hellofile.close()
# # print(a)
# print(b)

hellofile = open("./aldir/file01.txt", "a")
hellofile.write("\nmégvalami")
hellofile.close()
hellofile = open("./aldir/file01.txt", "r")
a = hellofile.readlines()
hellofile.close()
print(a)