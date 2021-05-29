import pywhatkit
import string
import random


def generate():
    s1 = string.ascii_uppercase

    s2 = string.ascii_lowercase

    s3 = string.digits

    s4 = string.punctuation

    passwordlength = int(input("Enter the password length:"))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)

    password = ("".join(s[0:passwordlength]))


    m1 = input("Please Enter the Mobile Number:")
    #t1=input("Please type the message:")
    tm1= int(input("Please Enter the time frame hour:"))
    ss1= int(input("Please Enter the time frame minutes "))
    try:
        pywhatkit.sendwhatmsg(m1,password,tm1,ss1)
        print("Message sent successfully!")
    except:
        print("Error!")

generate()
