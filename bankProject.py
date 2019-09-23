# Author: Dylan Murphy
# Name: bankProject.py
# Student Number: R00152607

# note:
# - for inputs that should be an int or float, I leave them as a string and convert them after they are entered as to
# avoid getting the program to exit on an error and to have easier error checking.

# imported this to use the 'randint()' function for getting a random account number.
from random import randint


# This function loads in data from the bank.txt text file and
# stores the data in 3 separate lists.
def load_files(account_number, balance, name):
    # opens file to use later.
    file = open("bank.txt")
    # creates a loop reading each line in the file.
    for line in file:
        if line != "":
            # breaks the string 'line' into parts to separate 3 pieces of data.
            items = line.split()
            # takes each piece of data per line and sorts them into lists.
            account_number.append(int(items[0]))
            balance.append(float(items[1]))
            name.append(items[2])
    # close the file because we are finished with it for now.
    file.close()


# this function is the main part of what you see when the program runs.
# It displays all the options for the different functions and gives an easy way to navigate to them.
def menu(account_number, balance, name):
    # print statements to show information on how to use this part of the function.
    print("We have a number of options to choose from, would you like to:")
    print("1.Open new account")
    print("2.Close an account")
    print("3.Deposit")
    print("4.Withdraw")
    print("5.generate report")
    print("6.Quit")
    print("please enter the number of your choice e.g enter \"3\" to withdraw from your account.")
    # this input will
    choice = input("would you like to to >>>")
    # if the user chooses '1' then it will run the open_account function.
    if choice == "1":
        print("open account")
        open_account(account_number, balance, name)

    # if the user chooses '2' then it will run the close_account account function.
    elif choice == "2":
        print("close account")
        close_account(account_number, balance, name)

    # if the user chooses '3' then it will run the deposit function.
    elif choice == "3":
        print("deposit")
        deposit(account_number, balance, name)

    # if the user chooses '4' then it will run the withdraw function.
    elif choice == "4":
        print("withdraw")
        withdraw(account_number, balance, name)

    # if the user chooses '5' then it will run the generate_report function.
    elif choice == "5":
        print("report")
        generate_report(account_number, balance, name)

    # if the user chooses '6' then it will run the quit_program function.
    elif choice == "6":
        print("quit")
        quit_program(account_number, balance, name)

    # if the user enters anything else then an error message will display, the function will be recalled to run again.
    else:
        print()
        print("Invalid entry.")
        print("\n\n\n\n\n\n\n")
        menu(account_number, balance, name)


# this function gets details and creates an account.
def open_account(account_number, balance, name):
    print("\n\n")
    # finds a random account number and assigns that to the account being created.
    account_num = randint(100000, 999999)
    # making sure the account number generated does not already exist in the list of account numbers.
    while account_num in account_number:
        account_num = randint(100000, 999999)
    # getting details for account data.
    fullname = input("what is your name >>>")
    # this add the new account data to the respective lists.
    account_number.append(account_num)
    balance.append(0)
    name.append(fullname)
    # this loops trough the account numbers and displays the info for the customer to note their account number.
    i = 0
    while i < len(account_number):
        if account_number[i] == account_num:
            # prints account details.
            print("Your details:")
            print("Name: ", name)
            print("Balance: ", balance)
            print("Account number: ", account_number)
            print("-----------------------------")
        i += 1
    # this is just a way to get back to the menu when finished in the current function.
    finished = input("when finished here just press the enter key.")
    if finished == "" or finished != "":
        menu(account_number, balance, name)


