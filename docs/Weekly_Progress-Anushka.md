### Week 1 [June 13] :
**Goals**
Getting familiarized with the GitHub Platform and understanding so far what has been done in the nutrition project.

**What went well**
I was able to learn the GitHub platform for code sharing and progress reporting.
I was able to get the overall idea about the project.

**What did not go well**
Few parameters / variables were not clear from the datasets.

**Did I learn anything important**

Github and was able to learn the overall working of the project.

**What is holding us back**
NA

**What urgent questions do I have**
NA

**Next step**
 Getting my doubts cleared about the datasets and the variables from my Phd Lead



### Week 2 [June 20]: 

**Goals**
Standardize the datasets using the onboarding tool

**What went well**
I was able to standardize the datasets by running the onboarding tool code for renaming the required variables and updating the key-map excel sheet with new variables.
Uploaded the log files to github created for each dataset after running the onboarding tool

**What did not go well**
NA

**Did I learn anything important**
A lot of time there was data having the same attribute but was named differently. I learnt to keep an eye for such variables in future and not to consider them as new variables.

**What is holding us back**
NA

**What urgent questions do I have**
NA

**Next step**
Will be discussed on tuesday's meeting.



### Week 3 [June 27] :

**Goal**
upload the log files and the key-map excel file for review.

**What went well**
Uploaded the key-map excel shit on github which will be reviewed and then worked on any changes if needed.

**What did not go well**
NA

**Did I learn anything important**
NA

**What is holding us back**
NA

**What urgent questions do I have**
NA

**Next step**
Start working on finding any correlations between the variables and explore various techniques such as Correlation Analysis, 
Correlation Matrix for determining the target variable, Classification, Time-Series Analysis.


### Week 4 [July 4]: 

**Goal**
Perform EDA on onboarded datasets

**What went well**
Performed EDA and found out correlation between variables of the onboarded datasets of WBB,STRB,OGTT using correlation matrix.

**What did not go well**
NA

**Did I learn anything important**
NA

**What is holding us back**
NA

**What urgent questions do I have**
NA

**Next step**
Start working on finding any correlations between the variables from the combined dataset.


### Week 5 [July 11]:

**Goal**
Run correlated_attribute.py file for finding out most important correlated variables from the combined datasets

**What went well**
Created a text file and stored all the most correlated variables of  WBB,STRB,OGTT datasets. Also included some more correlated variables which were found from the pearson correlation
plot.

**What did not go well**
NA

**Did I learn anything important**
NA

**What is holding us back**
NA

**What urgent questions do I have**
NA

**Next step**
Start working on finding any correlations between the variables from the combined dataset using other methods.

### Week 6 [July 18]:

**Goal**
Run correlated_attribute.py file for finding out most important correlated variables from the combined datasets using other methods.

**What went well**
Used spearman and kendall method to find out the correlation matrix.
Created a text file and stored all the most correlated variables of  WBB,STRB,OGTT datasets.

**What did not go well**
NA

**Did I learn anything important**
NA

**What is holding us back**
NA

**What urgent questions do I have**
NA

**Next step**
Further EDA and finding out more methods to get the target variables.

### Week 6 [July 25]:

**Goal**
Using PCA Method for finding out most important correlated variables from the combined datasets using other methods.

**What went well**
Used PCA method to find out the important features
Created separated jupyter notebooks of  WBB,STRB,OGTT,RRB datasets.

**What did not go well**
NA

**Did I learn anything important**
NA

**What is holding us back**
NA

**What urgent questions do I have**
NA

**Next step**
Further EDA and finding out more methods to get the target variables.

### Week 6 [August 1]:

**Goal**
Compare model accuracy for dataset before preprocessing for the target variable 'Insulin'

**What went well**
Used SVM to predict insulin levels for each dataset from the combined one.

**What did not go well**
Combined dataset consists of insulin value for few datasets as Zero after combining them together which was resulting in 100% accuracy for that particular dataset which was not correct as 
all values for insulin were zero.

**Did I learn anything important**
NA

**What is holding us back**
NA

**What urgent questions do I have**
NA

**Next step**
Try to compare accuracy for dataset before preprocessing with different ML models.



