# Use this program if the GUI version doens't work in your PC

import modules.logic as logic

def program():
    path_for_file = input("Enter the complete path of file: ")

    print("These ppl didn't follow you back!")
    for i in logic.logic(path_for_file):
        print(i)

program()