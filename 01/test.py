from utils import get_sequences_from_file, clean_zero_hits, total_zero_hits


def test_smaller_input() -> None:

    starting_point = 50
    file_content = get_sequences_from_file("smaller_input.txt")
    clean_zeros = clean_zero_hits(file_content, starting_point)
    total_zeros = total_zero_hits(file_content, starting_point)

    assert clean_zeros == 3
    assert total_zeros == 6
