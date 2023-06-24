# Documenting Weekly progress here

### Week 1 [June 12th] :white_check_mark:
**Goals**
- Have been briefed by Candace on the overview of the project and the long term goals. Have been introduced to the datasets to be explored and key elements of the project.
  
**What went well?**
- N/A
  
**What did not go well?**
- N/A
  
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

### Week 4 [July 3rd] :yellow_circle:
**Goals**

**What went well?**


**What did not go well?**


**Did I learn anything important?**


**What is holding us back?**


**What urgent questions do I have?**

**Next step?**


