surroundings = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

filename = "puzzle3.txt"

puzzle = open(filename, "r").readlines()

# print(puzzle)
numbers = []

def main():
    print(puzzle)
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
            
                if not inspect.isdigit() and inspect != "." and inspect != "\n":
                    return True
            
            except IndexError:
                pass
            
    return False
            
if __name__ == "__main__":
    main()

            
