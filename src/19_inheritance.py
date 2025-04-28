class Build:
    year = None
    city = None

    def __init__(self, year=None, city=None):
        self.year = year
        self.city = city
        

    def get_data(self):
        print("year: ", self.year, ". city:", self.city, sep="")


class School(Build):
    pupils = None

    def __init__(self, year=None, city=None, pupils=None):
        super(School, self).__init__(year, city)
        self.pupils = pupils
        self.get_data()

    def get_data(self):
        print("year: ", self.year, ". city:", self.city, " pupils: ", self.pupils, sep="")


class House(Build):
    pass


class Shop(Build):
    pass


school = School(2001, "Oslo", 444)
house = House(2021, "Paris")
shop = Shop(2005, "Miami")
