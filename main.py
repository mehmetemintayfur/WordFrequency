with open("SteveJobs.txt","r",encoding="utf-8") as f:
    allText = f.read()

def ayir(text):
     allwords = text.split()
     words = []
     for i in allwords:
        i = i.lower()
        i = i.strip("\n")
        i = i.strip(",")
        i = i.strip(".")
        words.append(i)
        if i=="—":
            words.remove("—")

     wordFrequency(words)


def wordFrequency(word):
    dict1 = dict()
    for k in word:
        if (k in dict1):
            dict1[k] += 1
        else:
            dict1[k] = 1
    print(dict1)


ayir(allText)

