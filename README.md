# Biomed titles 1946 - 2012 

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

## Python Notebooks

Replicating figure 2 and 7 from the paper. Use [nbviewer](https://nbviewer.jupyter.org/) to render the jupyter notebook if github isn't rendering the notebook.

### Strict Replication

"CogExt_Preprocessing_and_Inspection_V2.ipynb" is the final script. Uses the data labelled [data_process](https://www.dropbox.com/s/csibdzi9dl6nmls/data_process.zip?dl=0) to completely replicate. Data is also in my directory on the server

"Cog_Preprocessing_Inspection_I.ipynb" is an earlier version. The data used for this analysis has some minor data quality issues. Use [data_processed](https://www.dropbox.com/s/t2p9emvgcqns9f3/data_processed.csv?dl=0) to completely replicate if you wish (also in the server under the same name).

Everything in the notebook is documented

#### Pic

The folder called "pic" has all of the figures in a png format.

### NLP Extension

"CogExt_II__Using_SpacyForPhraseSeparation.ipynb" - Completed further analysis - exploring noun chunks using Spacy (python package)

Turned each title into a group of "noun chunks" and then counts the unique ones in each year. For example "The Study" is likely to be repetitive, and so should be collapsed, it is also likely to occur in each year. Note that I did this before removing the stop-words, because stopwords communicate information about phrase boundaries.


