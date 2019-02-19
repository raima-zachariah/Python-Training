def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2

def multiply(n1=1,n2=1):
    return n1 * n2

if __name__=="__main__":
    a = 10
    b = 20
    sum = add(a,b)
    print("Sum:",sum)
    diff = sub(b,a)
    print("Difference:",diff)
