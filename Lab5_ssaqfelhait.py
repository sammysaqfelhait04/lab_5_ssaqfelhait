"""
Program Name: Pick Up Sticks Game
Sammy Saqfelhait
 This program is a two player game. Each player takes 
1 to 4 sticks from the pile. The player who takes the last stick wins.
 02/11/2026
"""
max_sticks = 4
min_sticks = 1
total_sticks = 13
current_player = 1

print("Welcome to Pick Up Sticks.\n")
print("Each player takes turns picking up from 1 to 4 sticks.")

print("There are 13 sticks in the pile.")
print("Whoever picks up the last stick wins.\n")

while total_sticks > 0:
    print("There are", total_sticks, "stick(s) left.")
    print("Player", current_player)

    while True:
        sticks_taken = int(input("How many sticks will you take? "))

        if sticks_taken < min_sticks:
            print("You must take at least 1 stick.")

        elif sticks_taken > max_sticks:
            print("You cannot take more than 4 sticks.")

        elif sticks_taken > total_sticks:
            print("There are not that many sticks left.")

        else:
            break 

    total_sticks = total_sticks - sticks_taken
    print()

    if total_sticks == 0:
        print("Player", current_player, "wins!")
    else:
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1

input("\nPress Enter to exit.")
