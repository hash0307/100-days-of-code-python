import pandas

census_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#OPTION #1
# gray_squirrel_count = len(census_data[census_data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrel_count = len(census_data[census_data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(census_data[census_data["Primary Fur Color"] == "Black"])

# squirrel_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
# }

# print(squirrel_dict)

# df = pandas.DataFrame(squirrel_dict)
# df.to_csv("squirrel_count.csv")


#OPTION #2
fur_color = census_data["Primary Fur Color"].value_counts()
print(fur_color)

squirrel_dict = {
    "Fur Color": fur_color.index.to_list(),
    "Count": fur_color.to_list()
}
print(squirrel_dict)

df = pandas.DataFrame(squirrel_dict)
df.to_csv("squirrel_count_option2.csv")