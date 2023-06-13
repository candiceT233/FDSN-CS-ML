import pandas as pd
from sklearn.impute import SimpleImputer

# Define the data key map
data_key_map = {
    'name': 'Name',
    'age': 'Age',
    'gender': 'Gender',
    'city': 'City',
}

# Function to get user input
def get_user_input():
    user_input = {}
    for key, value in data_key_map.items():
        user_input[key] = input(f"Enter {value}: ")
    return user_input

# Function to perform data imputation
def impute_data(data):
    # Convert the user input to a DataFrame
    df = pd.DataFrame([data])

    # Initialize the imputer
    imputer = SimpleImputer(strategy='most_frequent')

    # Perform imputation
    df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

    # Get the imputed values as a dictionary
    imputed_data = df_imputed.iloc[0].to_dict()

    return imputed_data

# Get user input
user_input = get_user_input()

# Check if the user wants to use the imputation tool
use_imputation = input("Do you want to use the imputation tool? (y/n): ")

if use_imputation.lower() == 'y':
    imputed_data = impute_data(user_input)
    print("Imputed data:")
    print(imputed_data)
else:
    print("User input:")
    print(user_input)
