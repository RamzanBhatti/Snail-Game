import arcade



snail1 = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/snail.jpg")
snail2 = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/snail2.jpg")
back = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/game.jpg")
sp1 = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/download (1).png")
sp2 = arcade.load_texture("F:/1StudyData/5thSemester/AI/M.Ramzan_17 AI Lab4/AI/download (2).png")
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
MARGIN = 5
boxSize = SCREEN_HEIGHT // 10

class Game(arcade.View):
    def __init__(self):
        super().__init__()
        self.board = []
        self.human1 = 1
        self.Human2 = 2
        self.turn = "human1"
        self.win = "0"
        self.state = "GameMenu"
        self.Human2Score = 0
        self.human1Score = 0
        self.initilizeBoard(10, 10)


    #Function for initilization of backend 2D board array
    def initilizeBoard(self, rows, cols):
        for i in range(cols):
            tempBoard = []
            for i in range(0, rows):
                tempBoard.append(0)
            self.board.append(tempBoard)
        self.board[0][9] = 2
        self.board[9][0] = 1




    def on_key_press(self, key, modifiers):
        if self.state == "GameMenu":
            if key:
                self.human1 = 1
                self.Human2 = 2
                self.state = "GameOn"

    def on_show(self):
        arcade.set_background_color(arcade.color.RED_BROWN)
        arcade.set_background_color(arcade.color.RED_BROWN)

    def draw_horizental(self, grid_size, box_size, pixel):
        temp = box_size
        for i in range(1, grid_size):
            arcade.draw_line(0, box_size, (box_size*grid_size), box_size,  arcade.color.BLACK, pixel)
            box_size = box_size + temp 


    def draw_vertical(self, grid_size, box_size, pixel):
        temp = box_size
        for i in range(1, grid_size):
            arcade.draw_line(box_size, 0, box_size, (box_size*grid_size),  arcade.color.BLACK, pixel)
            box_size = box_size + temp 

    #Evaluation Function
    def evalBoard(self):
            count , count1 = 0, 0
            for check1 in range(10):
                for check in range(0,10):
                    if self.board[check1][check] == 1:
                        count += 1
                    elif self.board[check1][check] == 2:
                        count1 += 1
            
            if count > count1:
                if self.human1 == 1:
                    self.win = "human1"
                else:
                    self.win = "Human2"
            elif count1 > count:
                if self.human1 == 2:
                    self.win = "human1"
                else:
                    self.win = "Human2  "

            elif all(self.board):
                self.win = "draw"

            if self.win != "0":
                self.state = "GameOver"

    #Function to reset the values to the default
    def reset(self):
            self.board = []
            self.human1 = 1
            self.Human2 = 2
            self.turn = "human1"
            self.win = "0"
            self.state = "GameMenu"
            self.Human2Score = 0
            self.human1Score = 0
            self.initilizeBoard(10, 10) 

    def on_draw(self):
        arcade.start_render()
        if self.state == "GameMenu":
            arcade.draw_text("Welcome to Lazy Snails Game ", 100, 300, arcade.color.WHITE, font_size=50)
            arcade.draw_text("Press any key to continue", 480, 250, arcade.color.WHITE, font_size=30, anchor_x="center")
            self.__init__()

        elif self.state == "GameOn":
            arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,back)

            self.draw_horizental(10, boxSize, 4)
            self.draw_vertical(10, boxSize, 4)
            arcade.draw_lrwh_rectangle_textured(600, 0,1000, SCREEN_HEIGHT,back)
            

            arcade.draw_rectangle_filled(820, 535, 330,55, arcade.color.BEAU_BLUE)
            arcade.draw_rectangle_filled(770, 430, 230,55, arcade.color.BEAU_BLUE)
            arcade.draw_rectangle_filled(780, 370, 250,55, arcade.color.BEAU_BLUE)
            arcade.draw_rectangle_filled(780, 310, 250,55, arcade.color.BEAU_BLUE)
            arcade.draw_text("Lazy Snails Game", 670, 515, arcade.color.AMARANTH_PURPLE, font_size=25)
            arcade.draw_text(self.turn + " Turn", 660, 415, arcade.color.AMARANTH_PURPLE, font_size=25)
            arcade.draw_text("Human 1 Score = " + str(self.human1Score), 660, 350, arcade.color.AMARANTH_PURPLE, font_size=25)
            arcade.draw_text("Human 2 Score = " + str(self.Human2Score), 660, 300, arcade.color.AMARANTH_PURPLE, font_size=25)

            Y = boxSize
            temp = 0
            #print(self.board)
            for row in range (0, len(self.board)):
                X = 0
                for col in range (0, len(self.board)):
                    if self.board[row][col] == 1 : #Human1 snail
                        arcade.draw_lrwh_rectangle_textured( X+MARGIN, SCREEN_HEIGHT-Y, boxSize-MARGIN, boxSize-MARGIN, snail1)
                    
                    elif self.board[row][col] == 2 : #Human2 snail
                        arcade.draw_lrwh_rectangle_textured( X+MARGIN, SCREEN_HEIGHT-Y, boxSize-MARGIN, boxSize-MARGIN, snail2)
                    
                    elif self.board[row][col] == 11 : #Human snail
                        arcade.draw_lrwh_rectangle_textured( X+MARGIN, SCREEN_HEIGHT-Y, boxSize-MARGIN, boxSize-MARGIN, sp1)
                    
                    elif self.board[row][col] == 22 : #Human2 snail
                        arcade.draw_lrwh_rectangle_textured( X+MARGIN, SCREEN_HEIGHT-Y, boxSize-MARGIN, boxSize-MARGIN, sp2)
                    
                    X += boxSize
                temp += 1
                Y += boxSize
                

        elif self.state == "GameOver":

            if self.human1Score > self.Human2Score:
                self.win = "human1"
            elif self.human1Score < self.Human2Score:
                self.win = "Human2"
            else:
                self.win = "draw"

            if self.win == "human1":
                arcade.draw_text("Congratulations, Human 1 Wins !", 100, 300, arcade.color.WHITE, font_size=50)
                arcade.draw_text("Click to continue", 480, 250, arcade.color.WHITE, font_size=30, anchor_x="center")
               # self.__init__()
               # self.reset()
                #self.state = "GameMenu"

            elif self.win == "Human2":
                arcade.draw_text("congratulation Human 2 wins :)", 100, 300, arcade.color.WHITE, font_size=50)
                arcade.draw_text("Click to continue", 480, 250, arcade.color.WHITE, font_size=30, anchor_x="center")
               # self.__init__()
                #self.reset()
               # self.state = "GameMenu"

            elif self.win == "draw":
                arcade.draw_text("It's a draw..", 350, 300, arcade.color.WHITE, font_size=50)
                arcade.draw_text("Click to continue", 480, 250, arcade.color.WHITE, font_size=30, anchor_x="center")
              # self.__init__()
              # self.reset()
              # self.state = "GameMenu"


    #Slipping Functions
    def LSlip(self, Player):
        if Player == 2:
            x, y = self.getHuman2Position()
            x1, y1 = x, y
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 22 or self.board[x][y] == 2:
                    self.board[x1][y1] = 11
                    self.board[x][y+1] = 1
                    self.turn = "human1"
                    break
                elif y == 0:
                    self.board[x1][y1] = 11
                    self.board[x][y] = 1
                    self.turn = "human1"
                    break
                else:
                    y = y-1
        elif Player == 1:
            x, y = self.gethuman1Position()
            x1, y1 = x, y
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 11 or self.board[x][y] == 1:
                    self.board[x1][y1] = 22
                    self.board[x][y+1] = 2
                    self.turn = "Human2"
                    break
                elif y == 0:
                    self.board[x1][y1] = 22
                    self.board[x][y] = 2
                    self.turn = "Human2"
                    break
                else:
                    y = y-1


    def RSlip(self, Player):
        if Player == 2:
            x, y = self.getHuman2Position()
            x1, y1 = x, y
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 22 or self.board[x][y] == 2:
                    self.board[x1][y1] = 11
                    self.board[x][y-1] = 1
                    self.turn = "human1"
                    break
                elif y == 9:
                    self.board[x1][y1] = 11
                    self.board[x][y] = 1
                    self.turn = "human1"
                    break
                else:
                    y = y+1
        elif Player == 1:
            x, y = self.gethuman1Position()
            x1, y1 = x, y
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 11 or self.board[x][y] == 1:
                    self.board[x1][y1] = 22
                    self.board[x][y-1] = 2
                    self.turn = "Human2"
                    break
                elif y == 9:
                    self.board[x1][y1] = 22
                    self.board[x][y] = 2
                    self.turn = "Human2"
                    break
                else:
                    y = y+1

    def DownSlip(self, Player):
        if Player == 2:
            x, y = self.getHuman2Position()
            x1, y1 = x, y
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 22 or self.board[x][y] == 2:
                    self.board[x1][y1] = 11
                    self.board[x-1][y] = 1
                    self.turn = "human1"
                    break
                elif x == 9:
                    self.board[x1][y1] = 11
                    self.board[x][y] = 1
                    self.turn = "human1"
                    break
                else:
                    x = x+1
        elif Player == 1:
            x, y = self.gethuman1Position()
            x1, y1 = x, y
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 11 or self.board[x][y] == 1:
                    self.board[x1][y1] = 22
                    self.board[x-1][y] = 2
                    self.turn = "Human2"
                    break
                elif x == 9:
                    self.board[x1][y1] = 22
                    self.board[x][y] = 2
                    self.turn = "Human2"
                    break
                else:
                    x = x+1
    def UPSlip(self, Player):
        if Player == 2:
            x, y = self.getHuman2Position()
            x1, y1 = x, y
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 22 or self.board[x][y] == 2:
                    self.board[x1][y1] = 11
                    self.board[x+1][y] = 1
                    self.turn = "human1"
                    break
                elif x == 0:
                    self.board[x1][y1] = 11
                    self.board[x][y] = 1
                    self.turn = "human1"
                    break
                else:
                    x = x-1
        elif Player == 1:
            x, y = self.gethuman1Position()
            x1, y1 = x, y
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 11 or self.board[x][y] == 1:
                    self.board[x1][y1] = 22
                    self.board[x+1][y] = 2
                    self.turn = "Human2"
                    break
                elif x == 0:
                    self.board[x1][y1] = 22
                    self.board[x][y] = 2
                    self.turn = "Human2"
                    break
                else:
                    x = x-1

