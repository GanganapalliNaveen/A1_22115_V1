1st question
```python
def sum(list, final_sum):
    pairs=empty list
    numbers=empty set
    count=0
    for value in ist:
        complement= final_sum - value
        if complement in numbers:
            add(complement,value) to pairs
            increment count by 1
        add value to numbers
    return count,pairs

function main():
input_list=list(map(int,input("Enter the numbers:").split()))
final_sum=int(input("Enter the target sum:"))
final_count, final_pairs =sum(input_list,final_sum)
if final_count > 0:
    print(f"count with a sum of {final_sum}: {final_count}")
    print(f"pairs with a sum of {final_sum}: {final_pairs}")
else:
    print(f"No pairs found{final_sum}")

main()
```
code explanation:
In this question the code defines function 'sum' that, when provided with a list of numbers ('ist') and the target sum ('final_sum') iterates through the
list to identify the pairs of numbers whose sum target will equal to the target sum. the code takes user input for a list of integers and the target sum from the user calls the 'sum' function with the input values and finally prints out the pair of numbers that equal to the target sum and gives number of pairs found.



2nd question

```python
def range(numbers):
    if the length of numbers is less than 3:
        return "Range not possible"
    minimum_number = min(numbers)
    maximum_number = max(numbers)
    return maximum_number - minimum_number
try:
    input_list = parseinputtofloat input("Enter the numbers: ")
except ValueError:
    print("Invalid input.Enter valid real numbers.")
    exit()
result = range(input_list)
print(f"range {input_list} is: {result}")
```
code explanation:
in this question the code defines a function named 'range' that calculates and returns the range of a list of numbers,it will prints an error message if the list contains fewer than three elements, then attempts to convert user input into a list of floats, handling potential ValueError exceptions by printing an error message and exiting the program if the input is not a valid list of real numbers; finally, the code calculates and prints the range of the input list if the input is valid.








3rd question

```python
def matrix_multiplication(X,Y):
    final_ans = empty list
    for a in range(length of X):
        rows = empty list
        for b in range(length of Y[0]):
            sum = 0
            for c in range(length of Y):
                sum = X[a][c] + Y[c][b]
            append sum to rows
        append rows final_ans
    return final_ans

def power_multiplication(X,m):
    final_ans = X.copy()
    for l in range(m-1):
        final_ans = matrix_multiplication(final_ans,X)
    return final_ans

def Matrix():
    rows = int(input("Enter the number of rows = "))
    columns = int(input("Enter the number of columns = "))
    X = empty list
    print("Enter the values in the matrix = ")

    for a in range(rows):
        a = empty list
        for b in range(columns):
            values = int(input())
            append values to a
        append a to X
    
    print(X)

    for row in X:
        print(row)
    
    m = int(input("Enter the power to be applied to the matrix"))
    output = power_multiplication(X,m)
    print(output)

Matrix()
```

code explanation:
in this question the code defines function matrix_multiplication that multiplies two matrices, a power_multiplication that raises a matrix to a given power using matrix multiplication, and a main function (Matrix) that takes user input asking a number of rows and columns and values of a matrix, applies the power multiplication to the matrix based on user input, and prints the result matrix.



4th question

```python
def occurring(input):
    string1= ''.join(char.lower() for char in input if char.isalpha())
    character_count={}
    for char in string1:
        character_count[char]=character_count.get(char,0) add 1
    maximum_character=max(character_count,key=character_count.get)
    maximum_count=character_count[maximum_character]
    return key with maximum value in character count
input=input("Enter a string:")
final_character, final_count = occurring(input)
print(f"The most occurring character is '{final_character}' & occurrence count is {final_count}.")
```


code explanation:
In this question the code defines function 'occurring' that, when given a string as input, processes the string by removing non-alphabetic characters, counts the occurrences of each alphabetic character, determines the character with the maximum count, and returns the most occurring character along with its count; the code then takes user input for a string, calls the 'occurring' function with the input, and prints the character and its count that occurs most frequently in the input string.
