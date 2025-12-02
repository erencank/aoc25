def read_input(day: int, example: bool = False) -> str:
    prefix = "example_" if example else ""
    with open(f"inputs/{prefix}day{day}.txt") as f:
        lines = f.read()
    return lines
