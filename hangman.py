import os

def getBestGuess(wordfile, word, badletters):
    def possibleGuess(word, guess):

        assert len(word)==len(guess)

        word=word.lower()
        guess=guess.lower()
        for i in range(len(guess)):
            if word[i]!=guess[i] and word[i]!='_':
                return False
        return True

    def nonUnderlined(word):
        chars=[]
        for char in word:
            if(char!='_'):
                chars.append(char)
        return chars

    def getWordsFromFile(filename):
        bucket = set()
        file = open(filename, "r")
        nu=nonUnderlined(word)
        for line in file:
            line=line.replace("\n", "")
            if(len(line)==len(word)):
                flag=False
                for badletter in badletters:
                    if badletter in line:
                        flag=True
                for i in range(len(word)):
                    char=line[i]
                    realChar=word[i]
                    if(realChar=='_' and char in nu):
                        flag=True
                if not flag:
                    bucket.add(line)
        return bucket

    dictwords=getWordsFromFile(wordfile)

    naturalfrequency={
        "a":8.167,
        "b":1.492,
        "c":2.782,
        "d":4.253,
        "e":12.702,
        "f":2.228,
        "g":2.015,
        "h":6.094,
        "i":6.966,
        "j":0.153,
        "k":0.772,
        "l":4.025,
        "m":2.406,
        "n":6.749,
        "o":7.507,
        "p":1.929,
        "q":0.095,
        "r":5.987,
        "s":6.327,
        "t":9.056,
        "u":2.758,
        "v":0.978,
        "w":2.360,
        "x":0.150,
        "y":1.974,
        "z":0.074
    }

    def getBestNaturalGuess(word):

        def f(a):
            return 100-naturalfrequency[a]

        possibleGuesses=list(naturalfrequency.keys())
        for letter in word:
            if(letter in possibleGuesses):
                possibleGuesses.remove(letter)
        possibleGuesses.sort(key=f)
        return possibleGuesses[0]

    newDictWords=[]
    for dictword in dictwords:
        if(possibleGuess(word, dictword)):
            newDictWords.append(dictword)

    if(len(newDictWords)==1):
        return ("I've got it!", newDictWords[0])

    if(len(newDictWords)==0):
        return ("WTF?!","IS THAT A REAL WORD? ARE YOU SURE? BECAUSE TO ME IT LOOKS LIKE IT'S NOT! HAVE YOU FILLED IN ALL THE BLANKS FOR THE WORDS I GUESSED? YOU LITTLE SHIT, DON'T PLAY DIRTY WITH MEH")

    missingLetterOccurances=[]
    dictwords=newDictWords
    for dictword in dictwords:
        dictword=dictword.lower()
        for i in range(len(dictword)):
            if(dictword[i]!=word[i] and (dictword[i] not in word) and (dictword[i] not in badletters)):
                missingLetterOccurances.append(dictword[i])

    frequency={}
    for letter in missingLetterOccurances:
        frequency[letter]=frequency.get(letter, 0)+1

    for key in frequency.keys():
        frequency[key]=(frequency[key]*100)/len(missingLetterOccurances)

    def f(a):
        return 100-frequency[a]

    bestkeys=list(frequency.keys())
    bestkeys.sort(key=f)
    return (bestkeys, dictwords)

# word=""
# badletters=[]
# wordlength=int(input("How long is your word? Enter here: "))
# for i in range(wordlength):
#     word+='_'
#
# while('_' in word):
#     bestGuess=getBestGuess(word, badletters)
#     os.system('clear')
#     print(word)
#     inpt=input("Is "+ bestGuess+ " in your word?")
#     inpt=inpt.lower()
#     if(inpt[0]=='y'):
#         word

say=False
#ord=""
word="pogge_"
badletters=[]
guess=getBestGuess("words.txt", word, badletters=badletters)
if(len(guess)==1):
    for item in guess:
        print(item)
    if(say):
        os.system("say I guess the letter "+guess)
else:
    for item in guess:
        print(item)
    if(say):
        os.system("say "+guess)