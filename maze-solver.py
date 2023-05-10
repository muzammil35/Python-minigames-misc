from tkinter import Tk,BOTH, Canvas
import time
import random
import sys

class Window:
    
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="black", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False
    
    def draw_line(self,line_obj, fill_color):
        line_obj.draw(self.__canvas,fill_color)
        
class Point:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    
    def __init__(self,pt1,pt2):
        self.pt1 = pt1
        self.pt2 = pt2
    
    def draw(self,Canvas_obj,fill_color):
        Canvas_obj.create_line( self.pt1.x , self.pt1.y, self.pt2.x, self.pt2.y, fill=fill_color, width=2)
        Canvas_obj.pack(fill=BOTH, expand=1)
        
        
class Cell:
    
    
    def __init__(self,win=None):
        
       self.has_left_wall = True
       self.has_right_wall = True
       self.has_top_wall = True
       self.has_bottom_wall = True
       self.visited = False
       self._x1 = None
       self._x2 = None
       self._y1 = None
       self._y2 = None
       self._win = win
            
    def Draw(self,fill_color,x1,y1,x2,y2):
        
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line,fill_color)
        elif not self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line,"black")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line,fill_color)
        elif not self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line,"black")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line,fill_color)
        elif not self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line,"black")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line,fill_color)
        elif not self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2
                                             ))
            self._win.draw_line(line,"black")
            
    def draw_move(self,to_cell,undo=False):
        
        if self._win is None:
            return
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "blue"
        if undo:
            fill_color = "gray"

        # moving left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_cell._x2, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1))
            self._win.draw_line(line, fill_color)
            
            
class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].Draw("white",x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
        
        
    def _break_entrance_and_exit(self):
        
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
        
    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while(True):
            directions = []
            possible_visitors = []
            
             # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                directions.append("left")
                
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                directions.append("right")
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                directions.append("up")
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                directions.append("down")
            if(len(directions)==0):
                self._draw_cell(i,j)
                break
            else:
                
                ran = random.choice(directions)
                if(ran=="up"):
                    self._cells[i][j-1].has_bottom_wall = False
                    self._cells[i][j].has_top_wall = False
                    self._break_walls_r(i,j-1)
                if(ran=="down"):
                    self._cells[i][j+1].has_top_wall = False
                    self._cells[i][j].has_bottom_wall = False
                    self._break_walls_r(i,j+1)
                if(ran=="left"):
                    self._cells[i-1][j].has_right_wall = False
                    self._cells[i][j].has_left_wall = False
                    self._break_walls_r(i-1,j)
                if(ran=="right"):
                    self._cells[i+1][j].has_left_wall = False
                    self._cells[i][j].has_right_wall = False
                    self._break_walls_r(i+1,j)
                    
    def _reset_cells_visted(self):
        
        for col in self._cells:
            
            for cell in col:
                cell.visited = False
                
                
    def solve(self):
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visted()
        
        return(self._solve_r(0,0))
                
    def _solve_r(self,i,j):
        
        self._animate()
        self._cells[i][j].visited = True
        if(i == self._num_cols-1 and j == self._num_rows-1):
            return True
         # move left if there is no wall and it hasn't been visited
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # move right if there is no wall and it hasn't been visited
        if (
            i < self._num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # move up if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # move down if there is no wall and it hasn't been visited
        if (
            j < self._num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # we went the wrong way let the previous cell know by returning False
        return False
        
        
        
        
def main():
    
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin,margin, 12, 16, cell_size_x, cell_size_y, win)\
    
    
    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()
    
main()
