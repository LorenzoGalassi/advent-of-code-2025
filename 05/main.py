from utils import get_ingredients, process_ingredients
from test import test_smaller_input
import time


def main() -> None:

    file_content = get_ingredients("input.txt")
    counter, total_counter = process_ingredients(file_content)

    print(f"Fresh ingredients counter: {counter}")
    print(f"Total fresh ingredients counter: {total_counter}")


if __name__ == "__main__":
    start = time.perf_counter()
    test_smaller_input()
    print("Test passed!")
    main()
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Execution time: {elapsed_ms:.3f} ms")
