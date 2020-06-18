# -*- coding: utf-8 -*-
"""
       (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
         ~"` ~"~~`
Created on Thu Jun 18 11:10:16 2020
@author: Chris
"""
import random as ran #random function
import string as stri #string
import sqlite3 as sql #SQL for database
from PIL import Image #for importing the dice images
from IPython.display import display as disp #for displaying images

img2 = Image.open(r"images/thumps.jpg")
img1 = Image.open(r"images/pass1.jpg")
disp(img1)
print("-----------------------------------")
print("Welcome to the password Generator :")

#function to create the password with a length of 15
def makepass(name, surname):
    passw = name[0] + surname[0]
    for x in range(15):
        passw += ran.choice(charlist())
    return passw

#function to create a list containing all the letters, numbers, and characters.
def charlist():
    numbers = '1234567890'
    chars = '!@#$%^&*!@#$%^&*'
    letters = stri.ascii_letters
    return numbers + chars + letters 

#creates a connection between the database and the python file
connection = sql.connect("loginsDB.db") 
#allows the python file to execute SQL queries
crsr = connection.cursor() 

#function to create a new table if there isn't already one
#to store the rolls and a name for the rolls
def create_table(): 
    crsr.execute('CREATE TABLE IF NOT EXISTS logins (Name TEXT, Surname TEXT, Password TEXT)')

#creating the table if it doesn't already exist
create_table()

#function to add data to the rolls table, it is then updated.
def data_entry(name, surname, password): 
    #checking to see if the database contains what was entered
    for row in crsr.execute('SELECT * FROM logins'):
        crsr.execute("SELECT Name FROM logins WHERE Name = ? AND Surname = ?", (name, surname))
        data = crsr.fetchall()
    #checks if it contains anything, if so it adds to database, if not, it doesn't 
    if len(data) != 0:
        print("You've create a password before!")
        return "no"
    else:
        #adds to database
        crsr.execute("INSERT INTO logins (Name, Surname, Password) VALUES(?, ?, ?)", (name, surname, password)) 
        connection.commit() 
        print("Added to the database")
        return "yes"
      
start = input("Do you want to start ? (yes/no) \n > ").lower()

#starts the program if the user wants to
if start == "yes":
    #gets input
    name = input("What is your name : \n> ").lower()
    surname = input("What is your surname : \n> ").lower()
    #makes password
    passw = makepass(name, surname)
    ans = data_entry(name, surname, passw)
    #checks if it was added to database
    if ans == "yes":
        print("Your password is : " + passw)
    start = input("Would you like to make another password ? \n> ")
    
disp(img2)    
print("-----------------------------------")
print("      Done creating passwords!     ")
print("")
print("")
print("")
print("        Thank you for using        ")
print("          my password gen          ")
print("-----------------------------------")
    
    