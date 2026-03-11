# proofpoint-challenge
Python solution for the Proofpoint Intern Program technical challenge.

## How to run
python src/main.py

## Explanation 

**parser.py**  
This module reads the CSV file line by line (skipping the header row) and converts each record into a 
Python dictionary for easier processing. It also includes text normalization functions that trim extra 
whitespace and convert values to lowercase in order to ensure consistent comparisons across records. The 
output of this step is a list of dictionaries representing the raw episode records. 

**cleaner.py**  
This module receives the list of dictionaries and applies the validation and correction rules defined in 
the challenge. It converts season and episode numbers to integers, ensures they are valid values, and 
validates that the air date follows the expected format. It also counts discarded records (records without a 
series name) and corrected records. Valid records are stored in a new list which is returned for further 
processing. 

**deduplicator.py**  
This module generates three possible duplicate detection keys for each cleaned record. It checks whether 
any of these keys already exists in the processed dataset to detect duplicated episodes. When duplicates 
are found, the algorithm keeps the record with the highest data quality score (based on the presence of a 
valid air date, episode title, and season/episode numbers). The module returns the list of unique 
records and the number of duplicates detected.

**report.py**  
This module generates the report.md file containing the data quality summary requested in the challenge, 
including statistics about input records, discarded entries, corrected records, and detected duplicates, 
along with an explanation of the deduplication strategy.

**main.py**  
This file orchestrates the entire processing pipeline. It loads the CSV data, cleans the records, 
removes duplicates, writes the final cleaned catalog, and generates the data quality report.

## Additional Exercise – Word Frequency Analysis

A small additional script (`word_frequency.py`) was implemented to analyze word frequency in a text file.

The program:
- Reads a text file
- Normalizes the text (case-insensitive)
- Removes punctuation and special characters
- Counts word occurrences
- Displays the top 10 most frequent words

How to run this script 
    python src/word_frequency.py 



