import re # RegEx module

message = 'Hey, call me back at 415-555-1011 asap, or at 555-144-1337 for my office line'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObjects = phoneNumRegex.search(message)
print(matchObjects.group())
