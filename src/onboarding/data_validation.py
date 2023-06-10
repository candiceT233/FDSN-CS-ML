
import argparse
import os
import pandas as pd
from ydata_profiling import ProfileReport
from difflib import get_close_matches
from datetime import datetime


log_dir="./logs"
default_log_name="data_validation.log"
onboarded_dir="./data/onboarded"

# setup the logging
import logging
logging.basicConfig(level=logging.INFO)
# save the logs to a file in the logging directory
logger = logging.getLogger(__name__)

def remove_extension(file_name):
    base_name, extension = os.path.splitext(file_name)
    if extension.lower() in ['.csv', '.xlsx']:
        return base_name
    else:
        return base_name
    
# Function to match the simillar or nearlly simillar keys in the dataset and the dictionary and log them
def validate_match_keys(dataframe, dataframe_name, data_key_map_list, option, Data_key_map):
    """
    This function matches the simillar or nearly simillar keys in the dataset and the dictionary and log them
    """
    new_cols = []
    exist_cols = []
    for i in range(len(dataframe.columns)):
        if dataframe.columns[i].lower() not in data_key_map_list:
            if option in [0, 1]:
                new_cols.append(dataframe.columns[i])
                logger.info(f"{dataframe_name}: Column not present - {dataframe.columns[i]}")
            if option in [0, 1, 2]:
                close_match = get_close_matches(str(dataframe.columns[i]), str(data_key_map_list), n=1, cutoff=0.7)
                if close_match:
                    logger.info(f"{dataframe_name}: Close matches - {close_match}")
        elif option in [0]:
            exist_cols.append(dataframe.columns[i])
            # logger.info(f"{dataframe_name}: Columns which are present - {dataframe.columns[i]}")
    logger.info(f"{dataframe_name}: Columns which are present - {exist_cols}\n")
    new_cols_str = ""
    for nc in new_cols:
        new_cols_str+=str(nc) + ", "
    logger.info(f"{dataframe_name}: Columns which are not present - {new_cols_str}\n")

    return exist_cols


# Function to generate a pandas-profiling report for the initial EDA
def generateReport(dataframe, name):
    profile= ProfileReport(dataframe, explorative=True)
    profile.to_file(f'{name}_report.html')

def get_new_filename(data_filename):
    tmp_filename = input("Enter the new name for the file: ")
    if tmp_filename == "":
        tmp_filename = data_filename.split("/")[-1]
        tmp_filename = os.path.splitext(tmp_filename)[0]
        tmp_filename = tmp_filename.replace(" ","_")
        tmp_filename = tmp_filename.split("_")
        data_filenewname = ""
        if 'MMTT' in tmp_filename[0]:
            data_filenewname += tmp_filename.pop(0) + "_"
        data_filenewname+=tmp_filename.pop(0) + "-"
        data_filenewname+=tmp_filename.pop(0) + "-"
        for rest_ss in tmp_filename:
            data_filenewname+= rest_ss + "_"
        data_filenewname = data_filenewname[0: len(data_filenewname)-1]
            
        logger.info(f"Default filename name is: {data_filename}.csv")
    else:
        data_filenewname = remove_extension(tmp_filename)
        logger.info(f"New file name of {data_filename} is : {data_filenewname}")
    return data_filenewname 

def get_rename_map(Data_key_map):
    data_key_map_list = []
    data_key_map_dict = {}
    for i in range(len(Data_key_map)):
        data_key_map_list.append(Data_key_map['Column Name'][i].lower())
        if type(Data_key_map['Alternate Name'][i]) == str:
            if ',' in Data_key_map['Alternate Name'][i]:
                # print(Data_key_map['Alternate Name'][i].lower().split(','))
                data_key_map_dict[Data_key_map['Column Name'][i]] = Data_key_map['Alternate Name'][i].lower().split(',')
                data_key_map_list.extend(Data_key_map['Alternate Name'][i].lower().split(','))
            else:
                data_key_map_list.append(Data_key_map['Alternate Name'][i].lower())
                data_key_map_dict[Data_key_map['Column Name'][i]] = Data_key_map['Alternate Name'][i].lower()
    return data_key_map_list, data_key_map_dict

