# with open("weather_data.csv") as data_file:
#     #data = data_file.read()
#     data = data_file.readlines()
#     print(data)

import csv

#eliminates need for "readlines()"
with open("weather_data.csv") as data_file:
  data = csv.reader(data_file)
  for row in data:
    print(row)

    #print(row[1])  for printing only temperature