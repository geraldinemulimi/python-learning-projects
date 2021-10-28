#Step 1 
import random

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word
word_list = ["cat", "monkey", "koala","panda"]
chosen_word = random.choice(word_list)
word_length =len(chosen_word)
end_of_game = False
lives = 6

print(f"the word is {chosen_word}")
display = []
for _ in range (word_length):
  display += "_"
print(display)

while not end_of_game:
  guess = input("guess a letter: ").lower()
  if guess in display:
    print(f"you already guessed{guess}"  )
  

  for position in range (word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  print(display)
  
  
  if guess not in chosen_word:
    print(f"you guessed {guess} which is not in the word.You lose a life.")
    lives -= 1
    if lives ==0:
        end_of_game = True
        print("YOU LOSE.")

  if "_" not in display:
    end_of_game = True
    print("YOU WIN!")

    