from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression


def perform_modeling( preprocessed_df, target_variable):
    # Split the data into training and testing sets
    X = preprocessed_df.drop(target_variable, axis=1)  # Input features
    y = preprocessed_df[target_variable]  # Target variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Choose a machine learning algorithm (e.g., Logistic Regression)
    model = LogisticRegression()

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    # Calculate additional evaluation metrics
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Perform cross-validation
    # Example using 5-fold cross-validation
    from sklearn.model_selection import cross_val_score
    scores = cross_val_score(model, X, y, cv=5)
    print("Cross-validation scores:", scores)

    # Perform grid search for hyperparameter tuning
    # Example using GridSearchCV for logistic regression
    from sklearn.model_selection import GridSearchCV
    param_grid = {'C': [0.1, 1, 10]}
    grid_search = GridSearchCV(model, param_grid, cv=5)
    grid_search.fit(X_train, y_train)
    best_params = grid_search.best_params_
    print("Best parameters:", best_params)


    # Perform hyperparameter tuning if needed

    # Repeat steps 3-6 with different models
    # ...
