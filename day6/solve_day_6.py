with open('input.txt', 'r') as f:
    data = f.read().split('\n\n')

question_count = []

for i in range(len(data)):
    data[i] = data[i].translate({ord(i): '' for i in '\n'})
    question_count.append(len(set(data[i])))

print(data)
print(question_count)
print(sum(question_count))

with open('input.txt', 'r') as f:
    data = f.read().split('\n\n')

question_count = []


for i in range(len(data)):
    data[i] = data[i].split('\n')
    print(data[i])
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for person in data[i]:
        alphabet = set.intersection(set(alphabet),set(person))
        print(alphabet)
    print(alphabet)
    question_count.append(len(alphabet))

print(data)
print(question_count)
print(sum(question_count))