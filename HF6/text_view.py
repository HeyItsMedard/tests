from characters import Character

def render(board: list[list[Character | None]]) -> str:
    result = "-" * (len(board) * 2 + 1) + "\n"
    for row in board:
        result += "|" + "".join(str(cell) if cell else ".." for cell in row) + "|\n"
    result += "-" * (len(board) * 2 + 1) + "\n"
    return result
