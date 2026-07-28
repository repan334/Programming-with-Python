import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pandas.read_csv("data.csv")

d = { 'Inggris' : 0, 'Amerika Serikat' : 1, 'N' : 2}
df['Kebangsaan'] = df['Kebangsaan'].map(d)
d = {'YA' : 1, 'TIDAK' : 0}
df['Pergi'] = df['Pergi'].map(d)

features = ['Usia', 'Pengalaman', 'Pangkat', 'Kebangsaan']

X = df[features]
y = df['Pergi']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

tree.plot_tree(dtree, feature_names=features)
