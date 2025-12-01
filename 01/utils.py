def get_sequences_from_file(file_name: str) -> list[str]:

    file = open(file_name, "r")
    content = file.read()
    return content.split("\n")


def clean_zero_hits(sequences: list[str], starting_point: int) -> int:
    index = starting_point
    hit_zero = 0
    limit = 100
    for sequence in sequences:
        value = int(sequence[1:]) % limit
        if sequence[0] == "L":
            index -= value
            if index == 0 or index == limit:
                hit_zero += 1
            elif index < 0:
                index = limit + index
        elif sequence[0] == "R":
            index += value
            if index == 0 or index == limit:
                hit_zero += 1
            elif index >= limit:
                index = index - limit
    return hit_zero


def total_zero_hits(sequences: list[str], starting_point: int) -> int:
    index = starting_point
    hit_zero = 0
    limit = 100
    for sequence in sequences:
        quot, rem = divmod(int(sequence[1:]), limit)
        hit_zero += quot
        if sequence[0] == "L":
            initial = index
            index -= rem
            if index == 0 or index == limit:
                hit_zero += 1
            elif index < 0:
                if initial != 0:
                    hit_zero += 1
                index = limit + index
        elif sequence[0] == "R":
            initial = index
            index += rem
            if index == 0 or index == limit:
                hit_zero += 1
            elif index >= limit:
                if index > limit:
                    if initial != limit:
                        hit_zero += 1
                index = index - limit
    return hit_zero
