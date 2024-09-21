import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
   +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
   +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = ["aardvark", "baboon", "camel"]

lives = 6


chosen_word = random.choice(word_list)


display = ["_" for _ in chosen_word]
print(' '.join(display))

game_over = False

while not game_over:

    guess = input("Guess a letter: ").lower()

    
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    print(' '.join(display)) 

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print('You are lose. please try again..!')

    
    if "_" not in display:
        game_over = True
        print("You are winning!")

    print(stages[lives])
