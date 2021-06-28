import csv
import models

class DataLoader:
    def __init__(self, db, routes_prefix, cities_filename):
        self.__db = db
        self.__routes_prefix = routes_prefix
        self.__cities_filename = cities_filename

    def load_city(self, city_id, city_name):
        with open(self.__routes_prefix+str.lower(city_name)+".csv", newline='') as csvfile:
            routes_reader = csv.reader(csvfile, delimiter=',')
            next(routes_reader, None)  # skip the headers
            for route_id, route_short_name, route_desc in routes_reader:
                city = models.Routes(route_id=route_id,
                                     short_name=route_short_name,
                                     description=route_desc,
                                     city=city_id)
                self.__db.session.add(city)
            self.__db.session.commit()

    def load(self):
        with open(self.__cities_filename, newline='') as csvfile:
            cities_reader = csv.reader(csvfile, delimiter=',')
            next(cities_reader, None)  # skip the headers
            for _, city_name in cities_reader:
                city = models.Cities(name=str.lower(city_name))
                self.__db.session.add(city)
                self.__db.session.commit()

            cities = models.Cities.query.all()
            for city in cities:
                self.load_city(city.id, city.name)