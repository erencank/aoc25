from utils.read import read_input


class ChristmasTree:
    @staticmethod
    def beamsplitter(input: str) -> int:
        split_count = 0
        beam_map: list[list[str]] = []
        rows = input.split("\n")
        for _row in rows:
            beam_map.append([c for c in _row])

        for y, row in enumerate(beam_map):
            for x, char in enumerate(row):
                if char == "S":
                    beam_map[y + 1][x] = "|"

                if char == ".":
                    if y != 0:
                        # Move beam down
                        if beam_map[y - 1][x] == "|":
                            row[x] = "|"

                if char == "^":
                    # Update left
                    if beam_map[y - 1][x] == "|":
                        splitted = False
                        if row[x - 1] == "|":
                            pass
                        else:
                            row[x - 1] = "|"
                            splitted = True

                        # Update right
                        if row[x + 1] == "|":
                            pass
                        else:
                            row[x + 1] = "|"
                            splitted = True
                        if splitted:
                            split_count += 1

        return split_count

    @staticmethod
    def avengers_endgame(input: str) -> int:
        beam_map: list[list[str]] = []
        rows = input.split("\n")
        for _row in rows:
            beam_map.append([c for c in _row])

        timeline_map: list[list[int]] = [
            [0 for _ in range(len(_row))] for _ in range(len(beam_map))
        ]

        for y, row in enumerate(beam_map):
            for x, char in enumerate(row):
                if char == "S":
                    timeline_map[y][x] = 1

                if char == ".":
                    if y != 0:
                        timeline_map[y][x] += timeline_map[y - 1][x]

                if char == "^":
                    incoming_count = timeline_map[y - 1][x]
                    timeline_map[y][x - 1] += incoming_count
                    timeline_map[y][x + 1] += incoming_count

        return sum(timeline_map[-1])


def main() -> None:
    file = read_input(7, False)
    print(ChristmasTree.beamsplitter(file))
    print(ChristmasTree.avengers_endgame(file))


if __name__ == "__main__":
    main()
