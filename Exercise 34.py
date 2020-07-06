
import json
import sys

#This part for creating the json file and will only run once
"""
birthday_json = {
        "Albert Einstein" : "03/14/1879",
        "Benjamin Franklin" : "1/17/1706",
        "Ada Lovelace" : "12/10/1815"
        }

with open("birthdayfile.json","r+") as j:
    json.dump(birthday_json,j)
"""
#This is the main exercise
def add_data () :
    
    print ("Do you want to add new names to the birthday list?")
    new = input("Press 'Y' to add new data or any value to exit!\n")
    if new == "Y":
        new_name = input("Enter the name:\n")
        new_birthdate = input("Enter birthdate in mm/dd/yyyy format!\n")
        new_dict = {new_name : new_birthdate}
        with open("birthdayfile.json","r+") as updatex:
            newdata = json.load(updatex)
            newdata.update(new_dict)
            updatex.seek(0)
            json.dump(newdata,updatex)
        add_data ()
    else:
        sys.exit()


def jsonfunc ():

    with open("birthdayfile.json","r") as d:
        dicta = json.load(d)

    
    
    print("Welcome to the birthday dictionary. We know the birthdays of:")

    for i in dicta:
        print(i)

    inpt = input("Who's birthday do you want to look up?\n",)


    if inpt not in dicta:
        print("Birthday of ",inpt," is not present")
    else:
        print("{}'s birthday is {}".format(inpt,(dicta.get(inpt))))
        
    add_data()    
        
jsonfunc()
