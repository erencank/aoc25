from copy import deepcopy

from utils.read import read_input


class ForkLiftCertified:
    map: list[list[int]]
    to_pick: int = 3  # Equal or less to pick

    def map_a(self, input: list[str]) -> int:
        data = []
        for _row in input:
            data.append([0 if c == "." else 1 for c in _row])
        self.map = data

        max_x = len(self.map[0]) - 1
        max_y = len(self.map) - 1
        pickable = 0

        for y, row in enumerate(self.map):
            for x, square in enumerate(row):
                # Get top surrounding
                top = self.map[y - 1] if y > 0 else []
                left = max(x - 1, 0)
                right = x + 2
                top_sum = sum(top[left:right])

                middle_sum = row[x - 1] if x - 1 >= 0 else 0  # Middle left
                middle_sum += row[x + 1] if x + 1 <= max_x else 0  # Middle right

                # Get bottom surrounding
                bottom = self.map[y + 1] if y < max_y else []
                bottom_sum = sum(bottom[left:right])

                total_sum = bottom_sum + middle_sum + top_sum
                if square == 1:
                    if total_sum <= self.to_pick:
                        pickable += 1
        return pickable

    def map_b(self, input: list[str]) -> int:
        data = []
        for _row in input:
            data.append([0 if c == "." else 1 for c in _row])
        self.map = data

        max_x = len(self.map[0]) - 1
        max_y = len(self.map) - 1
        pickable = 0
        unable_to_pick = False

        while not unable_to_pick:
            picked_this_round = 0
            new_map = deepcopy(self.map)
            for y, row in enumerate(self.map):
                for x, square in enumerate(row):
                    # Get top surrounding
                    top = self.map[y - 1] if y > 0 else []
                    left = max(x - 1, 0)
                    right = x + 2
                    top_sum = sum(top[left:right])

                    middle_sum = row[x - 1] if x - 1 >= 0 else 0  # Middle left
                    middle_sum += row[x + 1] if x + 1 <= max_x else 0  # Middle right

                    # Get bottom surrounding
                    bottom = self.map[y + 1] if y < max_y else []
                    bottom_sum = sum(bottom[left:right])

                    total_sum = bottom_sum + middle_sum + top_sum
                    if square == 1:
                        if total_sum <= self.to_pick:
                            pickable += 1
                            picked_this_round += 1
                            new_map[y][x] = 0
            unable_to_pick = picked_this_round == 0
            self.map = new_map
        return pickable


def main() -> None:
    file = read_input(4, False)
    lines = file.split("\n")
    print(ForkLiftCertified().map_a(lines))
    print(ForkLiftCertified().map_b(lines))


if __name__ == "__main__":
    main()
