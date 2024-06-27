import pyfiglet, re, string, random
from data_control import *


def pw_query():
    password = input('\nEnter Master Password : ')
    return password

def title():
    print(pyfiglet.figlet_format("PyManager", font = "slant"))

def menu():
    print()
    print(('-'*24),' Menu ',('-'*23))
    print('1. Add Account')
    print('2. Account Search')
    print('3. All Accounts')
    print('4. Exit')
    print('5. Configure DB')
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
    elif(select == '5'):
        setup_db()
    else:
        print("ERROR... ABORTING")
        quit()

def add_account():
    print()
    print(('-'*21)," Add Account ",('-'*21))
    print("Welcome to the Account Adder!")
    print("If You Do Not Wish to Answer A Field, Simply Press Enter.\n")
    app_name = input('Enter Name of App / Website : ')
    url = input('Enter the Website URL : ')
    email = input('Enter Account Email : ')
    username = input('Enter Account Username : ')

    while(True):
        generate_bool = input("Would you like to Generate a password? (y/n): ")
        if(validate_input(generate_bool)):
            break
        else:
            "Invalid input!"
    
    if(generate_bool.lower() == 'y'):
        password = generate_password()
    else:
        password = input('Enter Account Password : ')
    send(password, email, username, url, app_name)
    print("Done!")
    menu()

def find_account():
    print()
    print(('-'*19)," Account Search",('-'*19))
    print()

    app_name = input("Enter Name of App / Website : ")
    print("Searching...\n")
    find_pass(app_name)
    menu()

def account_list():
    print()
    print(('-'*20)," Account List ",('-'*19))
    print()
    accounts = all_accounts()

    keyList = {}

    for i, account in enumerate(accounts):
        formatted = re.split(r"'(.*?)'", str(account))
        print(i+1,".",formatted[1],"     ")
        keyList[str(i+1)] = formatted[1]

    choice = input("\nEnter the Number of the Account You Want to View : ")

    print()
    print(('-'*20)," Account Info ",('-'*19))
    print()

    find_pass(keyList.get(choice))
    menu()

def generate_password():
    length = int(input("Enter Password Length: "))

    special_characters = '!@#$%^&*'

    while(True):
        letter_bool = input("Use Letters (y/n): ")
        if(validate_input(letter_bool)):
            break
        else:
            print("invalid input!")

    while(True):
        digit_bool = input("Use Digits (y/n): ")
        if(validate_input(digit_bool)):
            break
        else:
            print("invalid input!")

    while(True):
        specChar_bool = input("Use Speical Characters (y/n): ")
        if(validate_input(specChar_bool)):
            break
        else:
            print("invalid input!")
    
    chars = ''
    if(letter_bool.lower() == 'y'):
        chars += string.ascii_letters
    if(digit_bool.lower() == 'y'):
        chars += string.digits
    if(specChar_bool.lower() == 'y'):
        chars += special_characters
    
    if not chars:
        print("Invalid selections!")
        return None

    password = ''
    for i in range(length):
        password += random.choice(chars)

    print("Generated Password : " + password)
    return password


def validate_input(choice): 
    if(choice.lower() != "y" and choice.lower() != "n"):
        return False
    return True


    

