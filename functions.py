import os
import csv

def ClearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def GetMiceInfo(n=2):
    mice = []
    for i in range(n):
        current_mouse_name = input(f"Enter the name of mouse n°{i+1} : ")
        current_mouse_gender = input(f"Enter the gender of mouse n°{i+1} (M/F) : ")
        if current_mouse_gender in ['m', 'M', '0']:
            current_mouse_gender = 0
        else:
            current_mouse_gender = 1
        current_mouse_age = int(input(f"Enter the age of mouse n°{i+1} : "))
        current_mouse_weight = float(input(f"Enter the weight of mouse n°{i+1} : "))
        current_mouse_tested = int(input("Will the mouse be included in tests (0/1) : "))
        ClearConsole()
        mice.append(SaveMouseInDict(current_mouse_name, current_mouse_gender, current_mouse_age, current_mouse_weight, current_mouse_tested))
        unpacked_mice = ListOfDictsToLists(mice)
        PrintMouseInfo(unpacked_mice)
    return mice

def SaveMouseInDict(name, gender, age, weight, tested):
    mouse = {}
    mouse["name"] = name
    mouse["gender"] = gender
    mouse["age"] = age
    mouse["weight"] = weight
    mouse["tested"] = tested
    return mouse

def ListOfDictsToLists(list_of_dicts):
    names = [d['name'] for d in list_of_dicts]
    genders = [d['gender'] for d in list_of_dicts]
    for i in range(len(genders)):
        if genders[i] == 0:
            genders[i] = 'M'
        elif genders[i] == 1:
            genders[i] = 'F'
    ages = [d['age'] for d in list_of_dicts]
    weights = [d['weight'] for d in list_of_dicts]
    testeds = [d['tested'] for d in list_of_dicts]
    return [names, genders, ages, weights, testeds]

def ExportAsCSV(filename, lists):
    if not filename.endswith('.csv'):
        filename = AddCSVext(filename)
    print("Dumping data...")
    print('(Debug)', filename)
    with open(filename, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter=',')
        wr.writerow(['names', 'genders', 'ages', 'weights', 'testeds'])
        for i in range(len(lists[0])):
            wr.writerow([lists[0][i], lists[1][i], lists[2][i], lists[3][i], lists[4][i]])
    print("Dump file created as", filename)
    return True

def ImportCSV(filename):
    imported_mice = []
    if not filename.endswith('.csv'):
        filename = AddCSVext(filename)
    print(f"Importing file {filename}...")
    with open(filename, 'r') as myfile:
        rd = csv.reader(myfile, delimiter=',')
        header = True
        for row in rd:
            if not header:
                name = row[0]
                gender = row[1]
                age = int(row[2])
                weight = float(row[3])
                tested = int(row[4])
                mouse = SaveMouseInDict(name, gender, age, weight, tested)
                imported_mice.append(mouse)
            header = False
    return imported_mice


AddCSVext = lambda x: str(x+'.csv')

def PrintMouseInfo(lists):
    for i in range(len(lists[0])):
        print("---------------------------")
        print(f"Mouse n°{i+1} : {lists[0][i]} ({lists[1][i]})")
        print(f"Age : {lists[2][i]} | Weight : {lists[3][i]}")
        [print("Mouse is being tested.") if lists[4][i] else print("Mouse is being used as control.")]
        print("---------------------------")

def run():
    print("nope")
    return False

if __name__ == "__main__":
    run()