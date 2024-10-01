import csv

# get_list_from_csv is a function that reads a csv file and returns a list of strings
def get_list_from_csv(file_path, delimiter=None):
    with open(file_path) as csv_file:
        strings = []
        if delimiter:
            csv_reader = csv.reader(csv_file, delimiter=delimiter)
        else:
            csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            strings.append(row[0])
    return strings

# get_dictionary_from_csv is a function that reads a csv file and returns a dictionary
def get_dictionary_from_csv(file_path, list_values=False, list_delimiter=None, delimiter=None):
    with open(file_path) as csv_file:
        dictionary = {}
        if delimiter:
            csv_reader = csv.reader(csv_file, delimiter=delimiter)
        else:
            csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            if len(row) < 2:
                continue
            if list_values:
                dictionary[row[0]] = row[1].strip().split(list_delimiter)
            else:
                dictionary[row[0]] = row[1]
    return dictionary