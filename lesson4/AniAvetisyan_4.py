#1
print('N1')
num1 = 0 
num2 = 1 
range1 = 50 

for i in range(range1 + 1):
    print(num1)
    nextNum = num1 + num2
    num1 = num2
    num2 = nextNum

#2
print('N2')
scr1 = input('Enter some script:')
count1, count2 = 0, 0
for item in scr1:
    if str(item).isdigit():
        count1 += 1  
    elif str(item).isalpha():
        count2 += 1 

print('Letters:', count2)        
print('Digits:', count1)

#3
print('N3')
Lh = 7
Ll = 5
for x in range(Lh):
    for y in range(Ll):
        if y == 0 or x == Lh-1:
            print('* ', end='')    
        else:
            print(' ', end='')
    print('\r')

#4
print('N4')
month = int(input('Month:'))
if (month >=1 and month <=2) or month == 12:
    print('Season: Winter')
elif month >= 3 and month <= 5:
    print('Season: Spring')
elif month >= 6 and month <= 8:
    print('Season: Summer')
elif month >= 9 and month <= 11:
    print('Season: Autumn')
# elif str(month).isalpha:
#     print('Please enter valid number')    # while entering script does not work
else:
    print('Please enter valid number')

#5
print('N5')
firstNum = input('First number:')
secondNum = input('Second number:')
thirdNum = input('Third number:')

if firstNum > secondNum and firstNum > thirdNum:
    max = firstNum
elif secondNum > firstNum and secondNum > thirdNum:
    max = secondNum
else:
    max = thirdNum

print('The max value is: ', max)

#6
print('N6')
for j in range(11):
    for k in range(11):
        if j == 0 or k == 0:
            continue
        mul=j*k
        print(f'{j} * {k} = {mul}')

#7
print('N7')
numbers = 9
for a in range(numbers+1):
    for b in range(a):
        print(a, end='')
    print('\r')