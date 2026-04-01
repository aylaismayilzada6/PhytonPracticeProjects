import csv
import pandas

# data = pandas.read_csv("weather_data.csv")
#
# # #print(data["temp"])
# # data_dict = data.to_dict()
# # #print(data_dict)
# # temp_list = data["temp"].to_list()
# # #print(temp_list)
# #
# # #mean = sum(temp_list)/len(temp_list)
# #
# # mean = data["temp"].mean()
# maxi = data["temp"].max()
# # print(f"The mean: {mean} and max: {maxi} of Temp")
# # print(data["condition"])
#
# #get data in the form of a row
# # row_monday = data[data.day == "Monday"]
# # row_max_temp = data[data.temp == data.temp.max()]
# #
# # monday = data[data.day == "Monday"]
# # monday_temp = monday.temp[0]
# # monday_F_temp = (monday_temp * 9/5) + 32
#
#
# #How create a dataframe from scratch
# data_dict = {
#     "students" : ["Amy", "are", "you okay?"],
#     "score" : [67, 68, 69]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("test.csv")

data = pandas.read_csv("Squirrel_Data.csv")
gray = data[data["Primary Fur Color"] == "Gray"]
grays_count = len(data[data["Primary Fur Color"] == "Gray"])
red = data[data["Primary Fur Color"] == "Cinnamon"]
reds_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = data[data["Primary Fur Color"] == "Black"]
blacks_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
   # "Fur Color" : [gray, red, black],
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grays_count, reds_count, blacks_count]

}
data_squirrels  = pandas.DataFrame(data_dict)
data_squirrels.to_csv("Updated_Squirrels.csv")