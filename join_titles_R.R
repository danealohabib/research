library(purr)
library(tidyverse)

# path to data. Note: I am working with a project in R, so my working directory is already set to the project folder. 
# if you want to replicate this code, copy and paste the full path to the folder called "paper_titles_processed"

# path to the data

data_path <- "paper_titles_processed"  

# files and patten (.csv)

files <- dir(data_path, pattern = "*.csv") 

# joining titles and creating a new data frame called 
joined_titles <- files %>% 
  map_dfr(~ read_csv(file.path(data_path, .)))

# view the new dataframe we just created 

joined_titles

write_csv(joined_titles, "joined_titles.csv")
