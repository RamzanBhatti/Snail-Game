
import arcade

# Set how many rows and columns we will have

ROW_COUNT = 8
COLUMN_COUNT = 8
WIDTH = 80
HEIGHT = 80

MARGIN = 5
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
# print(SCREEN_WIDTH)
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Array Backed Grid Example"

SPRITE_SCALING_PLAYER = 0.5

player1 = []
player2 = []


class InstructionView(arcade.View):
    
    
    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.color.BLACK)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
        
    def on_draw(self):
        arcade.start_render()
        # arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/Code/welcome.jpg")
        arcade.draw_text("Instructions Screen", self.window.width/2, self.window.height/1.1,
                         arcade.color.WHITE, font_size=25, anchor_x="center")  
                
        arcade.draw_text("1: First turn will be of Player1.", self.window.width/7.4, self.window.height/1.2,
                         arcade.color.WHITE, font_size=10, anchor_x="center")

        arcade.draw_text("2: Use left click of mouse to move sprite.", self.window.width/6, self.window.height/1.3,
                         arcade.color.WHITE, font_size=10, anchor_x="center")
        
        arcade.draw_text("3: Can only click on boxes adjacent to sprite.", self.window.width/5, self.window.height/1.4,
                         arcade.color.WHITE, font_size=10, anchor_x="center")

        arcade.draw_text("4: Clicking on wrong box, opponent splash or sprite will considered as foul.", self.window.width/3.6, self.window.height/1.53,
                         arcade.color.WHITE, font_size=10, anchor_x="center")

        arcade.draw_text("5: On foul turn will be lost.", self.window.width/8.5, self.window.height/1.65,
                         arcade.color.WHITE, font_size=10, anchor_x="center")         

        arcade.draw_text("6: That player will be the winner who got maximum splashes.", self.window.width/4, self.window.height/1.78,
                         arcade.color.WHITE, font_size=10, anchor_x="center")  
        
        arcade.draw_text("Click to Play :", self.window.width/2, self.window.height/2-75,
                         arcade.color.ORANGE_PEEL, font_size=25, anchor_x="center") 
        
    
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)
        
class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/game-over.jpg")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)
        

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
            
