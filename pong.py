#this game is called pong, it is a digital adaptation of ping pong, the ball should bounce off the outer edges of the paddles and the dimensions of the window.

import pygame


# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   game_display=pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Pong')  
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
      pygame.key.set_repeat(20, 20)
      self.bg_color = pygame.Color('black')
     
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
     
      # === game specific objects
      game_display=pygame.display.set_mode((500, 400))
      self.small_dot = Dot('white', 5, [50, 50], [7, 2], self.surface)
      self.max_frames = 150
      self.frame_counter = 0
      #this variable gives me half the horizontal distance of the window
      middle_x = game_display.get_width()//2
      #this variable gives me half the vertical distance of window
      middle_y = game_display.get_height()//2
      #left paddle
      self.rect_1 = pygame.Rect(middle_x//2 ,middle_y - 25, 15, 50)
      pygame.key.set_repeat(20, 20)
     
      #right paddle
      self.rect_2 = pygame.Rect(middle_x + middle_x//2, middle_y - 25, 15, 50)
      self.score_left = 0
      self.score_right=0
     
     
     
#where game is played
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
   #Changes state of game in response to user action
   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled
     
      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         if event.type == pygame.KEYDOWN and self.continue_game==True:
            self.update()
                       
   
   #def handle_q_down(self,event):
      #lead_x=-30
      #lead_x_change=0
      #list_of_keys = pygame.key.get_pressed()
      #pygame.key.set_repeat(20,20)
      #if list_of_keys[pygame.K_q] == True:      
         #pygame.key.set_repeat(20,20)
         #lead_x_change += 4
         #lead_x+= lead_x_change
         #self.rect_1=self.rect_1.move(0,lead_x)              
         #pygame.display.update()
   #def handle_a_down(self,event):
      #lead_x=5
      #lead_x_change=0
      #list_of_keys = pygame.key.get_pressed()
      #pygame.key.set_repeat(20,20)
      #if list_of_keys[pygame.K_a] == True:
         #lead_x_change += 4
         #lead_x+= lead_x_change
         #self.rect_1=self.rect_1.move(0,lead_x)
         #pygame.key.set_repeat(20,20)
         #pygame.display.update()          
         
         
   def rect_1_ball_collides(self):
      for i in range(len(self.small_dot.center)):
         if self.rect_1.collidepoint(self.small_dot.center[0],self.small_dot.center[1]) and self.small_dot.velocity[0] < 0:
            self.small_dot.velocity[i]=-self.small_dot.velocity[i]
    #checks to see if ball has collided with right rectangle  
   def rect_2_ball_collides(self):
      for i in range(len(self.small_dot.center)):
         if self.rect_2.collidepoint(self.small_dot.center[0],self.small_dot.center[1]) and self.small_dot.velocity[0] > 0:
            self.small_dot.velocity[i]=-self.small_dot.velocity[i]      
      #draws 2 scores
   def draw_score(self):
   
      # this method draws the player's score in the top-right corner of the
      # game window.
      #  - self : the game the score is being drawn for
      font_color = pygame.Color("white")
      font_bg    = pygame.Color("black")
      font       = pygame.font.SysFont("arial", 35)
      text_img   = font.render(" " + str(self.score_left), True, font_color, font_bg)    
      text_pos   = (0,0)
      self.surface.blit(text_img, text_pos)
     
      font_color = pygame.Color("white")
      font_bg    = pygame.Color("black")
      font       = pygame.font.SysFont("arial", 35)
      text_img   = font.render(" " + str(self.score_right), True, font_color, font_bg)    
      text_pos   = (450,0)
      self.surface.blit(text_img, text_pos)      
    #draws game elements
   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      # define the color white in pygame
      white=(255,255,255)
     
      game_display=pygame.display.set_mode((500, 400))
      self.surface.fill(self.bg_color) # clear the display surface first
      self.small_dot.draw()
      #draw the paddles
      pygame.draw.rect(game_display,white,self.rect_1)
      pygame.draw.rect(game_display,white,self.rect_2)
      self.draw_score()
      #self.right_Rect.draw()
      #self.left_Rect.draw()
      pygame.display.update() # make the updated surface appear on the display
   #moves ball
   
     #checks to see if ball hits left or right wall, if it does it then adds score.
   def update_score(self):
     
      size = self.surface.get_size()
      for i in range(0,1):
         if self.small_dot.center[i] < self.small_dot.radius: # left or top
            self.score_right = self.score_right + 1
         if self.small_dot.center[i] + self.small_dot.radius > size[i]:# right or bottom
            self.score_left= self.score_left + 1
           
   
   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      #move the ball
      self.small_dot.move()
      #change the score
      self.update_score()
      #check if the ball collides with the left rectangle
      self.rect_1_ball_collides()
      #check if the ball collides with the right rectangle
      self.rect_2_ball_collides()
      self.handle_events()      
      lead_x=-3
      lead_x_change=0
      list_of_keys = pygame.key.get_pressed()
      if list_of_keys[pygame.K_q] == True and self.continue_game==True:      
         lead_x_change -= 2
         lead_x+= lead_x_change
         if not self.rect_1.top <= 0:
            self.rect_1=self.rect_1.move(0,lead_x)              
         pygame.display.update()    
         
      lead_y=3
      lead_y_change=0
      list_of_keys = pygame.key.get_pressed()
      if list_of_keys[pygame.K_a] == True and self.continue_game==True:
         lead_y_change += 2
         lead_y+= lead_y_change
         if not self.rect_1.bottom >= self.surface.get_height():
            self.rect_1=self.rect_1.move(0,lead_y)
         pygame.display.update()
      lead_z=-3
      lead_z_change=0
      if list_of_keys[pygame.K_p] == True and self.continue_game==True:
         lead_z_change -=2
         lead_z+= lead_z_change
         if not self.rect_2.top <= 0:
            self.rect_2=self.rect_2.move(0,lead_z)
           
      lead_l=3
      lead_l_change=0
      if list_of_keys[pygame.K_l] == True and self.continue_game==True:
         lead_l_change += 2
         lead_l+= lead_l_change
         if not self.rect_2.bottom >= self.surface.get_height():
            self.rect_2=self.rect_2.move(0,lead_l)

     
   #ends game if end of game condition happens.
   def decide_continue(self):
      max_score=11
      #if either scores reach 11
      if self.score_left==max_score or self.score_right == max_score:
         self.continue_game=False
         
         
         
         

#dot is the ball
class Dot:
   # An object in this class represents a Dot that moves
   
   def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, surface):
      # Initialize a Dot.
      # - self is the Dot to initialize
      # - color is the pygame.Color of the dot
      # - center is a list containing the x and y int
      #   coords of the center of the dot
      # - radius is the int pixel radius of the dot
      # - velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object

      self.color = pygame.Color(dot_color)
      self.radius = dot_radius
      self.center = dot_center
      self.velocity = dot_velocity
      self.surface = surface  
   def move(self):
      # Change the location of the Dot by adding the corresponding
      # speed values to the x and y coordinate of its center
      # - self is the Dot
      size = self.surface.get_size()
      for i in range(0,2):
         self.center[i] = (self.center[i] + self.velocity[i])
         if self.center[i] < self.radius : # left or top
            self.velocity[i] = -self.velocity[i] # bounce the dot
         if self.center[i] + self.radius > size[i] :# right or bottom
            self.velocity[i] = -self.velocity[i]
     
   
   def draw(self):
      # Draw the dot on the surface
      # - self is the Dot
     
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)



main()
