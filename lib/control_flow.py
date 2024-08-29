#!/usr/bin/env python3

def admin_login(username, password):
    return "Access granted" if username.lower() == "admin" and password == "12345" else "Access denied"

def hows_the_weather(temperature): 
    if temperature <= 40:
        description = "brisk"
    elif 40 < temperature < 65: 
        description = "a little chilly"
    elif temperature > 85:
        description = "too dang hot"
    else:
        description = "perfect"
    return f"It's {description} out there!"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0 and num % 5 > 0:
        return "Fizz"
    elif num % 3 > 0 and num % 5 == 0:
        return "Buzz"
    else:
        return num

# operations = {
#     "+": +,
#     "-": -,
#     "/": /,
#     "*": *
# }

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
    pass
