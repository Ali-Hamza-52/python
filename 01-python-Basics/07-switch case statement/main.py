#switch case statement
def switch_case_example(value):
    match value:
        case 1:
            return "You selected option 1"
        case 2:
            return "You selected option 2"
        case 3:
            return "You selected option 3"
        case _:
            return "Invalid option"# ternary operator
num4 = 10
result = "Even" if num4 % 2 == 0 else "Odd"
print(result)
