import re     
from utils.csv_helper import get_list_from_csv

strings = get_list_from_csv('archive.csv')

soma = 0

for string in strings:
    s = re.findall(r'[0-9]', string)
    if len(s) > 1:
        s = s[0] + s[len(s) - 1]
    else:
        s = s[0] + s[0]

    inteiro = "".join(s)
    
    soma += int(inteiro)

print(soma)