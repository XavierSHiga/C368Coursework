"""
-----------------------------------------------------------------------------------------------------------------------
The activities on this page will allow you to demonstrate your ability to:
Create a Python script that uses a for loop to repeat an activity until a specific criterion is met.
Create a Python script that uses a while loop to repeat an activity as long as a specific criterion holds true.
-----------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------
Activity 1
Given the list fruit_list, write a script that iterates through the list and prints each item on a separate line.
fruit_list = ["apple", "banana", "cherry", "gooseberry", "kumquat", "orange", "pineapple"]
-----------------------------------------------------------------------------------------------------------------------
"""
def act1():
    fruit_list = ["apple", "banana", "cherry", "gooseberry", "kumquat", "orange", "pineapple"]
    for item in fruit_list:
        print(item)

# Uncomment the next line and run the file:
# act1()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 2
Write a Python script that asks the user for a string and displays the characters of the string to the user, 
with each character on a new line.
For example, if the input is Hello, the output should be:
H
e
l
l
o
-----------------------------------------------------------------------------------------------------------------------
"""
def act2():
    inputString = input("Please enter a string: ")
    for char in inputString:
        print(char)

# Uncomment the next line and run the file:
# act2()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 3
Write a Python script that computes the length of a string without using the len() function.
-----------------------------------------------------------------------------------------------------------------------
"""
def act3():
    inputString = input("Please enter a string: ")
    count = 0
    for char in inputString:
        count += 1
    print(count)

# Uncomment the next line and run the file:
# act3()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 4
Create a program that starts with a list of strings, identifies all the strings with more than two characters, 
stores the results in another list, and displays the new list.
For example:
a = ["a", "bc", "rye", "hello", "c", ""]
Output:
["rye", "hello"]
-----------------------------------------------------------------------------------------------------------------------
"""
def act4():
    a = ["a", "bc", "rye", "hello", "c", ""]
    output = []
    for i in range(0, len(a)):
        if len(a[i]) > 2:
            output.append(a[i])
    print(output)

# Uncomment the next line and run the file:
# act4()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 5
Write two scripts, each of which displays all numbers divisible by 50 between 100 and 1000 (inclusive).
Use the range function with for in one script.
Use while without range in the other script.
Both scripts should have identical outputs.
-----------------------------------------------------------------------------------------------------------------------
"""
def act5():
    output = ""
    for i in range(100, 1001):
        if i % 50 == 0:
            output += f'{i}, '
    print(output[0: len(output)-2])

def act5b():
    output = ""
    i = 100
    while i < 1001:
        if i % 50 == 0:
            output += f'{i}, '
        i += 1
    print(output[0: len(output)-2])
# Uncomment the next line and run the file:
# act5()
# act5b()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 6
Create a script that computes the sum of all numbers between 0 and 100.
-----------------------------------------------------------------------------------------------------------------------
"""
def act6():
    sum = 0
    for i in range(0, 101):
        sum += i
    print(sum)

# Uncomment the next line and run the file:
# act6()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 7
Create a script that computes the factorial of any number input by the user.
-----------------------------------------------------------------------------------------------------------------------
"""
def act7():
    inputNum = int(input("Please enter an integer: "))
    factorial = 1
    for i in range(2, inputNum+1):
        factorial *= i
    print(factorial)

# Uncomment the next line and run the file:
# act7()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 8
Starting with the defined fruit_list in the code block below, update the script to perform the following tasks.
Prompt the user to enter the name of a fruit.
If the fruit is in fruit_list, display an appropriate message to the user and tell the user its index value in 
the list.
If the fruit is not in fruit_list, display an appropriate message to the user and prompt them to try again.
The script should repeat itself until the user enters a stop word at the prompt.
fruit_list = ["apple", "banana", "cherry", "gooseberry", "kumquat", "orange", "pineapple"]
Tip
It's always a good idea to tell the user how to end a loop!
-----------------------------------------------------------------------------------------------------------------------
"""
def act8():
    fruit_list = ["apple", "banana", "cherry", "gooseberry", "kumquat", "orange", "pineapple"]
    toContinue = True
    while toContinue:
        userInput = input("Enter the name of a fruit (type 'quit' to stop): ")
        if userInput.lower() == 'quit':
            toContinue = False
            break
        inList = False
        for i in range(0, len(fruit_list)):
            if userInput.lower() == fruit_list[i]:
                print(f'{userInput} was in the list and was found at index {i}.')
                inList = True
#                toContinue = False
                break
        if not inList:
            print(f'{userInput} was not in the list, please try again.')

# Uncomment the next line and run the file:
# act8()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 9
Create a script that asks the user for a variable number of values and displays the sum of those values to the user. 
The program should prompt the user for values until the user enters the word "quit" (uppercase or lowercase), display 
the values used in the calculation, and then display the total of those values.
-----------------------------------------------------------------------------------------------------------------------
"""
def act9():
    sum = 0
    output = "The sum of ["
    toContinue = True
    while toContinue:
        userInput = input("Enter a number [type 'quit' when done]: ")
        if userInput.lower() == 'quit':
            toContinue = False
            break
        userInput = int(userInput)
        output += f'{userInput}, '
        sum += userInput
    output = output[0:len(output)-2] + f'] is: {sum}'
    print(output)

