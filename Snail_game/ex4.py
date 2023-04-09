
import arcade

# Set how many rows and columns we will have
ROW_COUNT = 8
COLUMN_COUNT = 8
WIDTH = 80
HEIGHT = 80

MARGIN = 5
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Array Backed Grid Example"

SPRITE_SCALING_PLAYER = 0.5

player1 = []
player2 = []

class Player(arcade.Sprite):
    """ Player Class """

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1
            
class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  
        print(self.grid)
                        
        self.player_list = []
        self.player_splash = []
        self.player_sprite = None
        arcade.set_background_color(arcade.color.BLACK)
    
    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_splash = arcade.SpriteList()
        
        self.turn = 0

        self.player_sprite1 = Player("F:/1StudyData/5thSemester/AI/M.Ramzan AI Lab4/resources/images/snail.jpg", 0.1)
        self.player_sprite1.center_x = 45
        self.player_sprite1.center_y = 45
        self.player_list.append(self.player_sprite1)
        
        self.player_sprite2 = Player("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/How-to-Draw-a-Snail-.webp", 0.07)
        self.player_sprite2.center_x = 640
        self.player_sprite2.center_y = 640
        self.player_list.append(self.player_sprite2)
            
    def on_draw(self):
        self.clear()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    # self.grid[row+1][column]
                    # color = arcade.color.GREEN
                    pass
                else:
                    # color = arcade.color.WHITE
                    pass
                color = arcade.color.WHITE
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)
                
        self.player_list.draw()
        
    def on_key_press(self, key, modifiers):

        if self.turn == 0:
            self.player_sprite = self.player_list[0]
            self.turn = 1
        else:
            self.player_sprite = self.player_list[1]
            self.turn = 0
    
        x = 2* ((WIDTH // 2) +MARGIN)
        y = 2* ((HEIGHT // 2) + MARGIN)
        
        if key == arcade.key.UP:  
            if self.player_sprite.center_y < SCREEN_HEIGHT - 45:

                self.player_sprite.center_y =  (y + self.player_sprite.center_y) - MARGIN
                t1,t2 = self.player_sprite.center_x,self.player_sprite.center_y
                t1 ,t2 = t1 // (WIDTH+MARGIN),t2 // (HEIGHT+MARGIN)
                self.grid[t1][t2] = 1
                print(self.grid)
                coordinate = [t1,t2]
                if self.turn == 0:
                        player1.append(coordinate)
                        self.splash(self.turn,coordinate)
                        print("Score of player 1 is: ",len(player1))
                else:
                        player2.append(coordinate)
                        self.splash(self.turn,coordinate)
                        print("Score of player 2 is: ",len(player2))

        elif key == arcade.key.DOWN:
            if self.player_sprite.center_y > 45:
               
                    self.player_sprite.center_y = (self.player_sprite.center_y - y + MARGIN)
                    t1,t2 = self.player_sprite.center_x,self.player_sprite.center_y
                    t1 ,t2 = t1 // (WIDTH+MARGIN),t2 // (HEIGHT+MARGIN)
                    self.grid[t1][t2] = 1
                    coordinate = [t1,t2]
                    if self.turn == 0:
                                player1.append(coordinate)
                                print("Score of player 1 is: ",len(player1))
                            
                    else:
                    
                                player2.append(coordinate)
                                print("Score of player 2 is: ",len(player2))
                        
                            
               
        elif key == arcade.key.LEFT:
            if self.player_sprite.center_x > 45:
                
                    self.player_sprite.center_x = (self.player_sprite.center_x - x + MARGIN)
                    t1,t2 = self.player_sprite.center_x,self.player_sprite.center_y
                    t1 ,t2 = t1 // (WIDTH+MARGIN),t2 // (HEIGHT+MARGIN)
                    self.grid[t1][t2] = 1
                    coordinate = [t1,t2]
        
                    # print(coordinate)
                    if self.turn == 0:
   
                                # self.splash(self.turn,coordinate)
                                player1.append(coordinate)
                                print("Score of player 1 is: ",len(player1))
                         
                    else:
                      
                                player2.append(coordinate)
                                print("Score of player 2 is: ",len(player2))
                         
                        
        elif key == arcade.key.RIGHT:
            
            if self.player_sprite.center_x < SCREEN_WIDTH-45:
                            self.player_sprite.center_x = (x + self.player_sprite.center_x) - MARGIN
                            t1,t2 = self.player_sprite.center_x,self.player_sprite.center_y
                            t1 ,t2 = t1 // (WIDTH+MARGIN),t2 // (HEIGHT+MARGIN)
                            self.grid[t1][t2] = 1
                            coordinate = [t1,t2]
                            # print(coordinate)
                            if self.turn == 0:
                
                                        # self.splash(self.turn,coordinate)
                                        player1.append(coordinate)
                                        print("Score of player 1 is: ",len(player1))
                            
                            else:
                            
                                    # self.splash(self.turn,coordinate)
                                    player2.append(coordinate)
                                    print("Score of player 2 is: ",len(player2))
                        
                    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
            
    def splash(self,player,coordinate):
        x1 = coordinate[0]*(HEIGHT+MARGIN) + 45
        y1 = coordinate[1]*(HEIGHT+MARGIN) + 45
        if player == 0:
            self.player_sprite = Player("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/download (1).png", 0.2)
            self.player_sprite.center_x = x1 
            self.player_sprite.center_y = y1
            self.player_list.append(self.player_sprite)
        else:
            self.player_sprite = Player("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/download (2).png", 0.2)
            self.player_sprite.center_x = x1 
            self.player_sprite.center_y = y1 
            self.player_list.append(self.player_sprite)
            
            
    def on_update(self, delta_time):
        self.player_list.update()
        
def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    game.run()


if __name__ == "__main__":
    main()
    
    
    