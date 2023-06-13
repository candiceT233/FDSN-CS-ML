import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import os

new_df = []

def preprocess_data(folder_path, common_attributes, output_folder):
    # Identify the common attributes

    # Initialize an empty list to store preprocessed DataFrames
    preprocessed_dfs = []

    # Iterate over the Excel files
    for file in os.listdir(folder_path):
        if file.endswith(".xlsx"):
            # Construct the file paths for input and output
            input_file_path = os.path.join(folder_path, file)
            output_file_path = os.path.join(output_folder, file)

            # Read the Excel file into a DataFrame
            df = pd.read_excel(input_file_path)

            # Select only the common attributes from the DataFrame
            df = df[list(common_attributes)]

            # Perform additional preprocessing steps if needed
            # ...

            # Save the preprocessed DataFrame as an Excel file
            df.to_excel(output_file_path, index=False)
            print(f"Preprocessed data saved to {output_file_path}")

            # Append the preprocessed DataFrame to the list
            preprocessed_dfs.append(df)

    return preprocessed_dfs