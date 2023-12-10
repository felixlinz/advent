surroundings = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

filename = "puzzle3.txt"

puzzle = open(filename, "r").readlines()

# print(puzzle)
numbers = []

def main():
    gear_ratios = []
    
    for i, row in enumerate(puzzle):
        for j, char in enumerate(row):
            if char == "*":
                gear_ratios.append(check_star((i,j)))
                
    print(sum(gear_ratios))
                
                
            
def check(coordinates):
    for coordinate in coordinates:
        for surrounding in surroundings:
            y, x = coordinate
            i, j = surrounding
            
            a, b = x+i, y+j
            # print(a,b)

            try: 
            
                inspect = puzzle[b][a]
            
                if inspect == "*":
                    return True
            
            except IndexError:
                pass
            
    return False

def check_star(coordinate):    
    numbers = set()
    
    for surrounding in surroundings:
    
        y, x = coordinate
        i, j = surrounding
            
        a, b = x+i, y+j
        # print(a,b)

        try: 
        
            inspect = puzzle[b][a]
        
            if inspect.isnumeric():
                new_number = identify_number((b,a))
                if not new_number in numbers:
                    numbers.add(new_number)
        
        except IndexError:
            pass
        
    if len(numbers) == 2:
        return(numbers.pop()*numbers.pop())
    
    else: 
        return 0
    
def identify_number(coordinate):
    y,x = coordinate
    while True:
        if puzzle[y][x-1].isnumeric():
            x = x-1
        else:
            break
        
    number = puzzle[y][x]
    while True:
        x += 1
        if puzzle[y][x].isnumeric():
            number = number + puzzle[y][x]
        else: 
            break
        
    return int(number)
    
            
if __name__ == "__main__":
    main()
