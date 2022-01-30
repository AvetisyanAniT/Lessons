import re

#1
txt = 'December 25 2020'
dayYear = re.findall(r'\d+', txt)
print(dayYear)

#2
expr = """
user1-Operation
user2-Operation
user3-Operation
user1-Operation
user1-Operation
"""
user1 = re.findall(r'user1-\w+', expr)
print(user1)

#3
date = 'Date December 25 2020, Day 25'
replace = '26'
new_date = re.sub(r'25', replace, date, 1)
print(new_date)

#4
exp = 'username@gmail.com'
x = re.split(r'@', exp)
print(x)

