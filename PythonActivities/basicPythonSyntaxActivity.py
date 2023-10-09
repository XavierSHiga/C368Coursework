# --------------------------------------------------------------------------
# Activity 1
# --------------------------------------------------------------------------
# Block 1.1
# Display the text in quotation marks to an output block.
print("Python is fun!")

# --------------------------------------------------------------------------
# Block 1.2
# Display the text in quotation marks to an output block
# without moving any of the existing code to a different line.
print("Python is fun!"); print("Python is also easy.");

# --------------------------------------------------------------------------
# Block 1.3
# Display the text in quotation marks to an output block
# without moving any of the exisiting code to a different line.
print \
    ("Python is fun!")

# --------------------------------------------------------------------------
# Block 1.4
# Change each variable name to an appropriate name for Python.
# Do not use the same variable name mroe than one time.
fName = "Rebecca"
lName = "Roberts"

# --------------------------------------------------------------------------
# Block 1.5
# After changing the variable names, update the code below
# to print out each name.
print(fName)
print(lName)

# --------------------------------------------------------------------------
# Activity 2
# --------------------------------------------------------------------------
# Block 2.1
# Add a new line of code that displays the text in quotation marks
# to an output block without repeating the text in quotation marks.
output = "I love Python!"
print(output)
# - Was this one already solved for us??

# --------------------------------------------------------------------------
# Block 2.2
# Display only the text "Python is fun!" to an output block without
# deleting any of the existing code.
print("Python is fun!")
# - Really not sure what it is asking for here as it already
# - prints "Python is fun!" with just this line of code...

# --------------------------------------------------------------------------
# Activity 3
# --------------------------------------------------------------------------
# Create a script that prompts the user for the name of the state/region
# they were born in, and the name of the state/region where they currently
# live. Save each value to a variable and display the input values to the
# user.
stateBorn = input("Please enter the state/region where you were born: ")
stateCurr = input("Please enter the state/region where you currently live: ")
print("You said you were born in: " + stateBorn)
print("You said you live in: " + stateCurr)

# --------------------------------------------------------------------------
# Activity 4
# --------------------------------------------------------------------------
# Starting with the code provided below, add code to print out the title
# and released_in values. Use an f-string to output the values in this
# format: Pirates of the Caribbean: 2003
title = "Pirates of the Caribbean"
released_in = 2003
print(f"{title}: {released_in}")
