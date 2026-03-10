# Data Quality Report

## Summary

- Total number of input records: 32
- Total number of output records: 15
- Number of discarded entries: 3
- Number of corrected entries: 14
- Number of duplicates detected: 14

## Deduplication Strategy

Episodes were considered duplicates when they matched one of the following conditions:

1. `(SeriesName_normalized, SeasonNumber, EpisodeNumber)`  
   Used when both season and episode numbers are available.

2. `(SeriesName_normalized, 0, EpisodeNumber, EpisodeTitle_normalized)`  
   Used when the season number is missing but the episode number and title match.

3. `(SeriesName_normalized, SeasonNumber, 0, EpisodeTitle_normalized)`  
   Used when the episode number is missing but the season number and title match.

Normalized values are trimmed, lowercased, and internal spaces are collapsed to ensure consistent comparison.

## Record Selection Priority

When duplicate records were detected, the best record was selected according to the following priority:

1. Episodes with a valid **Air Date** over `"Unknown"`
2. Episodes with a known **Episode Title** over `"Untitled Episode"`
3. Episodes with valid **Season Number** and **Episode Number**
4. If records are still tied, the **first entry encountered in the file** is kept

## Notes

The data cleaning process also handled:

- Invalid or missing season and episode numbers
- Missing episode titles
- Invalid or malformed dates
- Extra whitespace and inconsistent capitalization