

import random
import hangman_words1
import hangman_art1


chosen_word = random.choice(hangman_words1.word_list)
word_length = len(chosen_word)


print(hangman_art1.logo)
lives=6




print(f'Pssst, the solution is {chosen_word}.')


display=[]
for a in range(0,len(chosen_word)):
  display.append("_")
print(display)

while display.count('_')!=0 and lives!=-1:
  starting_blanks=display.count('_')
  guess = input("Guess a letter: ").lower()
  count=0
  temp=0
  for letter in chosen_word:
    if letter==guess:
      display[count]=guess
      temp+=1
    count+=1
  ending_blanks=display.count('_')
  if starting_blanks==ending_blanks and temp==0:
    print(hangman_art1.stages[lives])
    lives-=1
  print(display)

if lives==-1:
  print("You lose")
else:
  print("You win")
