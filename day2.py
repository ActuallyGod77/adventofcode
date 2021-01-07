with open('day2.txt') as f:
    content = f.readlines()
    content = [x.strip() for x in content]

#test_input = """1-3 a: abcde
#1-3 b: cdefg
#2-9 c: ccccccccc"""

#passwords = test_input.split("\n")
valid = 0
for password in content:
    bits = password.split(" ")
    p_word = bits[2]
    criteria = bits[1][0]
    positions = bits[0].split("-")
    pos_1, pos_2 = int(positions[0]), int(positions[1])
    if (p_word[pos_1 - 1] + p_word[pos_2 - 1]).count(criteria) == 1:
        valid += 1


print(valid)
    

    





