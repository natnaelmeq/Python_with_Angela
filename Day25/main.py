# with open("weather_data.csv") as weather_data:
#     weather_this = weather_data.readlines()
#     print(weather_this)

# import csv
# with open("weather_data.csv") as data_file:
#     data =csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
    # print(temperatures)


import pandas
# data = pandas.read_csv("weather_data.csv")
#
# # temp_list = data["temp"].to_list()
# # print(len(temp_list))
# #
# # average = sum(temp_list)/len(temp_list)
# # print(average)
# print(data[data.temp == data.temp.max()])

data =pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240711.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirrels)



