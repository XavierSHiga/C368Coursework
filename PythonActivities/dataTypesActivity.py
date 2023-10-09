import math
# -----------------------------------------------------------------------------------------
# Activity 1 -
# Create a computer program that performs the following steps:
#   1. Prompt the user for an integer and store the value in a variable
#   2. Display the data type of the variable that holds the entered data.
#   3. Convert the value to an integer type and store the converted value in a new variable.
#   4. Display the value and type of the new variable in a single sentence.
#       (For example, "The value is 8 with type integer.")
#   5. Run the program and enter a float value at the prompt. What is its value in the last step?
# Refactor the program, using a float instead of an integer. What happens if you enter an integer
# rather than a float at the prompt?
# -----------------------------------------------------------------------------------------
def act1():
    inputValue = input('Please enter an integer: ')
    print(type(inputValue))
    convertedValue = int(inputValue)
    print(f'The value is {convertedValue} with type {type(convertedValue)}.')

# Uncomment next line and run file:
# act1()



def act1Float():
    inputValue = input('Please enter a float: ')
    print(type(inputValue))
    convertedValue = float(inputValue)
    print(f'The value is {convertedValue} with type {type(convertedValue)}.')

# Uncomment next line and run file:
# act1Float()

# -----------------------------------------------------------------------------------------
# Activity 2 -
# Update the code below so that the result is equal to 576. Do not change any of the existing
# values or operators or the order in which they appear.
#   1|# do not change the order in which the numbers and operators appear in the next line
#   2|result = 5 + 3 ** 2 * 9
#   3|
#   4| print(result) # the output should be 576
# -----------------------------------------------------------------------------------------
def act2():
    # do not change the order in which the numbers and operators appear in the next line
    result = (5 + 3) ** 2 * 9
    print(result)


# Uncomment next line and run file:
# act2()

# -----------------------------------------------------------------------------------------
# Activity 3 -
# Create a computer program that prompts the user for a float number and returns the integer
# portion of the floating number.
# -----------------------------------------------------------------------------------------
def act3():
    inputValue = input('Please enter a float: ')
    print('The integer portion of your number is: ' + str(int(float(inputValue))))


# Uncomment the next line and run file:
# act3()

# -----------------------------------------------------------------------------------------
# Activity 4 -
# Write a computer program that calculates and displays the current value of a deposit for
# a given initial deposit, interest rate, how many times interest is calculated per year,
# and the number of years since the initial deposit.
# The program should prompt the user for each of the values and use the following formula
# to calculate the current value of the deposit:
#   V = P(1 + r/n)^nt
# where:
#   V -- value
#   P -- initial deposit
#   r -- interest rate as a fraction (eg 0.05)
#   n -- the number of times per year interest is calculated
#   t -- the number of years since the initial deposit
# The program should display each of the values entered to the user in a meaningful way
# (so that the user can easily see what each value represents), along with the results
# of the calculation.
# -----------------------------------------------------------------------------------------
def act4():
    p = float(input('Please enter the initial deposit: '))
    r = float(input('Please enter the interest rate: '))
    n = int(input('Please enter the number of times per year interest is calculated: '))
    t = int(input('Please enter the number of years since the initial deposit: '))
    V = p * (1 + r/n)**(n*t)
    print(f'The initial deposit entered: {p} \n\
        The interest rate entered: {r} \n\
        The number of times per year interest is calculated entered: {n} \n\
        The number of years since the initial deposit entered: {t} \n\
        The current value of the deposit: {V:.2f}')

# Uncomment the next line and run file:
# act4()

# -----------------------------------------------------------------------------------------
# Activity 5 -
# Write a computer program that prompts the user for a principal amount, the rate of interest,
# and the number of days for a loan and then calculates and returns the simple interest for the
# life of the loan. Use the formula:
#   interest = principal * rate * days / 365
# -----------------------------------------------------------------------------------------
def act5():
    p = float(input('Please enter the principal amount: '))
    r = float(input('Please enter the rate of interest: '))
    d = int(input('Please enter the number of days of the loan: '))
    interest = p * r * d / 365
    print(f'The simple interest for the life of the loan is: {interest:.2f}')

