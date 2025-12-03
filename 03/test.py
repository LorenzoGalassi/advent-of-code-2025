from utils import get_batteries_from_file, get_max_voltage


def test_smaller_input() -> None:

    file_content = get_batteries_from_file("smaller_input.txt")

    total_voltage_part_1 = 0
    total_voltage_part_2 = 0

    for battery in file_content:
        max_voltage_part_1 = get_max_voltage(2, battery)
        total_voltage_part_1 += max_voltage_part_1
        max_voltage_part_2 = get_max_voltage(12, battery)
        total_voltage_part_2 += max_voltage_part_2

    assert total_voltage_part_1 == 357
    assert total_voltage_part_2 == 3121910778619
