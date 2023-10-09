"""
-----------------------------------------------------------------------------------------------------------------------
The following activities are provided to allow you to demonstrate the objectives of this lesson:
    - Use an if statement to determine the outcome of a program.
    - Use an if-else statement to define two potential outcomes.
    - Use nested if statements to define more than two potential outcomes.
    - Use match-case statements to match conditions to a value based on patterns.
Complete each activity and make sure that the code runs without errors before beginning the next activity.
-----------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------
Activity 1
Write a program that asks the user how much money they have in their wallet. The program should output "You're rich!"
if the user inputs $20 or more and "You're broke!" if the input is less than $20.
-----------------------------------------------------------------------------------------------------------------------
"""
def act1():
    money = int(input("Enter how much money you have in your wallet (Only dollar amounts): $"))
    if money >= 20:
        print("You're rich!")
    else:
        print("You're broke!")
# Uncomment the next line and run the file:
# act1()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 2
Write a program that performs the following steps:
    - Ask the user if they own any cats. (Yes/No answer)
    - Ask the user if they own any dogs. (Yes/No answer)
    - If the user responses indicate that they have both cats and dogs, output "You must really love pets!"
    - Otherwise, the output should be: "Maybe you need more pets."
The last step will apply if the user has cats but not dogs, dogs but not cats, or neither cats nor dogs.
Write three different versions of this program, one that uses only if statements, one that uses if-else statements,
and a third that uses the ternary version of if-else.
-----------------------------------------------------------------------------------------------------------------------
"""
def act2():
    cats = input("Do you own any cats (yes/no): ")
    dogs = input("Do you own any dogs (yes/no): ")
    if cats.lower() == 'yes' and dogs.lower() == 'yes':
        print("You must really love pets!")
    else:
        print("Maybe you need more pets.")


def act2b():
    cats = input("Do you own any cats (yes/no): ")
    dogs = input("Do you own any dogs (yes/no): ")
    catsTrue = True
    dogsTrue = True
    if cats.lower() != 'yes':
        catsTrue = False
    if dogs.lower() != 'yes':
        dogsTrue = False
    if catsTrue and dogsTrue:
        print("You must really love pets!")
    if not catsTrue or not dogsTrue:
        print("Maybe you need more pets.")

def act2c():
    cats = input("Do you own any cats (yes/no): ")
    dogs = input("Do you own any dogs (yes/no): ")
    output = "You must really love pets!" if cats.lower() == 'yes' and dogs.lower() == 'yes' else "Maybe you need more pets."
    print(output)
# Uncomment the next line and run the file:
# act2()
# act2b()
# act2c()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 3
Write a quiz that asks the user a few questions to which the user will respond either True or False. 
Display all the questions with the correct answer and the user's answers at the end of the program, along 
with the user's the correct response rate (number of questions answered correctly/number of questions).
-----------------------------------------------------------------------------------------------------------------------
"""
def act3():
    questions = ['5 > 3', '1000 < 5', 'Python is easy', 'Water is wet']
    answers = ['true', 'false', 'true', 'false']
    guesses = []
    print("Your quiz is about to begin, please enter either True or False for each question.")
    for i in range(0, len(questions)):
        guesses.append(input(f'{questions[i]}: ').lower())
    correct = 0
    for x in range(0, len(answers)):
        print(f'For question: {questions[x]}')
        print('-------------------------------------------------------')
        print(f'You answered: {guesses[x]}')
        print(f'Correct answer: {answers[x]}')
        print('-------------------------------------------------------')
        if guesses[x] == answers[x]:
            correct += 1
    print(f'You got {(correct/len(questions))*100:.2f}% correct.')

# Uncomment the next line and run the file:
# act3()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 4
Write a program that uses elif to produce five different possible outcomes based on a single user input.
    - Ask the user what season it is (fall, winter, spring, or summer).
    - If the user enters fall, output "I bet the leaves are pretty there!"
    - If the user enters winter, output "I hope you're ready for snow!"
    - If the user enters spring, output "I can smell the flowers!"
    - If the user enters summer, output "Make sure your AC is working!"
    - If the user enters a value that does not correspond to a season, output "I don't recognize that season."
The user should be able to enter the name of the season in any case and the program will still work.
Challenge: After you have the program working as described above, modify the program to use match-case instead. 
In a single case clause, allow the user to enter either "fall" or "autumn", for the same result.
-----------------------------------------------------------------------------------------------------------------------
"""
def act4():
    season = input('Please enter the current season (fall, winter, spring, summer): ').lower()
    if season == 'fall':
        print('I bet the leaves are pretty there!')
    elif season == 'winter':
        print("I hope you're ready for snow!")
    elif season == 'spring':
        print('I can smell the flowers!')
    elif season == 'summer':
        print('Make sure your AC is working!')
    else:
        print("I don't recognize that season.")


# def act4b():
#     season = input('Please enter the current season (fall, winter, spring, summer): ').lower()
#     match season:
#         case 'fall' | 'autumn':
#             print('I bet the leaves are pretty there!')
#         case 'winter':
#             print("I hope you're ready for snow!")
#         case 'spring':
#             print("I can smell the flowers!")
#         case 'summer':
#             print("Make sure your AC is working!")
#         case _:
#             print("I don't recognize that season.")
# Uncomment the next line and run the file:
# act4()