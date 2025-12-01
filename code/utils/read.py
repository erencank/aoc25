def read_input(day: int, example: bool = False) -> list[str]:
    prefix = "example_" if example else ""
    with open(f"inputs/{prefix}day{day}.txt") as f:
        lines = f.read().split("\n")
    return lines
