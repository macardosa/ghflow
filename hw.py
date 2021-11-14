#!/usr/bin/env python

def greet(name=""):
    print ("Hello ", name)
def greet_evelyn():
    greet("Evelyn")

def greet_manuel():
    greet("Manuel")

def inquire_age():
    age = input("Hey!, what's your age? ")
    return age

def say_age(age):
    print ("You are ", age, " years old")

if __name__=="__main__":
    greet()
    greet_evelyn()
    greet_manuel()
    manuel_age = inquire_age()
    say_age(manuel_age)