class MyGame(arcade.View):
    
    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()
    
    # def __init__(self, width, height, title):
    #     super().__init__(width, height, title)
    
        self.player_list = []
        self.player_splash = []
        self.player_sprite = None
        arcade.set_background_color(arcade.color.RED_DEVIL)
    
    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_splash = arcade.SpriteList()
        
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  
                
        # print(len(self.grid))
        
        self.turn = 0
        self.player_sprite1 = Player("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/snail2.jpg", 0.18)
        self.player_sprite1.center_x = 45
        self.player_sprite1.center_y = 45
        self.player_list.append(self.player_sprite1)
        
        self.player_sprite2 = Player("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/snail.jpg", 0.1)
        self.player_sprite2.center_x = 640
        self.player_sprite2.center_y = 640
        self.player_list.append(self.player_sprite2)
            
    def on_draw(self):
        self.clear()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    self.grid[row+1][column]
                else:
                    color = arcade.color.WHITE
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)
        
        arcade.draw_text("Lazy Snail Game",700, 630,arcade.color.WHITE,font_size=20)
        arcade.draw_text(" Snail 1 Score = " + str(len(player1)),690, 590,arcade.color.WHITE,font_size=20)
        arcade.draw_text(" Snail 2 Score = " + str(len(player2)),690, 550,arcade.color.WHITE,font_size=20)
        self.player_list.draw()
        
    def on_key_press(self, key, modifiers):
         
        if self.turn == 0:
            # if self.player_sprite.center_x < SCREEN_HEIGHT - 45 or self.player_sprite.center_y > 45 or self.player_sprite.center_x > 45 or self.player_sprite.center_x < SCREEN_WIDTH-45:
               self.player_sprite = self.player_list[1]
               self.turn = 1
            # else:
            #    self.turn = 0
        else:
            # if self.player_sprite.center_x < SCREEN_HEIGHT - 45 or self.player_sprite.center_y > 45 or self.player_sprite.center_x > 45 or self.player_sprite.center_x < SCREEN_WIDTH-45:
               self.player_sprite = self.player_list[0]
               self.turn = 0
            # else:
                # self.turn = 1
    
        x = 2* ((WIDTH // 2) +MARGIN)
        y = 2* ((HEIGHT // 2) + MARGIN)
        
        # if self.player_sprite.center_x < SCREEN_HEIGHT - 45 or self.player_sprite.center_y > 45 or self.player_sprite.center_x > 45 or self.player_sprite.center_x < SCREEN_WIDTH-45: 
        if key == arcade.key.UP:  
            if self.player_sprite.center_y < SCREEN_HEIGHT - 45:
                t1,t2 = self.player_sprite.center_x,self.player_sprite.center_y
                t3,t4 = self.player_sprite.center_x,(self.player_sprite.center_y + y)-MARGIN
                t1 ,t2 = int(t1 // (WIDTH+MARGIN)),int(t2 // (HEIGHT+MARGIN))
                current_coordinates = [t1,t2]
                t3 ,t4 = int(t3 // (WIDTH+MARGIN)),int(t4 // (HEIGHT+MARGIN))
                new_coordinates = [t3,t4]
                # self.grid.remove(self.grid[t1][t2])
                # print(self.grid)
                # print("previous current_coordinatess",current_coordinates)
                # print("new current_coordinatess",new_coordinates)
                if self.turn == 0:
                    if current_coordinates not in player1:
                        if new_coordinates not in player2:
                          if current_coordinates not in player2:
                                player1.append(current_coordinates)
                                
                                self.player_sprite.center_y =  (y + self.player_sprite.center_y) - MARGIN
                                print(player1)
                            #     self.player_sprite.center_y =  (y + self.player_sprite.center_y) - MARGIN
                                self.splash(self.turn,current_coordinates)
                                print("Score of player 1 is: ",len(player1))
                          else:
                                self.player_sprite.center_x,self.player_sprite.center_y = self.player_sprite.center_x,self.player_sprite.center_y
                                
                    else:
                        if new_coordinates not in player2:
                            self.player_sprite.center_x,self.player_sprite.center_y =  self.player_sprite.center_x,(self.player_sprite.center_y + y) - MARGIN
                else:
                        if current_coordinates not in player2:
                            if new_coordinates not in player1:
                              if current_coordinates not in player1:
                                    player2.append(current_coordinates)
                                    
                                    self.player_sprite.center_y =  (y + self.player_sprite.center_y) - MARGIN
                                    print(player2)
                                    #     self.player_sprite.center_y =  (y + self.player_sprite.center_y) - MARGIN
                                    self.splash(self.turn,current_coordinates)
                                    print("Score of player 2 is: ",len(player2))
                              else:
                                    self.player_sprite.center_x,self.player_sprite.center_y = self.player_sprite.center_x,self.player_sprite.center_y
                        else:
                            if new_coordinates not in player1:
                              self.player_sprite.center_x,self.player_sprite.center_y =  self.player_sprite.center_x,(self.player_sprite.center_y+y)-MARGIN
                        
        elif key == arcade.key.DOWN:
            if self.player_sprite.center_y > 45:
                t1,t2 = self.player_sprite.center_x,self.player_sprite.center_y
                t3,t4 = self.player_sprite.center_x,(self.player_sprite.center_y - y)+MARGIN
                print(t1,t2)
                t1 ,t2 = int(t1 // (WIDTH+MARGIN)),int(t2 // (HEIGHT+MARGIN))
                current_coordinates = [t1,t2]
                t3 ,t4 = int(t3 // (WIDTH+MARGIN)),int(t4 // (HEIGHT+MARGIN))
                new_coordinates = [t3,t4]
                # print(current_coordinates)
                if self.turn == 0:
                    if current_coordinates not in player1:
                        if new_coordinates not in player2:
                            if current_coordinates not in player2:
                                player1.append(current_coordinates)
                                print(player1)
                                self.player_sprite.center_y = (self.player_sprite.center_y - y + MARGIN)
                                self.splash(self.turn,current_coordinates)
                                print("Score of player 1 is: ",len(player1))
                            else:
                                self.player_sprite.center_y = self.player_sprite.center_y
                        
                    else:
                        if new_coordinates not in player2:
                           self.player_sprite.center_y = (self.player_sprite.center_y - y + MARGIN)
                else:
                    if current_coordinates not in player2:
                        if new_coordinates not in player1:
                            if current_coordinates not in player1:
                                player2.append(current_coordinates)
                                print(player2)
                                self.player_sprite.center_y = (self.player_sprite.center_y - y + MARGIN)
                                self.splash(self.turn,current_coordinates)
                                
                                print("Score of player 2 is: ",len(player2))
                            else:
                                self.player_sprite.center_y = self.player_sprite.center_y
                    else:
                        if new_coordinates not in player1:
                           self.player_sprite.center_y = (self.player_sprite.center_y - y + MARGIN)
                            
               
        elif key == arcade.key.LEFT:
            if self.player_sprite.center_x > 45:
                t1,t2 = self.player_sprite.center_x,self.player_sprite.center_y
                t3,t4 = self.player_sprite.center_x-x+MARGIN,self.player_sprite.center_y
                t1 ,t2 = int(t1 // (WIDTH+MARGIN)),int(t2 // (HEIGHT+MARGIN))
                current_coordinates = [t1,t2]
                t3 ,t4 = int(t3 // (WIDTH+MARGIN)),int(t4 // (HEIGHT+MARGIN))
                new_coordinates = [t3,t4]
                # print(current_coordinates)
                if self.turn == 0:
                    if current_coordinates not in player1:
                        if new_coordinates not in player2:
                            if current_coordinates not in player2:
                                player1.append(current_coordinates)
                                print(player1)
                                self.player_sprite.center_x = (self.player_sprite.center_x - x + MARGIN)
                                self.splash(self.turn,current_coordinates)
                                print("Score of player 1 is: ",len(player1))
                            else:
                                self.player_sprite.center_x = self.player_sprite.center_x
                    else:
                        if new_coordinates not in player2:
                            self.player_sprite.center_x = (self.player_sprite.center_x - x + MARGIN)
                else:
                    if current_coordinates not in player2:
                        if new_coordinates not in player1:
                            if current_coordinates not in player1:
                                player2.append(current_coordinates)
                                print(player2)
                                self.player_sprite.center_x = (self.player_sprite.center_x - x + MARGIN)
                                self.splash(self.turn,current_coordinates)
                                
                                print("Score of player 2 is: ",len(player2))
                            else:
                                self.player_sprite.center_x = self.player_sprite.center_x
                    else:
                        if new_coordinates not in player1:
                           self.player_sprite.center_x = (self.player_sprite.center_x - x + MARGIN)
                        
        elif key == arcade.key.RIGHT:
            if self.player_sprite.center_x < SCREEN_WIDTH-45:
                t1,t2 = self.player_sprite.center_x,self.player_sprite.center_y
                t3,t4 = self.player_sprite.center_x+x-MARGIN,self.player_sprite.center_y
                t1 ,t2 = int(t1 // (WIDTH+MARGIN)),int(t2 // (HEIGHT+MARGIN))
                current_coordinates = [t1,t2]
                t3 ,t4 = int(t3 // (WIDTH+MARGIN)),int(t4 // (HEIGHT+MARGIN))
                new_coordinates = [t3,t4]
                # print(current_coordinates)
                if self.turn == 0:
                    if current_coordinates not in player1:
                        if new_coordinates not in player2:
                            if current_coordinates not in player2:
                                player1.append(current_coordinates)
                                print(player1)
                                self.player_sprite.center_x = (x + self.player_sprite.center_x) - MARGIN
                                self.splash(self.turn,current_coordinates)
                                
                                print("Score of player 1 is: ",len(player1))
                            else:
                                self.player_sprite.center_x = self.player_sprite.center_x
                    else:
                        if new_coordinates not in player2:
                           self.player_sprite.center_x = (x + self.player_sprite.center_x) - MARGIN
                else:
                    if current_coordinates not in player2:
                        if new_coordinates not in player1:
                            if current_coordinates not in player1:
                                player2.append(current_coordinates)
                                print(player2)
                                self.player_sprite.center_x = (x + self.player_sprite.center_x) - MARGIN
                                self.splash(self.turn,current_coordinates)
                                
                                print("Score of player 2 is: ",len(player2))
                            else:
                                self.player_sprite.center_x = self.player_sprite.center_x
                    else:
                        if new_coordinates not in player1:
                           self.player_sprite.center_x = (x + self.player_sprite.center_x) - MARGIN
                
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
            
    def splash(self,player,current_coordinates):
                
        x1 = current_coordinates[0]*(HEIGHT+MARGIN) + 45
        y1 = current_coordinates[1]*(HEIGHT+MARGIN) + 45
        if player == 0:
            self.player_sprite = Player("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/download (1).png", 0.2)
            self.player_sprite.center_x = x1
            self.player_sprite.center_y = y1
            self.player_list.append(self.player_sprite)
        else:
            self.player_sprite = Player("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/download (2).png", 0.2)
            self.player_sprite.center_x = x1
            self.player_sprite.center_y = y1
            self.player_list.append(self.player_sprite)
            
    def on_update(self, delta_time):
        self.player_list.update()
        if len(player1) + len(player2) == 64:
            view = GameOverView()
            self.window.show_view(view)
        
def main():
    """ Main function """

    window = arcade.Window(SCREEN_WIDTH +300, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
    

        
    
    
    
    