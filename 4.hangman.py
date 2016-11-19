# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 17:22:30 2016

@author: Martin
"""

import requests
import random


# define a function for generating a random word
def choose_word():
    
    word_site = "http://hack.engeto.com/tasks/words.txt"
    
    response = requests.get(word_site)
    words = response.content.splitlines()
    
    
    chosenWord = str(random.choice(words))
    chosenWord = chosenWord[2:len(chosenWord)-1]
      
    return chosenWord

def theGame():
    
    turn = 0
    bad_turn = 0
    guesses = []
    
    chosenWord = choose_word()
        
    nLetters = len(chosenWord)

    currentState = []    
    
    for l in chosenWord:
        currentState.append("_")    
    
    # main loop
    while True:
        # print out current state of the game
        # for example - We're guessing the word: _ _ _ _ _ _ _ _ _ _
    
        turn += 1
                        
        currentStatePrint = " ".join(currentState)
        guessesPrint = ",".join(guesses)
        
        print("We're guessing the word:", currentStatePrint)
    
        # let's get a letter from the user
        while(True):
            letter = input("Guess the letter: ").lower()
        
            guesses.append(letter.upper())        
        
            # make sure the letter is only one character
            if len(letter) != 1:
                print("Invalid number of input letters")
            else:
                break   
    
        # print the letter to see if everything is ok by now
        print("You guessed:", letter.upper(), "\nYour old guesses were:", guessesPrint,
              "\nYou have ", MAX_UNSUC_TURNS - bad_turn, "turns remaining!")
    
        # determine if the letter is in the word
        if letter in chosenWord:        
            for i in range(nLetters):           
                if chosenWord[i] == letter:
                    
                    currentState[i] = letter.upper()
        else:
            bad_turn += 1
                        
    
        # check if the word is not guessed in its entirety
        victory = ("_" not in currentState)
        
        if (victory):
            print("You WON! Congrats. You correctly guessed", chosenWord.upper())
        
        if victory or bad_turn == MAX_UNSUC_TURNS:
            print("You are a LOSER! Congrats. The word was", chosenWord.upper())
            break


MAX_UNSUC_TURNS = 10

theGame()
