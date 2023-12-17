with open('Day3/input1.txt') as input_file:
    first_line = input_file.readline()
    c = len(first_line.rstrip('\n')) 
    input_file.seek(0)  
    r = sum(1 for line in input_file)

arr = [[0] * c for i in range(r)]

with open('Day3/input1.txt') as input_file:
    for i, line in enumerate(input_file):
        for j, item in enumerate(line.rstrip('\n')):
            arr[i][j] = item
            
partNumber = 0
gearRatio = 0

left = []
right = []
other = []
for i, item in enumerate(arr):
    if i > 0 and i < len(arr) - 1:
        for j, index in enumerate(item):
            if index != "." and index.isdigit() == False:
                if index == "*":
                    state = []
                    values = []
                    gearCheck = 0
                    tempValue = ""
                    column = i - 1
                    cell = j
                    for x in range(column, column + 3): 
                        if arr[x][j].isdigit():
                            # columnIndex += str(x)
                            # rowIndex += str(j)
                            for k in range(cell - 2, cell + 3):
                                if len(tempValue) >= 1:
                                    while arr[x][k].isdigit():
                                        tempValue = tempValue +  arr[x][k]
                                        k = k + 1
                                    partNumber += int(tempValue)
                                    state.append(1)
                                    values.append(int(tempValue))
                                    other.append(tempValue)
                                    tempValue = ""
                                    # print(tempValue)
                                    break
                                if arr[x][k].isdigit() and arr[x][k + 1].isdigit():
                                    tempValue = tempValue +  arr[x][k]
                                if arr[x][k].isdigit() and arr[x][k + 1].isdigit() == False and arr[x][k + 2].isdigit() == False:
                                    tempValue = tempValue +  arr[x][k]
                    tempValue = ""             
                    for x in range(column, column + 3):
                        cell = j - 1 
                        if arr[x][cell].isdigit():
                            if arr[x][j].isdigit() == False:
                                # k = cell
                                while arr[x][cell].isdigit():
                                    tempValue = arr[x][cell] + tempValue
                                    if cell != 0:
                                        cell = cell - 1
                                    else:
                                        break
                                partNumber += int(tempValue)
                                state.append(1)
                                values.append(int(tempValue))
                                other.append(tempValue)
                                tempValue = ""
                                # print(tempValue)
                    tempValue = ""
                    for x in range(column, column + 3):
                        cell = j + 1 
                        if arr[x][cell].isdigit():
                            # columnIndex += str(x)
                            # rowIndex += str(j)
                            if arr[x][j].isdigit() == False:
                                # k = cell
                                while arr[x][cell].isdigit():
                                    tempValue = tempValue +  arr[x][cell]
                                    if cell != len(item) - 1:
                                        cell = cell + 1
                                    else:
                                        break
                                partNumber += int(tempValue)
                                state.append(1)
                                values.append(int(tempValue))
                                other.append(tempValue)
                                tempValue = ""
                                # print(tempValue)
                    for x in state:
                        gearCheck = gearCheck + x
                    if gearCheck > 1:
                        temp = 1
                        for y in values:
                            temp = temp * y
                        gearRatio = gearRatio + temp
                else:
                    tempValue = ""
                    column = i - 1
                    cell = j
                    for x in range(column, column + 3): 
                        if arr[x][j].isdigit():
                            # columnIndex += str(x)
                            # rowIndex += str(j)
                            for k in range(cell - 2, cell + 3):
                                if len(tempValue) >= 1:
                                    while arr[x][k].isdigit():
                                        tempValue = tempValue +  arr[x][k]
                                        k = k + 1
                                    partNumber += int(tempValue)
                                    other.append(tempValue)
                                    # print(tempValue)
                                    tempValue = ""
                                    break
                                if arr[x][k].isdigit() and arr[x][k + 1].isdigit():
                                    tempValue = tempValue +  arr[x][k]
                                if arr[x][k].isdigit() and arr[x][k + 1].isdigit() == False and arr[x][k + 2].isdigit() == False:
                                    tempValue = tempValue +  arr[x][k]
                    tempValue = ""                
                    for x in range(column, column + 3):
                        cell = j - 1 
                        if arr[x][cell].isdigit():
                            if arr[x][j].isdigit() == False:
                                # k = cell
                                while arr[x][cell].isdigit():
                                    tempValue = arr[x][cell] + tempValue
                                    if cell != 0:
                                        cell = cell - 1
                                    else:
                                        break
                                partNumber += int(tempValue)
                                left.append(tempValue)
                                # print(tempValue)
                                tempValue = ""
                    for x in range(column, column + 3):
                        cell = j + 1 
                        if arr[x][cell].isdigit():
                            # columnIndex += str(x)
                            # rowIndex += str(j)
                            if arr[x][j].isdigit() == False:
                                # k = cell
                                while arr[x][cell].isdigit():
                                    tempValue = tempValue +  arr[x][cell]
                                    if cell != len(item) - 1:
                                        cell = cell + 1
                                    else:
                                        break
                                partNumber += int(tempValue)
                                right.append(tempValue)
                                # print(tempValue)
                                tempValue = ""
print(partNumber)
print(gearRatio)

# with open('Day3/output.txt', 'w') as file:
#     file.write('start other\n')
#     for x in other:   
#         file.write(x + '\n')
#     file.write('start left\n')
#     for x in left:
#         file.write(x + '\n')
#     file.write('start right\n')
#     for x in right:
#         file.write(x + '\n')
