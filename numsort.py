runs = [70,110,30,90,40]

if __name__=="__main__":
    print(runs)
    runs.sort()
    print("sorted runs:", runs)

    with open("runs.txt") as fh:
        runs_from_file = fh.read().split('\n')
        
    print("runs from file:",runs_from_file)
    # results = [int(x) for x in runs_from_file]
        results = list(map(int, runs_from_file))
    print(results)
    results.sort()
    print("runs from file in sorted order:", results)
