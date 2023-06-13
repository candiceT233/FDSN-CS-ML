import os
import pandas as pd

def identify_common_attributes(folder_path):
        # Get the list of Excel files in the folder
        excel_files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]

        # Initialize a set to store the common attributes
        common_attributes = set()

        # Iterate over the Excel files
        for file in excel_files:
            # Load the Excel file into a DataFrame
            df = pd.read_excel(os.path.join(folder_path, file))

            # Get the column names of the current DataFrame
            current_attributes = set(df.columns)

            # Update the common attributes by finding the intersection
            if not common_attributes:
                # If it's the first DataFrame, add all column names
                common_attributes.update(current_attributes)
            else:
                # Find the intersection with the existing common attributes
                common_attributes.intersection_update(current_attributes)

        return common_attributes
    