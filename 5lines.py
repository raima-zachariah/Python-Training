def read_first_5(filename):
    with open(filename,"r") as fh:
        headers = next(fh)
        for x in range (0,5):    
            text = fh.readline()
            #print(text)
            print(text.split(',',1)[0])
            
    #with open(filename,"r") as myfile:
    #    head = [next(myfile) for x in range(5)]
    #print(head)

def last_5(filename):
    line_count = 0
    with open(filename,"r") as fh:
        data = fh.read()
        lines = data.split('\n')
        no_lines = len(lines)
        #print(no_lines)
        for line in lines[-5:]:
            print(line)
            
def draw_lines():
    print("------------------------------------------")

if __name__ == "__main__":
    filename = 'captains.txt'
    print("First 5")
    draw_lines()
    read_first_5(filename)
    draw_lines()
    print("Last 5")
    draw_lines()
    last_5(filename)
