# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 18:57:15 2016

@author: Martin
"""

import requests
import random

# define a function to load the dictionary to internal structure
# we will load it from external file
def load_dict():
    
    word_site = "http://hack.engeto.com/tasks/words.txt"
    
    response = requests.get(word_site)
    words = response.content.splitlines()
    
    words_clean = []
    
    for word in words:
        word_str = str(word)
        words_clean.append(word_str[2:len(word_str) - 1])
    
    
    return words_clean

    
def main():
    # process the input word we're working with
    theWord = input("Provide the word to find anagrams for: ").lower()
    
    # logic behind the anagram program
    # ideal case - work with the internal structure (array) with all
    # words from the dictionary and try to find proper letters in those words
    # it is up to you how you'll handle this area, try to figure this out
    
    dictionary = load_dict()
    
    anagrams = []
    for dic in dictionary:
        
        dic_l = len(dic)
        word_l = len(theWord)
        
        if dic_l == word_l:
            
            letterMatchTotal = 0         
            
            for letter in theWord:
                letterMatchTotal += int(letter in dic)
                
            if letterMatchTotal == word_l:
            
                anagrams.append(dic)
    
    if theWord in anagrams:
        anagrams.remove(theWord)
    
    nAnagrams = len(anagrams)    
    
    # print the requested anagrams
    print("There are", str(nAnagrams), "anagrams we've been able to find for the word", 
          theWord.upper(), ": \n *", "\n * ".join(anagrams))


main()