def standardise_names(dataframe,data_key_map_list,data_key_map_dict):
    # Standardise column feature which will standardise the column names from alternate names to the column name
    data_columns_list = list(dataframe.columns)

    for i in range(len(data_columns_list)):
        if data_columns_list[i].lower() in data_key_map_dict.values():
            # Get the key for the value in the dictionary corresponding to the column name
            replace_key = list(data_key_map_dict.keys())[list(data_key_map_dict.values()).index(data_columns_list[i].lower())]
            dataframe.rename(columns={f"{dataframe.columns[i]}": f"{replace_key}"}, inplace=True)
            logger.info(f"{dataframe.columns[i]} renamed to {replace_key}")
    return dataframe

def validate_datatype(dataframe, dataframe_name, exist_cols, data_key_map_list, option, Data_key_map):
    print(Data_key_map)
    all_columns = dataframe.columns 
    for c in all_columns:
        dtype = dataframe[c].dtype
        if c not in exist_cols:
            logger.info(f"{dataframe_name}: Column [{c}] data type - {dtype}")
        

def main():
    # write the logs to a file
    file_handler = logging.FileHandler(f'{log_dir}/{default_log_name}')
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    parser = argparse.ArgumentParser()
    parser.add_argument('--newdata', type=str, help='File name of the new data') #TODO: make this required
    parser.add_argument('--keymap', type=str, help='File name of the key map') #TODO: make this required
    parser.add_argument('--loglevel', type=int, help='Logging level (0 - log everything, 1 - log close mathches and not present, 2 - log only close matches, 3 - log nothing))', default=0)
    args = parser.parse_args()

    # Access the file paths using the argument names
    data_filename = args.newdata
    keymap_filename = args.keymap
    loglevel = args.loglevel

    # Get the current working directory
    current_directory = os.getcwd()
    
    
    # Get the path to the file
    # data_path = os.path.join(current_directory, f'data/raw/{data_filename}')
    if "data/raw/" not in data_filename:
        data_filename = f"data/raw/{data_filename}"
    if "src/onboarding/" not in keymap_filename:
        keymap_filename = f"src/onboarding/{keymap_filename}"
    data_path = os.path.join(current_directory, f'{data_filename}')
    Data_key_map = os.path.join(current_directory, f'{keymap_filename}')

    # Read the data
    Data_finalized = pd.read_excel(data_path)
    logger.info(f"{data_filename} read successfully")
    Data_key_map = pd.read_excel(Data_key_map)
    logger.info(f"{keymap_filename} read successfully")

    # Option for the user to change the file name by displaying the current file name and the example format
    print(f"Current file name: {data_filename}")
    print("Example format: [study_name]-[data_type]-[suffix].csv")
    
    
    # Read the new file name from the user or press enter to continue with the same file name
    data_filenewname = get_new_filename(data_filename)
    
    # get the rename list from the key map
    data_key_map_list, data_key_map_dict = get_rename_map(Data_key_map)
    
    # Standardising column names
    Data_finalized = standardise_names(Data_finalized, data_key_map_list, data_key_map_dict)
    
    # Save the file with the new name and the standardized column names in the onboarding folder
    Data_finalized.to_csv(f"{onboarded_dir}/{data_filenewname}.csv", index=False)
    logger.info(f"{onboarded_dir}/{data_filenewname} saved successfully")

    exist_cols = validate_match_keys(Data_finalized, "Data_finalized", data_key_map_list, loglevel, Data_key_map)

    #TODO: Add the code to validate the data types
    validate_datatype(Data_finalized, "Datatype_validate", exist_cols, data_key_map_list, loglevel, Data_key_map)
    
    # Close logger and rename log file
    file_handler.close()
    # Get the current timestamp
    timestamp = datetime.now()
    # Format the timestamp to remove the delimiter
    formatted_timestamp = timestamp.strftime("%Y%m%d%H%M")
    new_log_filename = f'data_validation-{data_filenewname}-{formatted_timestamp}.log'
    new_log_file_path = os.path.join(log_dir, new_log_filename)
    os.rename(f"{log_dir}/{default_log_name}", new_log_file_path)

if __name__ == "__main__":
    main()
