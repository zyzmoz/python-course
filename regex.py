import re

# Search
text = "This is a string with term1, not the other"

patterns = ['term1', 'term2']

for pattern in patterns:
  print("I'm searching for: ", pattern)
  
  if re.search(pattern, text):
    print('MATCH')
  else:
    print('NO MATCH')
 
# Split   
email = "user@email.com"

split_term = "@"

print(re.split(split_term, email))


# Find

code = '123'

if (re.findall('123', code)):
  print('We got a match')
  
