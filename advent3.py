surroundings = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

filename = "puzzle3.txt"

puzzle = open(filename, "r").read().split("\n")

# print(puzzle)
numbers = []

def main():
    for y, line in enumerate(puzzle):
        index = 0
        number = ""
        coordinates = []
        for x, char in enumerate(line):
            if char.isdigit():
                number = number + char
                index = x
                coordinates.append((y,x))
                #print(index)
            elif x == index + 1:
                # print("CHECK", coordinates)
                if check(coordinates):
                    numbers.append(int(number))
                number = ""
                coordinates = []
                
    print(numbers)
    magic_number = sum(numbers)
    print(magic_number)
                
            
def check(coordinates):
    for coordinate in coordinates:
        for surrounding in surroundings:
            y, x = coordinate
            i, j = surrounding
            
            a, b = x+i, y+j
            # print(a,b)

            try: 
            
                inspect = puzzle[b][a]
            
                if not inspect.isdigit() and inspect != ".":
                    return True
            
            except IndexError:
                pass
            
    return False
            
if __name__ == "__main__":
    main()

            

# print(numbers)

# numbers = []

# for x, line in enumerate(puzzle):
#     for y, char in enumerate(line):
#         indexes = set()
#         if char.isdigit() and y not in indexes:
#             indexes.add(y)
#             coordinates = [(x,y)]
#             number = char
#             duration = 1
#             while True:
#                 try:
#                     if puzzle[x][y+duration].isdigit():
#                         index = y+duration
#                         number = number + (puzzle[x][y+duration])
#                         print(puzzle[x][y+duration])
#                         indexes.add(y+index)
#                         duration += 1
#                     else: 
#                         numbers.append(number)
#                         break
                            
#                 except IndexError:
#                     numbers.append(number)
#                     break

#print(numbers)
                