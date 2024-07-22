import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# CSV
data = pd.read_csv("E:\Studying_project\data.csv", header=0, sep=';')

# Data errors check-up

print('Headers:', data.columns)
print('Data types: ', data.dtypes)
print('Skipped values: ', data.isnull().sum())
print('Head rows: ', data.head())

# features(X) and target(Y) selection
X = data[['open', 'close', 'RSI', 'MACD', 'Momentum']]
y = data['Direction']

# Train and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Parameter selection with GridSearchCV
# *GridSearchCV is used for cross-validation check-up*
param_grid = {
    'n_estimators': [100, 200, 300, 400, 500, 600],    # number of trees
    'max_depth': [None, 10, 20, 30, 40],    # max depth of each tree
    # Other parameters...
}
rf = RandomForestClassifier()
stratified_cv = StratifiedKFold(n_splits=2)
grid_search = GridSearchCV(rf, param_grid, cv=stratified_cv)    # cv - cross-validation with '2' splits

grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_

# Learning with optimal parameters
best_rf = RandomForestClassifier(**best_params)
best_rf.fit(X_train, y_train)

# Evaluating the model with 'accuracy' metric
y_pred = best_rf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

print('Predicted price movement:', y_pred)
# Create 'new_data' with the result of analysis
# Example: predictions = best_rf.predict(new_data)
