import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("fertilizer.csv")

# Input features and output
X = data[['N', 'P', 'K']]
y = data['fertilizer']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

def recommend_fertilizer(n, p, k):
    prediction = model.predict([[n, p, k]])
    return prediction[0]
