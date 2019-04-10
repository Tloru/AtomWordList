import itertools as it
import random

file = open("elements.txt", "r")
elementList = []
elementDict = []
for line in file:
    for word in line.split():
        word.lower()
    elementList.append(line.split()[0].lower())
    elementDict.append(line.split()[1].lower())
elementDict = dict(zip(elementList,elementDict))

def is_element(word, elementList):
    if word in elementList:
        return True
    return False

def make_element(word, elementList, elementDict, many=True, real_name=False):
    elements = []
    for element in elementList:
        if element in word:
            elements.append(element)
    # print(elements)
    elementLetters = list("".join(elements))
    # print(elementLetters)
    for letter in word:
        if letter not in elementLetters:
            return None
    posib = []
    for perm in list(it.permutations(elements)):
        to_add = list(perm)[:len(word)]
        if to_add not in posib:
            if word in "".join(to_add):
                posib.append(to_add)
    final = []
    for chance in posib:
        to_add = chance[("".join(chance)).index(word):]
        if word == "".join(to_add):
            if to_add not in final:
                final.append(to_add)
    if len(final) == 0:
        return None
    if many == False:
        final = random.choice(final)
        if real_name == True:
            elements = []
            for element in final:
                elements.append(elementDict[element])
            return elements
    return final

input = str(input()).split()
elements = []
for word in input:
    elements.append(make_element(word, elementList, elementDict, many=False, real_name=True))
print(elements)
