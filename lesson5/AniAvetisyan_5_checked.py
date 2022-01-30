#1
def squere(n):
    return n**2
    #or
    # return(pow(n,2))

print(squere(5))
# Anna-correct

#2
def names(*name):
    for items in name:
        print(items, end=' ')
    return

names('Name1', 'Name2', 'Name3')
# Anna-correct

#4
def func_sum(n1, n2):
    sum1 = n1 + n2
    return sum1

sum1 = func_sum(5, 2)

def func_result_sum(result_sum):
 
    print(result_sum)  
    return
"""Anna-will be better to print function argument. result-sum, not sum1.
Maybe you will modify this value inside funtion, for example-  
result_sum+=1 and then print(result_sum) in this case if you print sum1
your changes inside funtion will not be visible"""

func_result_sum(sum1)

#5
file1 = open('somefile.txt', 'w+')
file1.write(10*'Python ')
file1.close()

# Anna-correct
#6
file1 = open('somefile.txt', 'r+')
file1_content = file1.read()
print(file1_content)
file1.close()
# Anna-correct