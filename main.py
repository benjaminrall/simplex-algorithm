def get_new_table(t):
    done = False
    while not done:
        print("\n")
        for row in t:
            print(row)
        done = True
        lowest = None
        for r, c in enumerate(t):
            if c[0] < 0:
                if lowest is None:
                    lowest = r
                elif c[0] < t[lowest][0]:
                    lowest = r
                done = False
        pivot_col = lowest
        if not done:
            ratios = [0]
            for r in range(1, len(t[-1])):
                if t[pivot_col][r] > 0:
                    ratios.append(t[-1][r] / t[pivot_col][r])
                else:
                    ratios.append(None)
            lowest = None
            for r in range(1, len(ratios)):
                if lowest is None:
                    lowest = r
                if ratios[r] is not None and ratios[r] < ratios[lowest]:
                    lowest = r
            pivot_row = lowest
            divisor = t[pivot_col][pivot_row]
            for c in t:
                c[pivot_row] = c[pivot_row] / divisor
            for r in range(len(t[0])):
                if r != pivot_row:
                    multiplier = -1 * t[pivot_col][r]
                    for j in range(len(t)):
                        t[j][r] = t[j][r] + (multiplier * t[j][pivot_row])
    return t

equations = int(input("Enter the amount of equations you wish to enter: "))
dimensions = int(input("Enter the amount of dimensions there are: "))
dimensions_list = []
for i in range(1, dimensions + 1):
    dimensions_list.append(input(f"Name dimension variable {i}: "))

slacks = []
for i in range(1, equations + 1):
    slacks.append("S" + str(i))

table_key = ['P']
for d in dimensions_list:
    table_key.append(d)
for s in slacks:
    table_key.append(s)
table_key.append('RHS')

table = []

left_table = [[0 for i in range(equations + 1)] for j in range(1 + len(dimensions_list))]
right_list = [0 for i in range(equations + 1)]
slack_table = [[0 for i in range(equations + 1)] for j in range(len(slacks))]

for i, slack_list in enumerate(slack_table):
    slack_list[i + 1] = 1

for i, left_list in enumerate(left_table):
    left_list[0] = int(input("Enter " + table_key[i] + " value: "))
right_list[0] = int(input("Enter right side value: "))

for i in range(1, equations + 1):
    print(f"-- Equation {i} --")
    for j, left_list in enumerate(left_table[1:len(left_table)]):
        left_list[i] = int(input("Enter " + table_key[j + 1] + " value: "))
    right_list[i] = int(input("Enter right side value: "))

table = left_table
for slack_list in slack_table:
    table.append(slack_list)
table.append(right_list)

table = get_new_table(table)

print("\n")
for i, col in enumerate(table[0:len(table) - 1]):
    found = False
    index = None
    for j, item in enumerate(col):
        if item != 1 and item != 0:
            found = False
            break
        if item == 1 and not found:
            found = True
            index = j
        elif item == 1 and found:
            found = False
            break
    if found:
        print(table_key[i], table[-1][index])
    else:
        print(table_key[i], 0.0)