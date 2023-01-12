import pygame,random,math

# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   pygame.mixer.init()
   
   
   # create a pygame display window and its size
   size = [1900,1000]
   screen = pygame.display.set_mode(size, pygame.RESIZABLE)
   # set the title of the display window
   pygame.display.set_caption('')   
   # get the display surface
   w_surface = pygame.display.get_surface() 
   # create a game object
   game = Game(w_surface, screen, size)
   #game = Game(w_surface, 350, 350)
   
   # start the main game loop by calling the play method on the game object
   game.play() 
   # quit pygame and clean up the pygame window
   pygame.quit() 
   


# User-defined classes

class Game:
   # An object in this class represents a complete game.

   def __init__(self, surface,screen,size):
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the display window surface object

      # === objects that are part of every game that we will discuss
      self.surface = surface
      #self.bg_color = pygame.Color('black')
      self.bg = pygame.image.load("bg.jpg")
      self.screen = screen
      self.size = size
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
      self.file = '1.mp3'
      self.volume = 1
      self.volume1 = 1
      #pygame.mixer.music.load(self.file)
      self.lit = [1,2,3,4]
      print(self.lit)
      
      # === game specific objects
      self.new = size
      self.paddle_increment = 10
      self.paddle = Paddle(50,50,160,152,'white',self.surface,'y1.png',self.screen)
      self.paddle1 = Paddle(200,50,160,152,'white',self.surface,'y2.png',self.screen)
      self.paddle2 = Paddle(200,50,160,152,'white',self.surface,'y4.png',self.screen)
      self.music1 = Paddle(200,50,72,72,'white',self.surface,'m1.png',self.screen)
      self.music2 = Paddle(200,50,72,72,'white',self.surface,'m2.png',self.screen)
      self.music3 = Paddle(200,50,72,72,'white',self.surface,'m3.png',self.screen)
      self.music4 = Paddle(200,50,72,72,'white',self.surface,'m4.png',self.screen)
      self.music5 = Paddle(200,50,72,72,'white',self.surface,'m5.png',self.screen)
      self.music6 = Paddle(200,50,72,72,'white',self.surface,'m6.png',self.screen)
      self.music7 = Paddle(200,50,72,72,'white',self.surface,'m7.png',self.screen)
      self.music8 = Paddle(200,50,72,72,'white',self.surface,'m8.png',self.screen)
      self.play1 = button(1790,750,100,100,'white',self.surface,'play.png',self.screen)
      self.pause = button(1790,900,100,100,'white',self.surface,'pause.png',self.screen)
      self.stop = button(1790,600,100,100,'white',self.surface,'stop.png',self.screen)
      self.down = button(1790,550,50,50,'white',self.surface,'down.png',self.screen)
      self.up = button(1840,550,50,50,'white',self.surface,'up.png',self.screen)
      self.auto = button(1790,450,100,100,'white',self.surface,'auto.png',self.screen)
      self.down1 = button(1790,350,50,50,'white',self.surface,'down.png',self.screen)
      self.up1 = button(1840,350,50,50,'white',self.surface,'up.png',self.screen)      
      
      voicelines = ['1000_jp.ogg','1004_jp.ogg','4004_jp.ogg','5002_jp.ogg','7001_jp.ogg','1000200_01_jp.ogg','1000200_03_jp.ogg','1000400_01_jp.ogg','1000400_02_jp.ogg','1000400_03_jp.ogg','5005_jp.ogg']
      self.mysound = pygame.mixer.Sound(voicelines[0])
      self.mysound1 = pygame.mixer.Sound(voicelines[1])
      self.mysound2 = pygame.mixer.Sound(voicelines[2])
      self.mysound3 = pygame.mixer.Sound(voicelines[3])
      self.mysound4 = pygame.mixer.Sound(voicelines[4])
      self.mysound5 = pygame.mixer.Sound(voicelines[5])
      self.mysound6 = pygame.mixer.Sound(voicelines[6])
      self.mysound7 = pygame.mixer.Sound(voicelines[7])
      self.mysound8 = pygame.mixer.Sound(voicelines[8])
      self.mysound9 = pygame.mixer.Sound(voicelines[9])
      self.mysound10 = pygame.mixer.Sound(voicelines[10])      
      
      
      
      
      
      
      
      
      
      self.small_ball = ball('white', 10, [50, 50], [6, 3], self.surface, self.screen, self.size)
      #print(self.small_ball.center)
      
      
      
                    
   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box
         # play frame
         self.handle_events()

         self.draw()            
         if self.continue_game:
            self.update()
            print('test')
            #self.decide_continue()
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 
   #def queue(self):
      
   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled
      #voicelines = ['1000_jp.ogg','1004_jp.ogg','4004_jp.ogg','5002_jp.ogg','7001_jp.ogg','1000200_01_jp.ogg','1000200_03_jp.ogg','1000400_01_jp.ogg','1000400_02_jp.ogg','1000400_03_jp.ogg','5005_jp.ogg']
      #mysound = pygame.mixer.Sound(voicelines[0])
      #mysound1 = pygame.mixer.Sound(voicelines[1])
      #mysound2 = pygame.mixer.Sound(voicelines[2])
      #mysound3 = pygame.mixer.Sound(voicelines[3])
      #mysound4 = pygame.mixer.Sound(voicelines[4])
      #mysound5 = pygame.mixer.Sound(voicelines[5])
      #mysound6 = pygame.mixer.Sound(voicelines[6])
      #mysound7 = pygame.mixer.Sound(voicelines[7])
      #mysound8 = pygame.mixer.Sound(voicelines[8])
      #mysound9 = pygame.mixer.Sound(voicelines[9])
      #mysound10 = pygame.mixer.Sound(voicelines[10])
      
      
      

      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         elif event.type == pygame.KEYDOWN:
            self.handle_key_down(event)
         elif event.type == pygame.KEYUP:
            self.handle_key_up(event)
         elif event.type == pygame.VIDEORESIZE:
            self.new = event.size  
         elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.paddle.collide(pos) or self.paddle1.collide(pos) or self.paddle2.collide(pos):
               self.music(1,1) # maybe add variable ex 1 is voicelines 2 is music
            if self.pause.collide(pos):
               pygame.mixer.music.pause()
               print('pause')
            if self.play1.collide(pos):
               pygame.mixer.music.unpause()
               print('uppause')
            if self.stop.collide(pos):
               print('stop')
               pygame.mixer.music.stop()
            if self.down.collide(pos):
               print('down')
               self.volume = self.volume - 0.1
               pygame.mixer.music.set_volume(self.volume)
            if self.up.collide(pos):
               self.volume = self.volume + 0.1
               pygame.mixer.music.set_volume(self.volume)
            if self.down1.collide(pos):
               print('down')
               self.volume1 = self.volume1 - 0.1
               self.mysound.set_volume(self.volume1)
               self.mysound1.set_volume(self.volume1)
               self.mysound2.set_volume(self.volume1)
               self.mysound3.set_volume(self.volume1)
               self.mysound4.set_volume(self.volume1)
               self.mysound5.set_volume(self.volume1)
               self.mysound6.set_volume(self.volume1)
               self.mysound7.set_volume(self.volume1)
               self.mysound8.set_volume(self.volume1)
               self.mysound9.set_volume(self.volume1)
               self.mysound10.set_volume(self.volume1)
               
               
               
            if self.up1.collide(pos):
               print(self.volume1)
               self.volume1 = self.volume1 + 0.1
               self.mysound.set_volume(self.volume1)
               self.mysound1.set_volume(self.volume1)
               self.mysound2.set_volume(self.volume1)
               self.mysound3.set_volume(self.volume1)
               self.mysound4.set_volume(self.volume1)
               self.mysound5.set_volume(self.volume1)
               self.mysound6.set_volume(self.volume1)
               self.mysound7.set_volume(self.volume1)
               self.mysound8.set_volume(self.volume1)
               self.mysound9.set_volume(self.volume1)
               self.mysound10.set_volume(self.volume1)
               
            if self.auto.collide(pos):
               done = False
               SONGS=['1.mp3','2.mp3','3.mp3','4.mp3','5.mp3','6.mp3','7.mp3','8.mp3',]               
               SONG_FINISHED = pygame.USEREVENT + 1
               random.shuffle(SONGS)
               pygame.mixer.music.set_endevent(SONG_FINISHED)
               pygame.mixer.music.load(SONGS[0])
               pygame.mixer.music.play(0)
               
               clock = pygame.time.Clock()
               song_idx = 0
               while not done:
                  
                  for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                           done = True
                     elif event.type == pygame.KEYDOWN:
                           # Press right arrow key to increment the
                           # song index. Modulo is needed to keep
                           # the index in the correct range.
                           if event.key == pygame.K_RIGHT:
                              print('Next song.')
                              song_idx += 1
                              song_idx %= len(SONGS)
                              pygame.mixer.music.load(SONGS[song_idx])
                              pygame.mixer.music.play(0)
                       # When a song ends the SONG_FINISHED event is emitted.
                       # Then just pick a random song and play it.
                     elif event.type == SONG_FINISHED:
                           #print('Song finished. Playing random song.')
                           pygame.mixer.music.load(random.choice(SONGS))
                           pygame.mixer.music.play()               
            
            elif self.music1.collide(pos):
               self.music(2,'1.mp3')
            elif self.music2.collide(pos):
               self.music(2,'2.mp3')    
            elif self.music3.collide(pos):
               self.music(2,'3.mp3')                   
            elif self.music4.collide(pos):
               self.music(2,'4.mp3')  
            elif self.music5.collide(pos):
               self.music(2,'5.mp3')    
            elif self.music6.collide(pos):
               self.music(2,'6.mp3')    
            elif self.music7.collide(pos):
               self.music(2,'7.mp3')    
            elif self.music8.collide(pos):
               self.music(2,'8.mp3')                                  
               
   def music(self,lol,music):
      #self.file = 
      if lol == 1:
         voicelines = ['1000_jp.ogg','1004_jp.ogg','4004_jp.ogg','5002_jp.ogg','7001_jp.ogg','1000200_01_jp.ogg','1000200_03_jp.ogg','1000400_01_jp.ogg','1000400_02_jp.ogg','1000400_03_jp.ogg','5005_jp.ogg']
         pygame.mixer.Channel(0).play(pygame.mixer.Sound(voicelines[random.randint(1,10)]))
         #pygame.mixer.music.set_volume(0.1)
      
         #pygame.mixer.music.play()
      if lol == 2:
         pygame.mixer.music.load(music)
         pygame.mixer.music.play()
      
            

            
        
            
         
  
         
   def handle_key_down(self,event):
      # reponds to KEYDOWN event
      # - self is the Game object
      #if event.key == pygame.K_a:
         #self.paddle.set_horizontal_velocity(self.paddle_increment)
      #if event.key == pygame.K_q:
         #self.paddle.set_horizontal_velocity(-self.paddle_increment)
      #if event.key == pygame.K_l:
         #self.paddle1.set_horizontal_velocity(self.paddle_increment)
      #if event.key == pygame.K_p:
         #self.paddle1.set_horizontal_velocity(-self.paddle_increment)
         pass
         
      
   
   def handle_key_up(self,event):
      # responds to KEYUP event
      # - self is the Game object
      #if event.key == pygame.K_a:
         #self.paddle.set_horizontal_velocity(0)
      #if event.key == pygame.K_q:
         #self.paddle.set_horizontal_velocity(0)
      #if event.key == pygame.K_l:
         #self.paddle1.set_horizontal_velocity(0)
      #if event.key == pygame.K_p:
         #self.paddle1.set_horizontal_velocity(0) 
         pass
   

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      #self.surface.fill(self.bg_color) # clear the display surface first
      self.screen.blit(self.bg, (0,0))
      self.lol = [100,50]
      self.paddle.draw(self.lol)
      self.paddle1.draw(self.new)
      self.paddle2.draw(self.new)
      self.music1.draw(self.new)
      self.music2.draw(self.new)
      self.music3.draw(self.new)
      self.music4.draw(self.new)
      self.music5.draw(self.new)
      self.music6.draw(self.new)
      self.music7.draw(self.new)
      self.music8.draw(self.new)
      self.pause.draw(self.new)
      self.play1.draw(self.new)
      self.stop.draw(self.new)
      self.down.draw(self.new)
      self.up.draw(self.new)
      self.auto.draw(self.new)
      self.up1.draw(self.new)
      self.down1.draw(self.new)
      
      
      
      
      
      #self.small_ball.draw(self.new)
      
      pygame.display.update() # make the updated surface appear on the display
   
   
   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      self.paddle.move(self.new)
      self.paddle1.move(self.new)
      self.paddle2.move(self.new)
      self.music1.move(self.new)
      self.music2.move(self.new)
      self.music3.move(self.new)
      self.music4.move(self.new)
      self.music5.move(self.new)
      self.music6.move(self.new)
      self.music7.move(self.new)
      self.music8.move(self.new)
      self.pause.move()
      self.play1.move()
      self.down.move()
      self.stop.move()
      self.up.move()
      self.auto.move()
      self.up1.move()
      self.down1.move()
      
      
      #self.small_ball.move(self.paddle.collide(self.small_ball.get_center()),self.paddle1.collide(self.small_ball.get_center()),self.new)
      
      
   
   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      # stop game when player has a scroe bugger then 10-
      check_end = []
      check_end = self.small_ball.return_score()
      if check_end[0] > 10 or check_end[1] > 10:
         self.continue_game = False

         

