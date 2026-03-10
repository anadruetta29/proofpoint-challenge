def generate_report( total_input: int, total_output: int, discarded: int, corrected: int, duplicates: int,
                     filepath: str = "report.md"):
    """
    Generate a data quality report.
    """

    report_content = f"""
# Data Quality Report

## Summary
- Total number of input records: {total_input}
- Total number of output records: {total_output}
- Number of discarded entries: {discarded}
- Number of corrected entries: {corrected}
- Number of duplicates detected: {duplicates}
- Explanation of the deduplication strategy: episodes were considered duplicates when they matched one 
of the following conditions:
1. (SeriesName_normalized, SeasonNumber, EpisodeNumber): used when both season and episode numbers are available.
2. (SeriesName_normalized, 0, EpisodeNumber, EpisodeTitle_normalized): used when the season number is missing 
but episode number and title match.
3. (SeriesName_normalized, SeasonNumber, 0, EpisodeTitle_normalized): used when the episode number is missing 
but season and title match.
Normalized values are trimmed, lowercased, and spaces are collapsed to ensure consistent comparison.
- Record Selection Priority - when duplicates were detected, the best record was selected according to 
the following priority:
1. Episodes with a valid Air Date over `"Unknown"`
2. Episodes with a known Episode Title over `"Untitled Episode"`
3. Episodes with valid Season and Episode numbers
4. If records were still tied, the first entry encountered in the file was kept.

## Notes
The data cleaning process also handled:
- Invalid or missing season and episode numbers
- Missing episode titles
- Invalid or malformed dates
- Extra whitespace and inconsistent capitalization

"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report_content.strip())