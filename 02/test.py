from utils import (
    get_sequences_from_file,
    sum_invalid_ids_part_one,
    sum_invalid_ids_part_two,
)


def test_smaller_input() -> None:

    file_content = get_sequences_from_file("smaller_input.txt")
    sum = sum_invalid_ids_part_one(file_content)
    sum_part_two = sum_invalid_ids_part_two(file_content)

    assert sum == 1227775554
    assert sum_part_two == 4174379265
