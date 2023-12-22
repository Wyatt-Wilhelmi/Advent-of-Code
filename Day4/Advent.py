with open('Day4/input.txt') as input_file:
    for line in input_file:
        setOne = ""
        setTwo = ""
        i = 10
        # for i,item in enumerate(line):
        #     if i < 40:
        #         setOne += item
        #     else:
        #         setTwo += item
        while i < len(line):
            if i < 40:
                setOne += line[i]
            elif i > 40:
                setTwo += line[i]
            i += 1

        # for num in setOne:

        #     for item in setTwo:
                