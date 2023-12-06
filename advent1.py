import re

document = "puzzle1.txt"
secret_number = int()

for line in open(document, "r"):
    linecharacters = re.findall(r'\d', line)
    secret_number += int(f"{linecharacters[0]}{linecharacters[-1]}") 
    
print(secret_number)
    
        