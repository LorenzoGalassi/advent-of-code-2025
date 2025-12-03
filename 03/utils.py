def get_batteries_from_file(file_name: str) -> list[str]:

    file = open(file_name, "r")
    content = file.read()
    return content.split("\n")


def get_max_voltage(number_of_iterations: int, battery_sequence: str) -> int:

    highest = ["0"] * number_of_iterations
    last_highest_index = 0

    for y in range(number_of_iterations):
        for i in range(last_highest_index, len(battery_sequence)):
            if i < len(battery_sequence) - (number_of_iterations - (y + 1)):
                if int(battery_sequence[i]) > int(highest[y]):
                    highest[y] = battery_sequence[i]
                    last_highest_index = i + 1

    return int("".join(highest))
