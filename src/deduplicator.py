def generate_keys(record):
    series = record["series_name_normalized"]
    season = record["season_number"]
    episode = record["episode_number"]
    title = record["episode_title_normalized"]

    return [
        (series, season, episode),
        (series, 0, episode, title),
        (series, season, 0, title)
    ]


def calculate_score(record):

    score = 0

    if record["air_date"] != "Unknown":
        score += 3

    if record["episode_title"] != "Untitled Episode":
        score += 2

    if record["season_number"] != 0 and record["episode_number"] != 0:
        score += 1

    return score


def deduplicate(records):

    unique_records = []
    key_index = {}

    duplicates = 0

    for record in records:

        keys = generate_keys(record)

        matched_record = None
        matched_index = None

        for key in keys:
            if key in key_index:
                matched_index = key_index[key]
                matched_record = unique_records[matched_index]
                break

        if matched_record is None:

            index = len(unique_records)
            unique_records.append(record)

            for key in keys:
                key_index[key] = index

            continue

        duplicates += 1

        if calculate_score(record) > calculate_score(matched_record):

            unique_records[matched_index] = record

            for key in keys:
                key_index[key] = matched_index

    return unique_records, duplicates