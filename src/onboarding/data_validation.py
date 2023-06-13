
import argparse
import os
import sys 
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
            logger.info(f"{dataframe_name}: Column present - {dataframe.columns[i]}")
        
    new_cols_str = ""
    for nc in new_cols:
        new_cols_str+=str(nc) + ", "
    if new_cols_str != "":
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
        column_name = data_columns_list[i].lower()
        if column_name in data_key_map_dict.values():
            # Get the key for the value in the dictionary corresponding to the column name
            replace_key = list(data_key_map_dict.keys())[list(data_key_map_dict.values()).index(column_name)]
            dataframe.rename(columns={f"{dataframe.columns[i]}": f"{replace_key}"}, inplace=True)
            logger.info(f"{dataframe.columns[i]} renamed to {replace_key}")
    return dataframe

def validate_datatype(dataframe, dataframe_name, exist_cols, Data_key_map,data_filenewname):
    all_columns = dataframe.columns 
    for c in all_columns:
        dtype = str(dataframe[c].dtype)
        if c not in exist_cols:
            logger.info(f"{dataframe_name}: Column [{c}] data type - {dtype}")
        else:
            # expect_dtype = Data_key_map[Data_key_map['Column Name'] == c]['Expected_Data_type']
            row = Data_key_map[Data_key_map['Column Name'] == c]
            if not row.empty:
                expect_dtype = row['Expected_Data_type'].values[0]
                if expect_dtype != dtype:
                    logger.info(f"{dataframe_name}: Column [{c}] expected type [{expect_dtype}] but actual type - {dtype}")
                    
                    # update the data type mismatch file
                    orig_files = str(row['Data_type_Mismatch File'].values[0])
                    orig_files += str(data_filenewname)+","
                    Data_key_map.loc[Data_key_map['Column Name'] == c, 'Data_type_Mismatch File'] = orig_files

def parsing_arguments():
    # Start the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--newdata', type=str, help='File name of the new data') #TODO: make this required
    parser.add_argument('--keymap', type=str, help='File name of the key map') #TODO: make this required
    parser.add_argument('--loglevel', type=int, help='Logging level (0 - log everything, 1 - log close mathches and not present, 2 - log only close matches, 3 - log nothing))', default=0)
    parser.add_argument('--logtime', type=int, help='Log file timestamp (0 - no timestamp, 1 - timestamp)', default=1)
    args = parser.parse_args()
    
    # Check if no arguments were provided
    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()
    
    if not args.newdata or not args.keymap:
        parser.print_help()
        sys.exit(1)

    # Access the file paths using the argument names
    return args.newdata, args.keymap, args.loglevel, args.logtime

def read_excel_dataframe_only(data_path, existing_keys, sheet=""):
    row_count_max = 10 # only check if header in the first 10 rows
    header_found = False
    row_count = 0
    
    if sheet == "":
        while header_found == False:
            df = pd.read_excel(data_path, skiprows=row_count)
            df_columns = df.columns.tolist()
            df_columns = df_columns[:4] # only check the first 4 columns
            # print(f"Checking valid header row {row_count} : {df_columns} ")
            for col in df_columns:
                if str(col).lower() in existing_keys:
                    # print(f"Found header row {row_count} : {df_columns} ")
                    if (row_count > 0):
                        logger.info(f" Found header at row {row_count} - {df.columns.tolist()} ")
                    header_found = True
                    break
            if row_count == row_count_max:
                header_found = True
            row_count += 1
        df = pd.read_excel(data_path, skiprows=(row_count-1))
    else:
        while header_found == False:
            df = pd.read_excel(data_path, sheet_name=sheet, skiprows=row_count)
            df_columns = df.columns.tolist()
            df_columns = df_columns[:4] # only check the first 4 columns
            # print(f"Checking valid header row {row_count} : {df_columns} ")
            for col in df_columns:
                if str(col).lower() in existing_keys:
                    if (row_count > 0):
                        logger.info(f" Found header at row {row_count} - {df.columns.tolist()} ")
                    header_found = True
                    break
            if row_count == row_count_max:
                header_found = True
            row_count += 1
        df = pd.read_excel(data_path, sheet_name=sheet, skiprows=(row_count-1))
    
    df = df.drop(df.filter(regex='Unnamed').columns, axis=1)
    return df

