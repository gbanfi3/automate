import os
a = os.path.join("folder1", "folder2", "folder3")
print(a)

print(os.sep)
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
a=os.getcwd()
print(a)
print(os.path.abspath('bb/alma.txt'))