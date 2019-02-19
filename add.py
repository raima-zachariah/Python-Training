"""
    adds 2 numbers
"""

def add(a,b):
    return a+b

if __name__== "__main__":
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
    res = add(num1, num2)
    print(res)
