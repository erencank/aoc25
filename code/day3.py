from utils.read import read_input


class Battery:
    @staticmethod
    def joltage(bank_str: str, amount: int) -> int:
        outputs: list[int] = [0] * amount
        banks = [int(char) for char in bank_str]

        search_start = 0
        for i in range(amount):
            remaining_needed = amount - 1 - i
            search_end = len(banks) - remaining_needed
            shuffleable = banks[search_start:search_end]
            best_digit = -1
            best_index_relative = -1
            for j, bank in enumerate(shuffleable):
                if bank > best_digit:
                    best_digit = bank
                    best_index_relative = j

                if bank == 9:
                    break
            outputs[i] = best_digit
            search_start += best_index_relative + 1

        result = int("".join([str(c) for c in outputs]))
        return result


def process_a_and_b(lines: list[str]) -> None:
    total_a = 0
    total_b = 0
    for line in lines:
        total_a += Battery.joltage(line, 2)
        total_b += Battery.joltage(line, 12)
    print(total_a)
    print(total_b)


def main() -> None:
    file = read_input(3, False)
    lines = file.split("\n")
    process_a_and_b(lines)


if __name__ == "__main__":
    main()
