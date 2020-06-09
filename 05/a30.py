import traceback
# raise Exception("hello world")
#
# print("aa")
# print(traceback.format_exc())
# print("bb")

try:
    raise Exception("valami gond")
except:
    errorFile = open("./erFil.txt","a")
    errorFile.write(traceback.format_exc())
    errorFile.close()