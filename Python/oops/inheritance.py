#!/usr/bin/python3
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def details(self):
        print("My name is {} and I'm {} years old".format(self.name,self.age))
    
class Singer(Person):
    
    def __init__(self,name,age,genre):
        self.genre = genre
        
        Person.__init__(self,name,age)
        
    def singerdetails(self):
        print("I'm {}, {} and a {} singer".format(self.name,self.age,self.genre))
        
Dave = Singer('Dave',29,'Rock')
Dave.singerdetails()
