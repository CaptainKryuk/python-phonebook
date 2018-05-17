import re

phonebook = {}


def add_name():
    name = input('\nAdd new name: ')
    if len(name) < 3:
        print("Name must be more than 2 letters. Try again")
        add_name()
    elif len(name) > 20:
        print("Name must be smaller than 20 letters. Try again")
        add_name()
    else:
        phonebook[name] = None
        add_number(name)


def add_number(name):
    number = input("\nAdd phone number now: ")
    phonebook[name] = number
    answer = input("Number was successfully added. Do you want add one more number [Y/N]: ")
    if answer == 'Y' or 'y':
        add_name()
    elif answer == "N" or 'n':
        print('Thank\'s for using programm, BB!')
        raise SystemExit


def start():
    d = input("What would you want to do? \n"
              "\"add name\" for new name; \n"
              "\"exit\" for leave; -- > ")
    if d == 'exit':
        print("Program was finished without error")
        raise SystemExit
    elif d == 'add name':
        add_name()
    else:
        print("Add correct (!) command")
        start()


if __name__ == '__main__':
    start()


