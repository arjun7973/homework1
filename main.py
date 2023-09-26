#task1
print("Hello, Replit!")

#task2
Variable1 = 5
Variable2 = 6.5
Variable3 = "Hi this is Arjun"
Variable4 = True

print(type(Variable1))
print(type(Variable2))
print(type(Variable3))
print(type(Variable4))

#test case for task2

#The code  provided assigns values to four different variables (Variable1, Variable2, Variable3, and Variable4) and then uses the type() function to determine and print the data type of each variable. Here's what the code will output:

#arduino
#Copy code
#<class 'int'>
#<class 'float'>
#<class 'str'>
#<class 'bool'>
#Here's a breakdown of the output:

#Variable1 has a value of 5, which is an integer, so its data type is <class 'int'>.
#Variable2 has a value of 6.5, which is a floating-point number (decimal), so its data type is <class 'float'>.
#Variable3 has a value of "Hi this is Arjun", which is a string (text), so its data type is <class 'str'>.
#Variable4 has a value of True, which is a boolean value representing True, so its data type is <class 'bool'>.

#task3
def number_check(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"


number1 = 8
number2 = -8
number3 = 0

print(number_check(number1))
print(number_check(number2))
print(number_check(number3))


#b
def isprime(num):
  if num <= 1:
    return False
  return all(num % i != 0 for i in range(2, num))


list1 = []
num = 2
while len(list1) <= 8:
  if isprime(num):
    list1.append(num)
  num += 1

print(list1)


#c
# Add the sum_numbers function
def sum_numbers():
  Sum_number = 0
  for i in range(1, 101):
    Sum_number += i
  return Sum_number


Sum_number = 0
for i in range(1, 101):
  Sum_number += i
print(Sum_number)

#test case for task4

#Part A: number_check Function
#This part defines a function number_check(number) that takes an input number and returns whether it's positive, negative, or zero.

#number1, number2, and number3 are assigned values 8, -8, and 0, respectively.
#The number_check function is called with each of these numbers, and the results are printed.
#Part B: Prime Number Generator
#This part defines a function isprime(num) that checks whether a given number num is prime or not. It then generates a list of the first 9 prime numbers (starting from 2) using a while loop and adds them to list1.

#An empty list list1 is initialized.
#A variable num is initialized to 2.
#A while loop runs until list1 contains 9 prime numbers.
#Inside the loop, the isprime function is used to check if num is prime.
#If num is prime, it's added to list1.
#num is incremented in each iteration of the loop.
#Part C: Sum of Numbers
#This part defines a function sum_numbers() that calculates the sum of numbers from 1 to 100. It then calculates and prints the sum of numbers from 1 to 100 using both the sum_numbers function and a separate loop.

#The sum_numbers function calculates the sum using a for loop.
#The result is stored in the variable Sum_number and returned by the function.
#Then, a separate for loop is used to calculate and print the sum of numbers from 1 to 100 without using the sum_numbers function.
#Overall, this code appears to be a set of functions and code snippets for performing various tasks such as classifying numbers as positive, negative, or zero, generating prime numbers, and calculating the sum of numbers. It should work as intended.

#task4
def calculate_discount(price, discount):
  return price - (price * discount / 100)


def main():
  total_price_input = float(input("Enter the total price: "))
  discount_input = float(input("Enter the discount percentage: "))

  discounted_price = calculate_discount(total_price_input, discount_input)

  print("Discounted Price:", discounted_price)


if __name__ == "__main__":
  main()
  
  #test case for task4

#The calculate_discount function takes two parameters: price (the total price of the product) and discount (the discount percentage). It calculates the discounted price by subtracting the product of the price and the discount percentage divided by 100 from the original price.

#The main function is the entry point of the program. It does the following:

#It prompts the user to enter the total price using the input function and converts the input to a floating-point number using float.
#It then prompts the user to enter the discount percentage using the input function and also converts the input to a floating-point number.
#It calls the calculate_discount function with the entered total price and discount percentage as arguments and stores the result in the discounted_price variable.
#Finally, it prints the discounted price to the console.
#The if __name__ == "__main__": condition ensures that the main function is executed when the script is run directly, but not when it is imported as a module in another script.

#When we run this script, it will ask the user to enter the total price and the discount percentage, and then it will calculate and display the discounted price.

#Here's an example of how the program might run:

#yaml
#Copy code
#Enter the total price: 100.0
#Enter the discount percentage: 10.0
#Discounted Price: 90.0
#In this example, the user entered a total price of 100.0 and a discount percentage of 10.0, so the discounted price is calculated as 100.0 - (100.0 * 10.0 / 100) = 90.0.

#task5
favorite_books = [
    {"Title": "The Great Gatsby", "Author": "Fitzgerald F. Scott"},
    {"Title": "To Kill A Mockingbird", "Author": "Harper Lee"},
    {"Title": "The Catcher In The Rye", "Author": "Salinger"},
    {"Title": "The Old Man And The Sea", "Author": "Ernest Hemingway"},
    {"Title": "Little Women", "Author": "Louisa May Alcott"},
    {"Title": "The Grace Of Kings", "Author": "Ken Liu"},
    {"Title": "Kings Of Gold", "Author": "Leigh Bardugo"}
]

print(favorite_books[:2])

student_database = {
    "Thor": "C201",
    "Alen": "C202",
    "Babar": "C203",
    "Amar": "C204",
    "Elven": "C205",
    "Faser": "C206",
    "Jhony": "C207"
}

print(student_database["Amar"])
print(student_database["Alen"])

#test case for task 5

#We have a list called favorite_books which contains dictionaries representing books with their titles and authors.

#We use slicing to print the first two elements of the favorite_books list, which are books at indices 0 and 1. This will print the information of the first two favorite books:

#python
#Copy code
#[{'Title': 'The Great Gatsby', 'Author': 'Fitzgerald F. Scott'}, {'Title': 'To Kill A Mockingbird', 'Author': 'Harper Lee'}]
#We have a dictionary called student_database which maps student names to their classroom codes.

#We print the classroom code for the student named "Amar" using student_database["Amar"], which will output "C204".

#Similarly, we print the classroom code for the student named "Alen" using student_database["Alen"], which will output "C202".

#So, the code will produce the following output:

#css
#Copy code
#[{'Title': 'The Great Gatsby', 'Author': 'Fitzgerald F. Scott'}, {'Title': 'To Kill A Mockingbird', 'Author': 'Harper Lee'}]
#C204
#C202

#task6
def count_words_in_file(file_path):
    try:
        with open(file_path, "r") as file:
            text = file.read()
            words = text.split()
        return len(words)
    except FileNotFoundError:
        return 0  # Return 0 words if the file is not found
    except Exception as e:
        return -1  # Return -1 to indicate an error occurred

# Example usage:
file_path = "demo.txt"  # Change this to the path of your file
word_count = count_words_in_file(file_path)

if word_count == 0:
    print("File path not found.")
elif word_count == -1:
    print("An error exists while reading the file.")
else:
    print(f"Word count in '{file_path}': {word_count}")

#test case for task6

#The code you provided defines a function count_words_in_file(file_path) that counts the number of words in a text file specified by the file_path. It handles two main exceptions: FileNotFoundError and a general Exception that can occur while reading the file. Depending on the situation, it returns the word count, 0 if the file is not found, or -1 if an error occurs. It then demonstrates the usage of this function.

#Here's a breakdown of the code:

#It defines a function count_words_in_file(file_path) that takes a file path as input.

#Inside the function, it attempts to open the file specified by file_path in read mode ("r").

#If the file is successfully opened, it reads the contents of the file into the text variable and splits the text into words using the split() method.

#It returns the count of words in the file using len(words).

#If the file specified by file_path is not found (raises a FileNotFoundError), it returns 0.

#If any other exception occurs during file reading (caught by the general Exception), it returns -1 to indicate that an error occurred.

#The example usage section demonstrates how to call the count_words_in_file function, specifying the file path as an argument. It then prints the result based on the return value of the function.

#Note: Make sure to replace "demo.txt" with the actual path to the file you want to analyze.

  #task7
import numpy as np
def calculate_statistics(values):
    mean = np.mean(values)
    std_deviation = np.std(values)
    return mean, std_deviation

# Example list of values
list1 = [10, 20, 30, 40, 50]

# Calculate statistics
mean, std_deviation = calculate_statistics(list1)

print("List of values:", np.array(list1))
print("Mean:", mean)
print("Standard Deviation:", std_deviation)

#test case for task7

#It imports the NumPy library as np.

#It defines a function called calculate_statistics(values) that takes a list of values as its input.

#Inside the calculate_statistics function:

#It calculates the mean of the input values using np.mean(values).
#It calculates the standard deviation of the input values using np.std(values).
#It returns both the mean and standard deviation as a tuple.
#It defines an example list of values named list1 containing [10, 20, 30, 40, 50].

#It calls the calculate_statistics function with list1 as an argument and assigns the returned mean and standard deviation to the variables mean and std_deviation, respectively.

#Finally, it prints the list of values, mean, and standard deviation.

#When you run this code, it will output the following:

#yaml
#Copy code
#List of values: [10 20 30 40 50]
#Mean: 30.0
#Standard Deviation: 15.811388300841896
#It displays the list of values, the calculated mean, and the calculated standard deviation of the input list.