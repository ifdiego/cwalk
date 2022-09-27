import csv
import json

def main():
    data = {}

    with open('ratings.csv', 'r') as file:
        reader = csv.DictReader(file)
        for index, row in enumerate(reader):
            data[index] = row
        file.close()

    print(json.dumps(data, indent=2))

if __name__ == '__main__':
    main()
