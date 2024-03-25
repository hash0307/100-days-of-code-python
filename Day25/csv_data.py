import csv

# with open("weather_data.csv") as f:
#     data = f.readlines()    
temperatures = []
with open("weather_data.csv") as f:
    data = csv.reader(f)
    
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
        # print(row)

# print(data)
print(temperatures)