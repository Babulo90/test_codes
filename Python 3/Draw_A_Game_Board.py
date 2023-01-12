def drawboard(Tamal):
    Tamal = int(Tamal)
    i = 0
    horizontal = "--- "
    vertical = "|  "
    horizontal = horizontal * Tamal
    vertical = vertical * (Tamal+1)
    while i < Tamal+1:
        print horizontal
        if not (i == Tamal):
            print vertical
        i += 1


#V2

def print_hirizontal_line():
    print(" --- " * board_size)


def print_vertical_line():
    print("|   " * (board_size * 1))

if __name__ == "__main__":
    board_size = int(input("what size of game board do you want? "))


    for index in range(board_size):
        print_horizontal_line()
        print_vertical_line()
    print horizontal_line()