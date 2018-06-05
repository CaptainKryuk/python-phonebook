#!/usr/bin/python

import re
"""Agenda telefonica insert nume telefon
    $ python phonebook.py
    -- > "add name" and "exit"
"""
phonebook = {} #Dictionary

class Contact:
    """Clasa Contact care creaza contactele
    Args:
        nume
        prenume
        telefon
    """
    nr_contacte = 0
    
    def __init__(self, nume, prenume, nr_telefon):
        self.nume = nume
        self.prenume = prenume
        self.nr_telefon = nr_telefon
        Contact.nr_contacte += 1
        
    def afiseazaNumarContacte(self):
        print "Numarul total de contacte %d" % Contact.nr_contacte
        
    def afiseazaContact(self):
        print "Numar Contact: ",Contact.nr_contacte
        print "Nume: ", self.nume," Prenume: ", self.prenume, "Tel: ", self.nr_telefon

def add_Contact():
    name = input('\nAdd new name: ')
    if len(name) < 3:
        print("Name must be more than 2 letters. Try again")
        add_Contact()
    elif len(name) > 20:
        print("Name must be smaller than 20 letters. Try again")
        add_Contact()
    else:
        phonebook[name] = None
        add_number(name)

def addContact():
    nume = input("Introduceti numele contactului: ")
    prenume = input("Introduceti prenumele contactului: ")
    nr_telefon = input("Introduceti numarul de telefon: ")
    cont = Contact(nume, prenume, nr_telefon)
    cont.afiseazaContact()
    phonebook[cont.nr_contacte] = "%s %s %s" % (cont.nume, cont.prenume, cont.nr_telefon)
    print phonebook[1]
    
def add_number(name):
    number = input("\nAdd phone number now: ")
    phonebook[name] = number
    answer = input("Number was successfully added. Do you want add one more number [Y/N]: ")
    if answer == 'Y' or 'y':
        add_Contact()
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
        addContact()
    else:
        print("Add correct (!) command")
        start()


if __name__ == '__main__':
    start()


