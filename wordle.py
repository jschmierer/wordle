# main.py

import random

f = open("validWords.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]

f2 = open("possibleWords.txt")
possibleWords = f2.readlines()
possibleWords = [x.strip() for x in possibleWords] 

f.close()

won = False

def strToDict(sting, diction):
  for letter in sting:
    if letter not in diction:
      diction[letter] = 1
    else:
      diction[letter] += 1
      
#string will be the string of the colored emojis
#index will be the index of the emoji to change
#num will either be 1 or 2: 1 to make it green, 2 to be yellow
def colorChange(string, index, num):
  colors = []
  for color in string:
    colors.append(color)
  if num == 1:
    colors[index * 2] = "🟩"
  else:
    colors[index * 2] = "🟨"
  newString = ""
  for color in colors:
    newString += color
  return newString

word = possibleWords[random.randint(0, len(possibleWords))]
wLetters = {}
strToDict(word, wLetters)

print ("Welcome to Wordle! You have 6 guesses to find the 5 letter word.")

guess = ""
guessNum = 1

while (guess != word and guessNum <= 6):
  guess = input("Guess #" + str(guessNum) + ": ")
  if len(guess) != 5:
    print("Has to be a 5 letter word.")
  elif guess not in validWords:
    print("Not a valid word.")
  else:
    
    correct = "🔳 🔳 🔳 🔳 🔳 "
    gDict = {}
    strToDict(guess, gDict)
    
    wLetters = {}
    strToDict(word, wLetters)
    
    i = 0
    for letter in guess:
      if letter in wLetters and letter == word[i]:
        correct = colorChange(correct, i, 1)
        gDict[letter] -= 1
        wLetters[letter] -= 1
      i += 1
    
    i = 0
    for letter in guess:
      if letter in wLetters and gDict[letter] >= wLetters[letter]:
        if correct[i * 2] != "🟩" and wLetters[letter] != 0:
          correct = colorChange(correct, i, 2)
          gDict[letter] -= 1
          wLetters[letter] -= 1
      i += 1
      
    print (correct)
    guessNum += 1
    
    if correct == "🟩 🟩 🟩 🟩 🟩 ":
      won = True
      print("You win!!")

if not won:
  print("Nice try. The word was " + word)
