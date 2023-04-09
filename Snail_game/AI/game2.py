

from logging import exception
from PIL.Image import FLIP_LEFT_RIGHT
import arcade
import os
import random
import math
from arcade import color
from arcade.texture import cleanup_texture_cache, load_texture

# constants here
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
GAME_SCREEN_TITLE = "Snails Game"
SIZE_OF_GRID= 10
CELL_SIZE = math.ceil(SCREEN_HEIGHT - 200) / SIZE_OF_GRID
MARGIN = 100


# section for defining class

"""
Welcome Screen View Here
"""

class WelcomeView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show(self):
        play_btn = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/playBTN.png")
        arcade.set_background_color(arcade.color.ALABAMA_CRIMSON)
    def on_draw(self):
        play_btn = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/playBTN.png")
        wlcm_scr_bkgd = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/welcome.jpg")
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
        0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
        wlcm_scr_bkgd
        )
        arcade.draw_lrwh_rectangle_textured(
            326, 320,
            130, 130,
            play_btn
        )
        arcade.draw_text(
            "Pic Credits: stream.com/",
            0, 790, color=arcade.color.BLACK,
            font_size=9, bold="true",
        )
    # def setup(self):
    #     """ setup window """
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if ( x > 326 and x < 456 and y > 320 and y < 450 ):
                welcome_done = InstructionWindow()
                self.window.show_view(welcome_done) 

class InstructionWindow(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ALMOND)
    def on_draw(self):
        instr_bkg = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/instrSCR.png")
        start_btn = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/startBTN.png")
        exit_btn = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/exitBTN.png")
        guide_btn = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/guideBTN.png")
        welcomePNG = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/welcome_PNG86.png")
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
        SCREEN_HEIGHT, SCREEN_WIDTH, 
        instr_bkg
        )
        # welcome text
        """arcade.draw_text(
            "Welcome to Snails Game",
            start_x=210, start_y=649,
            color=arcade.color.WHITE,
            font_size=20, font_name='Chilanka',
            bold='TRUE'
        )"""
        arcade.draw_lrwh_rectangle_textured(160, 580, 500, 200, welcomePNG)
        arcade.draw_lrwh_rectangle_textured(229, 410, MARGIN, MARGIN, start_btn)
        arcade.draw_lrwh_rectangle_textured(500, 415, MARGIN, MARGIN, guide_btn)
        arcade.draw_lrwh_rectangle_textured(350, 210, MARGIN, MARGIN, exit_btn)
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if(x >=229 and x <= 329 and y >= 410 and y <= 510):
                # Start of Game View Here
               print("Play Button Pressed")
               start_game = MainGame()
               self.window.show_view(start_game)   
            if( x >= 500 and x <= 600 and y >= 410 and y <= 510):
                # Guide module or View Here
                print("Guide Button Pressed")
            if( x >= 350 and x <= 450 and y >= 210 and y <=310):
                # Exite Module here 
                print("Exit Button Pressed")
                exit(0)    
