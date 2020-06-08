import os
for folderName, subfolders, fileName in os.walk('./aldir3'):
    print('the folder is ' + folderName)
    print('subfolders: ' + subfolders)
    print("file nevek: " +fileName)