import re

message = "hivjál fel a 123-456-7890 számon, vagy inkább ezen: 234-567-8901"

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(message)
print(mo.group(2))

message = "hivjál fel a 123-456-7890 számon, vagy inkább ezen: (234)-567-8901"
phoneNumRegex = re.compile(r'\(\d\d\d\)-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())

message = "a batmobile akármi batss"
mesRegex = re.compile(r'bat(man|valami|mobile|ss)')
mo = mesRegex.search(message)
print(mo.group())

message = "a batwowoman akármi batss"
mesRegex = re.compile(r'bat(wo)+man')
mo = mesRegex.search(message)
print(mo.group())