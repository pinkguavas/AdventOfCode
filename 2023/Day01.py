import re

# Part 1
file = open("path", "r+")
part1 = 0
for line in file:
    numbers = []
    for i in line:
        if i.isdigit():
            numbers.append(i)
    value = numbers[0] + numbers[len(numbers)-1]
    part1 += int(value)
file.close()

#Part 2
file = open("path", "r+")
part2 = 0
for line in file:
    numbers = []
    line = re.sub("one", "o1e", line)
    line = re.sub("two", "t2o", line)
    line = re.sub("three", "t3e", line)
    line = re.sub("four", "f4r", line)
    line = re.sub("five", "f5e", line)
    line = re.sub("six", "s6x", line)
    line = re.sub("seven", "s7n", line)
    line = re.sub("eight", "e8t", line)
    line = re.sub("nine", "n9e", line)
    for i in line:
        if i.isdigit():
            numbers.append(i)
    value = numbers[0] + numbers[len(numbers)-1]
    part2 += int(value)
file.close()

print(part1)
print(part2)
