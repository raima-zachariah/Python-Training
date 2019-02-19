import datetime

def find_age(yob, cy):
    return cy - yob

if __name__ == "__main__":
    yob = int(input("year of birth: "))
    cy = datetime.datetime.now().year
    age = find_age(yob,cy)
    print("Age: ",age)
    age_10 = age + 10
    print("Age after 10 years:", age_10)
