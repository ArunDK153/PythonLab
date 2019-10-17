def horizontal_line ( size ):
    #return " ---" * size + " \n"
    return u" \u2014\u2014\u2014" * size + " \n"

def vertical_lines ( size ):
    return "|   " * size + "|\n"

def gameboard ( size ):
    board = ""
    for i in range(size):
        board += horizontal_line(size)
        board += vertical_lines(size)
    board += horizontal_line(size)
    return board

size = int(input("What size game board do you want? "))
print(gameboard(size))
