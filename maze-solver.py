from tkinter import Tk,BOTH, Canvas
import time
import random

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
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
            
    def draw_move(self,to_cell,undo=False):
        
        if self._win is None:
            return
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "red"
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
    
    
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win=None):
        
        self.x1=x1
        self.y1=y1
        self.num_rows = num_rows
        self.num_cols = num_cols 
        self.cell_size_x = cell_size_x 
        self.cell_size_y = cell_size_y 
        self.win = win 
        
        self._cells = []
        
        self._create_cells()
        
    def _create_cells(self):
        
        for i in range(self._num_rows):
            col_cells = []
            for j in range(self._num_cols):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
                
    def _draw_cell(self,i,j):
        
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
        
        
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
        
        
        
        
            
        
            
            
        
        
            
            
    
            
        
        
    
    
        



        
def main():
    
    
    
    win = Window(800,600)
    pt1=Point(100,200)
    pt2=Point(200,200)
    pt3=Point(100,100)
    
    line = Line(pt3,pt2)
    win.draw_line(line,'blue')
    
    pt4=Point(100,200)
    pt5=Point(200,200)
    pt6=Point(100,100)

   
    win.wait_for_close()
    
main()

    
    