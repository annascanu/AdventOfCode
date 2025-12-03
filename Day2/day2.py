import string

ID_sequence = []

data = open("input.txt")
for line in data:
    ID_sequence = line.split(",")

ID_sum = 0
starting_number = 0
end_number = 0

for ID in ID_sequence:
    starting_number, end_number = ID.split("-")

    for number in range(int(starting_number), (int(end_number) + 1)):
        if len(str(number)) % 2 == 0:
            first_half = str(number)[:len(str(number))//2]
            second_half = str(number)[len(str(number))//2:]

            if (first_half == second_half):
                ID_sum += number

print("ID sum: ", ID_sum)

# Part two
ID_sum = 0

for ID in ID_sequence:
    starting_number, end_number = ID.split("-")

    for number in range(int(starting_number), (int(end_number) + 1)):
        # split_stop = len(str(number))/2
        for i in range(1, len(str(number))//2 + 1):
            tmp = str(number)[:i] * ((len(str(number)))//i)
            if tmp == str(number):
                ID_sum += number
                break

print("ID sum (part 2): ", ID_sum)