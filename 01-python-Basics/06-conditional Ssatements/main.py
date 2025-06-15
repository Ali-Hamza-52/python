# Conditional Statements
# if, elif, else
age = 20

if age > 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    
    
# even or odd
num1 = 11
if num1 % 2 == 0:
    print("Even")
else:
    print("Odd")
    
# Check if a number is positive, negative, or zero
num2 = 4
if num2 > 0:
    print("Positive")
elif num2 < 0:
    print("Negative")
else:
    print("Zero")
    
# Check if a number is divisible by 3 and 5
num3 = 15
if num3 % 5 ==0 and num3 %3 ==0:
    print("Divisible by 3 and 5")
elif num3 % 5 == 0:
    print("Divisible by 5")
elif num3 % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 3 or 5")


# ternary operator
num4 = 10
result = "Even" if num4 % 2 == 0 else "Odd"
print("result of ternary operator",result)