class ball:
   
   def __init__(self, ball_color, ball_radius, ball_center, ball_velocity, surface, screen,size):
      # Initialize a ball.
      # - self is the ball to initialize
      # - color is the pygame.Color of the ball
      # - center is a list containing the x and y int
      #   coords of the center of the ball
      # - radius is the int pixel radius of the ball
      # - velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object

      self.color = pygame.Color(ball_color)
      self.radius = ball_radius
      self.center = ball_center
      self.velocity = ball_velocity
      self.surface = surface
      self.p1score = 0
      self.p2score = 0
      self.screen =  screen
      self.size = size
   def move(self, paddle_1, paddle_2,new):
      # Change the location of the ball by adding the corresponding 
      # speed values to the x and y coordinate of its center
      # - self is the ball
      pass
      #self.center[1] = (self.center[1] + self.velocity[1])
     
   def return_score(self):
      return (self.p1score, self.p2score)
      
         
   def get_center(self):
      return self.center
   
   def draw(self,new):
      # Draw the ball on the surface
      # - self is the ball
      # also blits the score of each player to the screen
      text_string = (str(self.p1score))
      text_string2 = (str(self.p2score))
      text_color = pygame.Color('white')        
      text_font = pygame.font.SysFont('Times New Roman', 48, bold=True, italic=True)
      text_image1 = text_font.render(text_string, True, text_color)
      text_image2 = text_font.render(text_string2, True, text_color)
      
      text_pos1 = (10, 10)
      text_pos2 = ((0 ), new[1]-50)
      self.screen.blit(text_image1, text_pos1)
      self.screen.blit(text_image2, text_pos2)

      
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)
   
   

