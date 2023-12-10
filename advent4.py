import re
import math 


cards = []
cardslist = []
cards_value = 0
puzzle = open("puzzle4.txt", "r").readlines()
expression = r'^(Card\s+\d+):\s+([\d\s]+)\|\s+([\d\s]+)$'
    
for line in puzzle:
    card_name, winners, numbers = re.match(expression, line).groups()
    winners = {int(winners) for winners in winners.split() if winners.strip()}
    numbers = {int(numbers) for numbers in numbers.split() if numbers.strip()}
    
    card_number = int("".join(re.findall(r'\d', card_name)))
    
    new_cards = len(winners.intersection(numbers))
    
    card = (card_number, new_cards)
    cards.append(card)
    cardslist.append(card)
    
count = 0


while True:
    try:
        card_number, new_cards = cards[count]
        # print(f"total cards: {len(cards)}, card {card_number} drawn")
        count += 1
        
    except IndexError:
        print("count", count)
        break
    
    #print(f"round {count}, new cards drawn from card {card_number}:",new_cards)
    for i in range(new_cards):
        cards.append(cardslist[card_number+i])
        # print(f"cycle {i+1} adding card number {cardslist[card_number+i]} to the set")
    
    # print(f"list now containing {len(cards)}")
        

    
    

