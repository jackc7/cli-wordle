from colorama import Fore
import random
import readchar
import cursor
import sys

print(Fore.RESET,end="\r")
print("CLI Wordle\nvvvvv")
cursor.hide()

with open("all_words.txt","r") as f:
    words = set([x[:-1] for x in f.readlines() if len(x)==6])
with open("game_words.txt","r") as f:
    game_words = set([x[:-1] for x in f.readlines() if len(x)==6])


def checker(solution, user_input):    
    output = ""
    check = solution
    letter_count = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    for letter in solution:
        letter_count[letter] += 1

    for i in range(5):
        sol_letter = solution[i]
        user_letter = user_input[i]
        
        if sol_letter == user_letter:
            output += f"{Fore.GREEN}{user_letter}"
            letter_count[user_letter] -= 1
            check = check.replace(user_letter, " ")
        elif user_letter in check and letter_count[user_letter] > 0:
            output += f"{Fore.YELLOW}{user_letter}"
            check = check.replace(user_letter, " ")
        else:
            output += f"{Fore.WHITE}{user_letter}"
    
    output += Fore.RESET
    
    return output

# game_word = "spoon"
game_word = random.sample(game_words,1)[0]
for i in range(6):
    print(Fore.RESET,end="\r")

    attempt = ""
    while True:
        finished = False
        while True:
            print(attempt, end="\r")
            key = readchar.readkey()
            if key in "abcdefghijklmnopqrstuvwxyz":
                attempt += key
                break
            elif key == "\x08":
                attempt = attempt[:-1]
                sys.stdout.write("\033[K")
                break
            elif len(attempt) == 5 and key == "\r":
                finished = True
                break
            
        if finished and attempt in words:
            result = checker(game_word, attempt)
            print(f"\r{result}")
            
            break
    
    if attempt == game_word:
        print(f"you won in {i+1} attempts")
        break

print(game_word)
print(Fore.RESET,end="\r")