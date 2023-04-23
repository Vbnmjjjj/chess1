from tkinter import *
app = Tk()

class Board:
    cnvs = Canvas(app, height=800,width=800)
    fill = '#fff'
    outline = '#000'
    size = 101
    for i in range(8):
        for j in range(8):
            x1, y1, x2, y2 = i * size, j * size, i * size + size, j * size + size
            cnvs.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline)
            fill, outline = outline, fill
        fill, outline = outline, fill
    cnvs.pack()
class Pawn:
    def __init__(self,x1, y1):
        cnvs = Canvas()
        self.x1 = x1
        self.y1 = y1
        cnvs.create_text(self.x1, self.y1, text='p')
        cnvs.pack()

    def move(self, board, row, col, row1, col1):
        if col != col1:
            return False
        if not self.is_path_clear(board, row, col, row1, col1):
            return False
        if self.color == '#fff':
            direction = 650
            start_row = 50
        else:
            direction = 150
            start_row = 50
        if row + direction == row1:
            return True
        if row == start_row and row + 200 * direction == row1:
            return True
        return False

class Queen:
    def __init__(self,x1, y1):
        cnvs = Canvas()
        self.x1 = x1
        self.y1 = y1
        cnvs.create_text(self.x1, self.y1, text='q')
        cnvs.pack()

    def move(self, board, row, col, row1, col1):
        if not self.is_path_clear(board, row, col, row1, col1):
            return False
        if col == col1:
            return True
        if row == row1:
            return True
        if abs(row - row1) == abs(col - col1):
            return True

        return False
class Rook:
    def __init__(self, x1, y1):
        cnvs = Canvas()
        self.x1 = x1
        self.y1 = y1
        cnvs.create_text(self.x1, self.y1, text='r')
        cnvs.pack()

    def move(self, board, row, col, row1, col1):
        if row != row1 and col != col1:
            return False
        if not self.is_path_clear(board, row, col, row1, col1):
            return False
        return True

class Bishop:
    def __init__(self,x1, y1):
        cnvs = Canvas()
        self.x1 = x1
        self.y1 = y1
        cnvs.create_text(self.x1, self.y1, text='b')
        cnvs.pack()

    def move(self, board, row, col, row1, col1):
        if not self.is_path_clear(board, row, col, row1, col1):
            return False
        if abs(row - row1) == abs(col - col1):
            return True
        return False
class Knight:
    def __init__(self,x1, y1):
        cnvs = Canvas()
        self.x1 = x1
        self.y1 = y1
        cnvs.create_text(self.x1, self.y1, text='kn')
        cnvs.pack()

    def move(self, row, col, row1, col1):
        if abs(row - row1) == 2 and abs(col - col1) == 1:
            return True
        if abs(row - row1) == 1 and abs(col - col1) == 2:
            return True

        return False
class King:
    def __init__(self,x1, y1):
        cnvs = Canvas()
        self.x1 = x1
        self.y1 = y1
        cnvs.create_text(self.x1, self.y1, text='k')
        cnvs.pack()

    def move(self, board, row, col, row1, col1):
        if not self.is_path_clear(board, row, col, row1, col1):
            return False
        if max(abs(row - row1), abs(col - col1)) == 100:
            return True

        return False

def start():
    pawn_black = Pawn(50,150)
    pawn_white = Pawn(50,650)
    for i in range(8):
        pawn_black+=100,0
    for i in range(8):
        pawn_white+=100,0
    queen_black = Queen(350,50)
    queen_white = Queen(350,750)
    king_black = King(450,50)
    king_white = King(450,750)
    rook_black = Rook(50, 50)
    for i in range(2):
        rook_black+=700,0
    rook_white = Rook(50,750)
    for i in range(2):
        rook_white+=700,0
    bishop_black = Bishop(50,250)
    for i in range(2):
        bishop_black+=300,0
    bishop_white = Bishop(750, 250)
    for i in range(2):
        bishop_white += 300, 0
    start()
def main():
    Running = True
    board = Board()
    movements = {'pawn': Pawn,'bishop': Bishop,'knight': Knight, 'rook': Rook,'queen': Queen, 'king': King}
    while Running:

        if team_now == 'black':
            team_now = 'white'
        else:
            team_now = 'black'

        check = False
        cur_place, want = map(str, input('Ход команды {}: '.format(team_now)).split())
        while not check:
            check = not check
            if board.get_figures_coords()[cur_place[-1]][cur_place[0]] is None:
                cur_place, want = map(str, input('Невозможный ход, повторите попытку: ').split())
                check = not check
                continue
            if board.get_figures_coords()[cur_place[-1]][cur_place[0]].get_team() != team_now:
                cur_place, want = map(str, input('Невозможный ход, повторите попытку: ').split())
                check = not check
                continue
            if want not in movements[board.get_figure_type_on_place(cur_place)](cur_place, team_now,
                                                                                board.get_figures_coords()):
                cur_place, want = map(str, input('Невозможный ход, повторите попытку: ').split())
                check = not check
                continue



