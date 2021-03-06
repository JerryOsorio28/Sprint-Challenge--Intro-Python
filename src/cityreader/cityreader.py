# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon
  
  def __repr__(self):
    return f'{self.name}, {self.lat}, {self.lon}'

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
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list

  import csv

  path = 'cities.csv'
  file = open(path)
  reader = csv.reader(file)

  header = next(reader) #eliminates the first line of csv (header)
  data = [row for row in reader] #iterates over the file, line by line

  for i in data:
     cities.append(City(i[0], float(i[3]), float(i[4]))) #adds all the elements needed to the cities array as a new City instance --name / lat / lon--

  return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
# for c in cities:
#     print(type(c))

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
# Enter lat1,lon1: 45,-100 (lat1 greater, lon1 greater)
# Enter lat2,lon2: 32,-120 (lat2 less, lon2 less)
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
first_response = input('type the first coordinates, each separated by a comma ~~> ')
first_lat_lon = first_response.split(',')
nums = [int(num) for num in first_lat_lon]
lat1 = nums[0]
lon1 = nums[1]
print('first lat lon', lat1, lon1)

second_response = input('type the second coordinates, each separated by a comma ~~> ')
second_lat_lon = second_response.split(',')
nums = [int(num) for num in second_lat_lon]
lat2 = nums[0]
lon2 = nums[1]
print('second lat lon', lat2, lon2)

# if(lat1 < lat2 and lon1 < lon2):
#   temp_lat1 = lat1
#   temp_lon1 = lon1
#   lat1 = lat2
#   lon1 = lon2
#   lat2 = temp_lat1
#   lon2 = temp_lon1

# print('lat1 and lon 1', lat1, lon1)
# print('lat2 and lon 2', lat2, lon2)

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []

  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

  # iterate over cities array on index 1 and 2 (lat, lon)
  for city in cities:
  # we have to append to within array anything in city.lat less than lat1 and in city.lon anything less than lon1
  # as well as append to within array anything in city.lat less than lat2 and in city.lon anything less than lon2
    if(city.lat <= lat1 and city.lon <= lon1 and city.lat >= lat2 and city.lon >= lon2):
      within.append(city)
  # This checks if the inputs were typed in passing lat2 and lon2 first, if it did, it reverts the values so that lat1 and lon1 always comes first.
    elif(city.lat >= lat1 and city.lon >= lon1 and city.lat <= lat2 and city.lon <= lon2):
      temp_lat1 = lat1
      temp_lon1 = lon1
      lat1 = lat2
      lon1 = lon2
      lat2 = temp_lat1
      lon2 = temp_lon1
      within.append(city)

  return within

cityreader_stretch(45, -100, 32, -120, cities)
                #lat1, lon1 // lat2, lon2
cityreader_stretch(32, -120, 45, -100, cities)
                #lat2, lon2 // lat1, lon1  
