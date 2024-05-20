from Services import register_services
from Services import login_services

import sys

def r_and_l():
    print("====================================================")
    print("Hello, welcome to this service!! How can I help you?", end="\n\n")
    print("[1] I want to register my new account.")
    print("[2] I want to log in with my account.")
    print("[3] Nothing. Thank you. I would quit.")
    print("====================================================", end="\n")

    user_choice = input("Enter your choice: ")

    while True:
        if user_choice == "1" or user_choice == "2" or user_choice == "3":
            break
        else:
            print("\nInvalid input. Please try again.")
            user_choice = input("Enter your choice: ")

    if user_choice == "1":
        register()
    elif user_choice == "2":
        login()
    elif user_choice == "3":
        quit()


def register():
    print("Sign Up")

def login():
    print("Log In")

def quit():
    exit()