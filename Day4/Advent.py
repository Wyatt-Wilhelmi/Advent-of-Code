arr = []
lineNumber = 0
with open('Day4/input.txt') as input_file:
    for line in input_file:
        arr.append(1)

finalAnswer = 0

with open('Day4/input.txt') as input_file:
    for i, line in enumerate(input_file):
        setOne = ""
        setTwo = ""
        i = 10
        while i < len(line):
            if i < 40:
                setOne += line[i]
            elif i > 41:
                setTwo += line[i]
            i += 1
        base = ""
        tempValue = 0
        for num in setOne:            
            if num.isdigit():
                base += num
            elif len(base) > 0:
                pair = ""
                for item in setTwo:
                    if item.isdigit():
                        pair += item
                    elif len(pair) > 0:
                        if int(base) == int(pair):
                            # if(tempValue != 0):
                            #     tempValue = tempValue * 2
                            # else:
                            #     tempValue += 1
                            # Part One

                            tempValue += 1
                        pair = ""
                base = ""
        if tempValue != 0:
            for x in range(0, arr[lineNumber]):
                for j in range(1, tempValue + 1):
                    arr[lineNumber + j] += 1
        # finalAnswer += tempValue
        #Part One 
        lineNumber += 1
        
for x in arr:
    finalAnswer += x
print(finalAnswer)