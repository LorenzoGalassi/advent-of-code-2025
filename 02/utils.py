def get_sequences_from_file(file_name: str) -> list[str]:

    file = open(file_name, "r")
    content = file.read()
    return content.split(",")


def sum_invalid_ids_part_one(sequences: list[str]) -> int:

    counter = 0

    for sequence in sequences:
        indexes = sequence.split("-")
        start_index = int(indexes[0])
        end_index = int(indexes[1])
        for i in range(start_index, end_index + 1):
            number_as_string = f"{i}"
            quot, rem = divmod(len(number_as_string), 2)
            first_part, second_part = (
                number_as_string[: quot + rem],
                number_as_string[quot + rem :],
            )
            if first_part == second_part:
                counter += i

    return counter


def sum_invalid_ids_part_two(sequences: list[str]) -> int:

    counter = 0

    for sequence in sequences:
        indexes = sequence.split("-")
        start_index = int(indexes[0])
        end_index = int(indexes[1])
        for i in range(start_index, end_index + 1):
            number_as_string = f"{i}"
            str_len = len(number_as_string)
            quot, rem = divmod(len(number_as_string), 2)
            max_index = quot
            for y in range(0, max_index):
                substring = number_as_string[0 : (y + 1)]
                if number_as_string.count(substring) == str_len / len(substring):
                    counter += i
                    break

    return counter
