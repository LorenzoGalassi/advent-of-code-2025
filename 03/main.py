from utils import get_batteries_from_file, get_max_voltage
import time


def main() -> None:

    file_content = get_batteries_from_file("input.txt")

    total_voltage_part_1 = 0
    total_voltage_part_2 = 0

    for battery in file_content:
        max_voltage_part_1 = get_max_voltage(2, battery)
        total_voltage_part_1 += max_voltage_part_1
        max_voltage_part_2 = get_max_voltage(12, battery)
        total_voltage_part_2 += max_voltage_part_2

    print(
        f"Max voltage part 1: {total_voltage_part_1}\nMax voltage part 2: {total_voltage_part_2}"
    )
    return total_voltage_part_1, total_voltage_part_2


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Execution time: {elapsed_ms:.3f} ms")
