from calculator import add,sub
import sys

def get_scores():
    Aus1 = int(sys.argv[1])
    Ind1 = int(sys.argv[2])
    Aus2 = int(sys.argv[3])
    return Aus1,Ind1,Aus2

def find_target(Aus1,Ind1,Aus2):
    AusTotal = add(Aus1,Aus2)
    target = add(sub(AusTotal, Ind1),1)
    return target

if __name__=="__main__":
    Aus1, Ind1, Aus2 = get_scores()
    target = find_target(Aus1, Ind1, Aus2)
    print("India needs", target, "runs to win")
