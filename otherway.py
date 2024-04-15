import sudoku


def read_sudoku(filename):
    sudoku_grid = []
    with open(filename, 'r') as file:
        for line in file:
            sudoku_grid.append([int(num) for num in line.split()])
    return sudoku_grid


def write_sudoku(filename, sudoku_grid):
    with open(filename, 'w') as file:
        for row in sudoku_grid:
            file.write(' '.join(map(str, row)) + '\n')


def main():
    input_file = "input.txt"
    output_file = "output.txt"

    sudoku_grid = read_sudoku(input_file)
    puzzle = sudoku.Sudoku(3, board=sudoku_grid)
    solved = puzzle.solve()

    print(solved.board)
    if solved:
        write_sudoku(output_file, solved.board)

    else:
        print("Impossible")


if __name__ == "__main__":
    main()
