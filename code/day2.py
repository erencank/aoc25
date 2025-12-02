from dataclasses import dataclass

from utils.read import read_input

len_map: dict[int, list[int]] = {
    1: [],
    2: [1],
    3: [1],
    4: [1, 2],
    5: [1],
    6: [1, 2, 3],
    7: [1],
    8: [1, 2, 4],
    9: [1, 3],
    10: [1, 2, 5],
}


@dataclass
class IDRange:
    first: int
    last: int

    @classmethod
    def from_str(cls, input: str) -> "IDRange":
        split = input.split("-")
        return cls(first=int(split[0]), last=int(split[1]))

    def find_invalids_a(self) -> list[int]:
        invalid_ids = []
        for i in range(self.first, self.last + 1):
            s_id = str(i)
            len_str = len(s_id)
            if len_str % 2 == 1:
                continue
            half_len = len_str // 2
            if s_id[:half_len] == s_id[half_len:]:
                invalid_ids.append(i)

        return invalid_ids

    def find_invalids_b(self) -> list[int]:
        invalid_ids = []

        for i in range(self.first, self.last + 1):
            s_id = str(i)
            len_str = len(s_id)

            for sub in len_map[len_str]:
                unique_set = {s_id[n : n + sub] for n in range(0, len_str, sub)}
                if len(unique_set) == 1:
                    if i not in invalid_ids:
                        invalid_ids.append(i)
        return invalid_ids


def process_a(lines: list[str]):
    total_invalids_a = 0
    total_invalids_b = 0
    for line in lines:
        id_range = IDRange.from_str(line)
        total_invalids_a += sum(id_range.find_invalids_a())
        total_invalids_b += sum(id_range.find_invalids_b())

    print(total_invalids_a)
    print(total_invalids_b)


def main() -> None:
    file = read_input(2, False)
    rows = file.replace("\n", "").split(",")
    process_a(rows)


if __name__ == "__main__":
    main()
