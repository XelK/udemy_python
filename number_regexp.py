import re

message = 'Call me 415-111-2314 tomorrow, or at 134-543-2348 monday'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
#mo = phoneNumRegex.search(message)
#print(mo.group())

mo = phoneNumRegex.findall(message)
print (mo)
