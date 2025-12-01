from utils import get_sequences_from_file, clean_zero_hits, total_zero_hits
import time


def main() -> None:

    starting_point = 50
    file_content = get_sequences_from_file("input.txt")
    clean_zeros = clean_zero_hits(file_content, starting_point)
    total_zeros = total_zero_hits(file_content, starting_point)
    print(f"Clean zero hits: {clean_zeros}")
    print(f"Total zero hits: {total_zeros}")
    return clean_zeros, total_zeros


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Execution time: {elapsed_ms:.3f} ms")
