# html_view.py

def render_to_html(cells, filename):
    # Nyitunk egy .html fájlt a megadott névvel
    with open(filename, "w") as html_file:
        # Kezdjük az HTML tartalmát
        html_file.write("<html><head><title>Game Board</title></head><body>\n")
        # Kinyerjük a cellák számát
        size = len(cells)
        # Létrehozzuk a táblázatot az adatokkal
        html_file.write("<table>\n")
        for row in cells:
            html_file.write("<tr>\n")
            for cell in row:
                if cell is not None:
                    html_file.write(f"<td>{str(cell)}</td>\n")
                else:
                    html_file.write("<td>..</td>\n")
            html_file.write("</tr>\n")
        html_file.write("</table>\n")
        # Lezárjuk az HTML fájlt
        html_file.write("</body></html>\n")

# Példa használat:
# Az alábbi kód létrehoz egy példa játékteret és elmenti egy .html fájlba
# Az "example_board.html" fájlba.
if __name__ == "__main__":
    from board import Board
    board = Board(10)
    cells = board.get_cells()
    render_to_html(cells, "example_board.html")
