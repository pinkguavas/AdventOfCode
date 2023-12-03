# Part 1
file = open("path", "r+")
sumOfId = 0
for line in file:
    addOrNot = 0
    line = line.rstrip("\n")
    gameElement = line.split(":")
    splitGameElement = gameElement[0].split()
    gameId = int(splitGameElement[1])
    for part in line.split(";"):  # splits the line into subsets of one game
        part = part + "."
        cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        chunks = part.split()  # splits the subsets into list of number with color
        x = 0
        for word in chunks:  # splits the number and color
            word = word.rstrip(word[-1])
            for key, value in cubes.items():  # checks for each key in dictionary
                num = 0
                if word == key:  # when the word is the key, the element before the word is the number of cubes
                    num = int(chunks[x - 1])
                    value += num
                    cubes[key] = value
            x += 1
        if cubes.get("red") > 12 or cubes.get("green") > 13 or cubes.get("blue") > 14:  # checks criteria
            addOrNot += 1
    if addOrNot == 0:  # validates that all subsets were possible
        sumOfId += gameId
print(sumOfId)
file.close()

# Part 2
file = open("path", "r+")
sumOfSets = 0
for line in file:
    line = line.rstrip("\n")
    maxCubes = {  # minimum number of colors needed for every subset to be possible
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for part in line.split(";"):  # checks for color and number of cubes like in Part 1
        cubes = {  # number of colors for each subset
            "red": 0,
            "green": 0,
            "blue": 0
        }
        part = part + "."
        chunks = part.split()
        x = 0
        for word in chunks:
            word = word.rstrip(word[-1])
            for key, value in cubes.items():
                num = 0
                if key == word:
                    num = int(chunks[x - 1])
                    value += num
                    cubes[key] = value
            x += 1
        for key, value in cubes.items():
            if value > maxCubes.get(key):  # if value of current subset key is greater than previous values, replace
                maxCubes[key] = value
    powerOfSet = maxCubes.get("red") * maxCubes.get("blue") * maxCubes.get("green")
    sumOfSets += powerOfSet
print(sumOfSets)
file.close()
