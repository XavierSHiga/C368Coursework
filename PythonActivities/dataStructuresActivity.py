"""
------------------------------------------------------------------------------------------------------------
Activity 1
Prompt the user to answer a series of 3–5 questions about themselves (such as their name,
their age, their birthday, or where they live) and save the answers in a list. Display
the results to the user.
------------------------------------------------------------------------------------------------------------
"""
def act1():
    prompts = ['your name', 'your age', 'where you live']
    inputResponses = []
    i = 0
    while i < len(prompts):
        inputResponses.append(input(f'Please enter {prompts[i]}: '))
        i += 1
    for x in range(0, len(inputResponses)):
        print(f'You entered {inputResponses[x]} for {prompts[x]}.')


# Uncomment the next line and run the file:
# act1()
"""
------------------------------------------------------------------------------------------------------------
Activity 2
- Present the user with an existing list of items (such as the list created in the previous activity).
- Prompt the user for 2–4 more values to add to the list.
- Update the list with the new values.
- Display the updated list.
------------------------------------------------------------------------------------------------------------
"""
def act2():
    shoppingList = ['Banana', 'Apple', 'Fries']
    print('Your current shopping list includes: ')
    for item in shoppingList:
        print(item)
    end = False
    while not end:
        tempItem = input('Please enter another item to add to your shopping list (enter n to end): ')
        if (tempItem.lower() == 'n'):
            end = True
            break
        else:
            shoppingList.append(tempItem)
    print('Your updated shopping list now includes: ')
    for item in shoppingList:
        print(item)

# Uncomment the next line and run the file:
# act2()
"""
------------------------------------------------------------------------------------------------------------
Activity 3
- Present the user with a list of 7–9 items (such as the list created in the previous activities).
- Prompt them to enter a value to delete from the list by value, not by index.
- Delete the value from the list.
- Display the updated list.
------------------------------------------------------------------------------------------------------------
"""
def act3():
    shoppingList = ['Turtle', 'Orange', 'Car', 'Light', 'Bike', 'Computer', 'Hamster']
    print('Your current shopping list includes: ')
    for item in shoppingList:
        print(item)
    inList = False
    removeItem = ''
    print('Your shopping list has too many items!')
    while not inList:
        removeItem = input('Please enter an item to remove from your shopping list: ')
        if removeItem in shoppingList:
            print(f'Removing {removeItem} from your list now...')
            shoppingList.remove(removeItem)
            inList = True
        else:
            print(f'{removeItem} was not on your list!')
    print('Your updated shopping list now includes: ')
    for item in shoppingList:
        print(item)



# Uncomment the next line and run the file:
# act3()
"""
------------------------------------------------------------------------------------------------------------
Activity 4
- Present the user with a list of 7–9 items (such as the list created in the previous activities).
- Prompt them to select one value from the list to update, along with the new value.
- Change the selected value to the new value and display the updated list to the user.
Tip
Look up how to identify the index of a specific value in a list.
------------------------------------------------------------------------------------------------------------
"""
def act4():
    shoppingList = ['Turtle', 'Orange', 'Car', 'Light', 'Bike', 'Computer', 'Hamster']
    print('Your current shopping list includes: ')
    for item in shoppingList:
        print(item)
    updateItem = ''
    newItem = ''
    inList = False
    while not inList:
        tempItem = input('Please enter an item from the list to update: ')
        if tempItem in shoppingList:
            updateItem = tempItem
            newItem = input(f'Please enter what you would like to change {updateItem} to: ')
            inList = True
        else:
            print(f'{tempItem} is not an item on your list!')
    print(f'Changing {updateItem} to {newItem}...')
    uItemIndex = shoppingList.index(updateItem)
    shoppingList[uItemIndex] = newItem
    print('Your new list now includes: ')
    for item in shoppingList:
        print(item)


# Uncomment the next line and run the file:
# act4()
"""
------------------------------------------------------------------------------------------------------------
Activity 5
Create four tuples:
    - A tuple with a person's first name and last name.
    - A tuple with the person's current profession and the year they started in it.
    - A tuple with the person's current address.
    - A tuple with the person's previous address.
Combine all tuples into a new, flattened, single tuple that contains all items from the original tuples.
------------------------------------------------------------------------------------------------------------
"""
def act5():
    tuple1 = ('Xavier', 'Higa')
    tuple2 = ('Scientist', 2019)
    tuple3 = ('123 Main Street',)
    tuple4 = ('321 2nd Avenue',)
    theUltimateTuple = tuple1 + tuple2 + tuple3 + tuple4
    print(theUltimateTuple)

# Uncomment the next line and run the file:
# act5()
"""
------------------------------------------------------------------------------------------------------------
Activity 6
Create a tuple that contains the following:
    - A person's first name and last name as a string.
    - A list containing the titles of the person's favorite movies.
Then perform the following:
    - Display the tuple to the user.
    - Ask the user to provide a new favorite movie to the list.
    - Append the new movie to the list of favorite movies within the tuple.
    - Display the updated tuple to the user.
Tip
While the tuple itself is immutable, the list within the tuple is mutable, so you can modify its contents.
------------------------------------------------------------------------------------------------------------
"""
def act6():
    t = ('Sam Smith', ['Die Hard', 'Lilo & Stitch', 'Home Alone'])
    print(t)
    print(f"{t[0]}'s favorite movies are: ")
    for item in t[1]:
        print(item)
    t[1].append(input('Please enter another favorite movie: '))
    print(f"{t[0]}'s favorite movies are now: ")
    for item in t[1]:
        print(item)

# Uncomment the next line and run the file:
# act6()

