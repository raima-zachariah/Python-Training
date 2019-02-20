runs = [11,15,45,129,349,191,81]
#doesnt work
for run in runs:
    if run > 99:
        runs.remove(run)

print(runs)
runs = [11,15,45,129,349,191,81]

for run in runs[:]:
    if run > 99:
        runs.remove(run)
print(runs)

def magic(xl = []):
    xl.append(10)
    print(xl)

magic([12])
magic()
magic()

def no_magic(xl = None):
    if xl == None:
        xl = []
    xl.append(10)
    print(xl)

no_magic([12])
no_magic()
no_magic()

friends = ["Ajay","Vishal","Sumit","Dinakar"]
print(friends)
print("-"*16)

print(sorted(friends))
print("-"*16)

