from utils.read import read_input


class AncientMath:
    @staticmethod
    def elementary_class(input: str) -> int:
        rows = input.split("\n")
        operation_row = rows[-1].split()
        columns: list[int] = [int(nmbr) for nmbr in rows[0].split()]
        for row in rows[1:-1]:
            for i, nmbr_str in enumerate(row.split()):
                nmbr = int(nmbr_str)
                if operation_row[i] == "*":
                    columns[i] *= nmbr
                else:
                    columns[i] += nmbr
        return sum(columns)

    @staticmethod
    def what_the_fuck_is_this_math(input: str) -> int:
        operation_row = input.split("\n")[-1].split()
        all_nmbrs = input.replace("\n", "").split()[: -len(operation_row) + 1]
        for i in range(0, len(operation_row)):
            col_nmbrs = all_nmbrs[i :: len(operation_row)]
            max_len = max([len(nmbr) for nmbr in col_nmbrs])
            nmbrs_list = [""] * max_len
            for j, curr_len in enumerate(range(max_len - 1, 0 - 1, -1)):
                for nmbr in col_nmbrs:
                    if curr_len >= len(nmbr):
                        continue
                    nmbrs_list[j] += nmbr[curr_len]

            print(nmbrs_list)

        return 0


def main() -> None:
    file = read_input(6, True)
    print(AncientMath.elementary_class(file))
    print(AncientMath.what_the_fuck_is_this_math(file))


if __name__ == "__main__":
    main()
