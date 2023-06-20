# Data Preprocessing Requirements
## Expedted input:
    Onboraded datasets with formated file name: `[study_name]-[data_type]-[suffix].csv`.
## Expedted output:
    - Merged master datasets.
    - Optional dataset report with selective studies.

---
### 1. Data cleaning
    - Remove missing values, duplicates, and outliers from the dataset. 
    - Integrate data imputation as a optional tool.
    - Data normalization and scaling.

### 2. Feature engineering
    - Encoding categorical variables.
    - New features to improve the predictive power of the model.
    - Organize variables into meaningful groups and assign labels to facilitate pattern and relationship discovery.

### 3. Feature selection
    - Select the most important features based on their correlation with the target variable.

### 4. Database/Master dataset
    - Combining all the datasets with the relevant ID.

### 5. Splitting the dataset (optional)
    - Shuffle dataset.
    - Split the dataset into training and testing sets for model training and evaluation.

## 6. Master Dataset
    - Columns names.
    - List of input dataset nanmes.
    - Dataset size (rows).

### 7. Datasets report
    - Analysis report for the dataset.
    - Report should be generated based on meaningful grouping of features and target variables.
    - Take user input with their selection of studies and generate a panda-datafram report. Also give option of `all_studies`.
    - Take user input with variables to generate report. (Future)

## Features, Targets, and Modeling:
    - Evaluate different modles on different targest
    - Recursive feature elemination


--
---

## Old Notes:
To merge Excel files that include various columns and create the last dataset using algorithms for learning or Python, one can follow the steps that follow:

### 1.	Feed the Excel documents: 
Use a library such as Pandas to import each Excel file into a distinct DataFrame. The files can be loaded using the pd.read_excel() function.

### 2.	Determine common characteristics: 
Examine the columns in each the DataFrame to locate common characteristics or fields that can be used to establish connections between the datasets. Look for columns with similar names or that have information in common.

### 3.	Data clean up:
Data preparation To handle values that are missing, change data types, and carry out any necessary data transformations, preprocess each DataFrame separately. This stage assures uniformity and prepares information for merger. (Column name standardization is done in onboarding step).

### 4. Missing Values:
Dealing with missing values You might find missing values in the combined dataset after combining the DataFrames. If necessary, use appropriate imputation methods to fill in the missing values, such as mean imputation, median imputation, or machine learning-based imputation.

### 5. Feature architecture:
Perform features engineering to derive additional characteristics or modifications that can boost the prediction potential of your dataset. This may include creating additional columns, combining data, or performing mathematical operations.

### 6. DataFrame Merging:
Identify the common fields or attributes that can be used as keys to combine the DataFrames. To combine the DataFrames based on these shared attributes, use the merge() function in Pandas. Depending on your needs, you can specify the type of join (such as an inner join or an outer join).

### 7.	Modeling: 
Use algorithms or models for machine learning to evaluate the combined dataset. This can include tasks such as categorization, regression analysis, grouping, or any other appropriate analysis depending on your the project's objectives.

### 8.	Examine and confirm the model: 
Assess the efficacy of your model for machine learning using suitable assessment criteria and validation techniques. This step makes sure the model is trustworthy and works well with untested data.

### 9.	Export the completed datasets: 
- Once you have gone through and analyzed the combined the data set, you are able to export it to a specified format, like Excel, CSV, or a database.
- Particularly selection features and target can be exported into a dataset as record.

### 10. DataFrame Report
- Use pandas tool to generate DataFrame report.
- Report should be generated based on meaningful grouping of features and target variables.