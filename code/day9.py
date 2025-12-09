import itertools
from typing import NamedTuple, Self

from utils.read import read_input


class Coordinate(NamedTuple):
    x: int
    y: int

    @classmethod
    def from_line(cls, line) -> Self:
        x, y = line.split(",")
        return cls(x=int(x), y=int(y))

    def compute_area(self, other: "Coordinate") -> int:
        width = abs(self.x - other.x) + 1
        height = abs(self.y - other.y) + 1
        return width * height


class FancyTiles:
    @staticmethod
    def who_wants_red_tiles(input: str) -> int:
        coordinates: list[Coordinate] = [Coordinate.from_line(line) for line in input.split("\n")]
        combinations = itertools.combinations(coordinates, 2)

        areas: list[tuple[int, Coordinate, Coordinate]] = []
        for combination in combinations:
            left = combination[0]
            right = combination[1]
            areas.append((left.compute_area(right), left, right))

        areas.sort(key=lambda x: x[0])
        biggest = areas[-1]
        return biggest[0]

    @staticmethod
    def the_big_walls_of_christmas(input: str) -> int:
        coordinates: list[Coordinate] = [Coordinate.from_line(line) for line in input.split("\n")]

        walls: list[tuple[Coordinate, Coordinate]] = []
        for c1, c2 in zip(coordinates, coordinates[1:] + coordinates[:1]):
            walls.append((c1, c2))

        max_area = 0

        combinations = itertools.combinations(coordinates, 2)
        for c1, c2 in combinations:
            current_area = c1.compute_area(c2)
            if current_area <= max_area:
                continue

            if FancyTiles._is_on_my_lawn(c1, c2, walls):
                max_area = current_area

        return max_area

    @staticmethod
    def _is_on_my_lawn(
        c1: Coordinate, c2: Coordinate, walls: list[tuple[Coordinate, Coordinate]]
    ) -> bool:
        # all rectangle coordinates
        min_x, max_x = min(c1.x, c2.x), max(c1.x, c2.x)
        min_y, max_y = min(c1.y, c2.y), max(c1.y, c2.y)

        # middle point of rectangle
        mid_x = (min_x + max_x) / 2
        mid_y = (min_y + max_y) / 2

        crossings = 0
        for w1, w2 in walls:
            # Check from left to right.
            if w1.x == w2.x and w1.x > mid_x:
                # Is the point in the walls height?
                if min(w1.y, w2.y) <= mid_y < max(w1.y, w2.y):
                    crossings += 1
        if crossings % 2 == 0:
            return False

        for w1, w2 in walls:
            # Wall coordinates
            wall_min_x, wall_max_x = min(w1.x, w2.x), max(w1.x, w2.x)
            wall_min_y, wall_max_y = min(w1.y, w2.y), max(w1.y, w2.y)

            # Check for vertical or horizontal wall overlap
            if w1.x == w2.x:  # Vertical
                if (min_x < w1.x < max_x) and not (wall_max_y <= min_y or wall_min_y >= max_y):
                    return False

            if w1.y == w2.y:  # Horizontal
                if (min_y < w1.y < max_y) and not (wall_max_x <= min_x or wall_min_x >= max_x):
                    return False
        return True


def main() -> None:
    file = read_input(9, False)
    print(FancyTiles.who_wants_red_tiles(file))
    print(FancyTiles.the_big_walls_of_christmas(file))


if __name__ == "__main__":
    main()