# this function gets an account number and deletes all data connected to that account number.
def close_account(account_number, balance, name):
    print("\n\n\n")
    # just getting the account number to delete data later.
    account_num = input("What is your account number?")
    # making sure the data entered is a number.
    while account_num.isnumeric() is False:
        print("Account number must be a number.")
        account_num = input("What is your account number?")
    # checks to see that the input is within the range of account numbers.
    if 100000 < int(account_num) < 999999:
        # loops though to get the position of the input account number.
        i = 0
        while i < len(account_number):
            try:
                if str(account_number[i]) == account_num:
                    # creating variable for ease of removing from the list.
                    r_num = account_number[i]
                    r_bal = balance[i]
                    r_name = name[i]
                    # removing data from the list.
                    account_number.remove(r_num)
                    balance.remove(r_bal)
                    name.remove(r_name)
                    # could also be done this way:
                    # account_number.remove(account_number[i])
                    # balance.remove(balance[i])
                    # name.remove(name[i])

                    # printing a small bit of information so the user knows the account has successfully been closed.
                    print("Your account has been closed.")
                    print("We are sorry to see you go!")
                    print("-----------------------------")
                i += 1
            except ValueError:
                print("Account number not found")
                close_account(account_number, balance, name)
    # this is in the case that the input is outside the range of account numbers.
    else:
        print("Invalid entry")
        close_account(account_number, balance, name)
    # this is just a way to get back to the menu when finished in the current function.
    finished = input("when finished here just press the enter key.")
    if finished == "" or finished != "":
        print("\n\n")
        menu(account_number, balance, name)


# this function is to let the user deposit into the selected account.
def deposit(account_number, balance, name):
    print("\n\n\n")
    # just getting the account number to deposit later.
    account_num = input("What is your account number?")
    # making sure the data entered is a number.
    while account_num.isnumeric() is False:
        # a try accept to check if the variable can be set as an integer.
        try:
            int(account_num)
        except ValueError:
            print("Account number must be a number.")
            deposit(account_number, balance, name)
    # checks to see that the input is within the range of account numbers.
    if 100000 < int(account_num) < 999999:
        # loops though to get the position of the input account number.
        i = 0
        while i < len(account_number):
            try:
                if str(account_number[i]) == account_num:
                    # input for amount the user wants to deposit.
                    add_on = input("How much would you like to deposit >>>")
                    # error checking too make sure the input is a float.
                    while add_on.isnumeric() is False:
                        # a try accept to check if the variable can be set as a float.
                        try:
                            float(add_on)
                        except ValueError:
                            print("The data entered must be number to deposit.")
                            deposit(account_number, balance, name)
                    # checking to see that the input is negative.
                    while float(add_on) < 0:
                        print("You must deposit a positive number.")
                        add_on = float(input("How much would you like to deposit >>>"))
                    # setting the new balance.
                    balance[i] = balance[i] + float(add_on)
                    print("Your new balance is", balance[i])
                    print("-----------------------------")
                i += 1
            except ValueError:
                print("Account number not found")
                deposit(account_number, balance, name)
    # this is in the case that the input is outside the range of account numbers.
    else:
        print("Invalid entry.")
        deposit(account_number, balance, name)
    # this is just a way to get back to the menu when finished in the current function.
    finished = input("when finished here just press the enter key.")
    if finished == "" or finished != "":
        print("\n\n")
        menu(account_number, balance, name)


