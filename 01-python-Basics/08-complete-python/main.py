# # function with no parameter
# def funtionWithOutParameter():
#     print("This is a function with no parameter")

# funtionWithOutParameter()

# # function with parameter
# def funtionWithParameter(name):
#     print(f"Hello {name.upper()}")

# funtionWithParameter("Ali Hamza")

# #mini calculator

# # function to multiply two numbers
# def multiply(a, b):
#     return a * b

# # function to add two numbers
# def add(a, b):
#     return a + b
# # function to subtract two numbers
# def subtract(a, b):
#     return a - b
# # function to divide two numbers
# def divide(a, b):
#     return a / b
# # function to modulo two numbers
# def modulo(a, b):
#     return a % b

# calling the functions
# print("Press 1 for multiplication")
# print("Press 2 for addition")
# print("Press 3 for subtraction")
# print("Press 4 for division")
# print("Press 5 for modulo")

# choice = int(input("Enter your choice: "))

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if choice == 1:
#     print(f"The result of multiplication is: {multiply(num1, num2)}")
# elif choice == 2:
#     print(f"The result of addition is: {add(num1, num2)}")
# elif choice == 3:
#     print(f"The result of subtraction is: {subtract(num1, num2)}")
# elif choice == 4:
#     print(f"The result of division is: {divide(num1, num2)}")
# elif choice == 5:
#     print(f"The result of modulo is: {modulo(num1, num2)}")
# else:
#     print("Invalid choice please try again")

# array
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0]) # output: apple
# print(fruits[1]) # output: banana
# print(fruits[2]) # output: cherry

# dictionary
# student ={
#     "name": "Ali Hamza",
#     "age": 20,
#     "city": "Karachi"
# }
# print(type(student))
# print(student["name"])
# print(student["age"])
# print(student["city"])
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student)
# student.update({
#     "name": "Muhammad Ali",
#     "age": 21,
#     "city": "Lahore"
# })
# student["name"] = "Ghulam Raza"
# print(student)

# # Set
# setA = {1,3,5,7,9}
# setB = {2,4,6,8,10}
# setC = setA.union(setB)
# print(f"Union of setA and setB: {setC}")
# setD = setA.intersection(setB)
# print(f"Intersection of setA and setB: {setD}")
# setE = setA.difference(setB)
# print(f"Difference of setA and setB: {setE}")
# setF = setA.symmetric_difference(setB)
# print(f"Symmetric difference of setA and setB: {setF}")
# setA.update(setB)
# # update setA with setB its add all the elements of setB to setA
# print(f"Updated setA: {setA}")
# setA.intersection_update(setB)
# print(f"Intersection updated setA: {setA}")
# # update setA with setB its remove all the elements of setB from setA
# setA.difference_update(setB)
# print(f"Difference updated setA: {setA}")
# # update setA with setB its remove all the elements of setB from setA
# setA.symmetric_difference_update(setB)
# print(f"Symmetric difference updated setA: {setA}")
# # clear setA its remove all the elements of setA
# setA.clear()
# print(f"Cleared setA: {setA}")
# # check if setA is a subset of setB
# print(f"SetA is a subset of setB: {setA.issubset(setB)}")
# # check if setA is a superset of setB
# print(f"SetA is a superset of setB: {setA.issuperset(setB)}")
# # check if setA is a disjoint set with setB
# print(f"SetA is a disjoint set with setB: {setA.isdisjoint(setB)}")
# x= 12
# try:
#     x = 10 / "a"
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     print(x)
#     print("This will always execute")

# file handling
# def openFile(filename, mode):
#     file = open(filename, mode)
#     return file

# def closeFile(file):
#     file.close()

# def writeFile(fileName, data):
#     file = None
#     try:
#         file = openFile(fileName, "w")
#         file.write(data)
#         print("File written successfully")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         closeFile(file)

# # inputData = input("Enter the data to write to the file: ")
# # writeFile("file.txt", inputData)

# def readFile(fileName):
#     file = None
#     try:
#         file = openFile(fileName, "r")
#         data = file.read()
#         print(f"Type of data is: {type(data)}")
#         print(f"Data read from file: {data}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         closeFile(file)

# readFile("file.txt")

#Loops
# for loop
# for i in range(2,10,2):
#     print(f"Number: {i}")

# while loop
# i = 2
# while i <= 10:
#     print(f"Number: {i}")
#     i += 1


# colors = ["red", "green", "blue", "yellow", "purple"]
# for color in colors:
#     print(f"Color: {color}")

# testingObject =[
#     {
#         "name": "Ali Hamza",
#         "age": 20,
#         "city": "Karachi"
#     },
#     {
#         "name": "Muhammad Ali",
#         "age": 21,
#         "city": "Lahore"
#     },
#     {
#         "name": "Ghulam Raza",
#         "age": 22,
#         "city": "Islamabad"
#     }
# ]
# testingObject.append({
#     "name": "Hassan Raza",
#     "age": 23,
#     "city": "Karachi"
# })
# # print(testingObject)

