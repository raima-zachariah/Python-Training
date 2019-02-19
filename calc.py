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

#Test match problem
    Aus1 = 250
    Ind1 = 220
    Aus2 = 150
    AusTotal = add(Aus1,Aus2)
    target = add(sub(AusTotal, Ind1),1)
    print("India needs", target, "runs to win")

#Grocery shopping bill    
    VegBill = 120
    FruitsBill = 55
    CashPaid = 200
    Bill = add(VegBill,FruitsBill)
    Balance = sub(CashPaid, Bill)
    print("Balance money:", Balance)

#multiply with optional parameters
    print(multiply())
    print(multiply(10))
    print(multiply(10,2))
