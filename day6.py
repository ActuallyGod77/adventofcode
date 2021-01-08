with open('day6.txt', 'r') as f:
    content = f.read().split('\n\n')
content = [s.replace('\n', '~') for s in content]
def split(x):
    return [char for char in x]
x = -1
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
p1_total = 0
p2_total = 0
while len(content) > x + 1:
    x += 1
    group_p1 = split(content[x])
    unique_y = [x for x in alphabet if x in group_p1]
    p1_total += len(unique_y)
    group_p2 = content[x].split('~')
    y = 0
    common_y = split(group_p2[y])
    while len(group_p2) > y + 1:
        y += 1
        common_y = [x for x in common_y if x in split(group_p2[y])] #for some reason this doesn't work when checking the last set of answers in the last group (finds no common letters in the last element)
    p2_total += len(common_y)
print('Part 1 answer: ' +str(p1_total))
print('Part 2 answer: ' +str(p2_total))
