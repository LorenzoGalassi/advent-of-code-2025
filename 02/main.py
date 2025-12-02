from utils import (
    get_sequences_from_file,
    sum_invalid_ids_part_one,
    sum_invalid_ids_part_two,
)
import time


def main() -> None:

    file_content = get_sequences_from_file("input.txt")
    sum = sum_invalid_ids_part_one(file_content)
    sum_part_two = sum_invalid_ids_part_two(file_content)
    print(f"Sum of invalid ids (part one): {sum}")
    print(f"Sum of invalid ids (part two): {sum_part_two}")
    return sum


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Execution time: {elapsed_ms:.3f} ms")
