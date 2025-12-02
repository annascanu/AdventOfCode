import string

position = 50
password_count = 0
direction = 0
moving = 0

with open("input.txt") as data:
    for line in data:
        if line[0] == "L":
            direction = -1
        elif line[0] == "R":
            direction = 1

        moving = int(line[1:]) 
        position += direction * moving
        position = position % 100

        if (position == 0):
            password_count += 1

print("Password count:", password_count)

# Part two

position = 50
password_count = 0
direction = 0
moving = 0
initial_position = 0

with open("input.txt") as data:
    for line in data:
        if line[0] == "L":
            direction = -1
        elif line[0] == "R":
            direction = 1

        moving = int(line[1:])

        for _ in range(moving):
            position = (position + direction) % 100
            if position == 0:
                password_count += 1

        position = position % 100
        #print("Initial position:", initial_position, "New position:", position, "Move:", moving, "Direction:", direction, "Password count so far:", password_count)

print("Password count part two:", password_count)
