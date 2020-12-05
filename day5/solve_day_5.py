import re
import string

with open('input.txt', 'r') as f:
    data = f.read().split('\n')

max_row = 0
max_seat = 0

seats = []

# Process data and solve Part 1
for line in data:
    line = line.translate({ord(i): '1' for i in 'B'})
    line = line.translate({ord(i): '0' for i in 'F'})
    line = line.translate({ord(i): '1' for i in 'R'})
    line = line.translate({ord(i): '0' for i in 'L'})
    seats.append(8*int(line[0:7],2) + int(line[7:10],2))
    if int(line[0:7],2) >= max_row:
        max_row = int(line[0:7],2)
        print(max_row)
        if int(line[7:10],2) >= max_seat:
            max_seat = int(line[7:10],2)
            print(int(line[0:7],2), int(line[7:10],2))
            print(8*int(line[0:7],2) + int(line[7:10],2))

# Solve Part 2
a = sorted(seats)
for i in range(len(a)):
    if a[i] + 1 != a[i+1]:
        print(a[i], a[i+1])
        break


