import re     
from utils.csv_helper import get_list_from_csv
from utils.numbers import extract_numbers

strings = get_list_from_csv('./csv_files/day_1.csv')

soma = 0

for string in strings:
    numbers = extract_numbers(string)
    
    if len(numbers) == 0:
        continue

    numbers = numbers[0] + numbers[len(numbers) - 1]

    inteiro = "".join(numbers)

    print(inteiro)
    
    soma += int(inteiro)

print(soma)