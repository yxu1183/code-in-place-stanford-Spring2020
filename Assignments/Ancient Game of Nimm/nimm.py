"""
File: nimm.py
-------------------------
This game starts with a pile of 20 stones between the players.
The two players alternate turns.
On a give turn, a player may take either 1 or 2 stone from the center pile.
The two players continue until the center pile has run out of stones.
"""


def main():
    stones = 20
    player_number = 1
    while stones >= 0:
        print("\nThere are", stones, "stones left")
        print("Player", player_number, "would you like to remove 1 or 2 stones? ", end='')
        answer = int(input())
        while answer != 1 and answer != 2:
            print("Please enter 1 or 2: ", end='')
            answer = int(input())
            if answer == 1 or answer == 2:
                break
        if player_number == 1:
            player_number = 2
        else:
            player_number = 1
        stones = stones - answer
        if stones <= 0:
            print("\nPlayer", player_number, "wins!")
            break


if __name__ == '__main__':
    # This provided line is required at the end of a Python file
    # to call the main() function.
    main()
