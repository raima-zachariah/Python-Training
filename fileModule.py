def read_file(filename):
    with open(filename) as fh:
        data = fh.read()
    return data
if __name__=="__main__":
    data = read_file("excercise.txt.txt")
    print(data)
