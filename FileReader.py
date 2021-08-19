import csv

class CSVReader:

    def __init__(self, file):
        self.file = file

    def read(self):

        with open(self.file, newline='') as csvfile:
            fieldnames = [
                'region',
                'municipality',
                'settlement',
                'latitude',
                'longitude'
            ]
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            settlements = []
            for row in reader:
                settlements.append(row)

            return settlements