def load_built_in_examples(code_manager):
    """Load built-in examples into the code manager."""
    
    # Decision Tree Example
    dt_code = '''
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Create and train the model
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

# Make predictions
y_pred = dt.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
'''
    code_manager.save_code("decision_tree", dt_code)

    # Random Forest Example
    rf_code = '''
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Create and train the model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Make predictions
y_pred = rf.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
'''
    code_manager.save_code("random_forest", rf_code)

    # Data Preprocessing Example
    preprocessing_code = '''
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd

# Load your data
# df = pd.read_csv('your_data.csv')

# Handle missing values
df = df.fillna(df.mean())

# Encode categorical variables
le = LabelEncoder()
categorical_columns = ['column1', 'column2']  # Replace with your categorical columns
for col in categorical_columns:
    df[col] = le.fit_transform(df[col])

# Scale numerical features
scaler = StandardScaler()
numerical_columns = ['column3', 'column4']  # Replace with your numerical columns
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
'''
    code_manager.save_code("preprocessing", preprocessing_code)

    # Cross Validation Example
    cv_code = '''
from sklearn.model_selection import cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier

# Create model
rf = RandomForestClassifier(random_state=42)

# Perform k-fold cross validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(rf, X, y, cv=kf)

print("Cross Validation Scores:", cv_scores)
print("Mean CV Score:", cv_scores.mean())
print("Standard Deviation:", cv_scores.std())
'''
    code_manager.save_code("cross_validation", cv_code)

    # Grid Search Example
    grid_search_code = '''
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Define the parameter grid
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10]
}

# Create model
rf = RandomForestClassifier(random_state=42)

# Perform grid search
grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)
'''
    code_manager.save_code("grid_search", grid_search_code)
