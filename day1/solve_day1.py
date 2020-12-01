import csv

expense_report = []

with open('input.txt', 'r') as f:
    data = f.read()

expense_report = [int(i) for i in data.split()]
expense_report.sort()

# Problem 1

expense_report_small = [i for i in expense_report if i <= 1010]
expense_report_large = [i for i in expense_report if i > 1010]

for i in expense_report_small:
    for j in expense_report_large:
        if i + j == 2020:
            print(i,j,i*j)

# Problem 2

for i in expense_report:
    expense_report_small = [i for i in expense_report if i <= (2020 - i) / 2.]
    expense_report_large = [i for i in expense_report if i > (2020 - i) / 2.]
    for j in expense_report_small:
        for k in expense_report_large:
            if i + j + k == 2020:
                print(i,j,k,i*j*k)