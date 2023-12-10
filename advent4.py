import re
import math 

cards = []
cards_value = 0
puzzle = open("puzzle4.txt", "r").readlines()
expression = r'^(Card\s+\d+):\s+([\d\s]+)\|\s+([\d\s]+)$'
    
for line in puzzle:
    card_name, winners, numbers = re.match(expression, line).groups()
    winners = {int(winners) for winners in winners.split() if winners.strip()}
    numbers = {int(numbers) for numbers in numbers.split() if numbers.strip()}
    card = {"Name":card_name, "Winners":winners, "Numbers": numbers}
    cards.append(card)
    
for card in cards:
    card_value = 2 ** (len(card["Winners"].intersection(card["Numbers"]))-1)
    if card_value >= 1:
        cards_value += card_value

print(cards_value)
    
    