class Paddle:
   # An object in this class represents a Paddle that moves
   
   def __init__(self,x,y,width,height,color,surface,img,screen):
      # - self is the Paddle object
      # - x, y are the top left corner coordinates of the rectangle of type int
      # - width is the width of the rectangle of type int
      # - height is the heightof the rectangle of type int
      # - surface is the pygame.Surface object on which the rectangle is drawn
      self.i = pygame.image.load(img)
      self.img = pygame.image.load(img)
      self.screen = screen
      self.rect = self.img.get_rect()
      self.x = random.randint(10,900)
      self.y = random.randint(10,900)
      self.width = width
      self.height = height
      self.color = pygame.Color(color)
      self.surface = surface
      self.horizontal_velocity = random.randint(1,3)     
      self.vertical_velocity = random.randint(1,3) 
   def draw(self,new):
      # -self is the Paddle object to draw
      #self.test = self.img.get_rect()
      #print(self.test)
      
      self.rect.update(self.x,self.y,self.width,self.height)
      #self.rect = pygame.Rect(new[0]-self.x,self.y,self.width,self.height)
      #pygame.draw.rect(self.surface,self.color,self.rect)
      #self.rect.move(self.x,self.y)
      self.screen.blit(self.i,self.rect)
   def set_horizontal_velocity(self,horizontal_distance):
      # set the horizontal velocity of the Paddle object
      # -self is the Paddle object
      # -horizontal_distance is the int increment by which the paddle moves horizontally
      self.horizontal_velocity1 = horizontal_distance
      self.vertical_velocity1 = horizontal_distance
   def move(self,new):
      # moves the paddle such that paddle does not move outside the window
      # - self is the Paddle object
      speed = [1,1]
      #self.rect.move(speed)
      self.x = (self.x+self.horizontal_velocity)
      self.y = (self.y +self.vertical_velocity) 
      #print(self.vertical_velocity)
      #print(new[1])
      
      
      
      if self.rect.bottom >= self.surface.get_height() and self.vertical_velocity >0:
      
         self.vertical_velocity = -self.vertical_velocity
         
      if self.rect.top <= 0 and self.vertical_velocity <0:
         self.vertical_velocity = -self.vertical_velocity
         
      if self.rect.left < 0 and self.horizontal_velocity < 0 or self.rect.right > self.surface.get_width()-(new[1]/10) and self.horizontal_velocity > 0:
         self.horizontal_velocity = -self.horizontal_velocity
         
      
         
         
      
         
         
         
         
         
         
         
         
     
   def get_rect(self):
      return self.rect
   def collide(self,ball):
      if self.rect.collidepoint(ball):
         return True
   



