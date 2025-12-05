from utils import (
    get_ingredients,
    process_ingredients,
)


def test_smaller_input() -> None:

    file_content = get_ingredients("smaller_input.txt")
    counter, total_counter = process_ingredients(file_content)
    print(total_counter)
    assert counter == 3
    assert total_counter == 14
