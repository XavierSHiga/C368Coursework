import numpy as np
import pandas as pd
"""
-----------------------------------------------------------------------------------------------------------------------
The activities on this page allow you to demonstrate your ability to:
Create, manipulate, and analyze data using NumPy arrays and Pandas dataframes.
Perform mathematical operations, aggregation, and sorting on data.
-----------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------
Activity 1
Create a NumPy array with 20 random integers between 1 and 100.
Compute and display only the mean, median, and standard deviation of the values in the array.
-----------------------------------------------------------------------------------------------------------------------
"""
def act1():
    arrRandom = np.random.randint(1, 101, size=(1, 20))
    print(f'Mean: {arrRandom.mean()}')
    print(f'Median: {np.median(arrRandom)}')
    print(f'Standard Deviation: {arrRandom.std()}')


# Uncomment the next line and run the file:
# act1()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 2
Create a 5x5 NumPy array with random integers between 1 and 50.
Calculate and display the sum of each row and each column.
-----------------------------------------------------------------------------------------------------------------------
"""
def act2():
    arrRandom = np.random.randint(1, 51, size=(5, 5))
    print(arrRandom)
    print(f'Sum of rows: {arrRandom.sum(axis=1)}')
    print(f'Sum of cols: {arrRandom.sum(axis=0)}')


# Uncomment the next line and run the file:
# act2()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 3
Create a Pandas DataFrame from the following dictionary:
data = {
    "Product": ["Apple", "Banana", "Orange", "Grape", "Watermelon"],
    "Price": [1.5, 0.75, 1, 2, 4],
    "Quantity": [10, 20, 30, 5, 8]
}
Calculate and display the total value of each product (Price * Quantity).
-----------------------------------------------------------------------------------------------------------------------
"""
def act3():
    data = {
        "Product": ["Apple", "Banana", "Orange", "Grape", "Watermelon"],
        "Price": [1.5, 0.75, 1, 2, 4],
        "Quantity": [10, 20, 30, 5, 8]
    }
    dataDF = pd.DataFrame(data)
    dataDF['Total'] = dataDF['Price'] * dataDF['Quantity']
    print('Product: Total')
    print('---------------------------')
    for i in range(0, len(dataDF['Product'])):
        print(f'{dataDF["Product"].iloc[i]}: {dataDF["Total"].iloc[i]}')


# Uncomment the next line and run the file:
# act3()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 4
Load the dataset provided below into a Pandas DataFrame and perform the following tasks:
Calculate and display the average age of all passengers.
Calculate and display the number of passengers who survived.
Calculate and display the percentage of passengers who survived.
import pandas as pd
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic = pd.read_csv(url)
-----------------------------------------------------------------------------------------------------------------------
"""
def act4():
    titanicDF = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
#    pd.set_option('display.max_columns', None)
#    print(titanicDF.head())
    print(f"Average Age: {np.mean(titanicDF['Age'])}")
    print(f"Number of passengers who survived: {len(titanicDF[titanicDF['Survived'] == 1])}")
    print(f"Percentage of passengers who survived: {(len(titanicDF[titanicDF['Survived']==1])/len(titanicDF['PassengerId']))*100:.2f}")


# Uncomment the next line and run the file:
# act4()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 5
Using the Titanic dataset from the previous activity, calculate and display the following:
The average age of the passengers who survived.
The average age of the passengers who did not survive.
The number of passengers who survived, grouped by gender.
The number of passengers who did not survive, grouped by gender.
-----------------------------------------------------------------------------------------------------------------------
"""
def act5():
    titanicDF = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
    print(f"Average age of survivors: {np.mean(titanicDF[titanicDF['Survived']==1]['Age']):.0f}")
    print(f"Average age of non-survivors: {np.mean(titanicDF[titanicDF['Survived']==0]['Age']):.0f}")
    print(f"Number of passengers that survived by gender: {titanicDF[titanicDF['Survived']==1].groupby(['Sex'])['PassengerId'].count()}")
    print(f"Number of passengers that did not survive by gender: {titanicDF[titanicDF['Survived']==0].groupby(['Sex'])['PassengerId'].count()}")
#    pd.set_option('display.max_columns', None)
#    print(f'{titanicDF.head()}')


# Uncomment the next line and run the file:
# act5()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 6
Using the same Titanic dataset from the earlier activities, create a new DataFrame that includes only the 
following columns:
"PassengerId"
"Survived"
"Pclass"
"Name"
"Sex"
"Age"
"Fare"
Sort this DataFrame by "Fare" in descending order and display the first 10 rows.
-----------------------------------------------------------------------------------------------------------------------
"""
def act6():
    titanicDF = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
    newDF = titanicDF[['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Fare']]
    newDF = newDF.sort_values(by='Fare', ascending=False)
    pd.set_option('display.max_columns', None)
    print(newDF.head(10))



# Uncomment the next line and run the file:
# act6()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 7
Create a Pandas DataFrame with the following data:
grades = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Math": [90, 80, 85, 95, 75],
    "Science": [85, 95, 80, 75, 90],
    "English": [80, 85, 90, 75, 95]
}
Calculate and display the average grade for each student and the average grade for each subject.
-----------------------------------------------------------------------------------------------------------------------
"""
def act7():
    grades = {
        "Student": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Math": [90, 80, 85, 95, 75],
        "Science": [85, 95, 80, 75, 90],
        "English": [80, 85, 90, 75, 95]
    }
#    gDF = pd.DataFrame(grades, index=grades['Student'])
    gDF = pd.DataFrame(grades)
    gDF = gDF.set_index(gDF.columns[0])
    print(f"{gDF.mean(numeric_only=True, axis=1).round(2)}")
    print(f"{gDF.mean(numeric_only=True)}")


# Uncomment the next line and run the file:
# act7()
"""
-----------------------------------------------------------------------------------------------------------------------
Activity 8
Using the grades DataFrame from the previous activity, create a new column named "Status" with the following criteria:
If a student's average grade is 90 or above, the status should be "Excellent."
If a student's average grade is between 80 and 89, the status should be "Good."
If a student's average grade is below 80, the status should be "Needs Improvement."
Display the updated DataFrame with the new "Status" column.
-----------------------------------------------------------------------------------------------------------------------
"""
def act8():
    grades = {
        "Student": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Math": [90, 80, 85, 95, 75],
        "Science": [85, 95, 80, 75, 90],
        "English": [80, 85, 90, 75, 95]
    }
    gDF = pd.DataFrame(grades, index=grades['Student'])
    gDF['Avg'] = (gDF['Math'] + gDF['Science'] + gDF['English'])/3
    status = []
    for row in gDF['Avg']:
        if row >= 90:
            status.append('Excellent.')
        elif row >= 80:
            status.append('Good.')
        else:
            status.append('Needs Improvement')
    gDF['Status'] = status
    print(gDF.head())


# Uncomment the next line and run the file:
# act8()