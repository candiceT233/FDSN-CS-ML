import os
import pandas as pd
from sklearn.impute import SimpleImputer

from LoadingOnboardingDatasets.onboard import combine_excel_files
from CommonAttributes.checkcommon import identify_common_attributes
from DataPreprocessing.Preprocess import preprocess_data
from HandleMissingValues.imputer import handle_missing_values
from FeatureEngineering.FE import perform_feature_engineering
from ModelingEvaluationAndValidation.ME import perform_modeling
from ExportFinalDataset.EFD import write_combined_df_to_excel

class Index:
    def __init__(self, data_key_map):
        self.data_key_map = data_key_map

    def get_user_input(self):
        user_input = {}
        for key, value in self.data_key_map.items():
            user_input[key] = input(f"Enter {value}: ")
        return user_input

    def impute_data(self, data):
        # Convert the user input to a DataFrame
        df = pd.DataFrame([data])

        # Initialize the imputer with 'most_frequent' strategy
        imputer = SimpleImputer(strategy='most_frequent')

        # Perform imputation
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

        # Get the imputed values as a dictionary
        imputed_data = df_imputed.iloc[0].to_dict()

        return imputed_data


    def run(self):
        # Get user input
        user_input = self.get_user_input()

        # Check if the user wants to use the imputation tool
        use_imputation = input("Do you want to use the imputation tool? (y/n): ")

        if use_imputation.lower() == 'y':
            imputed_data = self.impute_data(user_input)
            print("Imputed data:")
            print(imputed_data)
        else:
            print("User input:")
            print(user_input)

        # STEP ONE 
        folder_path = "OnboardedDatasets"
        combined_df =  combine_excel_files(folder_path)
        print(combined_df)
        
        # STEP TWO 
        common_attributes = identify_common_attributes(folder_path)
        print("\nCommon attributes:")
        for attr in common_attributes:
            print(attr)

        # STEP THREE AND FOUR
        preprocessed_and_merged_data = preprocess_data(folder_path,common_attributes,'Preprocessed Datasets')

        #STEP FIVE
        non_missing_data = handle_missing_values(preprocessed_and_merged_data)

        #STEP SIX
        featured_engineered_data = perform_feature_engineering(non_missing_data)

        # Define the target variable column name
        target_variable = 'Target'  # Replace with the actual column name representing the target variable


        #STEP SEVEN AND EIGHT
        perform_modeling(featured_engineered_data,target_variable)

        # Write the combined dataframe to an Excel file
        output_file = "combined_data.xlsx"
        write_combined_df_to_excel(combined_df, output_file)


# Define the data key map
columns_to_filter = [
    'Subject', 'Randomization', 'Consentdate', 'Age', 'Visit', 'ScreenDate', 'Gender', 'BMI',
    'Ethnicity', 'Sequence', 'Tx', 'Time', 'TG', 'b_TG', 'N_TG', 'Chol', 'b_Chol', 'N_Chol',
    'Glc', 'b_Glc', 'N_Glc', 'Insulin', 'b_Ins', 'N_Ins', 'HOMA', 'b_HOMA', 'HOMACat', 'HOMAC2',
    'IR', 'RatioGlcIns', 'MetS', 'Sys1', 'Sys2', 'Sys3', 'SysM', 'Dia1', 'Dia2', 'Dia3', 'DiaM', 'HR1', 'HR2', 'HR3', 'HRM', 'QC1', 'QC2', 'Subj', 'Sex', 'Ethnic', 'Seq', 'Treat', 'RatioInsGlc', 'TAUCGlc', 'TAUCIns', 'PosiAUCGlc', 'PosiAUCIns'
]

# Define the data key map
data_key_map = {col: col for col in columns_to_filter}

# Create Index instance
index = Index(data_key_map)

# Run the data imputation process and combine Excel files
index.run()

