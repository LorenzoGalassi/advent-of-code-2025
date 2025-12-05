def get_ingredients(file_name: str) -> list[str]:

    file = open(file_name, "r")
    content = file.read()
    return content.split("\n")


def determine_freshness(ingredients: list[str], ranges: list[str]) -> int:

    counter = 0

    for ingredient in ingredients:
        for string in ranges:
            start, end = map(int, string.split("-"))
            if int(ingredient) >= start and int(ingredient) <= end:
                counter += 1
                break

    return counter


def process_ingredients(ranges: list[str]) -> tuple[int, int]:

    freshness_db = []
    freshness_to_be_determined = []
    delimiter_found = False

    for range in ranges:
        if range != "" and delimiter_found == False:
            freshness_db.append(range)
        elif range != "" and delimiter_found == True:
            freshness_to_be_determined.append(range)
        else:
            delimiter_found = True

    fresh_ingredients_counter = determine_freshness(
        freshness_to_be_determined, freshness_db
    )

    total_fresh_ingredients_counter = get_all_fresh_ingredients_counter(freshness_db)

    return fresh_ingredients_counter, total_fresh_ingredients_counter


def get_all_fresh_ingredients_counter(ranges: list[str]) -> int:

    sorted_ranges = []

    for r in ranges:
        start, end = map(int, r.split("-"))
        sorted_ranges.append((start, end))

    sorted_ranges.sort()

    merged = [sorted_ranges[0]]

    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    counter = 0

    for start, end in merged:
        counter += end - start + 1

    return counter
