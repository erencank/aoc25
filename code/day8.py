import itertools
import math
import uuid
from collections import Counter
from dataclasses import dataclass
from typing import Self

from utils.read import read_input


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int
    z: int

    @classmethod
    def from_line(cls, line: str) -> Self:
        x, y, z = line.split(",")
        return cls(x=int(x), y=int(y), z=int(z))

    def to_tuple(self) -> tuple[int, int, int]:
        return (self.x, self.y, self.z)

    def distance_to(self, other: "Coordinate") -> float:
        return math.dist(self.to_tuple(), other.to_tuple())


class MegaCircuit:
    @staticmethod
    def make_big_boxes(input: str, connections: int) -> tuple[int, int]:
        last_junction_box_prod = 0
        coordinates: list[Coordinate] = [Coordinate.from_line(row) for row in input.split("\n")]

        combinations: itertools.combinations[tuple[Coordinate, Coordinate]] = (
            itertools.combinations(coordinates, 2)
        )
        distances: list[tuple[float, Coordinate, Coordinate]] = []
        for combination in combinations:
            left = combination[0]
            right = combination[1]
            distances.append((left.distance_to(right), left, right))
            pass
        distances.sort(key=lambda x: x[0])
        circuits: dict[Coordinate, uuid.UUID] = {}
        for i, (_, left, right) in enumerate(distances):
            circuit_count = len(set(circuits.values()))
            if left not in circuits and right not in circuits:
                id = uuid.uuid4()
                circuits[left] = id
                circuits[right] = id
            elif left in circuits and right not in circuits:
                id = circuits[left]
                circuits[right] = id
            elif right in circuits and left not in circuits:
                id = circuits[right]
                circuits[left] = id
            else:
                left_id = circuits[left]
                right_id = circuits[right]
                if left_id == right_id:
                    pass
                else:
                    all_boxes_in_right = [box for box, id in circuits.items() if id == right_id]
                    for box in all_boxes_in_right:
                        circuits[box] = left_id

            if i == connections - 1:
                most_common = Counter(circuits.values()).most_common(3)

            if circuit_count == 1 and len(circuits.keys()) == len(coordinates):
                last_junction_box_prod = left.x * right.x
                break

        return math.prod([mc[1] for mc in most_common]), last_junction_box_prod


def main() -> None:
    print("Test")
    file = read_input(8, True)
    print(MegaCircuit.make_big_boxes(file, 10))

    print("Actual")
    file = read_input(8, False)
    print(MegaCircuit.make_big_boxes(file, 1000))


if __name__ == "__main__":
    main()
