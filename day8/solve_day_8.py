import re
# regex = r"(\w+) ([+-])(\d+)"
#
# with open('input.txt', 'r') as f:
#     data = f.read().split('\n')
#
# for i in range(len(data)):
#     data[i] = re.split(regex, data[i])
#
# line = 0
# accumulator = 0
# used_commands = []
# flag = True
# repeat_command = 0
#
# while flag == True:
#     if line in used_commands:
#         repeat_command = line
#         print(repeat_command, print(data[repeat_command]))
#         flag = False
#         break
#     else:
#         used_commands.append(line)
#
#     if data[line][1] == 'acc':
#         if data[line][2] == '+':
#             accumulator += int(data[line][3])
#             line += 1
#         elif data[line][2] == '-':
#             accumulator -= int(data[line][3])
#             line += 1
#     elif data[line][1] == 'jmp':
#         if data[line][2] == '+':
#             line += int(data[line][3])
#         elif data[line][2] == '-':
#             line -= int(data[line][3])
#     elif data[line][1] == 'nop':
#         line += 1

input = "input.txt"
test = "input.txt"


def read_file(filename):
    with open(filename) as f:
        return f.read().splitlines()


data = read_file(input)


# Each Operation gets stored in a dict, which are stored in an array
def get_instructions(data):
    trouble = []
    for line in data:
        instructions = re.match(r"(.+) (.+)$", line)
        if instructions:
            operation = instructions.group(1)
            parameter = instructions.group(2)
            trouble.append({'Operation': operation, 'Parameter': int(parameter), 'Acc before': 0, 'Acc after': 0,
                            'Visited': False})
    return trouble


# Running through the troubled data
def find_loop(trouble, index):
    i = 0
    prev = 0
    bfr = 0
    order = []

    # updating the current operation set
    def update_item(jmp, i, bfr, par):
        trouble[i]['Visited'] = True
        trouble[i]['Acc before'] = bfr
        trouble[i]['Acc after'] = bfr
        if not jmp:
            trouble[i]['Acc after'] = par + bfr

    while (True):
        if (i >= len(trouble)):
            break
        opr = trouble[i].get('Operation')
        par = trouble[i].get('Parameter')
        bfr = trouble[prev].get('Acc after')
        prev = i
        # order.append(str(i)+' | '+str(bfr)+' | '+opr+' '+str(par))

        # stop on seen item
        if (trouble[i].get('Visited')):
            # print('Order:')
            # for calc in order: print(calc)
            return str(bfr)

        if (opr == 'nop'):
            update_item(False, i, bfr, 0)
            i += 1
            continue

        if (opr == 'acc'):
            update_item(False, i, bfr, par)
            bfr += par
            i += 1
            continue

        if (opr == 'jmp'):
            update_item(True, i, bfr, par)
            i = i + par
            continue

    return "Real answer: " + str(bfr) + " Index:" + str(index)


# find the operation to change
def repair_trouble(trb):
    trouble = trb

    # toggle encounterd jmp and nop
    def toggle(operation):
        opr = operation.get('Operation')
        if opr == 'jmp':
            operation['Operation'] = 'nop'
            return operation
        elif opr == 'nop':
            operation['Operation'] = 'jmp'
            return operation

    # check each operation and toggle if needed. Then get result.
    for operation in trouble:
        if not (operation.get('Operation') == 'acc'):
            operation = toggle(operation)
            res = (find_loop(trouble, trouble.index(operation)))
            if re.match(r"(.+) (.+)$", res):
                print(res)
                break
            operation = toggle(operation)
            # print(troubled_data)
        else:
            res = (find_loop(trouble, trouble.index(operation)))
            # print(troubled_data)
            if re.match(r"(.+) (.+)$", res):
                print(res)
                break
        # needed to reset to initial state
        for visit in trouble:
            visit['Visited'] = False
            visit['Acc after'] = 0
            visit['Acc before'] = 0


troubled_data = get_instructions(data)
# print(troubled_data)
print(repair_trouble(troubled_data))

# print(find_loop(troubled_data,0))
