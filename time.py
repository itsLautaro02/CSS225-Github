# Ask the user to input the current time (as a string), and store it in 'currentTimeStr'
currentTimeStr = input("What is the current time (in hours 0-23)? ")

# Ask the user to input the number of hours they want to wait (as a string), and store it in 'waitTimeStr'
waitTimeStr = input("How many hours do you want to wait? ")

# Convert 'currentTimeStr' from a string to an integer and store it in 'currentTimeInt'
currentTimeInt = int(currentTimeStr)

# Convert 'waitTimeStr' from a string to an integer and store it in 'waitTimeInt'
waitTimeInt = int(waitTimeStr)

# Add 'currentTimeInt' and 'waitTimeInt' to get the final time and store it in 'finalTimeInt'
finalTimeInt = currentTimeInt + waitTimeInt

# Print the value of 'finalTimeInt'
print(finalTimeInt)
