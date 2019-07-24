# NLP - Biomed titles 1946 - 2012 

replicating figure 2 and 7 from the attached paper

First some prelimary scripts you have to run to get the data in order. These are listed below.

## Convert to csv
The first step is the convert all of the paper titles into csv files. This is done by running the python file called convert_to_csv.

This script accepts one requires argument (--input) that specifies the path to folder with the raw paper titles. You can specify the output directory by optional argument --output. If you don't specify the output directory, a directory called "paper_titles_processed" will be created and will contain all the CSV files. This is what I did for this analysis - I created a new folder called "paper_titles_processed".
join all files using 

Example code to run the file: python convert_to_csv.py --input paper_titles 

## Joining Titles

Joined all of the csv files into one large dataframe that contains all of the paper titles. This was done using the R script called "join_titles_R". Outcome: creates a data set called "joined_titles".

# Processing

The rest of the data processing is done in R

# NLP - python

the script called "CogExt_Preprocessing_and_Inspection_V2.ipynb" is the final script.

the script called "Cog_Preprocessing_Inspection_I.ipynb" is an earlier 
