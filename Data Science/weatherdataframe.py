import pandas as pd

weather = {
    "City": ["London","Edinburgh","Paris","Brussels","Texas"],
    "Temperature": [30,25,19,22,34],
    "Humidity": [3,8,5,4,2],
    "Rainfall": [5,7,2,3,0]
    }

weatherdf = pd.DataFrame(weather)
print(weatherdf)
print("")

hotest = weatherdf["Temperature"].max()
hotestrow = weatherdf[weatherdf["Temperature"] == hotest]
print(hotestrow)
print(hotestrow["City"])
#or
print(weatherdf[weatherdf["Temperature"] == weatherdf["Temperature"].max()]["City"])

print(weatherdf["Rainfall"].mean(axis=0))