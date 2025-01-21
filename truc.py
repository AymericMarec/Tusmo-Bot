import json
from unidecode import unidecode
# with open("wordList.json", "r") as f:
#     data = json.load(f)

# words = data["words"]
words = []
with open("words.txt", 'r', encoding='utf-8') as f:
    for line in f:
        word = unidecode(line.strip()).upper()
        words.append(word)

LetterUsed = {}
for word in words :
    for letter in word:
        if(letter not in LetterUsed.keys()):
            LetterUsed[letter] = 1
            continue
        LetterUsed[letter]+=1
sumLetter = 0
for key in LetterUsed.keys():
    sumLetter+= LetterUsed[key]
for key in LetterUsed.keys():
    LetterUsed[key] = (LetterUsed[key]/sumLetter)*100
data = {}
data["words"] = words
data["LetterData"] = LetterUsed

with open('wordList.json', 'w') as f:
    json.dump(data, f)