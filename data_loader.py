import csv
import models

class DataLoader:
    def __init__(self, db, routes_prefix, cities_filename):
        self.__db = db
        self.__routes_prefix = routes_prefix
        self.__cities_filename = cities_filename


    def load(self):
        with open(self.__cities_filename, newline='') as csvfile:
            cities_reader = csv.reader(csvfile, delimiter=',')
            next(cities_reader, None)  # skip the headers
            for row in cities_reader:
                print(row)
                city = models.Cities(name=row[1])
                self.__db.session.add(city)
                self.__db.session.commit()