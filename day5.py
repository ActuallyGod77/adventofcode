with open('day5.txt') as f:
    content = f.readlines()
    content = [x.strip() for x in content]
def split(x):
    return [char for char in x]
x = -1
ID = []
while len(content) > x + 1:
    x += 1
    ticket = split(content[x])
    y = -1
    row = 128
    power = 7
    while len(ticket) - 3 > y + 1:
        y += 1
        if ticket[y] == 'F':
            if y == 0:
                power -= 1
                row = (row - (2**power)) - 1
            else:
                power -= 1
                row = (row - (2**power)) 
        elif ticket[y] == 'B':
            if y == 0:
                row -= 1
                power -= 1
            else:
                power -= 1
    z = 6
    column = 8
    count = 3
    while len(ticket) > z + 1:
        z += 1
        if ticket[z] == 'L':
            if z == 7:
                count -= 1
                column = (column - (2**count)) - 1
            else:
                count -=1
                column = (column - (2**count))
        elif ticket[z] == 'R':
            if z == 7:
                column -= 1
                count -= 1
            else:
                count -= 1
    if 0 < row < 127:
        ID.append((row * 8) + column)
#highest_ID = max(ID)
#print('Highest seat ID: ' +str(highest_ID))
check = -1
while len(ID) > check + 1:
    check += 1
    if (ID[check] - 2) in ID and (ID[check] - 1) not in ID:
        print('Your seat ID: ' +str(ID[check]-1))
        break
    elif (ID[check] + 2) in ID and (ID[check] + 1) not in ID:
        print('Your seat ID: ' +str(ID[check]+1))
        break
    else:
        continue
