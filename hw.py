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
    age = inquire_age() # You already got the age save as variable
                        # manuel_age in main function
  
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

def say_age(age):
    print ("You are ", age, " years old")

if __name__=="__main__":
    greet()
    greet_evelyn()
    greet_manuel()
    manuel_age = inquire_age()
    say_age(manuel_age)
    age_group = age_range() # This should not ask again for the age
                            # It is a mistake and needs to be resolved
    print ("age_group:", age_group)
