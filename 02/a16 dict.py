import pprint
message = 'it was a bright cold day in April, and the clock were striking thirteen.'
count = {}

for char in message.upper():
    count.setdefault(char,0)
    count[char] +=1

pprint.pprint(count)
