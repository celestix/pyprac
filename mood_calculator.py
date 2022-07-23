# Mood Calculator - A part of pyprac
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

# DEFAULT_MOOD is normal mood of a person.
# Ideal value for default mood is 60 w.r.t. our script. 
DEFAULT_MOOD = 60

moods = {
    DEFAULT_MOOD+80:('😡', "very angry"), 
    DEFAULT_MOOD+60:('😠', "angry"), 
    DEFAULT_MOOD+40:('😀', "very happy"),
    DEFAULT_MOOD+20:('😃', "happy"), 
    DEFAULT_MOOD:('🙂', "normal"),
    DEFAULT_MOOD-20:('☹️', "sad"), 
    DEFAULT_MOOD-40:('😖', "very sad"), 
    DEFAULT_MOOD-60:('😭', "crying"),
}

# This function calculates the mood of a user by his energy scores.
#    - Lower the energy scores, more bad the mood will be.
#    - As the energy scores incease, user's happyness level would increase too.
#    - DO NOT FORGET that too high energy scores would lead to anger.
def calculate_mood(score: int) -> dict:
    for mood in moods:
        if score >= mood:
            return moods[round_off(score, abs(mood-20), abs(mood))]
    return moods[DEFAULT_MOOD]


# This function rounds off the the provided value to the nearest extreme of given range.
# [ext1, ext2] where ext1 and ext2 are extremes of the given range.
def round_off(value: int, ext1: int, ext2: int):
    res1 = abs(value-ext1)
    res2 = abs(value-ext2)
    return ext1 if res1 < res2 else ext2 

# This function parses the users input to boolean value.
# Fails with the integral code '1' if the input can not be recognized.
def parse_toggle(input_arg: str):
    input_arg = input_arg.lower().strip()
    if input_arg in ("yes", "true", "right"):
        return (True, 0)
    elif input_arg in ("no", "false", "wrong"):
        return (False, 0)
    else:
        return (False, 1)

# A simple questions set to check working of the mood calculator.
QUESTIONS = {
    1: ("Are you feeling good today?", 20),
    2: ("Are you angry on someone today?", 120, 0),
    3: ("Are you missing someone today?", -40),
    4: ("Was it a usual day, not that bad?", 20),
    5: ("Did you hit anybody today?", 140, 0)
}

import time 

# This function creates a simple countdown of 5 seconds.
def qd_counter():
    for i in range(0, 5):
        text = f"Displaying questions in {abs(5-i)} seconds."
        print(text, end="\r")
        time.sleep(1)
    text = len(text)*' '
    print(f"{text}")

# This function asks the user to input his answer through console.
# Asks again if not found in the supported input vars.
def ask(num: int):
    answer, code = parse_toggle(input(f"{QUESTIONS[num][0]} "))
    if code == 0:
        return answer
    print("Your input couldn't be recognized as a valid answer!")
    print("Please choose one from: yes, true, right, no, false, wrong")
    return ask(num)

def main():
    print("mood calculator".upper())
    name = input("\nPlease enter your name: ").capitalize()
    print(f"\nHello {name}, please answer the following questions:")
    qd_counter()
    score = 0
    for num in QUESTIONS:
        points = QUESTIONS[num]
        if ask(num=num):
            score += points[1]
        else:
            score -= points[2] if len(points) > 2 else points[1]
    score = 0 if score < 0 else score
    mood = calculate_mood(score)
    print(f"""
Hey {name}, You seem to be in a {mood[1]} mood today.
Your mood score is: {score},
This is the emoji based on your mood: {mood[0]}""")

if __name__=="__main__":
    main()

# ====================================================================

# TODO: register a signal call for ctrl + c quitting 

# ====================================================================
# Thank You for checking it out!
# Regards, Veer
# ====================================================================
