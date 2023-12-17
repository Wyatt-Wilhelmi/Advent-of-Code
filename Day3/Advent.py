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
# with open('Day3/input.txt') as input_file:
#     for i, line in enumerate(input_file):
#         num = ""
#         for j, item in enumerate(line.rstrip('\n')):
#             if item.isdigit():
#                 num += item
#                 continue
#             if item == ".":
#                 if num != "":
#                     arr[i][j - len(num)] = num
#                     arr[i][(j - len(num)) + 1] = item
#                     num = ""
#                     continue
#                 arr[i][j] = item
#                 continue
#             if num != "":
#                     arr[i][j - len(num)] = num
#                     arr[i][(j - len(num)) + 1] = item
#                     possUpdate = (j - len(num)) + 2
#                     num = ""
#                     continue
#             arr[i][j] = item

# for i, item in enumerate(arr):
#     for j, cell in enumerate(item):
#         if cell == 0:
#             arr[i].pop(j)
#             if arr[i][j] == 0:
#                 arr[i].pop(j)
finalAnswer = 0
left = []
right = []
other = []
for i, item in enumerate(arr):
    if i > 0 and i < len(arr) - 1:
        for j, index in enumerate(item):
            if index != "." and index.isdigit() == False:
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
                                finalAnswer += int(tempValue)
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
                            finalAnswer += int(tempValue)
                            left.append(tempValue)
                            # print(tempValue)
                            tempValue = "" 
                #     if arr[x][cell].isdigit():
                #         # columnIndex += str(x)
                #         # rowIndex += str(j)
                #         if arr[x][j].isdigit() == False:
                #             for k in range(cell - 3, j):
                #                 if len(tempValue) >= 1:
                #                     while arr[x][k].isdigit():
                #                         tempValue = tempValue +  arr[x][k]
                #                         k = k + 1
                #                     finalAnswer += int(tempValue)
                #                     left.append(tempValue)
                #                     # print(tempValue)
                #                     tempValue = ""
                #                     break
                #                 if arr[x][k].isdigit() and arr[x][k + 1] != ".":
                #                     tempValue = tempValue +  arr[x][k]
                # tempValue = ""
                
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
                            finalAnswer += int(tempValue)
                            right.append(tempValue)
                            # print(tempValue)
                            tempValue = ""
                            # for k in range(cell, cell + 3):
                            #     if len(tempValue) >= 1:
                            #         while arr[x][k].isdigit():
                            #             tempValue = tempValue +  arr[x][k]
                            #             if k != len(item) - 1:
                            #                 k = k + 1
                            #             else:
                            #                 break
                            #         finalAnswer += int(tempValue)
                            #         right.append(tempValue)
                            #         # print(tempValue)
                            #         tempValue = ""
                            #         break
                            #     if arr[x][k].isdigit() and arr[x][k + 1] != ".":
                            #         tempValue = tempValue +  arr[x][k]
# print('pizza time')
# for x in left:
#     print(x)
# for x in other:
#     print(x)
# for x in right:
#     print(x)
# print(finalAnswer)

with open('Day3/output.txt', 'w') as file:
    file.write('start other\n')
    for x in other:   
        file.write(x + '\n')
    file.write('start left\n')
    for x in left:
        file.write(x + '\n')
    file.write('start right\n')
    for x in right:
        file.write(x + '\n')
                # for x in range(column, column + 3):
                #     if arr[x][cell].isdigit():
                #         columnIndex += str(x)
                #         rowIndex += str(cell)
                # cell = j + 2        
                # for x in range(column, column + 3):
                #     if arr[x][cell].isdigit():
                #         columnIndex += str(x)
                #         rowIndex += str(cell)
# for x, y in zip(columnIndex, rowIndex):
#     print(x, y, arr[int(x)][int(y)])
    # if i == 0:
    #     for j, index in enumerate(item):
    #         if index != ".":
    #             if index.isdigit():


# for item in arr:
#     print(item)
# line1 = arr[0]
# line2 = arr[1]
# line3 = arr[2]

# for i,  in enumerate(line1):
#     print(i)

