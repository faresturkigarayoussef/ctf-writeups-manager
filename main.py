import json
def add_writeups () :  
    title = input("Enter the title of the writeup: ")
    category = input("Enter the category of the writeup: ")
    platform = input("Enter the platform of the writeup: ")
    difficulty = input("Enter the difficulty of the writeup: ")
    solution = input("Enter the solution of the writeup: ")
    writeup = {
        "title": title,
        "category": category,
        "platform": platform,
        "difficulty": difficulty,
        "solution": solution
    }
    with open("writeups.json", "r") as file:
        data = json.load(file)
    data.append(writeup)
    with open("writeups.json", "w") as file:
        json.dump(data, file, indent=4)
def search_writeups() : 
    while True:
        print("~~Welcome to writeups search system~~")
        print(" 1. to search by title ")
        print(" 2. to search by category ")
        print(" 3. to search by platform ")
        print(" 4. to exit")
        choice = int(input(" Enter your choice : "))
         
        if choice == 1:
            search_title = input("Enter the title of the writeup to search: ")
            with open("writeups.json", "r") as file:
                data = json.load(file)
            for writeup in data:
                if writeup["title"] == search_title:
                    print(writeup)
                    break
            else:
                print("Writeup not found.")

        elif choice == 2:
            search_title = input("Enter the category of the writeup to search: ")
            with open("writeups.json", "r") as file:
                data = json.load(file)
            for writeup in data:
                if writeup["category"] == search_title:
                    print(writeup)
                    break
            else:
                print("Writeup not found.")
        elif choice == 3:
            search_title = input("Enter the platform of the writeup to search: ")
            with open("writeups.json", "r") as file:
                data = json.load(file)
            for writeup in data:
                if writeup["platform"] == search_title:
                    print(writeup)
                    break
            else:
                print("Writeup not found.")

        elif choice == 4:
            break

def show_writeups() :
    with open("writeups.json", "r") as file:
        data = json.load(file)
    for writeup in data:
        print(writeup["title"],"--",writeup["category"],"--",writeup["platform"],"--",writeup["difficulty"])

def delete_writeups() :
    delete_title = input("Enter the title of the writeup to delete: ")
    with open("writeups.json", "r") as file:
        data = json.load(file)
    for i, writeup in enumerate(data):
        if writeup["title"] == delete_title:
            data.pop(i)
            break
    else:
        print("Writeup not found.")
    with open("writeups.json", "w") as file:
        json.dump(data, file, indent=4)

def statistics() :
    with open("writeups.json", "r") as file:
        data = json.load(file)
    category_count = {}
    for writeup in data:
        category = writeup["category"].lower()
        if category in category_count:
            category_count[category] += 1
        else:
            category_count[category] = 1
    total_writeups = len(data)
    print("Total number of writeups: ", total_writeups)
    print("Writeups by category:")
    for category, count in category_count.items():
        print(f"  {category}: {count} writeups")

while True:
    print("~~Welcome to writeup management system~~")
    print(" 1. to add writeups ")
    print(" 2. to show writeups ")
    print(" 3. to modify writeups ")
    print(" 4. to delete writeups ")
    print(" 5. to show statistics ")
    print(" 6. to exit")
    choice = int(input(" Enter your choice : "))
    if choice == 1:
        add_writeups()
    elif choice == 2:
        show_writeups()
    elif choice == 3:
        search_writeups()
    elif choice == 4:
        delete_writeups()
    elif choice == 5:
        statistics()
    elif choice == 6:
        break
