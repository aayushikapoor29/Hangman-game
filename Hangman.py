#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import requests

api_word = "https://random-word-api.herokuapp.com/word?number=1"


# In[2]:


def difficult_mode():
  while True:
    word_response = requests.get(api_word)
    if word_response.status_code == 200:
      word = word_response.json()[0]
      api_hint = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
      hint_response = requests.get(api_hint)
      if hint_response.status_code == 200:
        hint = hint_response.json()[0]['meanings'][0]['definitions'][0]['definition']
        break
  return (word, hint)


# In[3]:


def easy_mode():
  word_options =  {'Tiger': 'dangerous animal', 'Python':'a programming language', 'Male': 'Gender','Thor':'strong SuperHero', 'Apple':'red fruit', 'Bottle': 'tool to drink water',
                   'Football': 'ball game played with 11 player', 'Chess':'board game', 'Jupyter': 'open source web app used for python coding', 'bear':'furry animal'
                   }

  word = random.choice(list(word_options.keys()))
  hint = word_options[word]
  return word, hint


# In[4]:


def moderate():
  word_options = words_dictionary = {
    "Agile": "Nimble",
    "Brave": "Courage",
    "Crisp": "Fresh",
    "Dwell": "Reside",
    "Eager": "Keen",
    "Fiery": "Passion",
    "Glory": "Fame",
    "Harsh": "Severe",
    "Ivory": "White",
    "Jolly": "Merry",
    "Kneel": "Bow",
    "Lofty": "Noble",
    "Mirth": "Joy",
    "Noble": "Honored",
    "Overt": "Obvious",
    "Perky": "Cheerful",
    "Quiet": "Silent",
    "Radiant": "Glowing",
    "Stout": "Strong",
    "Tense": "Nervous"
}

  word = random.choice(list(word_options.keys()))
  hint = word_options[word]
  return word, hint


# In[5]:


def modes(mode):
  if mode.lower().strip() == "1":
    word, hint = easy_mode()
  elif mode.lower().strip() == "2":
    word, hint = moderate()
  elif mode.lower().strip() == "3":
    word, hint = difficult_mode()
  else:
    return "Invalid Input"
  return word, hint


# In[6]:


hangman_pics = [
        r"""
          _______
         |/      |
         |       |
                 |
                 |
                 |
                 
        """,
        r"""
          _______
         |/      |
         |       |  
         |       O
                 |
                 |
                  
        """,
        r"""
          _______
         |/      |
         |       |  
         |       O
         |       |
                 |
                
        """,
        r"""
          _______
         |/      |
         |       |  
         |       O
         |      /|
                 |
                
        """,
        r"""
          _______
         |/      |
         |       |  
         |       O
         |      /|\
                 |
                
        """,
        r"""
          _______
         |/      |
         |       |  
         |       O
         |      /|\ 
         |      / 
                
        """,
        r"""
          _______
         |/      |
         |       |  
         |       O 
         |      /|\
         |      / \
                
        """
    ]


# In[8]:


from IPython.display import clear_output
import time

def animate_figure():
    frames = [
        "   O\n  /|\\\n  / \\",
        " \\ O /\n   |\n  / \\",
        "    O\n   /|\\\n   / \\"
    ]

    for _ in range(5):
        for frame in frames:
            clear_output(wait=True)
            print("\n" * 2 + frame + "\n" * 2)
            time.sleep(0.5)

    clear_output(wait=True)
    print("\n" * 2 + " \\ O /\n   |\n  / \\\nYOU WIN!!! 🎉🎉🎉" + "\n" * 2)



# In[9]:


player_dict = {}

def display_word(secret_word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])


# In[10]:


def hangman_game():
    global player_dict
    player_name = input("Enter your name: ")
    print(f"Welcome, {player_name.capitalize()}! Let's play Hangman!")

    print('\nPlease select which mode you would like to try \n\t\t1. Easy mode, \n\t\t2. Moderate mode, \n\t\t3. Difficult Mode' )
    while True:
        mode = input('Enter your choice: ').lower()
        word_hint = modes(mode)
        if word_hint == "Invalid Input":
            print("Invalid mode. Please enter 'easy' or 'moderate' or 'difficult'.")
        else:
            word, hint = word_hint
            break

    secret_word = word.lower()
    guessed_letters = set()
    attempts = 7
    score = 0



    print("Welcome to Hangman!")
    print(f"\n\t\tHint for the word is: {hint}\t\n")
    print(display_word(secret_word, guessed_letters))

    while attempts > 0 and set(secret_word) != guessed_letters:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter only one letter at a time.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
        elif guess in secret_word:
            guessed_letters.add(guess)
            score += 10 * secret_word.count(guess)
            print(f"Good guess: {display_word(secret_word, guessed_letters)}")
            print(f"Your score: {score}")
        else:
            attempts -= 1
            print(hangman_pics[6 - attempts])
            print(f"Wrong guess! You have {attempts} attempts left.")


        if set(secret_word) == guessed_letters:
            animate_figure()

            print("Congratulations! You guessed the word!")
            print(f"Your final score: {score}")
            break


    else:
        print(f"Game over! The word was '{secret_word}'.")
        print(f"Your final score: {player_name}: {score}")



    if player_name in player_dict:
        player_dict[player_name] += score
    else:
        player_dict[player_name] = score

    print(f'{player_name} Your score is: {score}')
    print(player_dict)


    print("\t\t\nWanna Play More? (Yes/No)")

    choice = input('Enter your choice: ').lower()

    if choice == 'yes'.lower():
      hangman_game()
    elif choice == 'no'.lower():
      print('Thank You!!!')
    else:
      print('Invalid input, please select from yes/no')



# In[11]:


hangman_game()


# In[ ]:




