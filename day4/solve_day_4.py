import re
import string

with open('input.txt', 'r') as f:
    data = f.read().split('\n\n')

ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

valid_count = 0
for i in range(len(data)):
    data[i] = data[i].translate({ord(i): ' ' for i in '\n'})
    d = dict(x.split(":") for x in data[i].split(" "))
    # for k, v in d.items():
        # print(k, v)
    if "byr" in data[i]:
        if 1920 <= int(d["byr"]) <= 2002:
            # print(int(d["byr"]))
            if "iyr" in data[i]:
                if 2010 <= int(d["iyr"]) <= 2020:
                    # print(int(d["iyr"]))
                    if "eyr" in data[i]:
                        if 2020 <= int(d["eyr"]) <= 2030:
                            # print(int(d["iyr"]))
                            if "hgt" in data[i]:
                                tmp = re.split('(\d+)', d["hgt"])
                                flag = False
                                if tmp[2] == 'cm':
                                    flag = (150 <= int(tmp[1]) <= 193)
                                    print(int(tmp[1]), flag)
                                if tmp[2] == 'in':
                                    flag = (59 <= int(tmp[1]) <= 76)
                                    print(int(tmp[1]), flag)
                                if flag == True:
                                    if "hcl" in data[i]:
                                        d["hcl"] = d["hcl"].translate({ord(i): '' for i in '#'})
                                        if all(c in string.hexdigits for c in d["hcl"]):
                                            if "ecl" in data[i]:
                                                if d["ecl"] in ecls:
                                                    if "pid" in data[i]:
                                                        if len(d["pid"]) == 9:
                                                            print(data[i])
                                                            print("valid passport!")
                                                            valid_count += 1
print(len(data), valid_count)