def read_sheet_from_excel(data_path, data_file_path, Data_key_map):
    # get the existing list of keys
    existing_keys = Data_key_map['Column Name'].tolist()
    existing_keys = [x.lower() for x in existing_keys]
    for i,row in Data_key_map.iterrows():
        if row['Alternate Name']:
            alt_names = str(row['Alternate Name']).split(',')
            existing_keys.extend(alt_names)
    
    # get filename for display
    data_filename = os.path.basename(data_file_path)
    # Read the multiple sheets if present in the excel file
    worksheet_dict = {}
    
    onboard_data = pd.ExcelFile(data_path)
    onboard_data_sheets = onboard_data.sheet_names

    # Excel Sheet selection and log those sheets which are not present in the data
    worksheet_dict['shape'] = {}
    if len(onboard_data_sheets) > 1:
        for sheet in onboard_data_sheets:
            worksheet_dict['shape'][sheet] = pd.read_excel(data_path, sheet_name=sheet).shape

        worksheet_dict['compare'] = {}
        # Give the list of sheets in the onboard_data_sheets find the difference between the two sheets and update the worksheet_dict
        for sheet1, value1 in worksheet_dict['shape'].items():
            for sheet2, value2 in worksheet_dict['shape'].items():
                if sheet1 != sheet2:
                    if value1 != value2:
                        worksheet_dict['compare'][f'\"{sheet1}\" vs. \"{sheet2}\"'] = 'different'
                    else:
                        worksheet_dict['compare'][f'\"{sheet1}\" vs. \"{sheet2}\"'] = 'same'

        
        # Display sheet shape and comparison
        for sheet, value in worksheet_dict['shape'].items():
            logger.info(f" Worksheet \"{sheet}\" dataframe shape - {value}")
        for sheets, value in worksheet_dict['compare'].items():
            logger.info(f" Worksheet Comparison - {sheets} : {value}")
        
        # Read the sheet name from the user        
        # logger.info(f" Worksheet Dictionary: {worksheet_dict}")
        print(f" Sheets present in the file {data_filename}: {onboard_data_sheets}")
        sheet_name = input(f"Enter the sheet name which you want to select from the above list:")
        
        # default selecting the first sheet 
        if sheet_name == '':
            sheet_name = onboard_data_sheets[0]
            logger.info(f" Worksheet selected - name: \"{sheet_name}\", size: {worksheet_dict['shape'][sheet_name]}")
            
        # # TODO? select the largest sheet, if only valid content
        # if sheet_name == '':
        #     max_size_sheet, sheet_size = max(worksheet_dict['shape'].items(), key=lambda x: x[1][0] * x[1][1])
        #     sheet_name = max_size_sheet
        #     logger.info(f" Worksheet selected - name: \"{sheet_name}\", size: {sheet_size}")
        # else:
        #     logger.info(f" Worksheet selected - name: \"{sheet_name}\", size: {worksheet_dict['shape'][sheet_name]}")
        
            
        # Read the data from the sheet which is not a duplicate
        Data_finalized = read_excel_dataframe_only(data_path, existing_keys, sheet_name) # pd.read_excel(data_path, sheet_name=sheet_name)
        logger.info(f"{data_filename} read successfully with the sheet name \"{sheet_name}\"")
    else:
        # Read the data
        Data_finalized = read_excel_dataframe_only(data_path, existing_keys)
        logger.info(f"{data_filename} read successfully")
    return Data_finalized

def main():
    # Initialize logger and start file handler
    file_handler = logging.FileHandler(f'{log_dir}/{default_log_name}')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Parse the arguments
    data_filename,keymap_filename,loglevel,logtime = parsing_arguments()

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
    # Data_finalized = pd.read_excel(data_path)
    # logger.info(f"{data_filename} read successfully")
    Data_key_map = pd.read_excel(Data_key_map)
    Data_finalized = read_sheet_from_excel(data_path, data_filename, Data_key_map)
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

    # Validate the data types
    validate_datatype(Data_finalized, "Datatype_validate", exist_cols, Data_key_map, data_filenewname)
    
    # Close logger and rename log file
    file_handler.close()
    # Get the current timestamp
    timestamp = datetime.now()
    # Format the timestamp to remove the delimiter
    if logtime == 1:
        formatted_timestamp = timestamp.strftime("%Y%m%d%H%M")
        new_log_filename = f'data_validation-{data_filenewname}-{formatted_timestamp}.log'
    else:
        new_log_filename = f'data_validation-{data_filenewname}.log'
    new_log_file_path = os.path.join(log_dir, new_log_filename)
    os.rename(f"{log_dir}/{default_log_name}", new_log_file_path)

if __name__ == "__main__":
    main()
