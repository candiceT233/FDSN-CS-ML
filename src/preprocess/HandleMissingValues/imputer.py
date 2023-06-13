import pandas as pd
from sklearn.impute import SimpleImputer

def handle_missing_values(data):
    # Initialize the imputer with 'mean' strategy
    imputer = SimpleImputer(strategy='mean')

    # Perform mean imputation on the data
    imputed_data = imputer.fit_transform(data)

    # Convert the imputed data array back to a DataFrame
    imputed_df = pd.DataFrame(imputed_data, columns=data.columns)

    return imputed_df
