from utils.read import read_input


class SamsungSmartFridge:
    @staticmethod
    def use_ai(ranges_str: list[str], ingredients_str: list[str]) -> int:
        total_fresh = 0
        id_ranges: list[tuple[int, int]] = []
        for i, r in enumerate(ranges_str):
            left, right = r.split("-")
            id_ranges.append((int(left), int(right)))

        int_ingredients = [int(ing) for ing in ingredients_str]
        for ingredient in int_ingredients:
            for i, range in enumerate(id_ranges):
                if range[0] <= ingredient <= range[1]:
                    total_fresh += 1
                    break

        return total_fresh

    @staticmethod
    def save_world_hunger(ranges_str: list[str]) -> int:
        id_ranges: list[tuple[int, int]] = []
        for r in ranges_str:
            left, right = r.split("-")
            id_ranges.append((int(left), int(right)))

        id_ranges.sort(key=lambda x: x[0])

        merged_ranges: list[tuple[int, int]] = []
        for curr_start, curr_end in id_ranges:
            if not merged_ranges:
                merged_ranges.append((curr_start, curr_end))

            last_start, last_end = merged_ranges[-1]

            if curr_start <= last_end:
                new_end = max(last_end, curr_end)
                merged_ranges[-1] = (last_start, new_end)
            else:
                merged_ranges.append((curr_start, curr_end))
        return sum((ranges[1] - ranges[0] + 1) for ranges in merged_ranges)


def main() -> None:
    file = read_input(5, False)
    _ranges, _ingredients = file.split("\n\n")
    ranges = _ranges.split("\n")
    ingredients = _ingredients.split("\n")
    print(SamsungSmartFridge.use_ai(ranges, ingredients))
    print(SamsungSmartFridge.save_world_hunger(ranges))


if __name__ == "__main__":
    main()
