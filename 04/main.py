from utils import (
    get_rolls_from_file,
    get_accessible_rolls,
    get_accessible_rolls_part_two,
)
from test import test_smaller_input
import time


def main() -> None:

    file_content = get_rolls_from_file("input.txt")
    accessible_rolls = get_accessible_rolls(file_content)
    print(f"Accessible rolls (PART ONE): {accessible_rolls}")
    accessible_rolls_recursive = get_accessible_rolls_part_two(file_content)
    print(f"Accessible rolls (PART TWO): {accessible_rolls_recursive}")
    return accessible_rolls, accessible_rolls_recursive


if __name__ == "__main__":
    start = time.perf_counter()
    test_smaller_input()
    print("Test passed!")
    main()
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Execution time: {elapsed_ms:.3f} ms")
