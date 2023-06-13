FDSN-CS
==============================

Illinois Tech SCS lab collaboration with FDSN department on human nutrition studies.

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── onboarded       <- onboarded datasets.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original datasets downloaded from drive.
    │
    ├── docs               <- (TODO) A default Sphinx project; see sphinx-doc.org for details
    │
    │
    ├── notebooks          <- TODO: Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- (TODO) makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── onboarding           <- Scripts to onboard the datasets and log the information about new dataset.
        │   └── data_validation.py
        │
        ├── preprocess       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        ├── models         <- TODO: Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── predict_model.py
        │   └── train_model.py
        │
        └── visualization  <- TODO: Scripts to create exploratory and results oriented visualizations
            └── visualize.py
     

How to run the onboarding tool:
------------

- Clone the git repo with the below command:

        git clone https://github.com/candiceT233/FDSN-CS.git

- Go to the FDSN-CS project folder 

- Download the datasets from the drive and save it to the data/raw folder.

- Run the below python command to trigger the onboarding tool.

        python src/onboarding/data_validation.py --newdata <data_set path>  --keymap Data_Key-Map.xlsx --loglevel 1
         

Example:

    python3 src/onboarding/data_validation.py --newdata data/raw/RRB_datasets/RRB_Demo_for\ cs.xlsx --keymap Data_Key-Map.xlsx

Sample Output:
----

```
INFO:__main__:MMTT_FRTS_.xlsx read successfully
INFO:__main__:Data_Key-Map.xlsx read successfully
Current file name: MMTT_FRTS_.xlsx
Example format: [study_name]-[data_type]-[suffix].csv
Enter the new name for the file: 
INFO:__main__:File name of MMTT_FRTS_.xlsx is not changed
INFO:__main__:Subject renamed to Subject
INFO:__main__:Sequence renamed to Sequence
INFO:__main__:data/onboarded/MMTT_FRTS_.xlsx saved successfully
```

--------

Adding Entry to Data_Key-Map.xlsx:
   When adding a new row to this excel sheet, the `Column Name` and the `Expected_Data_type` is required.

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
