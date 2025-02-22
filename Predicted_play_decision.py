from sklearn.tree import DecisionTreeClassifier

# Sample dataset: Weather features and labels (play decision)
X = [
    ['Sunny', 85, 85, False], ['Sunny', 80, 90, True],
    ['Overcast', 83, 78, False], ['Rainy', 70, 96, False],
    ['Rainy', 68, 80, False], ['Rainy', 65, 70, True],
    ['Overcast', 64, 65, True], ['Sunny', 72, 95, False],
    ['Sunny', 69, 70, False], ['Rainy', 75, 80, False],
    ['Sunny', 75, 70, True], ['Overcast', 72, 90, True],
    ['Overcast', 81, 75, False], ['Rainy', 71, 91, True]
]
y = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']

# Initialize the DecisionTreeClassifier
dt_classifier = DecisionTreeClassifier(random_state=42)

# Train the classifier on the entire dataset
dt_classifier.fit(X, y)

# New weather data to predict play decision (e.g., ['Sunny', 70, 80, True])
new_weather = [['Sunny', 70, 80, True]]

# Predict the label for the new weather data
predicted_decision = dt_classifier.predict(new_weather)

print("Predicted play decision:", predicted_decision)
