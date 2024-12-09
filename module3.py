# Lautaro Possi
# 10/12/2024
# Assignment 3

# Remember to comment for each function

#Problem 1 - Write a program that prints "Hello World" to the screen.
def print_hello():
    # Prints "Hello World" to the screen
    print "Hello World"
    
#Problem 2 - Write a program that asks the user for their name and greets them with their name. 
def hello_user():
     # Asks the user for their name and stores it in the variable 'name'
    name = input("What is your name?")
    # Greets the user using their name
    print(f"Hello,{name}!")

# Problem 3 - Compute the area of a circle 
def get_circle_area():
     # Prompts the user to enter the radius of a circle and converts the input to a float
    radius = float(input("Enter the radius of the circle:"))
    # Calculates the area of the circle using the formula πr² and stores it in 'area'
    area = 3.4159 # radius ** 2 #Area formula: πr²
    # Prints the calculated area with a message
    print(f"The area of the circle with radius {radius} is {area}")
    
#Problem 4 - Compute miles per gallon (MPG) for a car.
def get_miles_per_galoon():
    # Prompts the user to enter the number of miles driven and converts it to a float
    miles = float(input("Enter the number of miles driven: "))
    # Prompts the user to enter the number of gallons used and converts it to a float
    gallons = float(input("Enter the number of gallons used: "))
    # Calculates the miles per gallon (MPG) by dividing miles by gallons
    mpg = miles / gallons
    # Prints the MPG value with a message
    print(f"The car's MPG is {mpg}")

#Problem 5 - Convert Fahrenheit to Celsius 
def convert_temperature():
    # Prompts the user to enter the temperature in Fahrenheit and converts it to a float
    temp_f = float(input("Enter temperature in Fahrenheit: "))
     # Converts Fahrenheit to Celsius using the formula (F - 32) * 5/9
    temp_c = (temp_f - 32) * 5/9  # Conversion formula
    # Prints the converted Celsius value with a message
    print(f"{temp_f} Fahrenheit is equal to {temp_c} Celsius")


#Problem 6 - Calculate the return day after a trip 
def return_day()
# Prompts the user to enter the starting day of the week (0 for Sunday to 6 for Saturday)
    starting_day = int(input("Enter the starting day number (0 for Sunday, 6 for Saturday): "))
# Prompts the user to enter the length of their stay in days and converts it to an integer
    length_of_stay = int(input("Enter the length of your stay (in days): "))
 # Calculates the day of the week they will return on by adding the length of stay to starting day and using modulo 7

    return_day = (starting_day + length_of_stay) % 7  # Calculate return day
# Prints the day of the week they will return on with a message
    print(f"You will return on day {return_day} of the week")

#Extra Credit Problem 7 - Print leap years from 1900 to 2100. 
def extra_credit_problem_1():
     # Loops through the years from 1900 to 2100
     for year in range(1900, 2101):
    # Checks if the year is a leap year using the conditions for leap years (divisible by 4 but not 100 unless also divisible by 400)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    # Prints the year if it is a leap year
            print(year)

# Extra Credit Problem 8 - Check if a number is prime. 
def extra_credit_problem_2(n):
     # Prompts the user to enter a number and converts it to an integer
   n = int(input("Enter a number: "))
    # Checks if the number is greater than 1 (since prime numbers are greater than 1)
    if n > 1:
    # Loops through numbers from 2 to n-1 to check if n is divisible by any of them
        for i in range(2, n):
     # If n is divisible by any number between 2 and n-1, it is not a prime number
            if (n % i) == 0:
     # Prints that n is not a prime number
                print(f"{n} is not a prime number.")
    # Exits the loop since we found a divisor
                break
    # If no divisors were found, n is a prime number
        else:
    # Prints that n is a prime number
            print(f"{n} is a prime number.")
    # If n is 1 or less, it is not a prime number
    else:
     # Prints that n is not a prime number
        print(f"{n} is not a prime number.")

# Main function to run all problems
def main():
# Calls the function to print "Hello World"
    print_hello() # Problem 1
# Calls the function to greet the user by their name
    hello_user()   # Problem 2
# Calls the function to calculate and print the area of a circle
    get_circle_area()  # Problem 3
# Calls the function to calculate and print miles per gallon (MPG)
    get_miles_per_gallon()  # Problem 4
# Calls the function to convert Fahrenheit to Celsius and print the result
    convert_temperature()  # Problem 5
 # Calls the function to calculate and print the day of the week the user will return from a trip
    return_day()  # Problem 6
 # Calls the extra credit function to print all leap years from 1900 to 2100
    extra_credit_problem_1()  # Extra Credit 1
 # Calls the extra credit function to check if a number is prime
    extra_credit_problem_2()  # Extra Credit 2

    
    
    #Call the main function 
main()


    


