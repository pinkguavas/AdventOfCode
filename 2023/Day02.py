file = open("path", "r+")
part1 = 0
part2 = 0
for line in file:
    addOrNot = 0
    line = line.rstrip("\n")
    gameElement = line.split(":")
    splitGameElement = gameElement[0].split()  # Part 1 - split game word and game id into list
    gameId = int(splitGameElement[1])  # Part 1 - second element is game id
    maxCubes = {  # Part 2 - minimum number of colors needed for every subset to be possible
        "red": 0,
        "green": 0,
        "blue": 0
    }
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
        if cubes.get("red") > 12 or cubes.get("green") > 13 or cubes.get("blue") > 14:  # Part 1 - checks criteria
            addOrNot += 1
        for key, value in cubes.items():  # Part 2 - if value of current subset is greater than previous values, replace
            if value > maxCubes.get(key):
                maxCubes[key] = value
    if addOrNot == 0:  # Part 1 - validates that all subsets were possible
        part1 += gameId
    powerOfSet = maxCubes.get("red") * maxCubes.get("blue") * maxCubes.get("green")  # Part 2 - calculate the power
    part2 += powerOfSet
print(part1)
print(part2)
file.close()
