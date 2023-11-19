import os
from time import sleep


def clean_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_matrix(matrix: [[int]]):
    lines = []
    for row in matrix:
        line = " ".join(["*" if x == 1 else " " for x in row])
        lines.append(f"|{line}|")
    print("\n".join(lines))
    sleep(0.1)
    clean_console()


def get_matrix_size(matrix: [[int]]):
    return len(matrix), len(matrix[0])


def parse_file(state_file_path: int):
    matrix = []
    with open(state_file_path, "r") as f:
        for line in f:
            matrix.append([int(x) for x in line.split()])
    return matrix
