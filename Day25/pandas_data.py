import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"]) #Prints the column temp

print(type(data))           #DataFrame (Like a table, 2-D)
print(type(data["temp"]))   #Series (Like a list, 1-D)


data_dict = data.to_dict()
temp_list = data["temp"].to_list()

print(data_dict)
print(temp_list)

#CHALLENGE
print(f"Average of Temperatures: {sum(temp_list)/len(temp_list):.2f}")
#OR
print(data["temp"].mean())

print(data["temp"].max())   # Highest value

print(data["condition"])    # Like a dictionary, condition is here is like the key 
#OR
print(data.condition)       # Both statements are same, BTS - pandas converts the column headers as attributes for easier access

# Get Data in the Row
print(data[data.day == "Monday"])
# Get Data where temperature is max
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32      # Converted to Farenheit
print(monday_temp_F)

# Create a dataframe from scratch
data_dictionary = {
    "students": ["Amy", "James", "Ang"],
    "scores": [76,56,65]
}

data_from_dictionary = pandas.DataFrame(data_dictionary)
print(data_from_dictionary)
data_from_dictionary.to_csv("new_data.csv")