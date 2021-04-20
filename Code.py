def next_pallindrome(number):
    number=number+1
    while not isPallindrome(number):
        number+=1
    return number

def isPallindrome(n):
    return str(n)==str(n)[::-1]

n=int(input("Enter the nummber of test cases\n"))
numbers=[]
for i in range(n):
    num=int(input("Enter the numbers\t"))
    numbers.append(num)

for i in range(n):
    print(f"The next pallindrome of {numbers[i]} is {next_pallindrome(numbers[i])}")

 
'''__________________________________________________________________________________________________________________________________________'''
    
'''palindrome concept for list You are given a list that contains some numbers. You have to print a list of next palindromes only if the number is greater than 10; otherwise, you will print that number.

Input:
[1, 6, 87, 43]

Output:
[1, 6, 88, 44]
'''
# def next_palindrome(n):
#     n = n+1
#     while not isPallindrome(n):
#         n += 1
#     return n

# def isPallindrome(n):
#     return str(n)==str(n)[::-1]

# if __name__ == '__main__':
#     list=[]
#     n=int(input("Enter the size of list \n"))
#     for i in range(n):
#         num=int(input("Enter the numbers of the list\n"))
#         list.append(num)
#     print(f'Your list is {list}')
#     list2=[]
#     for i in list:
#        if i<10:
#            list2.append(i)
#        else:
#            i1=next_palindrome(i)
#            list2.append(i1)
#     print(list2)
