def read_sudoku(filename):
    sudoku = []
    with open(filename, 'r') as file:
        for line in file:
            sudoku.append([int(num) for num in line.split()])
    return sudoku


def is_valid_move(sudoku, row, col, num):
    for x in range(9):
        if sudoku[row][x] == num:
            return False

    for y in range(9):
        if sudoku[y][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for x in range(3):
        for y in range(3):
            if sudoku[start_row + x][start_col + y] == num:
                return False
    return True


def solve_sudoku(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(sudoku, row, col, num):
                        sudoku[row][col] = num
                        if solve_sudoku(sudoku):
                            return True
                        sudoku[row][col] = 0
                return False
    return True


def write_sudoku(filename, sudoku):
    with open(filename, 'w') as file:
        for row in sudoku:
            file.write(' '.join(map(str, row)) + '\n')


def main():
    input_file = "input.txt"
    output_file = "output.txt"

    sudoku = read_sudoku(input_file)

    if solve_sudoku(sudoku):
        write_sudoku(output_file, sudoku)

    else:
        print("Impossible")


if __name__ == "__main__":
    main()
