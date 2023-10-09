import os
import sys
import requests
import json
"""
-----------------------------------------------------------------------------------------------------------------------
The following exercises allow you to demonstrate your understanding of the Python libraries:
os
sys
requests
-----------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------
Activity 1
Write a program that creates a new directory named "my_folder". Use the os.path.exists() method
to check whether the directory already exists before creating it. If it already exists, ask the user if
they want to delete the directory and create a new one, or if they want to use the existing directory.
-----------------------------------------------------------------------------------------------------------------------
"""
def act1():
    fPath = os.path.join(os.getcwd(), 'my_folder')
    if os.path.exists(fPath):
        makeNew = input('Directory already exists, would you like to overwrite the current directory (y/n): ').lower()
        if makeNew == 'y':
            os.rmdir(fPath)
            os.mkdir(fPath)
    else:
        os.mkdir(fPath)


# Uncomment the next line and run the file:
# act1()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 2
Write a program that lists all the files and directories in the current working directory.
Use the os.listdir() method to list all the files and directories, and the os.path.isdir() method to determine 
which items in the list are directories.
Print out only the directories in the list, sorted in alphabetical order. You can use the sorted() function to 
sort the list, like so:
my_list = [8, 1, 5, 3, 9, 2]
my_sorted_list = sorted(my_list)
print(my_list)
print(my_sorted_list)
Output:
[8, 1, 5, 3, 9, 2]
[1, 2, 3, 5, 8, 9]
-----------------------------------------------------------------------------------------------------------------------
"""
def act2():
    allFiles = os.listdir()
    folders = []
    for x in allFiles:
        if os.path.isdir(x):
            folders.append(x)
    sortedFolders = sorted(folders)
    print(folders)
    print(sortedFolders)


# Uncomment the next line and run the file:
# act2()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 3
Write a program that changes the current working directory to "my_folder".
Use the os.chdir() method to change the current working directory and the os.getcwd() method to print out the 
new current working directory.
If the directory does not exist, ask the user if they want to create it.
-----------------------------------------------------------------------------------------------------------------------
"""
def act3():
    newPath = os.path.join(os.getcwd(), 'my_folder')
    if os.path.exists(newPath):
        os.chdir(newPath)
        print(os.getcwd())
    else:
        toCreate = input('my_folder does not exist, would you like to create it (y/n): ').lower()
        if toCreate == 'y':
            os.mkdir(newPath)
            os.chdir(newPath)
            print(os.getcwd())



# Uncomment the next line and run the file:
# act3()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 4
Write a program that prompts the user for a filename and then creates a new file with that name.
Use with and the open() function to create a new file with the name entered by the user.
Use the write() method to write some data to the file.
If the file already exists, ask the user if they want to overwrite it or append to it.
If they choose to append, add some new data to the end of the file.
-----------------------------------------------------------------------------------------------------------------------
"""
def act4():
    fName = input('Enter the name of a file you would like to create: ')
    fPath = os.path.join(os.getcwd(), fName)
    if os.path.exists(fPath):
        print(f'{fName} already exists.')
        toEdit = input('Would you like to overwrite (w) or append (a) to it: ').lower()
        if toEdit == 'w' or toEdit == 'a':
            with open(fPath, toEdit) as file:
                file.write("Adding some data...")
    else:
        with open(fPath, 'w') as file:
            file.write('Making a new file...')


# Uncomment the next line and run the file:
# act4()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 5
Write a script that takes a file path as a command-line argument and reads the contents of the file.
The program should count the number of words in the file and print the count.
-----------------------------------------------------------------------------------------------------------------------
"""
def act5():
    fPath = sys.argv[1]
    with open(fPath, 'r') as file:
        print(len(file.read().split(' ')))


# Uncomment the next line and run the file:
# act5()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 6
Write a script that accepts a single command-line argument that can be either start or stop.
If the command-line argument is start, the script should print a message indicating that a process has started.
If the command-line argument is stop, the script should print a message indicating that the process has stopped.
If the command-line argument is not one of these values, the script should exit with an exit status of 1.
-----------------------------------------------------------------------------------------------------------------------
"""
def act6():
    userInput = sys.argv[1].lower()
    if userInput == 'start':
        print('Process has started.')
    elif userInput == 'stop':
        print('Process has stopped.')
    else:
        sys.exit(1)


# Uncomment the next line and run the file:
# act6()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 7
Write a program that sends a POST request to the URL https://httpbin.org/post with a JSON payload.
The payload should contain a dictionary with three keys: username, password, and email.
Prompt the user for values for these keys and include them in the payload.
The program should then display the status code and JSON response.
-----------------------------------------------------------------------------------------------------------------------
"""
def act7():
    uName = input('Enter a username: ')
    pWord = input('Enter a password: ')
    email = input('Enter an email: ')
    payload = {
        'username': uName,
        'password': pWord,
        'email': email
    }
    payloadJSON = json.dumps(payload)
    response = requests.post('https://httpbin.org/post', data=payloadJSON)
    print(response.text)
    print(response.status_code)


# Uncomment the next line and run the file:
# act7()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 8
Write a program that sends a GET request to the URL https://httpbin.org/image/png and saves the image to 
the filesystem. You will need to open the file with the 'wb' file mode, where "wb" stands for "write binary."
-----------------------------------------------------------------------------------------------------------------------
"""
def act8():
    response = requests.get('https://httpbin.org/image/png')
    with open(os.path.join(os.getcwd(), 'my_folder', 'testing.png'), 'wb') as file:
        file.write(response.content)



# Uncomment the next line and run the file:
# act8()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 9
Write a program that:
Prompts the user for their favorite fruit, color, and number.
Creates a dictionary containing the user's input with the keys: fruit, color, and number.
Encodes the dictionary into a JSON formatted string.
Writes the JSON string to a file named "favorites.json".
Reads the file "favorites.json" and converts the JSON formatted string back into a dictionary.
Prints the dictionary, mentioning the user's favorite fruit, color, and number in a sentence.
-----------------------------------------------------------------------------------------------------------------------
"""
def act9():
    prompts = ['fruit', 'color', 'number']
    uInfo = dict()
    for i in range(0, len(prompts)):
        uInfo[prompts[i]] = input(f'Enter your favorite {prompts[i]}: ')
#    uInfoJSON = json.dumps(uInfo)
    with open(os.path.join(os.getcwd(), 'my_folder', 'favorites.json'), 'w') as file:
        json.dump(uInfo, file)
    with open(os.path.join(os.getcwd(), 'my_folder', 'favorites.json'), 'r') as file:
        readInfo = json.load(file)
#    readInfo = json.load(os.path.join(os.getcwd(), 'my_folder', 'favorites.json'))
    print(readInfo)


# Uncomment the next line and run the file:
# act9()