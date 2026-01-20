import sys
import os
import random

path_of_ascaii_art = r"E:\Program Files\RobinData\WORK\RawData\HigherAndLowerGameArt.py"
path_to_data = r"E:\Program Files\RobinData\WORK\RawData"


sys.path.append(path_to_data)
sys.path.append(path_of_ascaii_art)

import GAME_DATA
import HigherAndLowerGameArt as Art

RawData = (GAME_DATA.data)
RawAscaii = (Art.logo)

def Check_answer(User, Follower_A, Follower_B):
    if Follower_A > Follower_B:
        return User == "A"
    elif Follower_B > Follower_A:
        return User == "B"
    else:
        return None
    
def formatted_data(Compare):
    compare_Name = Compare["Name"]
    compare_description = Compare["Occupation"]
    compare_country = Compare["Country"]
    return f"{compare_Name}, a {compare_description}, from {compare_country}"

def play_game():
    print(Art.logo)
    score = 0
    is_continue_game = True
    Compare1 = random.choice(RawData)

    while is_continue_game:
        Compare2 = random.choice(RawData)
        while Compare1 == Compare2:
            Compare2 = random.choice(RawData)

        print(f"\n🔥 Compare A: {formatted_data(Compare1)}")
        print(f"{Art.vs}")
        print(f"\n⚡ Compare B: {formatted_data(Compare2)}")

        User_Guess = input("👉 Who has more followers? Type 'A' or 'B': \n").upper()

        a_followers = Compare1["Follower_count"]
        b_followers = Compare2["Follower_count"]

        checker = Check_answer(User_Guess, a_followers, b_followers)

        if checker:
            score += 1
            print(f"\n✅ Correct! 🎉 +1 point\n⭐ Current Score: {score}")
            if a_followers > b_followers:
                Compare1 = Compare1
            else:
                Compare1 = Compare2
        else:
            print(f"\n❌ Wrong answer.\n🏁 Final Score: {score}")
            is_continue_game = False

while True:
    play_game()
    while True:
        replay = input("\n🔄 Do you want to play again? (YES/NO): ").strip().upper()
        if replay == "YES":
            print("\n🚀 Restarting the game... Good luck! 🍀\n")
            break
        elif replay == "NO":
            print("\n🙏 Thanks for playing Higher or Lower! 🎮✨\nSee you next time 👋😎")
            exit()
        else:
            print("⚠️ Invalid choice! Please type YES or NO.")