# PYPRAC
# Copyright (C) 2022 
# Veer Pratap Singh <hello@veer.codes>
# => github.com/anonyindian
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program. If not, see [http://www.gnu.org/licenses/].

# ====================================================================

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

# ====================================================================
# Thank You for checking it out!
# Regards, Veer
# ====================================================================
