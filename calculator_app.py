# ==========================
# CALCULATOR APP by Parth Pandey
# ==========================
# A calculator which can switch between
# normal and scientific mode.
# made for practice and learning purpose :)

import math

# --- basic operations ---
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# --- scientific ones ---
def sin_val(x):
    return math.sin(math.radians(x))

def cos_val(x):
    return math.cos(math.radians(x))

def tan_val(x):
    return math.tan(math.radians(x))

def asin_val(x):
    if x < -1 or x > 1:
        return "Invalid input"
    return math.degrees(math.asin(x))

def acos_val(x):
    if x < -1 or x > 1:
        return "Invalid input"
    return math.degrees(math.acos(x))

def atan_val(x):
    return math.degrees(math.atan(x))

def sqrt_val(x):
    if x < 0:
        return "Invalid input"
    return math.sqrt(x)

def power_val(a, b):
    return a ** b

def factorial_val(x):
    if x < 0:
        return "Invalid input"
    return math.factorial(int(x))

def log_val(x):
    if x <= 0:
        return "Invalid input"
    return math.log10(x)

def ln_val(x):
    if x <= 0:
        return "Invalid input"
    return math.log(x)

def pi_val():
    return math.pi


# --- modes ---
def normal_calc():
    print("\nNormal Calculator Mode")
    print("Available operations: + , - , * , /")
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operator: ")
        b = float(input("Enter second number: "))
        
        if op == '+':
            print("Result =", add(a,b))
        elif op == '-':
            print("Result =", sub(a,b))
        elif op == '*':
            print("Result =", mul(a,b))
        elif op == '/':
            print("Result =", div(a,b))
        else:
            print("Unknown operator")
    except ValueError:
        print("Please enter numbers only!!")

def scientific_calc():
    print("\nScientific Calculator Mode")
    print("Operations: sin, cos, tan, asin, acos, atan, sqrt, pow, fact, log, ln, pi")
    choice = input("Enter operation: ").lower()

    try:
        if choice in ['sin','cos','tan','asin','acos','atan','sqrt','fact','log','ln']:
            num = float(input("Enter number: "))
            if choice == 'sin':
                print("Result =", sin_val(num))
            elif choice == 'cos':
                print("Result =", cos_val(num))
            elif choice == 'tan':
                print("Result =", tan_val(num))
            elif choice == 'asin':
                print("Result =", asin_val(num))
            elif choice == 'acos':
                print("Result =", acos_val(num))
            elif choice == 'atan':
                print("Result =", atan_val(num))
            elif choice == 'sqrt':
                print("Result =", sqrt_val(num))
            elif choice == 'fact':
                print("Result =", factorial_val(num))
            elif choice == 'log':
                print("Result =", log_val(num))
            elif choice == 'ln':
                print("Result =", ln_val(num))
        
        elif choice == 'pow':
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print("Result =", power_val(a,b))

        elif choice == 'pi':
            print("Pi =", pi_val())
        else:
            print("Invalid operation selected")

    except Exception as e:
        print("Something went wrong:", e)

def main():
    print("====== Welcome to My Calculator ======")
    while True:
        print("\n1. Normal Calculator")
        print("2. Scientific Calculator")
        print("3. Exit")
        ch = input("Choose option: ")

        if ch == '1':
            normal_calc()
        elif ch == '2':
            scientific_calc()
        elif ch == '3':
            print("Thanks for using! :)")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
