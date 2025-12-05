from utils import (
    get_rolls_from_file,
    get_accessible_rolls,
    get_accessible_rolls_part_two,
)


def test_smaller_input() -> None:

    file_content = get_rolls_from_file("smaller_input.txt")
    accessible_rolls = get_accessible_rolls(file_content)
    accessible_rolls_recursive = get_accessible_rolls_part_two(file_content)

    assert accessible_rolls == 13
    assert accessible_rolls_recursive == 43
