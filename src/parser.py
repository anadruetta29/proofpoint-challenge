import csv

def normalize_text(value: str) -> str:
    """
    Trim whitespace and remove extra spaces between words.
    """
    if value is None:
        return ""

    value = value.strip()
    value = " ".join(value.split())

    return value


def normalize_series_name(value: str) -> str:
    """
    Clean series name and lowercase it for comparison purposes.
    """
    value = normalize_text(value)
    return value.lower()


def normalize_title(value: str) -> str:
    """
    Normalize episode title for comparison.
    """
    value = normalize_text(value)
    return value.lower()


def load_csv(filepath: str):
    """
    Read episodes from the CSV and return them as a list of dicts.
    """

    records = []

    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:

            row = row + [""] * (5 - len(row))

            series_name = normalize_text(row[0])
            season_number = normalize_text(row[1])
            episode_number = normalize_text(row[2])
            episode_title = normalize_text(row[3])
            air_date = normalize_text(row[4])

            record = {
                "series_name": series_name,
                "series_name_normalized": normalize_series_name(series_name),
                "season_number": season_number,
                "episode_number": episode_number,
                "episode_title": episode_title,
                "episode_title_normalized": normalize_title(episode_title),
                "air_date": air_date,
            }

            records.append(record)

    return records