# Uncomment the next line and run the file:
# act9()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 10
Write a script that asks the user for an integer value and then displays the multiplication table of that input 
number from 1 through the integer squared.
-----------------------------------------------------------------------------------------------------------------------
"""
def act10():
    userInput = int(input('Please enter an integer: '))
    print(f'The multiplication table for {userInput} is: ')
    for i in range(1, userInput+1):
        print(f'{i}x{userInput}={i*userInput}')

# Uncomment the next line and run the file:
# act10()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 11
Create a script that identifies all prime numbers between 0 and 100.
-----------------------------------------------------------------------------------------------------------------------
"""
def act11():
    primes = []
    for i in range(2, 101):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    print(f'The primes are: {primes}')

# Uncomment the next line and run the file:
# act11()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 12
Write a script that calculates the greatest common denominator between two numbers.
For example, given the numbers 18 and 27, the greatest common denominator is 9.
-----------------------------------------------------------------------------------------------------------------------
"""
def act12():
    num1 = int(input('Please enter an integer: '))
    num2 = int(input('Please enter another integer: '))
    if num1 == num2:
        print(f'The greatest common denominator is {num1} because they are the same number.')
    else:
        biggerNum = num1 if num1 > num2 else num2
        smallerNum = num1 if num1 < num2 else num2
        for i in range(smallerNum, 0, -1):
            if biggerNum % i == 0 and smallerNum % i == 0:
                print(f'The greatest common denominator is {i}.')
                break

# Uncomment the next line and run the file:
# act12()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 13
Write a Python script that computes the frequency of each digit in a given integer.
For example, if the input number is 334, the output should be:
3 occurs 2 times
4 occurs 1 time
-----------------------------------------------------------------------------------------------------------------------
"""
def act13():
    numIn = input('Please enter an integer: ')
    nums = dict()
    for i in range(0, 10):
        nums[f'{i}'] = 0
    for i in range(0, len(numIn)):
        nums[f'{numIn[i]}'] += 1
    for k, v in nums.items():
        if v > 0:
            if v == 1:
                print(f'{k} occurs {v} time')
            else:
                print(f'{k} occurs {v} times')

# Uncomment the next line and run the file:
# act13()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 14
Write a script that calculates the lowest common multiple of two given integers.
For example, given the values 4 and 6, the lowest common multiple is 12.
-----------------------------------------------------------------------------------------------------------------------
"""
def act14():
    num1 = int(input('Please enter an integer: '))
    num2 = int(input('Please enter another integer: '))
    if num1 == num2:
        print(f'{num1} is equal to {num2}.')
    else:
        biggerNum = num1 if num1 > num2 else num2
        smallerNum = num1 if num1 < num2 else num2
        for i in range(biggerNum+1, biggerNum*smallerNum+1):
            if i % biggerNum == 0 and i % smallerNum == 0:
                print(f'The lcm of {biggerNum} and {smallerNum} is {i}.')
                break

# Uncomment the next line and run the file:
# act14()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 15
Write a Python script that determines if an input number can be expressed as the sum of two prime numbers.
For example, the number 10 can be expressed as the sum of two prime numbers:
10 = 3 + 7 : both prime numbers
10 = 5 + 5 : both prime numbers
However, the number 11 cannot be:
11 = 1 + 10 : neither 1 nor 10 are prime numbers
11 = 2 + 9 : 9 is not a prime number
11 = 3 + 8 : 8 is not a prime number
11 = 4 + 7 : 4 is not a prime number
11 = 5 + 6 : 6 is not a prime number
-----------------------------------------------------------------------------------------------------------------------
"""
def act15():
    numIn = int(input('Please enter an integer: '))
    primes = []
    for i in range(2, numIn):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    canBeDone = False
    solutions = []
    for x in range(0, len(primes)):
        for y in range(x, len(primes)):
            if primes[x] + primes[y] == numIn:
                canBeDone = True
                solutions.append(f'{primes[x]}+{primes[y]}')
    if canBeDone:
        for x in solutions:
            print(f'{numIn}={x}')
    else:
        print(f'{numIn} cannot be expressed as the sum of two primes.')
# Uncomment the next line and run the file:
# act15()