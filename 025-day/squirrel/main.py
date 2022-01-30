import pandas

dict_data = {
    "Fur Color": [],
    "Count": []
}

data    = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors  = data["Primary Fur Color"].unique()
print(colors)

for color in colors[1:]:
    row_with_color = data[data["Primary Fur Color"] == color]
    amount = row_with_color["Primary Fur Color"].count()
    dict_data["Fur Color"].append(color)
    dict_data["Count"].append(amount)

data = pandas.DataFrame(dict_data)
data.to_csv("squirrel_count.csv")