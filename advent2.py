import regex as re
from word2number import w2n

document = "puzzle1.txt"
secret_number = 0

for line in open(document, "r"):
    linecharacters = re.findall(r'(one|two|three|four|five|six|seven|eight|nine|\d)', line, overlapped=True)
    for i in range(len(linecharacters)):
        if not linecharacters[i].isnumeric():
            linecharacters[i] = w2n.word_to_num(linecharacters[i])
    secret_number += int(f"{linecharacters[0]}{linecharacters[-1]}") 
    print(int(f"{linecharacters[0]}{linecharacters[-1]}"))
    
print(secret_number)
            
    
        