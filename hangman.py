try:
    import csv
except ImportError:
    print("This script requires 'csv' package, and it wasn't found")
    quit()

try:
    import random
except ImportError:
    print("This script requires 'random' package, and it wasn't found")
    quit()


ManPieces = [' O\n', '/', '|', '\\\n', '/ ', '\\\n']  # pieces of the hanged man


def draw(pieces):  # draws hangman based on pieces, which is ErrCount
    drawing = []
    for u in range(pieces):
        drawing.append(ManPieces[u])
    print(''.join(drawing))


try:
    with open('words.csv') as f:  # this section converts cvs into one list, Data
        reader = csv.reader(f)
        RawData = list(reader)
except FileNotFoundError:
    print("This script requires 'words.csv' file, and it wasn't found. Check that the file is in the\n"
          "same directory as hangman.py")
    quit()

del RawData[0]
Data = []
for i in range(len(RawData)):
    Data.append(RawData[i][0])

while True:  # loop to allow replay
    randomInt = random.randint(0, len(Data) - 1)  # chooses random word from list
    ansString = Data[randomInt]

    # print(ansString)  # for debug

    ansList = [char for char in ansString]
    foundList = ["_" for r in ansString]

    ErrList = []
    ErrCount = 0
    foundString = " ".join(foundList)
    print(foundString)

    while True:
        LetInp = input("Guess?: \n").lower()
        FoundCount = 0
        UnknownCount = 0
        for i in range(len(ansList)):
            if LetInp == ansList[i]:
                foundList[i] = LetInp
                FoundCount += 1
            if foundList[i] == "_":
                UnknownCount += 1
        if UnknownCount == 0:
            print(ansString)
            print("you won!")
            break
        if FoundCount == 0:
            if LetInp in ErrList:
                pass
            else:
                ErrCount += 1
                ErrList.append(LetInp)
        if ErrCount == 6:
            draw(ErrCount)
            print("you're dead")
            print("Correct word: " + ansString)
            break
        draw(ErrCount)
        foundString = " ".join(foundList)
        print(foundString)
        ErrString = " ".join(ErrList)
        print("Wrong letters: " + ErrString)
    replay = input('want to play again? y/n\n').lower()
    if replay == 'n':
        break

print("done")
