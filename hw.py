#!/usr/bin/env python

def greet(name=""):
    print ("Hello ", name)

def greet_evelyn():
    greet("Evelyn")

def greet_manuel():
    greet("Manuel")

def inquire_age():
    age = int (input("Hey!, what's your age? "))
    return age

def age_range():
    age = inquire_age()
  
    if 1 <= age <= 5:
          return "toodler"
    elif 6 <= age <= 13:
          return "kid"
    elif 14 <= age <= 18:
          return "teen"
    elif 19 <= age <= 59:
          return "adult"
    else:
          return "senior adult"


if __name__=="__main__":
    greet()
    greet_evelyn()
    greet_manuel()
    manuel_age = inquire_age()
    age_group = age_range()
    print ("age_group:", age_group)
