import pyfiglet, re
from data_control import *


def pw_query():
    password = input('Enter Master Password : ')
    password2 = input('Re-Enter Master Password : ')
    if(password != password2):
        print('Passwords do not match!')
        pw_query()
    else:
        return password

def title():
    print(pyfiglet.figlet_format("PyManager", font = "slant"))

def menu():
    print(('-'*24),' Menu ',('-'*23))
    print('1. Add Account')
    print('2. Account Search')
    print('3. All Accounts')
    print('4. Exit')
    print('-'*55)
    select = input()
    if(select == '1'):
        add_account()
    elif(select == '2'):
        find_account()
    elif(select == '3'):
        account_list()
    elif(select == '4'):
        quit()
    else:
        print("ERROR... ABORTING")
        quit()

def add_account():
    print(('-'*21)," Add Account ",('-'*21))
    print("Welcome to the Account Adder!")
    print("If You Do Not Wish to Answer A Field, Simply Press Enter.\n")
    app_name = input('Enter Name of App / Website : ')
    url = input('Enter the Website URL : ')
    email = input('Enter Account Email : ')
    username = input('Enter Account Username : ')
    password = input('Enter Account Password : ')
    send(password, email, username, url, app_name)
    print("Done!")
    menu()

def find_account():
    print(('-'*19)," Account Search",('-'*19))
    app_name = input("Enter Name of App / Website : ")
    print("Searching...\n")
    find_pass(app_name)
    menu()

def account_list():
    print(('-'*20)," Account List ",('-'*19))
    print()
    accounts = all_accounts()

    keyList = {}

    for i, account in enumerate(accounts):
        formatted = re.split(r"'(.*?)'", str(account))
        print(i+1,".",formatted[1],"     ")
        keyList[str(i+1)] = formatted[1]

    choice = input("\nEnter the Number of the Account You Want to View : ")

    print(('-'*20)," Account Info ",('-'*19))

    find_pass(keyList.get(choice))
    menu()



    

