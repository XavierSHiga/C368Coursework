"""
-----------------------------------------------------------------------------------------------------------------------
The activities on this page allow you to demonstrate your ability to:
Store, retrieve, and manipulate a data collection using a dictionary with defined index values.
Store, retrieve, and manipulate data in a set.
-----------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------
Activity 1
Create a program that sums all the values in a dictionary and displays the sum, with a message that indicates it.
For example, if we have the following dictionary:
dictionary = {"hello": 4, "world": 4, "I": 1, "am": 2, "Martha": 3}
The program should output:
The sum of values is 14.
-----------------------------------------------------------------------------------------------------------------------
"""
dictionary = {"hello": 4, "world": 4, "I": 1, "am": 2, "Martha": 3}
def act1(d):
    sum = 0
    for v in d.values():
        sum += v
    print(f'The sum of the values is {sum}')
# Uncomment the next line and run the file:
# act1(dictionary)
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 2
Write a program that displays the maximum and minimum values in a dictionary. You may use the same dictionary you
used in the previous activity or create a new one.
-----------------------------------------------------------------------------------------------------------------------
"""
def act2(d):
    max = 'First'
    min = 'First'
    for v in d.values():
        if max == 'First':
            max = v
            min = v
        else:
            if v > max:
                max = v
            if v < min:
                min = v
    print(f'The max is {max} and the min is {min}.')

# Uncomment the next line and run the file:
# act2(dictionary)
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 3
Write a program that returns the sum of the integer elements in a set.
-----------------------------------------------------------------------------------------------------------------------
"""
testSet = {1, 5, 10, "Blue", 11}
def act3(s):
    sum = 0
    for i in s:
        if type(i) == int:
            sum += i
    print(f'The sum is {sum}.')
# Uncomment the next line and run the file:
# act3(testSet)
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 4
Write a program that computes and displays the maximum and the minimum values in a set.
-----------------------------------------------------------------------------------------------------------------------
"""
def act4(s):
    max = 'First'
    min = 0
    for i in s:
        if type(i) == int:
            if max == 'First':
                max = i
                min = i
            else:
                if i > max:
                    max = i
                if i < min:
                    min = i
    if max == 'First':
        print("No numbers found in the set.")
    else:
        print(f'The max is {max} and the min is {min}.')

# Uncomment the next line and run the file:
# act4(testSet)
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 5
Given the following dictionary storage, complete the following tasks:
Add a key named "freezer".
Set the value of "freezer" to be a list containing the items "ice cubes", "ice cream", and "pepperoni pizza".
Sort the items in the cupboard using sort.
Add "cream" to the fridge.
Remove "sugar" from the cupboard.
Subtract $25 from the emergency jar.
storage = {
    "cupboard": ["spices", "flour", "sugar"],
    "drawer": ["fork", "knife", "spoon"],
    "fridge": ["butter", "milk", "cheese"],
    "emergency jar": 150
}
-----------------------------------------------------------------------------------------------------------------------
"""
storage = {
    "cupboard": ["spices", "flour", "sugar"],
    "drawer": ["fork", "knife", "spoon"],
    "fridge": ["butter", "milk", "cheese"],
    "emergency jar": 150
}
def act5(d):
    d['freezer'] = ['ice cubes', 'ice cream', 'pepperoni pizza']
    d['cupboard'].sort()
    d['fridge'].append('cream')
    d['cupboard'].remove('sugar')
    d['emergency jar'] = d['emergency jar'] - 25
    print(d)
# Uncomment the next line and run the file:
# act5(storage)
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 6
Create a new dictionary named shopping_list and add the following items to the dictionary:
"milk" : 4,
"butter" : 2,
"crackers" : 1.5,
"rice" : 2.25,
"spaghetti" : 1.75,
"dish soap": 3.25
Loop through each item in the list and print out each key with its price. Print the answer in this format:
milk
----
price: 4
butter
------
price: 2
Next, calculate how much it will cost if you purchase all the items on the list.
Use a variable named total_cost to store the calculated value.
Loop through the dictionary and add the price of each item to the total cost.
After looping through the dictionary, print out the total cost in a message that is meaningful to the user.
-----------------------------------------------------------------------------------------------------------------------
"""
def act6():
    shopping_list = {"milk": 4, "butter": 2, "crackers": 1.5, "rice": 2.25, "spaghetti": 1.75, "dish soap": 3.25}
    total_cost = 0
    for k, v in shopping_list.items():
        print(k)
        print('-----------')
        print(f'price: {v}')
        total_cost += v
    print(f'The total comes out to: {total_cost}')

# Uncomment the next line and run the file:
# act6()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 7
Create two dictionaries: price and quantity.
The price dictionary should be the same as the shopping_list dictionary in the previous activity:
"milk" : 4,
"butter" : 2,
"crackers" : 1.5,
"rice" : 2.25,
"spaghetti" : 1.75,
"dish soap": 3.25
The quantity dictionary should have the same keys, but with values that represent the number of items to purchase 
rather than the price:
"milk" : 1,
"butter" : 1,
"crackers" : 3,
"rice" : 2,
"spaghetti" : 5,
"dish soap": 1
Write a script that loops through both dictionaries to calculate the total cost if we purchase the indicated quantity 
of each item in the dictionaries.
-----------------------------------------------------------------------------------------------------------------------
"""
def act7():
    price = {"milk": 4, "butter": 2, "crackers": 1.5, "rice": 2.25, "spaghetti": 1.75, "dish soap": 3.25}
    quantity = {"milk": 1, "butter": 1, "crackers": 3, "rice": 2, "spaghetti": 5, "dish soap": 1}
    cost = 0
    for k, v in quantity.items():
        print(k)
        print(f'quantity: {v}')
        print(f'price: ${price[k]:.2f}')
        print(f'cost: ${v * price[k]:.2f}')
        print('------------------------')
        cost += v*price[k]
    print(f'That brings your total to: ${cost:.2f}')

# Uncomment the next line and run the file:
# act7()