# main game class here
class MainGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.gameBoard = [[0]*10]*10
        self.playerTurn = "P1"
        self.score_player1 = 0
        self.score_player2 = 0
        self.initializeBoard()
        print(self.gameBoard)

    def on_show(self):
        arcade.set_background_color(arcade.color.ALMOND)
    def initializeBoard(self):
        
        self.gameBoard = [ [0]*10 for _ in range(10)]
        self.gameBoard[0][0] = 1
        self.gameBoard[9][9] = 2
    def initializeGrid(self):
        for i in range(SIZE_OF_GRID+1):
            #x-axis
            arcade.draw_line(MARGIN+CELL_SIZE*i, MARGIN, CELL_SIZE*i+MARGIN, SCREEN_HEIGHT - MARGIN, arcade.color.BUBBLES, 3)
            #y-axis
            arcade.draw_line(MARGIN, MARGIN+CELL_SIZE*i, SCREEN_WIDTH - MARGIN, CELL_SIZE*i+MARGIN, arcade.color.BUBBLES, 3)

    # def on_update():
    #     pass
        
    def on_draw(self):
        bkg_game = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/gameBKG.png")
        snail_p1 = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/snail1.jpg")
        snail_p2 = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/snail2.jpg")
        splash_p1 = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/splash1.png")
        splash_p2 = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/splash2.png")
        box1 = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/box1.png")
        box2 = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/box2.png")
        vrs = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/vrs.png")
        arcade.start_render()
        
        arcade.draw_lrwh_rectangle_textured(0, 0,
            SCREEN_WIDTH, SCREEN_HEIGHT ,
            bkg_game
        )
        self.initializeGrid()
        arcade.draw_lrwh_rectangle_textured(250, 670, 300, 160, vrs)
        arcade.draw_lrwh_rectangle_textured(0, 185, CELL_SIZE + 30, CELL_SIZE + 30, box1)
        arcade.draw_text("Score \nPlayer \nOne",10, 185+CELL_SIZE + 30, color=arcade.color.WHITE, font_size=20, align="left")
        arcade.draw_text("Score \nPlayer \nOne",10, 185+CELL_SIZE + 30, color=arcade.color.WHITE, font_size=20, align="left")
        arcade.draw_text("Score \nPlayer \nOne",10, 185+CELL_SIZE + 30, color=arcade.color.WHITE, font_size=20, align="left")
        arcade.draw_text("Score \nPlayer \nOne",10, 185+CELL_SIZE + 30, color=arcade.color.WHITE, font_size=20, align="left")
        arcade.draw_text("Score \nPlayer \nOne",10, 185+CELL_SIZE + 30, color=arcade.color.WHITE, font_size=20, align="left")

        arcade.draw_text(str(self.score_player1),20, 200, color=arcade.color.WHITE, font_size=40, align="center")
        #score box of 2nd player
        arcade.draw_lrwh_rectangle_textured(SCREEN_HEIGHT-MARGIN, SCREEN_HEIGHT-MARGIN-(CELL_SIZE*2)
                                            ,CELL_SIZE + 30, CELL_SIZE + 30, box2)
        arcade.draw_text("Score \nPlayer \nTwo",710, 700-MARGIN*2, color=arcade.color.WHITE, font_size=20, align="left")
        arcade.draw_text("Score \nPlayer \nTwo",710, 700-MARGIN*2, color=arcade.color.WHITE, font_size=20, align="left")
        arcade.draw_text("Score \nPlayer \nTwo",710, 700-MARGIN*2, color=arcade.color.WHITE, font_size=20, align="left")
        arcade.draw_text("Score \nPlayer \nTwo",710, 700-MARGIN*2, color=arcade.color.WHITE, font_size=20, align="left")
        arcade.draw_text("Score \nPlayer \nTwo",710, 700-MARGIN*2, color=arcade.color.WHITE, font_size=20, align="left")
        arcade.draw_text(str(self.score_player2),710, SCREEN_HEIGHT - MARGIN*2, color=arcade.color.WHITE, font_size=40, align="center")
        arcade.draw_text(str(self.score_player2),710, SCREEN_HEIGHT - MARGIN*2, color=arcade.color.WHITE, font_size=40, align="center")

        # arcade.draw_text(str(self.score_player1),20, 200, color=arcade.color.WHITE, font_size=40, align="center")                                    
        for rowLoop in range(SIZE_OF_GRID):
            # print(self.gameBoard)
            start_x = 0
            start_y = 0
            snail_to_draw = None
            for colLoop in range(SIZE_OF_GRID):
                snail_to_draw = arcade.texture
                if ( self.gameBoard[rowLoop][colLoop] == 1):
                    snail_to_draw = snail_p1
                    start_x = (colLoop * CELL_SIZE) + MARGIN
                    start_y = (rowLoop * CELL_SIZE) + MARGIN       
                    arcade.draw_lrwh_rectangle_textured(start_x, start_y, CELL_SIZE, CELL_SIZE, snail_to_draw)
                elif ( self.gameBoard[rowLoop][colLoop] == 2):
                    snail_to_draw = snail_p2
                    start_x = (colLoop * CELL_SIZE) + MARGIN
                    start_y = (rowLoop * CELL_SIZE) + MARGIN    
                    # print(self.gameBoard[rowLoop][colLoop])   
                    arcade.draw_lrwh_rectangle_textured(start_x, start_y, CELL_SIZE, CELL_SIZE, snail_to_draw)
                    # self.gameBoard[rowLoop][colLoop] = -2
                elif ( self.gameBoard[rowLoop][colLoop] == -1):
                    snail_to_draw = snail_p2
                    start_x = (colLoop * CELL_SIZE) + MARGIN
                    start_y = (rowLoop * CELL_SIZE) + MARGIN    
                    # print(self.gameBoard[rowLoop][colLoop])   
                    arcade.draw_lrwh_rectangle_textured(start_x, start_y, CELL_SIZE, CELL_SIZE, splash_p1)
                elif ( self.gameBoard[rowLoop][colLoop] == -2):
                    snail_to_draw = snail_p2
                    start_x = (colLoop * CELL_SIZE) + MARGIN
                    start_y = (rowLoop * CELL_SIZE) + MARGIN    
                    # print(self.gameBoard[rowLoop][colLoop])   
                    arcade.draw_lrwh_rectangle_textured(start_x, start_y, CELL_SIZE, CELL_SIZE, splash_p2)


    def find_RowCol(self, x, y):
        column = int( (x - MARGIN) // CELL_SIZE )
        row = int( (y - MARGIN) // CELL_SIZE )
        return row, column
    def getPlayerLocation(self,playerName):
        player1Location = None
        player2Location = None
        for i in range(SIZE_OF_GRID):
            for j in range(SIZE_OF_GRID):
                if self.gameBoard[i][j] == 1:
                    player1Location = [i,j]
                elif self.gameBoard[i][j] == 2:
                    player2Location = [i,j]                        

        if playerName == "P1":
            return player1Location[0], player1Location[1]
        if playerName == "P1":
            return player2Location[0], player2Location[1]    

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if(x>=MARGIN and x <= SCREEN_WIDTH - MARGIN and y >= MARGIN and y <= SCREEN_HEIGHT - MARGIN):
            if (button == arcade.MOUSE_BUTTON_LEFT):
                row, column = self.find_RowCol(x, y)
                if self.playerTurn == "P1":
                    if self.evaluateMove(row, column):
                        self.gameBoard[row][column] = 1
                        self.score_player1 += 1
                    self.playerTurn = "P2"
                elif self.playerTurn ==  "P2":
                    # print(row, column)
                    if self.evaluateMove(row, column):
                        self.gameBoard[row][column] = 2
                        self.score_player2 += 1
                    self.playerTurn = "P1"  
        else:
            if self.playerTurn == "P1":
                self.playerTurn = "P2"
            elif self.playerTurn == "P2":
                self.playerTurn = "P1"
            else:
                raise exception("Invalid Turn")

    def evaluateMove(self, row, column):
       #condions for Player -1 
        if self.playerTurn == "P1":
            if (self.gameBoard[row - 1][column] == 1 or self.gameBoard[row][column - 1] == 1) and (self.gameBoard[row][column] == 0):
                if self.gameBoard[row - 1][column] == 1:
                    self.gameBoard[row - 1][column] = -1
                else:
                    self.gameBoard[row][column - 1] = -1    
                return True
            elif row + 1 < SIZE_OF_GRID and column + 1 < SIZE_OF_GRID:    
                if (self.gameBoard[row + 1][column] == 1 or self.gameBoard[row][column + 1] == 1) and (self.gameBoard[row][column] == 0):
                    if self.gameBoard[row +1][column] == 1:
                        self.gameBoard[row + 1][column] = -1
                    else:
                        self.gameBoard[row][column + 1] = -1    
                    return True
            elif (self.gameBoard[row][column] == -1):
                if self.gameBoard[row - 1][column] == 1:
                    iteri = row
                    while(iteri < SIZE_OF_GRID):
                        if(self.gameBoard[iteri + 1][column] == 0):
                            self.gameBoard[iteri][column] = 1
                            self.gameBoard[row - 1][column] = -1
                            return False
                        iteri = iteri + 1
                elif self.gameBoard[row + 1][column] == 1:
                    iteri = row
                    while(iteri >= 0):
                        if(self.gameBoard[iteri - 1][column] == 0):
                            self.gameBoard[iteri][column] = 1
                            self.gameBoard[row + 1][column] = -1
                            return False
                        iteri = iteri - 1
                elif self.gameBoard[row ][column - 1] == 1:
                    iteri = column
                    while(iteri < SIZE_OF_GRID):
                        if(self.gameBoard[row][iteri + 1] == 0):
                            self.gameBoard[row][iteri] = 1
                            self.gameBoard[row][column - 1] = -1
                            return False
                        iteri = iteri + 1
                elif self.gameBoard[row][column + 1] == 1:
                    iteri = column
                    while(iteri >= 0):
                        if(self.gameBoard[row][iteri - 1] == 0):
                            self.gameBoard[row][iteri] = 1
                            self.gameBoard[row][column + 1] = -1
                            return False
                        iteri = iteri - 1                     
                else:
                    return False
            return False
       #Conditionns for Player 2     
        if self.playerTurn == "P2":
            print(self.gameBoard[row][column])
            if (self.gameBoard[row - 1][column] == 2 or self.gameBoard[row][column - 1] == 2) and (self.gameBoard[row][column] == 0):
                if self.gameBoard[row - 1][column] == 2:
                    self.gameBoard[row - 1][column] = -2
                else:
                    self.gameBoard[row][column - 1] = -2    
                return True
            elif (row + 1 <= SIZE_OF_GRID -1) and (column + 1 <= SIZE_OF_GRID -1):
                if (self.gameBoard[row + 1][column] == 2 or self.gameBoard[row][column + 1] == 2) and (self.gameBoard[row][column] == 0):
                    if self.gameBoard[row +1][column] == 2:
                        self.gameBoard[row + 1][column] = -2
                    else:
                        self.gameBoard[row][column + 1] = -2    
                    return True
            elif (row + 1 <= SIZE_OF_GRID -1) and (column + 1 >= SIZE_OF_GRID):
                if (self.gameBoard[row + 1][column] == 2) and self.gameBoard[row][column] == 0:
                    self.gameBoard[row + 1][column] = -2
                    return True 
            elif (column + 1 <= SIZE_OF_GRID -1) and (row + 1 >= SIZE_OF_GRID):
                if (self.gameBoard[row][column + 1] == 2) and self.gameBoard[row][column] == 0:
                    self.gameBoard[row][column + 1] = -2
                    return True                
            if (self.gameBoard[row][column] == -2):
                print("entered here")
                if self.gameBoard[row - 1][column] == 2:
                    iteri = row
                    while(iteri < SIZE_OF_GRID):
                        if(self.gameBoard[iteri + 1][column] == 0):
                            self.gameBoard[iteri][column] = 2
                            self.gameBoard[row - 1][column] = -2
                            return False
                        iteri = iteri + 1
                elif self.gameBoard[row + 1][column] == 2:
                    iteri = row
                    while(iteri >= 0):
                        if(self.gameBoard[iteri - 1][column] == 0):
                            self.gameBoard[iteri][column] = 2
                            self.gameBoard[row + 1][column] = -2
                            return False
                        iteri = iteri - 1
                elif self.gameBoard[row ][column - 1] == 2:
                    iteri = column
                    while(iteri < SIZE_OF_GRID):
                        if(self.gameBoard[row][iteri + 1] == 0):
                            self.gameBoard[row][iteri] = 2
                            self.gameBoard[row][column - 1] = -2
                            return False
                        iteri = iteri + 1
                elif self.gameBoard[row][column + 1] == 2:
                    iteri = column
                    while(iteri >= 0):
                        if(self.gameBoard[row][iteri - 1] == 0):
                            self.gameBoard[row][iteri] = 2
                            self.gameBoard[row][column + 1] = -2
                            return False
                        iteri = iteri - 1                     
                else:
                    return False

            return False                 


#end of classes section

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_SCREEN_TITLE)
    welcome_view = MainGame()
    window.show_view(welcome_view)
    arcade.run()


if __name__ == "__main__":
    main()
