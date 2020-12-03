with open("input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

moves = len(content)
horizontal_length = len(content[0])
tree_counter = 0

# Solve Part 1

for i in range(moves):
    location = (3 * i) %horizontal_length
    if content[i][location] == '#':
        print("Hit!", content[i][0:location+1])
        tree_counter += 1

print(tree_counter)

# Solve Part 2

tree_counter = 0
slope_x = 1

for i in range(moves):
    location = (slope_x * i) % horizontal_length
    if content[i][location] == '#':
        print("Hit!", content[i][0:location+1])
        tree_counter += 1

print(tree_counter)

tree_counter = 0
slope_x = 3

for i in range(moves):
    location = (slope_x * i) % horizontal_length
    if content[i][location] == '#':
        print("Hit!", content[i][0:location+1])
        tree_counter += 1

print(tree_counter)

tree_counter = 0
slope_x = 5

for i in range(moves):
    location = (slope_x * i) % horizontal_length
    if content[i][location] == '#':
        print("Hit!", content[i][0:location+1])
        tree_counter += 1

print(tree_counter)

tree_counter = 0
slope_x = 7

for i in range(moves):
    location = (slope_x * i) % horizontal_length
    if content[i][location] == '#':
        print("Hit!", content[i][0:location+1])
        tree_counter += 1

print(tree_counter)

tree_counter_1 = 0
slope_x = 1

for i in range(int(moves/2.) + 1):
    location = (slope_x * i) % horizontal_length
    if content[i*2][location] == '#':
        print(i, "Hit!")
        tree_counter_1 += 1

print(tree_counter_1)