class button:
   # An object in this class represents a Paddle that moves
   
   def __init__(self,x,y,width,height,color,surface,img,screen):
      # - self is the Paddle object
      # - x, y are the top left corner coordinates of the rectangle of type int
      # - width is the width of the rectangle of type int
      # - height is the heightof the rectangle of type int
      # - surface is the pygame.Surface object on which the rectangle is drawn
      self.i = pygame.image.load(img)
      self.img = pygame.image.load(img)
      self.screen = screen
      self.rect = self.img.get_rect()
      self.x = x
      self.y = y
      self.width = width
      self.height = height
      self.color = pygame.Color(color)
      self.surface = surface
      self.horizontal_velocity = random.randint(1,3)     # paddle is not moving at the start
      self.vertical_velocity = random.randint(1,3) 
      #self.set_horizontal_velocity(1)
   def draw(self,new):
      # -self is the Paddle object to draw
      #self.test = self.img.get_rect()
      #print(self.test)
      
      self.rect.update(self.x,self.y,self.width,self.height)
      #self.rect = pygame.Rect(new[0]-self.x,self.y,self.width,self.height)
      #pygame.draw.rect(self.surface,self.color,self.rect)
      #self.rect.move(self.x,self.y)
      self.screen.blit(self.i,self.rect)
   def move(self):
            # moves the paddle such that paddle does not move outside the window
            # - self is the Paddle object      
         pass
      
   
   def get_rect(self):
      return self.rect
   def collide(self,ball):
      if self.rect.collidepoint(ball):
         return True
   

main()