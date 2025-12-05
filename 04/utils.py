def get_rolls_from_file(file_name: str) -> list[str]:

    file = open(file_name, "r")
    content = file.read()
    return content.split("\n")


def get_accessible_rolls(rolls: list[str]) -> int:

    counter = 0

    for i in range(len(rolls)):
        for y in range(len(rolls[i])):
            occurrencies = 0
            char = rolls[i][y]

            if char == "@" and i != 0 and rolls[i - 1][y] == "@":
                occurrencies += 1
            if char == "@" and i != 0 and y != 0 and rolls[i - 1][y - 1] == "@":
                occurrencies += 1
            if (
                char == "@"
                and i != 0
                and y != (len(rolls[i]) - 1)
                and rolls[i - 1][y + 1] == "@"
            ):
                occurrencies += 1
            if char == "@" and y != 0 and rolls[i][y - 1] == "@":
                occurrencies += 1
            if char == "@" and y != (len(rolls[i]) - 1) and rolls[i][y + 1] == "@":
                occurrencies += 1
            if char == "@" and i != (len(rolls) - 1) and rolls[i + 1][y] == "@":
                occurrencies += 1
            if (
                char == "@"
                and i != (len(rolls) - 1)
                and y != 0
                and rolls[i + 1][y - 1] == "@"
            ):
                occurrencies += 1
            if (
                char == "@"
                and i != (len(rolls) - 1)
                and y != (len(rolls[i]) - 1)
                and rolls[i + 1][y + 1] == "@"
            ):
                occurrencies += 1

            if char == "@" and occurrencies < 4:
                counter += 1

    return counter


def get_accessible_rolls_part_two(
    prev_rolls: list[str],
    prev_coordinates: list[tuple[int, int]] = [],
    prev_counter: int = 0,
    total_counter: int = 0,
    iteration: int = 0,
) -> tuple[int, list[tuple[int, int]]]:

    coordinates = prev_coordinates.copy()
    counter = 0
    rolls = prev_rolls.copy()

    if prev_counter == 0 and iteration > 0:
        return total_counter

    if len(prev_coordinates) > 0:
        for coord in prev_coordinates:
            x, y = coord
            row = rolls[x]
            rolls[x] = row[:y] + "." + row[y + 1 :]

    for i in range(len(rolls)):
        for y in range(len(rolls[i])):
            occurrencies = 0
            char = rolls[i][y]

            if char == "@" and i != 0 and rolls[i - 1][y] == "@":
                occurrencies += 1
            if char == "@" and i != 0 and y != 0 and rolls[i - 1][y - 1] == "@":
                occurrencies += 1
            if (
                char == "@"
                and i != 0
                and y != (len(rolls[i]) - 1)
                and rolls[i - 1][y + 1] == "@"
            ):
                occurrencies += 1
            if char == "@" and y != 0 and rolls[i][y - 1] == "@":
                occurrencies += 1
            if char == "@" and y != (len(rolls[i]) - 1) and rolls[i][y + 1] == "@":
                occurrencies += 1
            if char == "@" and i != (len(rolls) - 1) and rolls[i + 1][y] == "@":
                occurrencies += 1
            if (
                char == "@"
                and i != (len(rolls) - 1)
                and y != 0
                and rolls[i + 1][y - 1] == "@"
            ):
                occurrencies += 1
            if (
                char == "@"
                and i != (len(rolls) - 1)
                and y != (len(rolls[i]) - 1)
                and rolls[i + 1][y + 1] == "@"
            ):
                occurrencies += 1

            if char == "@" and occurrencies < 4:
                counter += 1
                coordinates.append([i, y])

    new_iteration = iteration + 1
    return get_accessible_rolls_part_two(
        rolls, coordinates, counter, total_counter + counter, new_iteration
    )
