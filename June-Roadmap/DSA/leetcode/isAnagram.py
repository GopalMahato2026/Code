def countWords(word):
    countDict = {}
    for alpha in word.lower():
        if alpha in countDict:
            countDict[alpha] += 1
        else:
            countDict[alpha] = 1
    return countDict
def isAnagram(s, t):
    s = countWords(s)
    t = countWords(t)
    return s == t
print(isAnagram("Gopal","Palgo"))   
print(isAnagram("Gopal","Goutam"))    
