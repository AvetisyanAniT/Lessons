#1
str1 = 'My String'
print(len(str1))

#2
sampleString = 'w3resource'
string = sampleString[:2] + sampleString[-2:]
print(string)

#3
str2 = 'abc'
print(str2 + 'ing')

#4
sampleString2 = 'I have a cat and I love it'
newString = sampleString2.replace('cat', 'dog')
print(newString)

#5
sampleString3 = 'I have 123 books'
reversedNumber = ''.join(reversed(sampleString3[7:10]))
newString2 = f'I have {reversedNumber} books'
print(newString2)

#6
x = 2.5
y = 13.75
z = int(x) + int(y)
reversedSum = ''.join(reversed(str(z)))
print(int(reversedSum))

#7
mylist = [1, 2, 5, 6, 7, 8, 9]
mylist.reverse()
print(mylist)
# or
# print(mylist[::-1])

#8
mylist2 = [1, 2, 3, 4, 5, 6, 7]
del(mylist2[1::2])
print(mylist2)

#9
list_1 = [1, 2, 'test', 3, 4, 8, 9]
print('test' in list_1)

#10
d_list = ['a', 'b', 'c', 'f', 'c', 's', 'a']
print(set(d_list))