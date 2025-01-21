import json

with open("wordList.json", "r") as f:
    data = json.load(f)

words = data["words"]
letterData = data["LetterData"]

def GuessWord(Guess,YellowLetters,UsedLetters,UsedWord):
    PotentialWord = []
    print(UsedWord)
    for word in words:
        if word in UsedWord:
            continue
        if not len(word) == len(Guess) :
            continue
        if IsUsedLetter(word,UsedLetters):
            continue
        if not IsAllYellowLetter(word,YellowLetters):
            continue
        if not SameWord(word,Guess):
            continue        
        PotentialWord.append(word)
    return SortWords(PotentialWord)[0]

def SameWord(word,Guess):
    for i,letter in enumerate(Guess):
        if letter == "_":
            continue
        elif not letter == word[i]:
            return False
    return True

def IsAllYellowLetter(word,YellowLetters):
    for letter in YellowLetters:
        if letter not in word:
            return False
    return True

def IsUsedLetter(word,UsedLetter):
    for letter in UsedLetter:
        if(letter in word):
            return True
    return False

def SortWords(PotentialWord):
    WordScore = {}
    for word in PotentialWord:
        WordScore[word] = GetWordScore(word)
    return [k for k, v in sorted(WordScore.items(), key=lambda item: item[1], reverse=True)]


def GetWordScore(word):
    score = 0
    letterChecked = []
    for letter in word:
        if letter in letterChecked:
            continue
        score += letterData[letter]
        letterChecked.append(letter)
    return score

# print(GuessWord("RAM_NE_",[],["T","I","S","Z","O"]))