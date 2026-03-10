# proofpoint-challenge
Python solution for the Proofpoint Intern Program technical challenge.

## How to run
python src/main.py

### CSV Data Parser
This script processes and standardizes episode data from CSV files. 
It ensures consistency across series names and titles, making it easier to compare or search through the records.

- Data Structure
Each record returned by the parser includes:
    series_name: The original name (trimmed).
    series_name_normalized: Lowercase version for matching.
    season_number / episode_number: Episode identifiers.
    episode_title / episode_title_normalized: Original and standardized titles.
    air_date: Release date string.