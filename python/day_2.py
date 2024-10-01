from utils.csv_helper import get_dictionary_from_csv
import re
from utils.strings import extract_numbers

sumOfGames = 0
dictionary = get_dictionary_from_csv('./csv_files/day_2.csv', True, ";",":")

colorMap = {"red": 12,"green": 13,"blue": 14}

regex = r"(\d+)\s+(\w+)"

for key, value in dictionary.items():
    gameID = int("".join(extract_numbers(key)))
    possible = True

    for v in value:
        splittedValues = v.split(",")

        for item in splittedValues:
            match = re.search(regex, item)
            if match:
                number = match.group(1)
                color = match.group(2)

                if int(number) > colorMap[color]:
                    possible = False
                    break
    
    if possible:
        sumOfGames += gameID

print(sumOfGames)
