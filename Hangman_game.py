import hangman_words    #also can be written as from hangman_words import word_list
import hangman_art,logo 
import random
lives=6
print(logo.hangman_logo)
chosen_word=random.choice(hangman_words.word_list)
#print(chosen_word)
placeholder=""
for position in chosen_word:   #used to print the "_" as per the no of letters in the word
    placeholder+="_"
print(placeholder)
game_over=False
correct_letters=[]
while not game_over:
    print(f"You have {lives} left")
    guess=input("Take a guess: ").lower()
    print(hangman_art.stages[lives])
    #print(guess)
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    display=""
    for letter in chosen_word: #print the guessed word,if guessed letter is crct print the letter or else print "_"
        if letter==guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    #print(display)
    if guess not in chosen_word:
        lives-=1
        print(f"You guessed {guess} which is not present, you lose a life!")
        if lives==0:
            game_over=True
            print("Game Over...You lose!")
            print(f"The word was {chosen_word}")
    if "_" not in display:
        game_over=True
        print("You Win!!")
