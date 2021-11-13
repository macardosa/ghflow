#!/usr/bin/env python

def greet(name=""):
    print ("Hello ", name)
def greet_evelyn():
    greet("Evelyn")

def greet_manuel():
    greet("Manuel")

if __name__=="__main__":
    greet()
    greet_evelyn()
    greet_manuel()
