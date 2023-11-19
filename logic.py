from utils import clean_console, get_matrix_size, print_matrix


def get_number_of_live_neighbours(matrix: [[int]], x: int, y: int):
    number_of_live_neighbours = 0
    rows, columns = get_matrix_size(matrix)
    for i in range(max(x - 1, 0), min(x + 2, rows)):
        for j in range(max(y - 1, 0), min(y + 2, columns)):
            if x == i and y == j:
                continue
            if matrix[i][j] == 1:
                number_of_live_neighbours += 1
    return number_of_live_neighbours


def next_generation(matrix: [[int]]):
    if not matrix:
        return matrix
    rows, columns = get_matrix_size(matrix)
    next_matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            living_neighbours = get_number_of_live_neighbours(matrix, i, j)
            if living_neighbours < 2 or living_neighbours > 3:
                next_matrix[i][j] = 0
            if living_neighbours == 3:
                next_matrix[i][j] = 1
            if living_neighbours == 2:
                next_matrix[i][j] = matrix[i][j]
    return next_matrix


def run_simulation(matrix: [[int]], generations: int):
    clean_console()
    print("Generation 0")
    print_matrix(matrix)
    for i in range(generations):
        print(f"Generation {i+1}")
        matrix = next_generation(matrix)
        print_matrix(matrix)
    return matrix
