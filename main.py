import morse_code as m
import os
import time

def pause():
    """pauses the program until the user presses enter"""
    print("Press enter to continue...")
    user = input()
def clear():
    """Clears the screen"""
    os.system('cls')

def main():
    """main function"""
    while True:
        clear()
        while True:
            print("1. Encode text to Morse code\n2. Decode Morse code to text\n3. Exit")
            user = input("What would you like to do: ")
            clear()
            if user == "1" or user == "2" or user == "3":
                break
        if user == "3":
            break
        elif user == "2":
            user2 = input("Input morse code to decode: ")
            a = m.decode(user2)
            print(a)
            pause()
        else:
            user2 = input("Input text to encode: ")
            a = m.encode(user2)
            print(a)
            pause()
main()