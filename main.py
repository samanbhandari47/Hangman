import random
from asci_art import hangman, hangman_logo  # ASCII art/logo for Hangman
from animals_species import animal_data     # List of animal species/names

print(hangman_logo)

# Choose a random word and create placeholder underscores
chosen_word = random.choice(animal_data).lower()
word_length = len(chosen_word)


placeholder = ""
for i in range(word_length):
    placeholder += "_"
print(f"Guess the word: {placeholder}")


game_over = False
correct_letters = []   
game_lives = 0

while not game_over: 
    user_input = input("Guess a letter: ").lower()
    
    # Skip if letter was already guessed
    if user_input in correct_letters:
        print(f"You've already guessed the letter '{user_input}'")
        continue
    
    # Build the display string based on guessed letters
    display = ""
    for i in chosen_word:
        if i == user_input:
            display += i
            correct_letters.append(i)
        elif i in correct_letters:
            display += i
        else:
            display += "_"
               
    print("keep guessing:" + display)
    print(hangman[game_lives])  
    
    if user_input not in chosen_word:
        game_lives += 1
        print(f"The letter '{user_input}' is not in the word.")
        print("\n")
        
    if game_lives == 7:
        game_over = True
        print("You Lose!!")

    if "_" not in display:
        game_over = True
        print("You won!! 🎉")