##############################################
####### RETURN THE INDEX VALUE OF 2D BACK-END
####### BOARD ACCORDING TO X,Y VALUES
##############################################

    def calcRowCol(self, x, y):
        x1 = y // boxSize
        y1 = x // boxSize
        return 9-x1, y1



    #To check the validity of the code
    def checkValidClick(self, x, y):
        if 0 <= x <= SCREEN_WIDTH and 0 <= y <= SCREEN_HEIGHT:
            return True
        elif 0 > x > SCREEN_WIDTH and 0 > y > SCREEN_HEIGHT:
            return False


    #Functions to get the positions where we are currently standing
    def gethuman1Position(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if self.board[i][j] == 2:
                    return i,j


    def getHuman2Position(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if self.board[i][j] == 1:
                    return i,j


    def on_mouse_press(self, x, y, _button, _modifiers):
        if self.state == "GameOn":
            row, col = self.calcRowCol(x,y)
            print(row , col)
            if self.checkValidClick(x, y):
                # Now check weather the clicked space is next to the Position of player
                if self.turn == "human1":
                    
                    x,y = self.gethuman1Position()

                    if   row==x and y+1==col and self.board[row][col]==0 or self.board[row][col] == 22 and row==x and y+1==col: #Right Move
                        if self.board[row][col] == 22:
                            self.RSlip(1)
                        else:
                            self.board[row][col], self.board[x][y] = 2, 22
                            self.turn = "Human2"
                            self.human1Score += 1
                    elif row==x and y-1==col and self.board[row][col]==0 or self.board[row][col] == 22 and row==x and y-1==col: #Left Move
                        if self.board[row][col] == 22:
                            self.LSlip(1)
                        else:
                            self.board[row][col], self.board[x][y] = 2, 22
                            self.turn = "Human2"
                            self.human1Score += 1
                    elif x+1==row and y==col and self.board[row][col]==0 or self.board[row][col] == 22 and x+1==row and y==col: #down Move
                        print("check")
                        if self.board[row][col]==22:
                            self.DownSlip(1)
                        else:
                            self.board[row][col], self.board[x][y] = 2, 22
                            self.turn = "Human2"
                            self.human1Score += 1
                    elif x-1==row and y==col and self.board[row][col]==0 or self.board[row][col]==22 and x-1==row and y==col: #Up Move
                        if self.board[row][col]==22:
                            self.UPSlip(1)
                        else:
                            self.board[row][col], self.board[x][y] = 2, 22
                            self.turn = "Human2"
                            self.human1Score += 1
                    else:
                        self.turn = "Human2"
                        print("INVALID CLICK, human1 TURN LOST !!!!")

                elif self.turn == "Human2":
                    
                    x, y = self.getHuman2Position()
                    
                    if   row==x and y+1==col and self.board[row][col]==0 or self.board[row][col] == 11 and  row==x and y+1==col: #Right Move
                        if self.board[row][col] == 11:
                            self.RSlip(2)
                        else:
                            self.board[row][col], self.board[x][y] = 1, 11
                            self.turn = "human1"
                            self.Human2Score += 1
                    elif row==x and y-1==col and self.board[row][col]==0 or self.board[row][col] == 11 and row==x and y-1==col: #Left Move
                        if self.board[row][col] == 11:
                            self.LSlip(2)
                        else:
                            self.board[row][col], self.board[x][y] = 1, 11
                            self.turn = "human1"
                            self.Human2Score += 1
                    elif x+1==row and y==col and self.board[row][col]==0 or self.board[row][col] == 11 and x+1==row and y==col: #Up Move
                        if self.board[row][col] == 11:
                            self.DownSlip(2)
                        else:
                            self.board[row][col], self.board[x][y] = 1, 11
                            self.turn = "human1"
                            self.Human2Score += 1
                    elif x-1==row and y==col and self.board[row][col]==0 or self.board[row][col]==11 and x-1==row and y==col: #Down Move
                        if self.board[row][col]==11:
                            self.UPSlip(2)
                        else:
                            self.board[row][col], self.board[x][y] = 1, 11
                            self.turn = "human1"
                            self.Human2Score += 1
                    else:
                        self.turn = "human1"
                        print("INVALID CLICK, Human2 TURN LOST !!!!")
                self.score()
            

        elif self.state == "GameOver":
            self.board = []
            self.human1 = 1
            self.Human2 = 2
            self.turn = "human1"
            self.win = "0"
            self.state = "GameMenu"

    def score(self):
        print(self.human1Score)
        print(self.Human2Score)

        if self.human1Score > 49 or self.Human2Score > 49:
            self.state = "GameOver"
            if self.human1Score > self.Human2Score:
                self.win = "human1"
            elif self.human1Score < self.Human2Score:
                self.win = "Human2"
        elif self.human1Score == 49 and self.Human2Score == 49:
            self.state = "GameOver"
            self.win = "draw"
         
            

if __name__ == "__main__":
    window = arcade.Window(SCREEN_HEIGHT+400, SCREEN_WIDTH, "SNAILS GAME")
    game_view = Game()
    window.show_view(game_view)
    arcade.run()