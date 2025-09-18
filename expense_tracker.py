import time

print("--------------> Welcome to Expense Tracker <-------------------")

dic_catogury = {"Food":0,"Travel":0,"Entertainment":0,"Shopping":0,"Health":0,"Debt":0,"Necessity":0}
catogurys = list(dic_catogury.keys())


def asking_user():
    user_input = input("Would you like to add an EXPENSE or VIEW? (e/v) : ").lower().strip()
    return user_input


def expense_tracker(user_input):
    global catogurys
    if user_input == 'e':
        amount = int(input("How much do you want to add? : ₹"))
        print("  |  ".join(catogurys))
        catogury_choice = input("What category you want to add? : ").title()
        return catogury_choice, amount

    elif user_input == 'v':
        try:
            with open("expense.txt", "r") as f:
                data = f.read()
                print("\nYour Saved Expenses:\n")
                print(data)
        except FileNotFoundError:
            print("No expenses recorded yet.")
        return None, None

    else:
        print("Please enter a valid input")
        return None, None


def add_expense(category_choice, amount):
    global dic_catogury
    if category_choice in catogurys:
        dic_catogury[category_choice] += amount
    else:
        dic_catogury[category_choice] = amount


def project_start():
    while True:
        user_input = asking_user()
        catagury_choice, amount = expense_tracker(user_input)

        if user_input == 'e' and catagury_choice:
            add_expense(catagury_choice, amount)

        asking_to_quit = input("Would you like to add one more log or press q to quit (y/q): ").lower().strip()
        if asking_to_quit == 'q':
            with open("expense.txt", "a") as f:
                f.write("\n------------> WELCOME TO EXPENSE TRACKER <--------\n")
                for cat, amt in dic_catogury.items():
                    print(f"{cat} ---- {amt}")
                    f.write(f"{cat} ---- {amt}\n")

            asking_to_view = input("Would you like to see the expense? (y/n): ").lower().strip()
            if asking_to_view == 'y':
                try:
                    with open("expense.txt", "r") as f:
                        data = f.read()
                        print(data)
                except FileNotFoundError:
                    print("No expenses recorded yet.")
            else:
                print("Thank you")
            break


project_start()