import pandas as pd

cars = pd.read_csv("data2.csv")
ohe_cars = pd.get_dummies(cars['Mobil'])

print(ohe_cars.to_string())
