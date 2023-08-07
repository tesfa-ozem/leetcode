from typing import List


def depth_first_search(
    boards: List[List[str]],
    diagonal_right_collusions: List[int],
    diagonal_left_collusions,
    possible_board: List[int],
    n: int,
):
    row = len(possible_board)

    if row == n:
        boards.append([". " * i + "Q " + ". " * (n - 1 - i) for i in possible_board])

        return

    for col in range(n):
        if (
            col in possible_board
            or row - col in diagonal_right_collusions
            or row + col in diagonal_left_collusions
        ):
            continue

        depth_first_search(
            boards,
            [*diagonal_right_collusions, row - col],
            [*diagonal_left_collusions, row + col],
            [*possible_board, col],
            n,
            )

def n_queens_solutions(n: int) -> None:
    boards: List[List[str]] = []
    depth_first_search(boards, [], [], [], n)

    # for board in boards:
    #     for colunm in board:
    #         print(colunm)
    #     print("")

    print(len(boards), "solutions were found")

if __name__ == "__main__":
    n_queens_solutions(10)
