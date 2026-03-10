def generate_keys(record):
    """
    Generate different keys to find duplicates even if some data is missing.
    """

    series = record["series_name_normalized"]
    season = record["season_number"]
    episode = record["episode_number"]
    title = record["episode_title_normalized"]

    keys = []

    keys.append((series, season, episode))

    keys.append((series, 0, episode, title))

    keys.append((series, season, 0, title))

    return keys


def calculate_score(record):
    """
    Score records to determine which duplicate to keep. Higher score implicates a better record.
    """

    score = 0

    if record["air_date"] != "Unknown":
        score += 3

    if record["episode_title"] != "Untitled Episode":
        score += 2

    if record["season_number"] != 0 and record["episode_number"] != 0:
        score += 1

    return score


def deduplicate(records):
    """
    Find and remove duplicates, keeping only the record with the most info.
    """

    seen = {}
    duplicates = 0

    for record in records:

        keys = generate_keys(record)

        existing_key = None

        for key in keys:
            if key in seen:
                existing_key = key
                break

        if existing_key is None:

            seen[keys[0]] = record
            continue

        duplicates += 1

        existing_record = seen[existing_key]

        if calculate_score(record) > calculate_score(existing_record):
            seen[existing_key] = record

    return list(seen.values()), duplicates