# Uncomment the next line and run file:
# act5()


# -----------------------------------------------------------------------------------------
# Activity 6 -
# Create a computer program that displays three statements to evaluate to True and three
# statements that evaluate to False.
# Example:
#   a = 0
#   b = 1
#   Output: a < b = True
# -----------------------------------------------------------------------------------------
def act6():
    a = 2
    b = 5
    print(f'a < b = {a<b}')
    print(f'a % 2 == 0 = {a%2==0}')
    print(f'a != b = {a!=b}')
    print(f'a >= b = {a>=b}')
    print(f'b % 2 == 0 = {b%2==0}')
    print(f'a == b = {a==b}')

# Uncomment the next line and run the file:
# act6()

# -----------------------------------------------------------------------------------------
# Activity 7 -
# Create a computer program that prompts the user for a number and calculates the following:
#   - the boolean of the number entered
#   - the binary equivalent of the number entered
#   - the square root of the number entered
# The program should display the following to the user:
#   - The number the user entered, in a phrase like, "You selected {value}"
#   - The boolean of the number, in a phrase like, "The boolean of your number is {value}"
#   - The binary equivalent of the number, in a phrase like, "The binary equivalent of your
#     number is {value}"
#   - The square root of the number, in a phrase like, "The square root of your number is
#     {value}" with the value rounded to three decimal places
# -----------------------------------------------------------------------------------------
def act7():
    inputNum = int(input('Please enter a number: '))
    print(f'You selected: {inputNum}')
    print(f'The boolean of your number is: {bool(inputNum)}')
    print(f'The binary equivalent of your number is: {bin(inputNum)}')
    print(f'The square root of your number is: {math.sqrt(inputNum):.3f}')

# Uncomment the next line and run the file:
# act7()


# -----------------------------------------------------------------------------------------
# Activity 8 -
# Create a computer program that completes the following tasks:
#   - It prompts the user for a series of 5 integers.
#       - The user must be prompted for 5 numbers.
#   - After the fifth entry, the program stops prompting for values and performs the following
#     calculations:
#       - the product of the integers
#       - the average of the integers
#       - the sum of the integers
#   - After performing the calculations, the program should display the following to the user:
#       - the values the user entered
#       - each of the calculations, using a phrase that identifies the value
# -----------------------------------------------------------------------------------------
def act8():
    i = 0
    inputNums = []
    outputString = ''
    while i < 5:
        inputNums.append(int(input('Please enter an integer: ')))
        i += 1
    for i in range(0, len(inputNums)):
        outputString += f'{inputNums[i]}, '
    product = 1
    for i in range(0, len(inputNums)):
        product *= inputNums[i]
    sum = 0
    for i in range(0, len(inputNums)):
        sum += inputNums[i]
    avg = sum / len(inputNums)
    print(f'The numbers you entered were: {outputString[:-2]}')
    print(f'The product of the integers is: {product}')
    print(f'The sum of the integers is: {sum}')
    print(f'The average of the integers is: {avg}')

# Uncomment the next line and run the file:
# act8()


# -----------------------------------------------------------------------------------------
# Activity 9 -
# Write a program that performs the following steps:
#   - Start with a street address that includes a building/house number, the name of the street,
#     and the type of street (e.g., Street, Avenue, Boulevard, etc.).
#       - You can use any address you wish and abbreviations are acceptable.
#       - An example is 25 Main Street
#   - Display the full address to the user.
#   - Display the house number only in a phrase like, "The building or house number is 25."
#   - Display the street name in a phrase like, "The street name is Main Street."
# -----------------------------------------------------------------------------------------
def act9():
    inputAddress = input('Please enter a street address (123 Something Street): ')
    print(f'The full address you entered was: {inputAddress}')
    indexOfFirstSpace = inputAddress.index(' ')
    print(f'The building or house number is: {inputAddress[:indexOfFirstSpace]}')
    print(f'The street name is: {inputAddress[indexOfFirstSpace+1:]}')



# Uncomment the next line and run the file:
# act9()