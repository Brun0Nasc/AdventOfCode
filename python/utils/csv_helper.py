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
