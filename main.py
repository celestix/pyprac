import os

scripts = []

for path in os.listdir("."):
    if not os.path.isfile(os.path.join(".", path)):
        continue
    if not path.endswith(".py"):
        continue
    if path == "main.py":
        continue
    path = path.replace(".py", "").replace("_", " ")
    scripts.append(path.upper())
num = 0
script_list = ""

for script in scripts:
    num += 1
    script_list += f"{num} - {script}"

print("Hello, Welcome to the pyprac repository program!")
print("\nPlease choose the script you want to run:")
print(script_list)

from time import sleep
# let the user read the list :P
sleep(2)

def scri():
    try:
        return abs(int(input("Please enter the number written before the script you want to run: ")))
    except BaseException:
        print("Looks like the digit you entered wasn't even a valid integer!")
        return scri()

def finder():
    scrindex = scri()
    try:
        return scripts[scrindex-1]
    except IndexError:
        print("Couldn't find the script associated with this number!")
        return finder()

script = finder().replace(" ", "_").lower()

import os
os.system("clear")
os.system(f"python {script}.py")