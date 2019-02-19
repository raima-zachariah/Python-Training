from calculator import add,sub
import sys

if __name__=="__main__":
    Aus1 = int(sys.argv[1])
    Ind1 = int(sys.argv[2])
    Aus2 = int(sys.argv[3])
    AusTotal = add(Aus1,Aus2)
    target = add(sub(AusTotal, Ind1),1)
    print("India needs", target, "runs to win")
