# NLP - Biomed titles 1946 - 2012 

replicating figure 2 and 7 from the attached paper

First some prelimary scripts you have to run to get the data in order. These are listed below.

## Convert Paper Titles to CSV
The first step is the convert all of the paper titles into csv files. This is done by running the python file called convert_to_csv.

This script accepts one requires argument (--input) that specifies the path to folder with the raw paper titles. You can specify the output directory by optional argument --output. If you don't specify the output directory, a directory called "paper_titles_processed" will be created and will contain all the CSV files. This is what I did for this analysis - I created a new folder called "paper_titles_processed".

Example code to run the file: python convert_to_csv.py --input paper_titles 

## Join CSV Paper Titles

Joined all of the csv files into one large dataframe that contains all of the paper titles. This was done using the purr package in R. This script is titled "join_titles_R". Outcome: creates a data set called "joined_titles".

## Data Processing

All of the data wrangling is done in R. Everything is documented.

Script: data_processing_v1

Output: Final data set is called "data_process"

## NLP - python

Use [nbviewer](https://nbviewer.jupyter.org/) to render the jupyter notebook if github isn't rendering the notebook (version two of the final notebook isn't rendering). Just copy the url of the python notebook and paste it in nbviewer.

"CogExt_Preprocessing_and_Inspection_V2.ipynb" is the final script. Uses the data labelled [data_process](https://www.dropbox.com/s/csibdzi9dl6nmls/data_process.zip?dl=0) to completely replicate

"Cog_Preprocessing_Inspection_I.ipynb" is an earlier version. The data used for this analysis has some minor data quality issues. Use "data_processed" to completely replicate if you wish.

Everything in the notebook is documented
