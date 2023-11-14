# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = float(lat)
        self.lon = float(lon)

    def __repr__(self) -> str:
        return f"City('{self.name}', {self.lat}, {self.lon})"


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
import csv

cities = []


def cityreader(cities=[]):
    # Specify the path to your CSV file
    csv_file_path = "src/cityreader/cities.csv"

    # Open the CSV file
    with open(csv_file_path, "r") as csv_file:
        # Create a CSV reader
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            # Create a City instance and add it to the cities list

            city = City(row["city"], row["lat"], row["lng"])
            cities.append(city)
            print(city)

    return cities


# Call the cityreader function
cityreader(cities)

# Print the populated cities list
# print(cities)


# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # Ensure that lat1 is less than lat2 and lon1 is less than lon2
    min_lat, max_lat = min(lat1, lat2), max(lat1, lat2)
    min_lon, max_lon = min(lon1, lon2), max(lon1, lon2)

    within = []

    for city in cities:
        city_lat, city_lon = city.lat, city.lon

        if min_lat <= city_lat <= max_lat and min_lon <= city_lon <= max_lon:
            within.append(city)

    return within


# input from the user
lat1, lon1 = map(float, input("Enter lat1,lon1: ").split(","))
lat2, lon2 = map(float, input("Enter lat2,lon2: ").split(","))


result = cityreader_stretch(lat1, lon1, lat2, lon2, cities)


# get result like
#  Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)
for city in result:
    print(f"{city.name}: ({city.lat},{city.lon})")