def withdraw(account_number, balance, name):
    print("\n\n\n")
    # just getting the account number to withdraw later.
    account_num = input("What is your account number?")
    # making sure the data entered is a number
    while account_num.isnumeric() is False:
        # a try accept to check if the variable can be set as an integer.
        try:
            int(account_num)
        except ValueError:
            print("Account number must be a number.")
            withdraw(account_number, balance, name)
    # making sure the data entered is a number.
    while account_num.isnumeric() is False:
        print("Account number must be a number")
        account_num = input("What is your account number?")
    # checks to see that the input is within the range of account numbers.
    if 100000 < int(account_num) < 999999:
        # loops though to get the position of the input account number.
        i = 0
        while i < len(account_number):
            try:
                if str(account_number[i]) == account_num:
                    # input for amount the user wants to withdraw
                    minus = input("How much would you like to withdraw >>>")
                    # error checking too make sure the input is a float
                    # while minus.isnumeric() is False:
                    # a try accept to check if the variable can be set as a float.
                    #    try:
                    #        float(minus)
                    #    except ValueError:
                    #        print("The data entered must be  number to withdraw.")
                    #        withdraw(account_number, balance, name)
                    # making sure the amount in the account balance allows for the deduction of the withdrawal amount.
                    print(minus, balance[i])
                    if float(minus) <= balance[i]:
                        balance[i] -= float(minus)
                        print("Your new balance is", "%.2f" % balance[i])
                    # if the withdrawal amount is greater than the balance this deals with getting new withdraw amount.
                    else:
                        print("you are trying to withdraw more than whats in your account.")
                        print("you only have", "%.2f" % balance[i], "available.")
                        withdraw(account_number, balance, name)
                    print("-----------------------------")
                i += 1
            except ValueError:
                print("Account number not found")
                withdraw(account_number, balance, name)
    # this is in the case that the input is outside the range of account numbers.
    else:
        print("Invalid entry.")
        deposit(account_number, balance, name)
    # this is just a way to get back to the menu when finished in the current function.
    finished = input("when finished here just press the enter key.")
    if finished == "" or finished != "":
        print("\n\n")
        menu(account_number, balance, name)


def generate_report(account_number, balance, name):
    print("\n\n\n")
    # some information to the user.
    print("Restricted access please enter a supervisor code to proceed or press enter to return to the previous menu.")
    validation = input("Supervisor number >>>")
    # validate the supervisor code.
    if int(validation) == 7346 or int(validation) == 1717:  # supervisor codes are '1717' and '7346'.
        print("\n")
        # a. Details of all accounts.
        i = 0
        print("Account number - Balance - Name of account holder")
        # his prints details of each account on separate lines.
        while i < len(account_number):
            print("\t\t " + str(account_number[i]) + " - " + str(balance[i]) + " - " + str(name[i]))
            i += 1
            # b. Total amount on deposit in the bank.
        print()
        # displays the total amount in the bank by getting the sum of all balances.
        print("Bank contains:", "%.2f" % sum(balance))
        # c. Largest amount on deposit specifying the account holder(s).
        i = 0
        maximum = 0
        max_name = ""
        print()
        while i < len(account_number):
            # if the current balance is larger than the current maximum then the new max is set as the current balance.
            if maximum < balance[i]:
                maximum = balance[i]
                max_name = name[i]
            # this is in case multiple accounts have the same balance that is also the highest.
            elif maximum == balance[i]:
                max_name += ", " + name[i]
            i += 1
        # shows the maximum amount in one persons balance and the name of the account owner.
        print("largest amount in one account is", "%.2f" % maximum, "that is in the account with the name(s)", max_name)
        print("-----------------------------")
        # this is just a way to get back to the menu when finished in the current function.
        finished = input("when finished here just press the enter key.")
        if finished == "" or finished != "":
            print("\n\n")
            menu(account_number, balance, name)
    # this is for normal users that want to go back to the menu
    elif validation == "":
        menu(account_number, balance, name)
    # this is in the case that the input is not a supervisor code.
    else:
        print("That is not a valid supervisor code.")
        generate_report(account_number, balance, name)


def quit_program(account_number, balance, name):
    # this opens the bank.txt file to write to it.
    # i use 'w+' to overwrite the file as to not create duplicates.
    file = open("bank.txt", "w+")
    # loops to write all the current data stored in lists back to the file.
    i = 0
    while i < len(account_number):
        # adds all data from just one account to a variable.
        text = str(account_number[i]) + " " + str(balance[i]) + " " + str(name[i]) + "\n"
        # writes the data into the file in the form of a variable.
        file.write(str(text))
        i += 1
    # close the file because we are done with it which is good practice.
    file.close()
    # closes program.
    exit()


# main method to run the functions.
def main():
    # created empty lists to store the data seen above.
    account_number = []
    balance = []
    name = []
    # calling load_files so the lists are set up to be used at any time.
    load_files(account_number, balance, name)
    # calling the menu to run the bulk of the program.
    menu(account_number, balance, name)


# calling the 'main()' function so that the program actually does something.
main()
