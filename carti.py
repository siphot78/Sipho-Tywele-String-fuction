
import re

str = input("please enter username")

def Username(str):

    regex = ("^(?=.*[a-z])(?=." +
             "*[A-Z])(?=.*\\d)" +
             "(?=.*[-+_!@#$%^&*., ?]).+$")

    p = re.compile(regex)


    if (str == None):
        print("You havent entered anyhing")
        return
    if (len(str) <=4):
     print('please enter a username more than 4 charecters')
    # Print Yes if string
    # matches ReGex
    if(len(str)>14):
       print("please enter a username less thab 14 charecters")
    if (re.search(p, str)):
     print("Username is correct")
    else:
     print("Your username should be over 4 charecters and less than 14 and have special charecters (?=.*[-+_!@#$%^&*., ?]).+$ contain uppercase and lower case charactrs ")




# Function Call
Username(str)