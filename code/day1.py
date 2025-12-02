from dataclasses import dataclass
from typing import Any, Self

from utils.read import read_input


@dataclass
class Dial:
    start: int
    zeroed = 0

    def __add__(self, other: int) -> Self:
        self.zeroed += (self.start + other) // 100
        self.start = (self.start + other) % 100
        return self

    def __sub__(self, other: int) -> Self:
        to_zero = self.start if self.start > 0 else 100

        if other >= to_zero:
            remaining_steps = other - to_zero
            self.zeroed += 1 + (remaining_steps // 100)
        self.start = (self.start - other) % 100
        return self

    def __eq__(self, value: Any) -> bool:
        return self.start == value


def process_a_and_b(file: list[str]) -> None:
    passwd = 0
    dial = Dial(50)
    for line in file:
        d = line[0]
        c = int(line[1:])
        if d == "R":
            dial += c
        else:
            dial -= c
        if dial == 0:
            passwd += 1

    print(passwd)
    print(dial.zeroed)


def main() -> None:
    file = read_input(1, False)
    process_a_and_b(file.split("\n"))


if __name__ == "__main__":
    main()
