import os
import pandas as pd


def combine_excel_files(folder_path):
    # Initialize an empty list to store the dataframes
    dfs = []

    # Iterate over the files in the folder
    for file in os.listdir(folder_path):
        if file.endswith(".xlsx"):
            # Construct the file path
            file_path = os.path.join(folder_path, file)
            # Read the Excel file into a dataframe
            df = pd.read_excel(file_path)
            # Append the dataframe to the list
            dfs.append(df)

    # Combine the dataframes into a single dataframe
    combined_df = pd.concat(dfs)

    return combined_df