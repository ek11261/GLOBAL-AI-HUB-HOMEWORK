import random
from words import words
import string
def get_valid_word(words):
    word=random.choice(words)
    while "-" in word or " "in word:
        word=random.choice(words)
    return word.upper()

def hangman():
    word=get_valid_word(words)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()

    lives=6

    while len(word_letters)>0 and lives>0:

        print("You have:", lives, "Lives left and you have used these letters:", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("current word: ", " ".join(word_list))


        user_letter=input("Guess a letter:").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(used_letter)
            if user_letter in word_letter:
                word_letters.remove(user_letter)
                print("")

            else:
                lives=lives-1
                print('/nYour letter,', user_letter,'is not in the world.')

        elif user_letter in used_letters:
            print("You have already used that letter. Guess another letter.")
        else:
            print("that is not a valid letter.")

    if lives==0:
        print("you died, sorry. The word was", word)

    else:
        print("YAY!! yOU GUESSED THE WORD",WORD,"!!")

if __name__=="__main__":
    hangman()



