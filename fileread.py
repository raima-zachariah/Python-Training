import sys

if __name__=="__main__":
    file_name = sys.argv[1]
    print(file_name)
    with open(file_name,"r") as fh:
        data = fh.read()
        print(data)
