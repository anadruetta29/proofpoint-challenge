from parser import load_csv
from cleaner import clean_records
from deduplicator import deduplicate
import csv


INPUT_FILE = "data/episodes_input.csv"
OUTPUT_FILE = "data/episodes_clean.csv"


def save_clean_csv(records, filepath):
    """
    Save cleaned episodes to CSV.
    """

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow([
            "SeriesName",
            "SeasonNumber",
            "EpisodeNumber",
            "EpisodeTitle",
            "AirDate"
        ])

        for r in records:
            writer.writerow([
                r["series_name"],
                r["season_number"],
                r["episode_number"],
                r["episode_title"],
                r["air_date"]
            ])


def main():

    records = load_csv(INPUT_FILE)
    total_input = len(records)

    cleaned_records, clean_stats = clean_records(records)

    unique_records, duplicates = deduplicate(cleaned_records)

    save_clean_csv(unique_records, OUTPUT_FILE)

    generate_report(
        total_input=total_input,
        total_output=len(unique_records),
        discarded=clean_stats["discarded"],
        corrected=clean_stats["corrected"],
        duplicates=duplicates
    )

    print("Processing completed.")
    print(f"Input records: {total_input}")
    print(f"Output records: {len(unique_records)}")
    print(f"Duplicates detected: {duplicates}")


if __name__ == "__main__":
    main()