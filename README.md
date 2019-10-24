# Biomed Titles 1946 - 2012 

Use [nbviewer](https://nbviewer.jupyter.org/) to render the jupyter notebook if github isn't rendering.

## Replication 

Jupyter Notebooks for the replication is called [CogExt_I.ipynb](https://github.com/danealohabib/research-MP/blob/master/CogExt_I.ipynb). 

Uses the data labelled [data_process](https://www.dropbox.com/s/csibdzi9dl6nmls/data_process.zip?dl=0) to completely replicate (the name in the code is different, but it is the same data). Data is also in my directory on the server. 

The folder called `pic` has all of the figures in a png format.

### Earlier Version of Replication

[CogExt.ipynb](https://github.com/danealohabib/research-MP/blob/master/CogExt.ipynb) is the earlier version. The data used for this analysis has some minor data quality issues. Use [data_processed](https://www.dropbox.com/s/t2p9emvgcqns9f3/data_processed.csv?dl=0) to completely replicate if you wish (also in the server under the same name). 

## Extensions

### Extension 1: biomed word2vec - Spacey + Clustering

Jupyter: [CogExt_III_clustering.ipynb](https://github.com/danealohabib/research-MP/blob/master/CogExt_III_clustering.ipynb) 

Uses spacy to segment the titles, then shoves each noun phrase into the biomed word2vec vector space. Umap dimensionality reduction is then used to get a 2D visualization. Note that after the GIF, there is a section that explains the noun-phrase methodology as well as  contains the code for the alternative chart showing the rise of unique noun-phrases over time. 

**Website to download biomedical NLP tools ([http://bio.nlplab.org/](http://bio.nlplab.org/))**

### Extension 2:  exploring noun chunks using Spacy (python package)

[CogExt_Spacy.ipynb](https://github.com/danealohabib/research-MP/blob/master/CogExt_Spacy.ipynb) 

Turned each title into a group of "noun chunks" and then counts the unique ones in each year. For example "The Study" is likely to be repetitive, and so should be collapsed, it is also likely to occur in each year. Note that I did this before removing the stop-words, because stopwords communicate information about phrase boundaries. I used a quota of 10k titles for the above graph, per year.

## Data Processing

This section will show you the steps I took to process and create the data I used above.

### Convert Paper Titles to CSV
The first step is the convert all of the paper titles into csv files. This is done by running the python file called `convert_to_csv`.

This script accepts one requires argument (--input) that specifies the path to folder with the raw paper titles. You can specify the output directory by optional argument --output. If you don't specify the output directory, a directory called `paper_titles_processed` will be created and will contain all the CSV files. This is what I did for this analysis - I created a new folder called `paper_titles_processed`.

Example code to run the file: python convert_to_csv.py --input paper_titles 

### Join CSV Paper Titles

Joined all of the csv files into one large dataframe that contains all of the paper titles. This was done using the purr package in R. This script is titled [join_titles_R](https://github.com/danealohabib/research-MP/blob/master/join_titles_R.R). 

Outcome: creates a data set called `joined_titles`.

### Data Wrangling

All of the data wrangling is done in R. Everything is documented and submitted as a PDF.

[Script](https://github.com/danealohabib/research-MP/blob/master/data_processing_v1.Rmd)

[PDF file](https://github.com/danealohabib/research-MP/blob/master/data_processing_v1.pdf)

Output: Final data set is called `data_process`

## Python Notebooks

Use [nbviewer](https://nbviewer.jupyter.org/) to render the jupyter notebook if github isn't rendering the notebook.




