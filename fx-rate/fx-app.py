import json
import os

global fx_rate
fx_rate = None


def get_fx_rate():

    global fx_rate
    if fx_rate == None:
        with open("fx-rate.json", mode="r") as f:
            fx_rate = json.loads(f.read())

    return fx_rate


def display_rate():
    print(get_fx_rate())

    for entry in get_fx_rate().get("currencies"):
        print("{} - {} = {}".format(
                entry.get("baseCurr"),
                entry.get("foreign"),
                entry.get("rate")))

def add_rate():
    print("Add New Rate")
    base_curr = input("Base currency: ")
    foreign = input("Foreign currency: ")
    rate = float(input("FX rate: "))
    new_entry = {"baseCurr": base_curr,
                "foreign": foreign,
                "rate": rate}

    add_new_fx_rate(new_entry)

def add_new_fx_rate(fx_entry):
    global fx_rate
    fx_rate = get_fx_rate()
    fx_rate["currencies"].append(fx_entry)

    with open("fx-rate.json", mode="w") as f:
        f.write(json.dumps(fx_rate))
    print("updated: ", fx_rate)

def clear_screen():
    os.system("cls")

display_rate()

def display_menu():
    clear_screen()
    print("Forex App")
    print("\t1. Display Rates")
    print("\t2. Add New Rate")
    selection = input("\nEnter selection: ")

    if selection == "1":
        clear_screen()
        display_rate()
    else:
        clear_screen()
        add_rate()

display_menu()