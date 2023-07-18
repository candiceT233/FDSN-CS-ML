# Documenting Weekly progress here

### Week 1 [June 12th] :white_check_mark:
**Goals**
- Have been briefed by Candace on the overview of the project and the long term goals. Have been introduced to the datasets to be explored and key elements of the project.
  
**What went well?**
- N/A
  
**What did not go well?**
- The dataset 'MMTT_MCP-1_AVOC1_chooseA.xlsx' has not been onboarded as instructed because it has formatting issues that need to resolved first.
  
**Did I learn anything important?**
- Datasets still required alot of cleaning before it can be passed to the ML pipeline
  
**What is holding us back?**
- N/A
  
**What urgent questions do I have?**
- N/A
  
**Next step?**
- Setup the working environment
- familiarize with the datasets
- get access to github repo and one drive link to dataset


### Week 2 [June 19th] :white_check_mark:
**Goals**
- Onboarding tool discussed. Opened issues to clean datasets and prepare them as instructed using the data validator script. Divided 10 datasets among Anushka and I. Will be working on : MMTT_AVOC1, MMTT_FRTS, MMTT_SAT, MMTT_STRB, RRB
  
**What went well?**
- Succesfully onboarded the following datasets and uploaded the log files:
 - RRB
 - MMTT_FRTS

**What did not go well?**
- Could not process following:
 - MMTT_STRB -> UnicodeDecodeError: 'utf-8' codec can't decode bytes in position 15-16: invalid continuation byte
 - MMTT_AVOC1 -> same error, csv issue
 - MMTT_FRTS -> same

**Did I learn anything important?**
- data validation script uses 'pd.readexcel()' to read excel files but most of my datasets were in csv format. Adding a try catch to accomodate csv filetypes should help. 
- by using a separate script I checked that the file types are utf8-sig but specifying this encoding doesnt help.

**What is holding us back?**
- converting the csv to xlsx did not resolve the problem due to Unicode error

**What urgent questions do I have?**
- Errors to be discussed in the meeting and mitigated

**Next step?**
- Finish the other datasets


### Week 3 [June 26th] :white_check_mark:

**Goals**
- Data pre-processing discussed. Problems with onboarding discussed and plan to solve them had been laid out.

**What went well?**
- all datasets were successfully onboarded
- keymap file cross checked and multiple changes have been made as requested

**What did not go well?**
- N/A

**Did I learn anything important?**
- learned the correct hierarchy of the repo
- learned some semantic context behind the features present in the datasets

**What is holding us back?**
- N/A

**What urgent questions do I have?**
- N/A

**Next step?**
- Data preprocessing
- optimizing onboarding scripts, if necessary

### Week 4 [July 3rd] :white_check_mark:
**Goals**

Onboarded datasets cross checked and to be uploaded for Exploratory data analysis (EDA)

**What went well?**

- cross checked updated key map with main branch to ensure consistency
- renamed onboarded datasets to remove any redundant extensions
- re ran some datasets again
- added a notebook for EDA performed on RBB dataset
- created a templete for implementing correlation matrix from processed dataframes

**What did not go well?**

N/A

**Did I learn anything important?**

- learned which features in RBB are most related in order to find our target variable

**What is holding us back?**

N/A

**What urgent questions do I have?**

N/A

**Next step?**

- Continue with other datasets

### Week 5 [July 11th] :white_check_mark:

**Goals**

Data exploration for identifying target variables

**What went well?**

created a template to calculate correlation matrix from raw dataset


**What did not go well?**

needed to wait for preprocessed an merged dataset


**Did I learn anything important?**

N/A

**What is holding us back?**

N/A

**What urgent questions do I have?**

N/A

**Next step?**

Experiment with more methods


### Week 6 [July 18th] :white_check_mark:

**Goals**

Data exploration for identifying target variables

**What went well?**

- developed intuition between correlated attributes per dataset
- Separate notebooks per dataset discussing the possible pairs of attributes that can be considered for target
- Comparing pearson and spearman method for correlation


**What did not go well?**

- Could not handle datetime attribute
- Time attribute has inconsistent data


**Did I learn anything important?**

N/A

**What is holding us back?**

N/A

**What urgent questions do I have?**

- what can we do with the large Nulls in some attributes where simply imputing with mean is not practical?

**Next step?**

- Further EDA


### Week 7 [July 25th] :yellow_circle:

**Goals**

**What went well?**


**What did not go well?**


**Did I learn anything important?**


**What is holding us back?**


**What urgent questions do I have?**

**Next step?**


