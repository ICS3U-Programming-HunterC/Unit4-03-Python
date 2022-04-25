#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: April 24, 2022
# This program asks the user to enter a whole number
# it then calculates the It then uses a for loop  to calculate
# the power of two of each number from 0 until that number.


def main():

    # Get the user input as a string
    user_input_string = input("Enter a whole number: ")
    print("")

    try:
        # get the user number
        user_input = int(user_input_string)

        if user_input < 0:
            print("That is not a whole number")
        else:
            for counter in range(user_input + 1):
                power_of_two = counter**2
                print("{}^2 = {}".format(counter, power_of_two))

    except Exception:
        print("That is not a number!!")


if __name__ == "__main__":
    main()
