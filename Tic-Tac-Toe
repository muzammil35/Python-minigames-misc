import pygame,random

# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Tic Tac Toe')  
   # get the display surface
   w_surface = pygame.display.get_surface()
   # create a game object
   game = Game(w_surface)
   # start the main game loop by calling the play method on the game object
   game.play()
   # quit pygame and clean up the pygame window
   pygame.quit()


# User-defined classes

class Game:
   # An object in this class represents a complete game.

   def __init__(self, surface):
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the display window surface object

      # === objects that are part of every game that we will discuss
      self.surface = surface
      self.bg_color = pygame.Color('black')
     
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
     
      # === game specific objects
      self.player_1 = 'X'
      self.player_2 ='O'
      self.flashers = []
      self.filled = []
      self.turn = self.player_1
      self.board = []
      self.board_size = 3
      self.create_board()
   def create_board(self):
      Tile.set_surface(self.surface)
      width = self.surface.get_width()//self.board_size
      height = self.surface.get_height()//self.board_size
      for row_index in range(0, self.board_size):
         row = []
         for col_index in range(0,self.board_size):
            x = width * col_index
            y = height * row_index
            tile = Tile(x,y,width,height)
            row.append(tile)
         self.board.append(row)
     

   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box
         # play frame
         self.handle_events()
         self.draw()            
         if self.continue_game:
            self.update()
            self.decide_continue()
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second

   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled

      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         if event.type == pygame.MOUSEBUTTONUP and self.continue_game:
            self.handle_mouse_up(event)
   def handle_mouse_up(self,event):
      for row in self.board:
         for tile in row:
            valid_click=tile.select(event.pos,self.turn)
            if valid_click == True:
               self.filled.append(tile)
               # time to change the turn
               self.change_turn()
   def change_turn(self):
      if self.turn == self.player_1:
         self.turn = self.player_2
      else:
         self.turn = self.player_1
     
     

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
     
      self.surface.fill(self.bg_color) # clear the display surface first
      if not self.continue_game:
         tile = random.choice(self.flashers)
         # tile.flashing = True
         tile.set_flashing()
      # Draw the tiles
      for each_row in self.board:
         for each_tile in each_row:
            each_tile.draw()
      pygame.display.update() # make the updated surface appear on the display

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      pass
   def is_same(self,alist):
      # alist i a list of tiles
      first = alist[0]
      index = 1
      same = True
      while index < len(alist) and same == True:
         #if alist[index] != first:
         #   same = False
         same = alist[index] == (first) # comparing 2 Tile object
         index = index + 1
      if same == True:
         self.flashers = alist
      return same
   def is_diagonal_win(self):
      diagonal1 = []
      diagonal2 = []
      for index in range(0,self.board_size):
         # index will be 0,1,2
         tile = self.board[index][index]
         diagonal1.append(tile)
         tile = self.board[index][self.board_size -1 - index]
         diagonal2.append(tile)
      if self.is_same(diagonal1) or self.is_same(diagonal2):
         return True
      else:
         return False
   def is_column_win(self):
      col_win = False
      for col_index in range(0,self.board_size):
         column = []
         for row_index in range(0,self.board_size):
            tile = self.board[row_index][col_index]
            column.append(tile)
         if self.is_same(column) == True:
            col_win = True
      return col_win
   def is_row_win(self):
      row_win = False
      for row in self.board:
         if self.is_same(row):
            row_win = True
      return row_win
   def is_win(self):
      if self.is_row_win() or self.is_column_win() or self.is_diagonal_win():
         return True
      else:
         return False
   def is_tie(self):
      if len(self.filled) == self.board_size ** 2:
         self.flashers = self.filled
         return True
      else:
         return False
   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      if self.is_win() or self.is_tie():
         self.continue_game = False


class Tile:
   # An object in this class represents a Dot that moves
   # Shared Attrbutes or Class Attributes
   surface = None
   border_size = 3
   border_color = pygame.Color('white')
   font_size = 144
   @classmethod
   def set_surface(cls,game_surface):
      cls.surface = game_surface
   # Instance Methods
   def __init__(self,x,y,width,height):
      self.rect = pygame.Rect(x,y,width,height)
      self.content = ''
      self.flashing = False
   def draw(self):
      # Draw the dot on the surface
      # - self is the Dot
      if self.flashing == True:
         # white rectangle
         pygame.draw.rect(Tile.surface,Tile.border_color,self.rect)
         self.flashing = False
      else:
         # black rectangle with a white border
         pygame.draw.rect(Tile.surface,Tile.border_color,self.rect,Tile.border_size)
         self.draw_content()
   def set_flashing(self):
      self.flashing = True
   def draw_content(self):
      font = pygame.font.SysFont('',Tile.font_size)
      text_surface = font.render(self.content,True,Tile.border_color)
      # Compute the location
      r_x = self.rect.x
      r_y = self.rect.y
      r_w = self.rect.width
      r_h = self.rect.height
      t_w = text_surface.get_width()
      t_h = text_surface.get_height()
      t_x = r_x + (r_w - t_w)//2
      t_y = r_y + (r_h - t_h) //2
      Tile.surface.blit(text_surface,(t_x,t_y))
   def select(self, position,current_player):
      valid_click = False
      if self.rect.collidepoint(position):
         if self.content == '':
            self.content = current_player
            valid_click = True
         else:
            self.flashing = True
      return valid_click
   def __eq__(self,other_tile):
      if self.content != '' and self.content == other_tile.content:
         return True
      else:
         return False

main()
