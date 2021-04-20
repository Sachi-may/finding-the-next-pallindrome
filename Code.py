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
