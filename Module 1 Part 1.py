#!/usr/bin/env python
# Program to simulate a basic login system
# Author: Lautaro Possi
# Date: 2024-10-01
# This program prompts the user for a username and grants or denies access based on predefined usernames.
username = input("Login: >> ")
# Taking the username input from the user
user1 = "Jack"
# Predefined user1
user2 = "Jill"
# Predefined user2
if username == user1:
    # Checking if the entered username matches predefined usernames
    print("Access granted")
    # If username is "Jack", grant access
elif username == user2:
    print("Welcome to the system") 
     # If username is "Jill", display a welcome message
else:
    print("Access denied")
# For any other username, deny access