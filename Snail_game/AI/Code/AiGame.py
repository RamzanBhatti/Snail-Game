from ctypes import memmove
import random
import arcade
from arcade import color
from arcade import application
from arcade.color import ALLOY_ORANGE, BLACK
import arcade.gui
import os
import copy
import math
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)
WIDTH = 1000
HEIGHT = 600
SCREEN_TITLE = "Happy Snailing"


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        # Creating a UI MANAGER to handle the UI
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable() 
        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()
        # Create the buttons  #Creating Button using UIFlatButton
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=30))
        instruction_button = arcade.gui.UIFlatButton(text="Instructions", width=200)
        self.v_box.add(instruction_button.with_space_around(bottom=30))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box.add(quit_button)

        start_button.on_click = self.on_start_button
        instruction_button.on_click = self.on_ins_button
        quit_button.on_click = self.on_quit_button
        self.uimanager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x",anchor_y="center_y",align_y=-50,child=self.v_box))
    def on_quit_button(self,event):
        arcade.exit()
    def on_ins_button(self,event):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)      
    def on_start_button(self,event):
        game_view = GameView()
        self.window.show_view(game_view)
    
    def on_show(self):
        arcade.set_background_color(arcade.color.WHEAT)
    def on_draw(self):
        arcade.start_render()
        t0 = arcade.load_texture("back.jpg")
        t1 = arcade.load_texture("name9.png")
        t2 = arcade.load_texture("new_hs.png")
        t3 = arcade.load_texture("slogo.png")
        arcade.draw_texture_rectangle(500,300,1000,600, t0,0,180)
        arcade.draw_texture_rectangle(500,500,600,150, t1,0,255)
        arcade.draw_texture_rectangle(100,520,230,140, t2,0,255)
        arcade.draw_texture_rectangle(900,500,250,250, t3,0,255)        

        self.uimanager.draw()
    # def on_mouse_press(self, _x, _y, _button, _modifiers):



class InstructionView(arcade.View):
    def __init__(self):
        super().__init__()
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable() 
        start_button = arcade.gui.UIFlatButton(text="Start  Game",width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(align_x=150,align_y=-220,
                child=start_button))
        back_button = arcade.gui.UIFlatButton(text="Back to Main Menu",width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(align_x=-150,align_y=-220,
                child=back_button))
        start_button.on_click = self.on_start_button
        back_button.on_click = self.on_back_button
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        tex0 = arcade.load_texture("instruction.jpg")
        tex1 = arcade.load_texture("cur1.png")
        tex2 = arcade.load_texture("cur2.png")
        # tex3 = arcade.load_texture("new_hs.png")
        # tex4 = arcade.load_texture("slogo.png")
        tex5 = arcade.load_texture("ins.png")
        arcade.draw_texture_rectangle(500,300,1000,600, tex0,0,210)
        arcade.draw_texture_rectangle(80,300,600,700, tex1,0,255)
        arcade.draw_texture_rectangle(920,300,600,700, tex2,0,255)
        # arcade.draw_texture_rectangle(100,520,230,140, tex3,0,255)
        # arcade.draw_texture_rectangle(900,500,250,250, tex4,0,255) 
        arcade.draw_texture_rectangle(500, 500,500,200,tex5,0,255)
        arcade.draw_text("~ This is Human VS Bot 2-player game.", 200, 350,arcade.color.YELLOW_ROSE,font_size=20)
        arcade.draw_text("~ For every turn, player has chance to score 1 point.", 200, 300,arcade.color.YELLOW_ROSE,font_size=20)
        arcade.draw_text("~ Score is count on the basis of number of splashes.", 200, 250,arcade.color.YELLOW_ROSE,font_size=20)
        arcade.draw_text("~ The player with more number of splashes wins.", 200, 200,arcade.color.YELLOW_ROSE,font_size=20)
        self.uimanager.draw()

    def on_start_button(self, event):
        game_view = GameView()
        self.window.show_view(game_view)
    def on_back_button(self, event):
        menu_view = MenuView()
        self.window.show_view(menu_view)


    # def on_mouse_press(self, _x, _y, _button, _modifiers):
    #     menu_view = MenuView()
    #     self.window.show_view(menu_view)
