from utils.csv_helper import get_dictionary_from_csv
import re
from utils.strings import extract_numbers
from math import prod

sumOfGames = 0
sumOfMultiplication = 0
dictionary = get_dictionary_from_csv('./csv_files/day_2.csv', True, ";",":")

colorMap = {"red": 12,"green": 13,"blue": 14}

regex = r"(\d+)\s+(\w+)"

for key, value in dictionary.items():
    gameID = int("".join(extract_numbers(key)))
    possible = True
    fewestPossibleMap = {"red": 0,"green": 0,"blue": 0}

    for v in value:
        splittedValues = v.split(",")

        for item in splittedValues:
            match = re.search(regex, item)
            if match:
                number = int(match.group(1))
                color = match.group(2)

                if number > colorMap[color]:
                    possible = False
                
                if number > fewestPossibleMap[color]:
                    fewestPossibleMap[color] = number
    
    if possible:
        sumOfGames += gameID
    
    sumOfMultiplication += prod(fewestPossibleMap.values())

print(f"Number of possible games on part 1: {sumOfGames}")
print(f"Sum of the fewest possible games on part 2: {sumOfMultiplication}")
