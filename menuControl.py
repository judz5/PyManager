import pyfiglet



def start():
    print(pyfiglet.figlet_format("PyManager", font = "slant"))
    print(('-'*24),' Menu ',('-'*23))
    print('1. Add Password')
    print('2. Website/App Search')
    print('3. Find Connected Accounts')
    print('-'*55)
    return input()

3