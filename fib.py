def fib(n):
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    n -= 2
    while(n > 0):
        n3 = n1 + n2
        print(n3)
        n1 = n2
        n2 = n3
        n -=1

def draw_line():
    print("-----------------------------------")
    
if __name__ == "__main__":
    print("Fibonacci series")
    draw_line()
    n = 10
    fib(n)

    print("Pattern")
    draw_line()
    for num in range(94,108):
        if(num < 100):
            print(num / 2)
        else:
            print(num * 2)

    print("odd numbers from 120 to 150")
    draw_line()
    for num in range(121,150,2):
        print(num)
