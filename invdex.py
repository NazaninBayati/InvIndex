import re
from stemming.porter2 import stem
from nltk.tokenize import sent_tokenize, word_tokenize

def token(text):
    tok_text = re.findall("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+",text)
    return tok_text


i = 0
lines = []
dictionary = {}
start="docID=1"
id = 1


while True:
    line = input()
    if(line[0:6] == "docID="):
        id=line[6]

    elif line:
        st = token(line)
        for i in range(st.__len__()):
            if stem(st[i].lower()) not in dictionary:
                dictionary[stem(st[i].lower())] = [id]
            else:
                dictionary[stem(st[i].lower())].append(id)
    else:
        break

dictionary = sorted(dictionary.items())


for i in range(dictionary.__len__()):
    p = dictionary[i][0] + ":"
    v = sorted(set(dictionary[i][1]))
    for j in range(v.__len__()):
        p = p + " " + str(v[j])
    print(p)


