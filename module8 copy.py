# Function to check if two numbers are equal without using an if statement
def p1(a, b):
    # I used the == operator because it directly checks if the two numbers are the same
    return a == b  # This returns True if a equals b, otherwise False

# Function to check if the sum of two numbers is larger than, less than, or equal to 10
def p2(a, b):
    # First, calculate the sum of the two numbers
    sum_value = a + b
    # Use if-elif-else to check the conditions
    if sum_value > 10:
        return "larger than 10"
    elif sum_value == 10:
        return "equal to 10"
    else:
        return "less than 10"

# Recursive function to check if the number 5 is in a list
def p3(arr):
    # Base case: If the list is empty, 5 is not in it
    if not arr:
        return False
    # Check the first element, or continue checking the rest of the list
    return arr[0] == 5 or p3(arr[1:])

# Function to check if a year is a leap year
def p4(year):
    # A year is a leap year if it is divisible by 4,
    # but not divisible by 100 unless also divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

####################################################################################################

# Character class with attributes and methods
class character:
    # Constructor to initialize nickname, weapons, and weaknesses
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname  # Character's nickname
        self.weapons = weapons  # List of weapons
        self.weaknesses = weaknesses  # List of weaknesses

    # Method to return the nickname
    def get_model(self):
        return self.nickname

    # Method to return the weapons
    def get_year(self):
        return self.weapons

    # Method to return the weaknesses
    def get_color(self):
        return self.weaknesses

    # Method to return a complete profile of the character
    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

# Creating an instance of the character class
player1 = character('', '', '')  # Initialize with empty values
player1.nickname = 'Dragon Slayer'  # Set nickname to "Dragon Slayer"
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']  # List of weapons
player1.weaknesses = ['slow']  # List of weaknesses

# Loop through weapons and print each one
for item in player1.weapons:
    print("Weapon: ", item)

# Loop through weaknesses and print each one
for debuff in player1.weaknesses:
    print("Weakness: ", debuff)

####################################################################################################

# Testing the functions

# Test for p1 (checking equality)
print("p1(3, 3):", p1(3, 3))  # Should return True because 3 == 3
print("p1(3, 4):", p1(3, 4))  # Should return False because 3 != 4

# Test for p2 (checking sum comparison)
print("p2(4, 6):", p2(4, 6))  # Should return "equal to 10" because 4 + 6 = 10
print("p2(3, 2):", p2(3, 2))  # Should return "less than 10" because 3 + 2 = 5
print("p2(8, 5):", p2(8, 5))  # Should return "larger than 10" because 8 + 5 = 13

# Test for p3 (checking if 5 is in the list)
print("p3([1, 2, 3, 4, 5]):", p3([1, 2, 3, 4, 5]))  # Should return True because 5 is in the list
print("p3([1, 2, 3, 4]):", p3([1, 2, 3, 4]))  # Should return False because 5 is not in the list

# Test for p4 (checking leap year)
print("p4(2020):", p4(2020))  # Should return True because 2020 is a leap year
print("p4(2021):", p4(2021))  # Should return False because 2021 is not a leap year
print("p4(1900):", p4(1900))  # Should return False because 1900 is not a leap year
print("p4(2000):", p4(2000))  # Should return True because 2000 is a leap year