# for object in testingObject:
#     print("--------------------------------")
#     print(f"Name: {object['name']}")
#     print(f"Age: {object['age']}")
#     print(f"City: {object['city']}")
#     print("--------------------------------")

#import modukes
# import math
# print(math.ceil(1.2))
# print(math.floor(1.2))
# print(math.factorial(5))
# print(math.sqrt(16))
# print(math.pow(2, 3))
# print(math.pi)
# print(math.e)

# -----------------------------------
# Starting Object Oriented Programming
# -----------------------------------

# class Person:
#     def __init__(self, name , age , city):
#         self.name = name
#         self.age = age
#         self.city = city
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")
    
#     # getters and setters
#     def getAge(self):
#         return self.age
#     def getCity(self):
#         return self.city
#     def getName(self):
#         return self.name
#     def setAge(self, age):
#         self.age = age
#     def setCity(self, city):
#         self.city = city
#     def setName(self, name):
#         self.name = name

# p1 = Person("Ali Hamza", 20, "Burewala")
# p1.display()
# print(p1.getAge())
# print(p1.getCity())
# print(p1.getName())
# p1.setAge(21)
# p1.setCity("Lahore")
# p1.setName("Muhammad Ali")
# p1.display()

# # different types of constructors
# class Person:
#     # constructor with default values
#     # constructor with no values
#     def __init__(self):
#         self.name = "Ali Hamza"
#         self.age = 20
#         self.city = "Burewala"
#     # constructor with one value
#     def __init__(self, name):
#         self.name = name
#         self.age = 20
#         self.city = "Burewala"
#     # constructor with two values
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.city = "Burewala"
#     # constructor with three values
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")

# p1 = Person("Ali Hamza", 20, "Burewala")
# p2 = Person("Muhammad Ali", 21)
# p3 = Person("Sulman")
# p4 = Person()

# print("Three Params")
# p1.display()
# print("Two Params")
# p2.display()
# print("One Param")
# p3.display()
# print("No Params")
# p4.display()

# inheritance
# class Person:
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#         print("Person Constructor")
#     def display(self):
#         print("Person Display")
#         print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")

# class Student(Person):
#     def __init__(self):
#         super().__init__("Ali Hamza", 20, "Burewala")
#         print("Student Constructor")
#         super().display() # call the parent class display method
#         self.display() # call the current class display method
#     def display(self):
#         print("Student Display")
#         print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")
# # p1 = Person("Ali Hamza", 20, "Burewala")
# p2 = Student()

# #Encapsulation
# class BankAccount:
#     def __init__(self, accountNumber, balance):
#         self.__accountNumber = accountNumber
#         self.__balance = balance
#     def getAccountNumber(self):
#         return self.__accountNumber
#     def getBalance(self):
#         return self.__balance
#     def setBalance(self, balance):
#         self.__balance = balance
#     def display(self):
#         print(f"Account Number: {self.__accountNumber}, Balance: {self.__balance}")

# userAccountNumber = int(input("Enter your account number: "))
# defaultAccountNumber = 112233
# p1 = BankAccount(defaultAccountNumber, 1000)

# if userAccountNumber == defaultAccountNumber:
#     p1.display()
# else:
#     print("Invalid account number")

# class Example1:
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")
    
#     @classmethod
#     def displayClassMethod(cls):
#         print(f"Class Method: Name: {cls.name}, Age: {cls.age}, City: {cls.city}")
    
#     @classmethod
#     def classSetterMethod(cls, name, age, city):
#         cls.name = name
#         cls.age = age
#         cls.city = city

# class Example2:
#     name = "Ali Hamza"
#     age = 20
#     city = "Burewala"
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")
    
#     @classmethod
#     def displayClassMethod(cls):
#         print(f"Class Method: Name: {cls.name}, Age: {cls.age}, City: {cls.city}")
    
#     @classmethod
#     def classSetterMethod(cls, name, age, city):
#         cls.name = name
#         cls.age = age
#         cls.city = city

# e1 = Example1("Ali Hamza", 20, "Burewala")
# e3 = Example1("Ali Hamza", 20, "Burewala")
# Example1.classSetterMethod("Mohammad", 30, "Karachi")
# e1.display()
# e3.display()
# Example1.displayClassMethod()
# print("--------------------------------")
# e2 = Example2("Muhammad Ali", 21, "Lahore")
# e4 = Example2("Ghulam Raza", 22, "Islamabad")
# Example2.classSetterMethod("Hassan Raza", 23, "Karachi")
# e2.display()
# e4.display()
# Example2.displayClassMethod()