class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        
        arcade.set_background_color(arcade.color.WHEAT)
        self.grid = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2]]
        self.previous_turn = 0
        self.sprite = 1
        self.splash = 11
        self.turn_show = "Human"
        self.winner = ""
        self.p1_scores = []
        self.p2_scores = []
        
    def scores(self):
        p1 = 0
        p2 = 0
        for i in range(10):
            p1 += self.grid[i].count(11)
            p2 += self.grid[i].count(22)
        return p1, p2

    def on_draw(self):
        arcade.start_render()
        for x in range(50, 551, 50): 
            arcade.draw_line(x, 50, x, 550, arcade.color.BLACK, 2)
        for y in range(50, 551, 50):
            arcade.draw_line(50, y, 550, y, arcade.color.BLACK, 2)
        texture = arcade.load_texture("interface.jfif")
        texture1 = arcade.load_texture("s1.png")
        texture2 = arcade.load_texture("s2.png")
        texture3 = arcade.load_texture("s22.png")
        texture4 = arcade.load_texture("s11.png")
        texture5 = arcade.load_texture("logo1.png")
        texture6 = arcade.load_texture("img2.png")
        texture7 = arcade.load_texture("human.png")
        texture8 = arcade.load_texture("bot.png")
        arcade.draw_texture_rectangle(300,300,580,580, texture,0,160)
        arcade.draw_texture_rectangle(800,240,370,400,texture,0,160)
        arcade.draw_texture_rectangle(800,520,400,300, texture5,0,255)
        arcade.draw_text("Turn:",660,315, arcade.color.WHEAT,20,bold=1)
        arcade.draw_text(str(self.turn_show),760,315, arcade.color.WHEAT,27,bold=1)
        arcade.draw_text("Score",660,210, arcade.color.WHEAT,20,bold=1)
        arcade.draw_text("Score",660,90, arcade.color.WHEAT,20,bold=1)
        arcade.draw_texture_rectangle(805,390,330,110, texture6,0,255)
        arcade.draw_texture_rectangle(730,270,150,70, texture7,0,255)
        arcade.draw_texture_rectangle(720,150,110,70, texture8,0,255)
        p1,p2 = self.scores()
        arcade.draw_text(str(p1),805,210, arcade.color.WHEAT,23,bold=1)
        arcade.draw_text(str(p2),805,90, arcade.color.WHEAT,23,bold=1)
        arcade.draw_rectangle_outline(820,220,130,35,arcade.color.BLACK,2,0)
        arcade.draw_rectangle_outline(820,100,130,35,arcade.color.BLACK,2,0)
        for x in range(10):
            for y in range(10):
                if self.grid[y][x] == 1:
                    x_c, y_c = self.coordinates(x,y)
                    arcade.draw_texture_rectangle(x_c, y_c,50,50, texture2,0)   
                if self.grid[y][x] == 2:
                    x_c, y_c = self.coordinates(x,y)   
                    arcade.draw_texture_rectangle(x_c, y_c,50,50, texture1,0)
                if self.grid[y][x] == 11:
                    x_c, y_c = self.coordinates(x,y)
                    arcade.draw_texture_rectangle(x_c, y_c,50,50, texture3,0)   
                if self.grid[y][x] == 22:
                    x_c, y_c = self.coordinates(x,y)   
                    arcade.draw_texture_rectangle(x_c, y_c,50,50, texture4,0)

    def coordinates(self,x,y):
        X = 75
        Y = 75
        for i in range(75,((x*50)+76),50):
            for j in range(75,((y*50)+76),50):
                X=i
                Y=j
        return X, Y

    def curr_pos(self, player):
        for x in range(10):
            for y in range(10):
                if self.grid[y][x] == player:
                    curr_x = x
                    curr_y = y
        return curr_x,curr_y

    def isLegalMove(self, direction):
        curr_x,curr_y = self.curr_pos(self.sprite)
        if direction == "UP":
            if curr_y<9:
                if self.grid[curr_y+1][curr_x] == 0:
                    return True
                elif self.grid[curr_y+1][curr_x] == self.splash:
                    return 0
                else:
                    return False
            else:
                return False

        elif direction == "DOWN":
            if curr_y>0:
                if self.grid[curr_y-1][curr_x] == 0:
                    return True
                elif self.grid[curr_y-1][curr_x] == self.splash:
                    return 0
                else:
                    return False
            else:
                return False

        elif direction == "LEFT":
            if curr_x>0:
                if self.grid[curr_y][curr_x-1] == 0:
                    return True
                elif self.grid[curr_y][curr_x-1] == self.splash:
                    return 0
                else:
                    return False
            else:
                return False

        elif direction == "RIGHT":
            if curr_x<9:
                if self.grid[curr_y][curr_x+1] == 0:
                    return True
                elif self.grid[curr_y][curr_x+1] == self.splash:
                    return 0
                else:
                    return False
            else:
                return False
        
        else:
            return False


    def allowed_actions(self,location,board,turn):
        # It also uses possible_actions function
        # Returns List of possible moves for AI Agent
        if turn == 1:
            pos = copy.deepcopy(location)
            slime = 11
        else:
            pos = copy.deepcopy(location)
            slime = 22
        actions = self.check_possible_actions(list(pos))
        # print(actions)
        allowed = []
        slimed = []        
        for acts in actions:
            if board[acts[0]][acts[1]] == 0: 
                allowed.append(acts)
            elif board[acts[0]][acts[1]] == slime:
                slimed.append(acts)
        return allowed,slimed

    def findBestMove(self):

        copied_board = copy.deepcopy(self.grid)
        best_value = -10000

        
        bot_pos = self.current_position(copied_board, False)

        best_move = copy.deepcopy(bot_pos)

        zero_boxes, slipped_boxes = self.allowed_actions(bot_pos, copied_board, 0)
        bot_pos = copy.deepcopy(bot_pos)
        if len(zero_boxes) != 0:
            
            for x in zero_boxes:
                copied_board[x[0]][x[1]] = self.sprite
                prev_mov = copy.deepcopy(x)
                copied_board[bot_pos[0]][bot_pos[1]] = self.splash
                bot_pos[0] = x[0]
                bot_pos[1] = x[1]
                
                value = self.minimax(copied_board,0,8,True)
                
                copied_board[prev_mov[0]][prev_mov[1]] = 0
                copied_board[bot_pos[0]][bot_pos[1]] = self.sprite
                bot_pos = copy.deepcopy(bot_pos)
                if value >= best_value :
                    best_value = value
                    best_move[0] = x[0]
                    best_move[1] = x[1]

        

        # print(best_move)

        return best_move, False

    def current_position(self,board,human):
        if human:
            for x in range(len(board)):
                for y in range(len(board[x])):
                    if board[x][y] == 1:
                        return [x,y]
        else:
            for x in range(len(board)):
                for y in range(len(board[x])):
                    if board[x][y] == 2:
                        return [x,y]

    def on_key_press(self, key, modifiers):
        # print(self.grid[::-1])
        if self.evaluate_board():
            over = GameOver_View(self.winner)
            self.window.show_view(over)
        if key == arcade.key.UP or key == arcade.key.DOWN or key == arcade.key.LEFT or key == arcade.key.RIGHT:
            # if self.previous_turn == 0 or self.previous_turn == 1:
            self.sprite = 1
            self.splash = 11
                # self.previous_turn = 2


        curr_x,curr_y = self.curr_pos(self.sprite)
        # print(curr_x,curr_y)

        if self.sprite == 1:
            if key==arcade.key.UP:
                if self.isLegalMove("UP")==True:
                    self.grid[curr_y+1][curr_x] = self.sprite
                    self.grid[curr_y][curr_x] = self.splash
                elif self.isLegalMove("UP")==0:
                    self.slide("UP",True,0)

            elif key==arcade.key.DOWN:
                if self.isLegalMove("DOWN")==True:
                    self.grid[curr_y-1][curr_x] = self.sprite
                    self.grid[curr_y][curr_x] = self.splash
                elif self.isLegalMove("DOWN")==0:
                    self.slide("DOWN",True,0)
                
            elif key==arcade.key.LEFT:
                if self.isLegalMove("LEFT")==True:
                    self.grid[curr_y][curr_x-1] = self.sprite
                    self.grid[curr_y][curr_x] = self.splash
                elif self.isLegalMove("LEFT")==0:
                    self.slide("LEFT",True,0)
                
            elif key==arcade.key.RIGHT:
                if self.isLegalMove("RIGHT")==True:
                    self.grid[curr_y][curr_x+1] = self.sprite
                    self.grid[curr_y][curr_x] = self.splash
                elif self.isLegalMove("RIGHT")==0:
                    self.slide("RIGHT",True,0)
                curr_x,curr_y = self.curr_pos(self.sprite)
                # print(curr_x,curr_y)
                
                
            elif key == arcade.key.ESCAPE:
                pause = PauseView(self)
                self.window.show_view(pause)
            

            self.sprite = 2  
            self.splash = 22       
            legal_move, slipped_move = list(self.findBestMove())
            # print(legal_move)

            curr_x,curr_y = self.curr_pos(self.sprite)
            if slipped_move is False:  
                if legal_move[1] < curr_x and legal_move[0] == curr_y:
                    # if self.isLegalMove("LEFT")==True:
                    self.grid[curr_y][curr_x-1] = self.sprite
                    self.grid[curr_y][curr_x] = self.splash
                    # elif self.isLegalMove("LEFT")==0:
                    #     self.slide("LEFT",False,0)

                elif legal_move[1] == curr_x and legal_move[0] < curr_y:
                    # if self.isLegalMove("DOWN")==True:
                    self.grid[curr_y-1][curr_x] = self.sprite
                    self.grid[curr_y][curr_x] = self.splash
                    # elif self.isLegalMove("DOWN")==0:
                    #     self.slide("DOWN")
                
                elif legal_move[1] > curr_x and legal_move[0] == curr_y:
                    # if self.isLegalMove("RIGHT")==True:
                    self.grid[curr_y][curr_x+1] = self.sprite
                    self.grid[curr_y][curr_x] = self.splash
                    # elif self.isLegalMove("RIGHT")==0:
                    #     self.slide("RIGHT")
                elif legal_move[1] == curr_x and legal_move[0] > curr_y:
                    # if self.isLegalMove("UP")==True:
                    self.grid[curr_y+1][curr_x] = self.sprite
                    self.grid[curr_y][curr_x] = self.splash
                    # elif self.isLegalMove("UP")==0:
                    #     self.slide("UP")
            # print(slipped_move)
            # elif slipped_move:
            #     self.slide("UP",False,slipped_move)

    def slide(self, direction,turn,move):
        if turn:
            curr_x,curr_y = self.curr_pos(self.sprite)
            new_x = curr_x
            new_y = curr_y
            if direction=="RIGHT":
                while(new_x<9 and (self.grid[curr_y][new_x+1]==self.splash)):
                    new_x += 1
            
            if direction=="LEFT":
                while(new_x>0 and (self.grid[curr_y][new_x-1]==self.splash)):
                    new_x -= 1
            
            if direction=="UP":
                while(new_y<9 and (self.grid[new_y+1][curr_x]==self.splash)):
                    new_y += 1
            
            if direction=="DOWN":
                while(new_y>0 and (self.grid[new_y-1][curr_x]==self.splash)):
                    new_y -= 1

            self.grid[curr_y][curr_x] = self.splash
            self.grid[new_y][new_x] = self.sprite
        else:

            curr_x,curr_y = self.curr_pos(self.sprite)
            new_x = curr_x
            new_y = curr_y
            if move[0] > new_y and move[1] == new_x:
                 while(new_x<9 and (self.grid[curr_y][new_x+1]==self.splash)):
                    new_x += 1
            elif move[0] < new_y and move[1] == new_x:
                while(new_x>0 and (self.grid[curr_y][new_x-1]==self.splash)):
                    new_x -= 1
            elif move[0] == new_y and move[1] > new_x: 
                while(new_y<9 and (self.grid[new_y+1][curr_x]==self.splash)):
                    new_y += 1
            elif move[0] == new_y and move[1] < new_x: 
                while(new_y>0 and (self.grid[new_y-1][curr_x]==self.splash)):
                    new_y -= 1
            self.grid[curr_y][curr_x] = self.splash
            self.grid[new_y][new_x] = self.sprite

        

    def evaluate_board(self):
        p1, p2 = self.scores()
        self.p1_scores.append(p1)
        self.p2_scores.append(p2)
        if p1>=50:
            self.winner = "Human"
            return True
        elif p2>=50:
            self.winner = "Bot"
            return True
        elif (p1==50 and p2==50):
            self.winner = "Draw"
            return True
        else:
            return False



    def check_possible_actions(self,location):
        row , column= location
        possible_actions = []
        if (row > 0 and row < 9) and (column > 0 and column < 9):
            possible_actions.append([row,column-1]) 
            possible_actions.append([row,column+1])
            possible_actions.append([row-1,column])
            possible_actions.append([row+1,column])
        
        elif row == 0:
            if column == 0:
                possible_actions.append([row+1,column])
                possible_actions.append([row,column+1])
            elif column == 9:
                possible_actions.append([row+1,column])
                possible_actions.append([row,column-1])
            elif column > 0 and column < 9:
                possible_actions.append([row,column+1])
                possible_actions.append([row,column-1])
                possible_actions.append([row+1,column])
        elif row == 9:
            if column == 0:
                possible_actions.append([row-1,column])
                possible_actions.append([row,column+1])
            elif column == 9:
                possible_actions.append([row-1,column])
                possible_actions.append([row,column-1])
            elif column > 0 and column < 9:
                possible_actions.append([row,column+1])
                possible_actions.append([row,column-1])
                possible_actions.append([row-1,column])
        elif row < 9 and column == 9:
            possible_actions.append([row,column-1])
            possible_actions.append([row-1,column])
            possible_actions.append([row+1,column])
        elif (row > 0 and row < 9) and column == 0:
            possible_actions.append([row,column+1])
            possible_actions.append([row-1,column])
            possible_actions.append([row+1,column])
          

        return possible_actions
        

    def heuristic(self,board):
        wining_chances = 0
        # 1st Condition
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == 22 :
                    wining_chances += 1 

        # 2nd condition
        bot_pos_x, bot_pos_y = self.curr_pos(self.sprite)
        #3rd Condition       
        if bot_pos_x in range(4,7) and bot_pos_y in range(4,7):
            wining_chances += 10 

        return wining_chances

    def minimax(self, board, depth, max_depth, is_max):
        result = self.evaluate_board()
        bot_places = []

        if result == "Bot" or result == "Human" or result == "Draw" or depth == max_depth:
            return result + self.heuristic(board)

        if is_max:
            best = -1000
            board = copy.deepcopy(self.grid)
            bot_pos = self.current_position(board, False)
            

            zero_boxes , slipped_boxes = self.allowed_actions(bot_pos, board, 0)
            if len(zero_boxes) != 0:
                for x in zero_boxes:
                    board[x[0]][x[1]] = 2
                    board[bot_pos[0]][bot_pos[1]] = 22
                    # print(bot_pos)
                    bot_places.append(bot_pos)
                    bot_pos = copy.deepcopy(x)
                    best = max(best, self.minimax(board, depth+1, 7, False))
                    board[x[0]][x[1]] = 0
                    pos = list(bot_places.pop())
                    bot_pos = copy.deepcopy(pos)
                    board[pos[0]][pos[1]] = 2
            
            elif len(zero_boxes) == 0:
                temp = []
                for x in slipped_boxes:
                    board[x[0]][x[1]] = 2
                    board[bot_x][bot_y] = 22
                    temp.append(bot_pos)
                    board[bot_pos[0]][bot_pos[1]] = 22
                    board[result[0]][result[1]] = 2
                    bot_pos[0] = result[0]
                    bot_pos[1] = result[1]
                    best = max(best,self.minimax(board, depth+1, 8, False))
                    board[result[0]][result[1]] = 22
                    pos = list(temp.pop())
                    bot_pos = copy.deepcopy(pos)
                    board[pos[0]][pos[1]] = 2
            return best

        else:
            best = 1000
            player_places = []


            # player_x, player_y = self.curr_pos(1)
            # possible = self.check_possible_actions()
            player_position = self.current_position(board, True)
            zero_boxes , slipped_boxes = self.allowed_actions(player_position, board, 1)
            

            if len(zero_boxes) != 0:
                for x in zero_boxes:
                    board[x[0]][x[1]] = 1
                    board[player_position[0]][player_position[1]] = 11
                    player_places.append(player_position)
                    player_position = copy.deepcopy(x)
                  
                    best = min(best,self.minimax(board, depth+1, 7, True))
                    board[x[0]][x[1]] = 0
                    pos = list(player_places.pop())
                    player_position = copy.deepcopy(pos)
                    
                    board[pos[0]][pos[1]] = 1
            return best


    



