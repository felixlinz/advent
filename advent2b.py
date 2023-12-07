filename = "puzzle2.txt"

games = []

for line in open(filename, "r"):
    game = line.split(":")
    gamenumber, data = game
    infos = data.replace('\n', '').split(";")
    
    
    red = 0
    green = 0
    blue = 0
    
    for info in infos:
        for subinfo in info.split(","):
            amount, color = subinfo.strip().split(" ")
            if color == "red":
                red = max(red,int(amount))
            elif color == "green":
                green = max(green,int(amount))
            elif color == "blue":
                blue = max(blue,int(amount))
            
    gamenumber = int(''.join(map(str, [char for char in gamenumber if char.isdigit()])))
    
    games.append({"game":gamenumber, "red": red , "green": green, "blue": blue})
        
secret_number = 0

threshold = {"red": 12, "green": 13, "blue": 14}

for game in games: 
    secret_number += game["red"]*game["green"]*game["blue"]
        
print(secret_number)