# Method Overriding
# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     def sound(self):
#         print("Bark Bark")

# d1 = Dog()
# d1.sound()
# a1 = Animal()
# a1.sound()

# Polymorphism
# class Dog:
#     def sound(self):
#         print("Bark")

# class Cat:
#     def sound(self):
#         print("Meow")

# animals = [Dog(), Cat()]

# for a in animals:
#     a.sound()

# ====================================
#  Complete Banking System OOP Example
# ====================================


# from abc import ABC, abstractmethod

# # =========================
# # 1. ABSTRACTION (Base Class)
# # =========================
# class BankSystem(ABC):

#     @abstractmethod
#     def withdraw(self, amount):
#         pass

#     @abstractmethod
#     def deposit(self, amount):
#         pass


# # =========================
# # 2. ENCAPSULATION + INHERITANCE
# # =========================
# class ATM(BankSystem):

#     def __init__(self, bank_name, balance):
#         self.bank_name = bank_name
#         self.__balance = balance   # Encapsulation (private)

#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"{amount} deposited successfully")

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"{amount} withdrawn successfully")
#         else:
#             print("Insufficient balance")

#     def get_balance(self):
#         return self.__balance

#     def show_bank(self):
#         print("Bank:", self.bank_name)


# # =========================
# # 3. POLYMORPHISM (Different Banks)
# # =========================
# class HBL(ATM):
#     def withdraw(self, amount):
#         print("HBL ATM Processing...")
#         super().withdraw(amount)


# class UBL(ATM):
#     def withdraw(self, amount):
#         print("UBL ATM Processing...")
#         super().withdraw(amount)


# # =========================
# # MAIN PROGRAM
# # =========================

# hbl_account = HBL("HBL Bank", 5000)
# ubl_account = UBL("UBL Bank", 3000)

# # Polymorphism (same method different behavior)
# hbl_account.withdraw(1000)
# ubl_account.withdraw(500)

# print("\nBalances:")
# print("HBL:", hbl_account.get_balance())
# print("UBL:", ubl_account.get_balance())

# print("\nDepositing money:")
# hbl_account.deposit(2000)

# print("HBL New Balance:", hbl_account.get_balance())

# Comprehensive List
# Bad practice
# numbers=[1,2,3,4,5,6,7,8,9,10]
# print("Bad practice: ",numbers)
# numbers= [number for number in range(1,11)]
# print("Good practice: ",numbers)
# numbers= [number for number in range(1,11)]
# print("Numbers: ",numbers)
# squares= [number**2 for number in numbers]
# print("Squares: ",squares)
# import math
# roots= [int(math.sqrt(number)) for number in squares]
# print("Roots: ",roots)

#Generator Functions
# def count():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# for i in count():
#     print(i)

# Decorator Functions
# def vat_decorator(func):
#     def wrapper(subtotal):
#         vat = subtotal * 0.15
#         net_bill = func(subtotal, vat)
#         return net_bill
#     return wrapper

# @vat_decorator
# def calculate_bill(subtotal, vat):
#     return subtotal + vat

# bill = calculate_bill(1000)
# print("Net Bill:", bill)

# def discount_decorator(func):
#     def wrapper(subtotal,vat_type):
#         if vat_type == 'pre_vat':
#             vatAdded=subtotal + (subtotal*0.15)
#             return func(vatAdded)
#         else:
#             discounted=func(subtotal)
#             return discounted+(discounted*0.15)
#     return wrapper

# @discount_decorator
# def calculate_discount(subtotal):
#     return subtotal - (subtotal * 0.10)

# bill1 = calculate_discount(1200,'pre_vat')
# bill2 = calculate_discount(1200,'post_vat')
# print("Bill1:", bill1)
# print("Bill2:", bill2)

# Async Programming
# Synchronous Programming Example
# import time

# def task1():
#     print("Task 1 start")
#     time.sleep(3)
#     print("Task 1 end")

# def task2():
#     print("Task 2")

# task1()
# task2()

# Async Programming Example
# import asyncio
# async def task1():
#     print("Task 1 start")
#     await asyncio.sleep(3)
#     print("Task 1 end")
# async def task2():
#     print("Task 2")

# async def main():
#     print("Main function start")
#     await task1()
#     await task2()
#     print("Main function end")

# asyncio.run(main())

# import asyncio

# async def download():
#     await asyncio.sleep(0)
#     print("Downloading file...")
#     await asyncio.sleep(3)
#     print("Download complete")

# async def email():
#     await asyncio.sleep(0)
#     print("Sending email...")
#     await asyncio.sleep(2)
#     print("Email sent")

# async def main():
#     await asyncio.gather(
#         download(),
#         email()
#     )

# asyncio.run(main())