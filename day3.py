with open('day3.txt') as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    content.pop(0)

toboggan = 0
trees = 0
index = 0

for line in content:
    toboggan += 1
    index = toboggan % len(line)
    if line[index] == '#':
        trees += 1


toboggan1 = 0
trees1 = 0
index1 = 0

for line1 in content:
    toboggan1 += 3
    index1 = toboggan1 % len(line1)
    if line1[index1] == '#':
        trees1 += 1


toboggan2 = 0
trees2 = 0
index2 = 0

for line2 in content:
    toboggan2 += 5
    index2 = toboggan2 % len(line2)
    if line2[index2] == '#':
        trees2 += 1


toboggan3 = 0
trees3 = 0
index3 = 0

for line3 in content:
    toboggan3 += 7
    index3 = toboggan3 % len(line3)
    if line3[index3] == '#':
        trees3 += 1


del content[::2]
print(content)

toboggan4 = 0
trees4 = 0
index4 = 0

for line4 in content:
    toboggan4 += 1
    index4 = toboggan4 % len(line4)
    if line4[index4] == '#':
        trees4 += 1


BIGTREES = trees*trees1*trees2*trees3*trees4
print(BIGTREES)
