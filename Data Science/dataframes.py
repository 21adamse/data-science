import pandas as pd

data = {
    "Name": ["Aarav", "Diya", "Kunal", "Meera", "Rohan", "Anaya"],
    "Maths": [78, 85, 67, 92, 74, 88],
    "Science": [82, 79, 70, 90, 76, 85],
    "English": [75, 88, 72, 91, 80, 86]
    }

df = pd.DataFrame(data)
print(df)
print("")

#printing certain rows
print(df.head(3))
print("")

#printing certain collumns
print(df["Name"])
print("")
print(df[["Maths","Science"]])
print("")

#adding new collumn
df["Average"] = df[["Maths","Science","English"]].mean(axis=1)
print(df)
print("")

#finding max values
print(df[["Maths","Science","English"]].max())
print("")

#conditional selection (rows)
print(df[df["Average"] > 75])