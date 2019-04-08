#!/usr/bin/env python

# basic hello function
def greet(name):
  print("Hello "+name+"!")
greet("limpehsh")

# initialise empty list for people
people = []
def get_person():
  # get info about the person
  person_name = input("What is their name?")
  person_age = int(input("How old are they?"))
  # make that info a dictionary
  person = {
  "name" : person_name,
  "age" : person_age
  }
  # pass back the person
  return person

# basic example running the program
person_count = int(input("Indicate the number of people?"))
for count in range(person_count):
  people.append(get_person())
print("You've added "+str(person_count)+" people!")
print("Here they are: "+str(people))