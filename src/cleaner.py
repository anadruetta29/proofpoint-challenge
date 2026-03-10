from datetime import datetime

def parse_number(value: str) -> int:
    """
    Turn season/episode into an int. Defaults to 0 if it's negative or not a number.
    """
    try:
        number = int(value)
        if number < 0:
            return 0
        return number
    except:
        return 0


def parse_air_date(value: str) -> str:
    """
    Check for YYYY-MM-DD format. Return 'Unknown' if the date is wrong.
    """
    if not value:
        return "Unknown"

    try:
        datetime.strptime(value, "%Y-%m-%d")
        return value
    except:
        return "Unknown"


def clean_records(records):
    """
    Apply validation and correction rules to all records.
    Returns cleaned records and statistics.
    """

    cleaned = []

    stats = {
        "discarded": 0,
        "corrected": 0
    }

    for record in records:

        series_name = record["series_name"]

        if not series_name:
            stats["discarded"] += 1
            continue

        season_number = parse_number(record["season_number"])
        episode_number = parse_number(record["episode_number"])

        episode_title = record["episode_title"]
        air_date = parse_air_date(record["air_date"])

        corrected = False

        if not episode_title:
            episode_title = "Untitled Episode"
            corrected = True

        if air_date == "Unknown" and record["air_date"] != "Unknown":
            corrected = True

        if season_number == 0 and record["season_number"] not in ("0", "", None):
            corrected = True

        if str(episode_number) != record["episode_number"]:
            corrected = True

        if (
            episode_number == 0
            and episode_title == "Untitled Episode"
            and air_date == "Unknown"
        ):
            stats["discarded"] += 1
            continue

        cleaned_record = {
            "series_name": series_name,
            "series_name_normalized": record["series_name_normalized"],
            "season_number": season_number,
            "episode_number": episode_number,
            "episode_title": episode_title,
            "episode_title_normalized": episode_title.lower(),
            "air_date": air_date,
        }

        if corrected:
            stats["corrected"] += 1

        cleaned.append(cleaned_record)

    return cleaned, stats