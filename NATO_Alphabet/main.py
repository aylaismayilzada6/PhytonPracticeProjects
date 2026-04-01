from logging import exception

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_with_exception():
    user_input = input("Enter the word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_with_exception()
    else:
        print(f"Your phonetic nato output is :  {output_list}")

generate_with_exception()