class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_draw(self):
        arcade.start_render()
        texx0 = arcade.load_texture("pause.jpg")
        arcade.draw_texture_rectangle(500,300,1050,650, texx0,0,100)
        arcade.draw_text("GAME PAUSED", 500, 520,arcade.color.BLACK, font_size=60, anchor_x="center",bold=1)
        arcade.draw_text("Press Esc to continue", 500, 350,arcade.color.BLACK, font_size=30,anchor_x="center",bold=1,italic=1)
        arcade.draw_text("Press Enter to restart", 500, 280,arcade.color.BLACK, font_size=30, anchor_x="center",bold=1,italic=1)
        # self.uimanager.draw()


    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.game_view)
            arcade.set_background_color(arcade.color.WHEAT)
        elif key == arcade.key.ENTER:  # reset game
            game = GameView()
            self.window.show_view(game)

class GameOver_View(arcade.View):
    def __init__(self,winner):
        super().__init__()
        self.winner = winner
    
    def on_draw(self):
        arcade.start_render()
        texx0 = arcade.load_texture("pause.jpg")
        arcade.draw_texture_rectangle(500,300,1050,650, texx0,0,100)
        arcade.draw_text("Game Over", 500, 450,arcade.color.BLACK, font_size=100, anchor_x="center",bold=1)
        arcade.draw_text("Winner is:", 500, 300,arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text(self.winner, 500, 100,arcade.color.BLACK, font_size=100, anchor_x="center",bold=1)


def main():
    window = arcade.Window(WIDTH, HEIGHT, "Happy Snailing")
    window.total_score = 0
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()

