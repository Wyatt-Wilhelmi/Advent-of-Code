# Game 1: 19 blue, 12 red; 19 blue, 2 green, 1 red; 13 red, 11 blue
# possible = []

# with open('Day2\input.txt') as input_file:
#     for i,line in enumerate(input_file):
#         game = 0
#         red = 0
#         green = 0
#         blue = 0
#         for j, item in enumerate(line):
#             # match currVal:
#             #     case currVal.startswith("Game"):
#             #         game = i + 1
#             #         j + 5
#             #     case currVal.startswith("red"):
#             #         red = item[j - 5: j - 1]
#             #         print(red)
#             if(line[j:].startswith("Game")):
#                 game = i + 1
#                 j += 6
#             if(line[j:].startswith("red")):
#                 red = line[j - 4: j - 1]
#                 print(red)

possible = []
finalAnswer = 0
with open('Day2/input.txt') as input_file:
    for i, line in enumerate(input_file):
        possRed = 0
        possGreen = 0
        possBlue = 0
        j = 7
        while j < len(line):
            if line[j:].startswith("red"):
                red = int(line[j - 3: j - 1])
                if red > possRed:
                    possRed = red
                j += len("red") + 2
                continue
            if line[j:].startswith("green"):
                green = int(line[j - 3: j - 1])
                if green > possGreen:
                    possGreen = green
                j += len("green") + 2
                continue
            if line[j:].startswith("blue"):
                blue = int(line[j - 3: j - 1])
                if blue > possBlue:
                    possBlue = blue
                j += len("blue") + 2
                continue
            j += 1  # Move to the next character
        if possRed != 0 and possGreen != 0 and possBlue != 0:
            game = possRed * possGreen * possBlue
            possible.append(game)
for num in possible:
    finalAnswer += num

print(finalAnswer)
        # If there's logic to append to 'possible', add it here

