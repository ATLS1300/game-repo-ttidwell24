#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:45:43 2020

@author: taylortidwell
"""

import turtle, random, time
turtle.colormode(255)
turtle.tracer(0)

# =============CLASSES============

class Manager:
    def __init__(self):
        self.panel=turtle.Screen()
        self.w=900
        self.h=900
        turtle.setup(self.w,self.h)
        turtle.listen()
        self.height = self.h/2 # makes managing x,y values a bit easier for me
        self.width = self.w/2
        
        self.running = True # for controlling the while loop
        self.computer_player = "soup.gif"
        self.human_player = "warhol.gif"
        self.panel.addshape(self.computer_player)
        self.panel.addshape(self.human_player)
        
        self.director = turtle.Turtle()
        
        self.board_line = turtle.Turtle()
        # player piece
        self.warhol = turtle.Turtle(shape = self.human_player)
        # computer piece
        self.soup = turtle.Turtle(shape = self.computer_player)
        # turtle that says whether you won or not
        self.ref = turtle.Turtle()
        # writes number in top left corner of tile
        self.board_numbers = turtle.Turtle()
        
        self.warhol.penup()
        self.soup.penup()
        self.ref.penup()
        self.director.color("black")
        self.ref.color('white')
        self.board_numbers.penup
        self.board_numbers.color('white')
        
        self.director.hideturtle()
        self.warhol.hideturtle()
        self.soup.hideturtle()
        self.ref.hideturtle()
        self.board_numbers.hideturtle()
        self.board_line.hideturtle()
        
        
        # bring in your global variables and initial setup tasks here
        # try to put as many setup tasks into methods and define them OUTSIDE
        # of the init method
        
        
        
    #     # call methods you want to run AS SOON AS YOUR GAME STARTS here
        
    #     self.draw_board()
        self.start()
        
    def start(self):
        # copy and paste the ACTIONS that happened BELOW all of your classes 
        # in PC08 here (this is things like instantiating objects, calling
        # methods, etc.)
        self.game = Game_board()
        self.intro = [" "," ", "Ready...", "set...", "Play!!"]
        self.ref.clear
        for repeat in range(5):
            self.ref.goto(-self.width/6, -self.height/10)
            self.ref.write(self.intro[repeat], font=('helvetica', 46))
            self.game.panel_colors()
            turtle.time.sleep(1)
            turtle.update()
        self.director.goto(-self.width/2.6, -self.height+30)
        self.director.write("(Press the number key of the tile you would like to play)", font = ('helvetica', 14))
        self.player = Players()
        
        self.player.playKeys()
        self.player.player_move(self.player.tiles_played)
        
        
    
        # self.player.player_move(self.player.tiles_played)
        # self.panel.mainloop() # keep listeners on
        
    # def draw_board(self):
    #     self.game.panel_colors() # creates the game panel
        
        
        
# Copy and paste BOARD class here

class Game_board:
    def __init__(self):
        # super(). __init__()
        # and warhol color palette
        # draws the player board
        self.board_line = turtle.Turtle()
        self.w=900
        self.h=900
        self.height = self.h/2 # makes managing x,y values a bit easier for me
        self.width = self.w/2
        self.red = [242,58,58]
        self.salmon = [250,140,130]
        self.yellow = [240,216,72]
        self.green =[119,204,98]
        self.blue = [82,128,199]
        self.magenta = [237,12,158]
        self.pink = [219,27,86]
        self.forest_green = [54,107,104]
        self.turquoise = [117, 223, 202]
        self.colors = [self.red, self.salmon, self.yellow, self.blue, self.magenta, self.pink, self.turquoise]
        
        self.playable_places = 3
        self.square = 2
        self.angle = 90
        self.square_width = self.w/3
        self.square_height = self.h/3
        
        
    def panel_colors(self): 
        """This method is the nested for loop that actaully draws the 3x3 game board
        as well as created the random color palette for each game played"""
        for row in range(self.playable_places):
            for column in range(self.playable_places):
            
                self.board_line.penup()
                self.board_line.goto(-self.width + (self.width/1.5)*row, self.height\
                                - (self.height/1.5)*column)
                self.board_line.begin_fill()
                self.board_line.width(8)
                self.board_line.pencolor('white')
                self.board_line.fillcolor(random.choice(self.colors))
                self.board_line.pendown()
                for line in range(self.square):
                    self.board_line.forward(self.square_width)
                    self.board_line.right(self.angle)
                    self.board_line.forward(self.square_height)
                    self.board_line.right(self.angle)
                self.board_line.end_fill()
        self.board_line.hideturtle()
        
        
        


# Copy and paste PLAYER class here

class Players:
    def __init__(self):
        
        self.panel=turtle.Screen()
        self.computer_player = "soup.gif"
        self.human_player = "warhol.gif"
        self.panel.addshape(self.computer_player)
        self.panel.addshape(self.human_player)
        
        # player piece
        self.warhol = turtle.Turtle(shape = self.human_player)
        # computer piece
        self.soup = turtle.Turtle(shape = self.computer_player)
        self.ref = turtle.Turtle()
        
        
        
        # writes number in top left corner of tile
        self.board_numbers = turtle.Turtle()
        self.w=900
        self.h=900
        self.height = self.h/2
        self.width = self.w/2
        self.total_tiles = 9
        self.tile_row = 3
        self.tile_column = 3
        self.keys = 1
        self.base = 0
        self.grid = self.create_grid() # calling the function create_grid() to 
                                        # allocate nested for loop lists to grid
        self.tiles_played = [self.tile_one, self.tile_two, self.tile_three,\
                             self.tile_four, self.tile_five, self.tile_six,\
                            self.tile_seven, self.tile_eight, self.tile_nine] 
                            # list of tile functions, each tile function calls
                            # and _warhol and the add_warhol then subsequently 
                            # calls the play_soup
        self.warhol.penup()
        self.soup.penup()
        self.ref.penup()
        self.ref.color('white')
        self.board_numbers.penup
        self.board_numbers.color('white')
        
        self.warhol.hideturtle()
        self.soup.hideturtle()
        self.ref.hideturtle()
        self.board_numbers.hideturtle()
            
    
    def tile_one(self):
        """each one of these methods calls add_warhol and passes the row 
        and column number for the possition of tile_one - tile_nine"""
        self.play_warhol(0,0)
        
    def tile_two(self):
        """each one of these methods calls add_warhol and passes the row 
        and column number for the possition of tile_one - tile_nine"""
        self.play_warhol(1,0) 
        
    def tile_three(self):
        """each one of these methods calls add_warhol and passes the row 
        and column number for the possition of tile_one - tile_nine"""
        self.play_warhol(2,0)
        
    def tile_four(self):
        """each one of these methods calls add_warhol and passes the row 
        and column number for the possition of tile_one - tile_nine"""
        self.play_warhol(0,1)
        
    def tile_five(self):
        """each one of these methods calls add_warhol and passes the row 
        and column number for the possition of tile_one - tile_nine"""
        self.play_warhol(1,1)
        
    def tile_six(self):
        """each one of these methods calls add_warhol and passes the row 
        and column number for the possition of tile_one - tile_nine"""
        self.play_warhol(2,1)
        
    def tile_seven(self):
        """each one of these methods calls add_warhol and passes the row 
        and column number for the possition of tile_one - tile_nine"""
        self.play_warhol(0,2)
        
    def tile_eight(self):
        """each one of these methods calls add_warhol and passes the row 
        and column number for the possition of tile_one - tile_nine"""
        self.play_warhol(1,2)
        
    def tile_nine(self):
        """each one of these methods calls add_warhol and passes the row 
        and column number for the possition of tile_one - tile_nine"""
        self.play_warhol(2,2)
        
        
        

    def stamp_warhol(self,x,y):
        """this method sends the turtle to the tile selected and stamps the GIF"""
        self.warhol.goto(x,y)
        self.warhol.stamp()
        
    def stamp_soup(self,x,y):
        """this method sends the turtle to the x,y posiiton and stamps the GIF"""
        self.soup.goto(x,y)
        self.soup.stamp()
    
    def create_grid(self):
        """this nested for loop is the method that creates the game board for the 
        computer to store x's and o's. this is done by creating and empty list 
        named grid, then for count in range 3 create a second empty list named row. 
        nested in that loop is another count in range 3 that adds a space to each 
        individual space. this results in three spaces inside of three lists 
        that are then appended to the overall list grid."""
        grid = []
        for row in range(self.tile_row):
            # creates three empty lists
            row = []
            for column in range(self.tile_column):
                # adds three spaces into each empty row list
                row.append(" ")
            # adds the row list filled with three empty spaces to the list 
            # grid three times
            grid.append(row)
        # returning grid is how we get this nested for loop pulle out of this 
        # method
        return grid
    
    
        
    def playKeys(self):
        """This will write the tile number in the top corner of each playable 
        tile. this is how the player will choose which tile to play"""
        tile_number = 1
        # the nested for loop is making the turtle write 1-3 on the top three space
        # then go down on column and label 4-6 on go down one column and label 7-9
        for row in range(self.tile_row):
            for column in range(self.tile_column):
                self.board_numbers.penup()
                # sending the turtle to the top corner of each tile. Pulled just
                # slightly away from the exact corner of each tile
                self.board_numbers.goto((-self.width+15) + column * self.width/1.5,\
                                   (self.height-30) - row * self.height/1.5)
                self.board_numbers.pendown()
                # write the tile number once the turtle is in the top left corner
                self.board_numbers.write(tile_number, font=('helvetica', 20))
                # add 1 to tile number each time the nested for loop is run to 
                # label 1-9
                tile_number += 1  
                
    def player_move(self, tiles_played):
        """this is the MOST IMPORTANT method. This method is what allows 
        the actual game to be played. when player_move is called it associates 
        every individual tile_XXX function to the relative key as the for loop 
        runs through 9 iterations. This causes tile_one for example to be associated
        with they key 1 when pressed becuase in tile_one the play_warhol fucntion 
        is called which will stamp the players move, and then calls play_soup inside of
        play_warhol so that after every player move, the computer makes it's turn.
        this method MUST BE CALLED at the end for the game to play."""
        for move in range(len(self.tiles_played)):
            # on numbr key press allocate the tile in tiles_played to the correlated 
            # number key being pressed in 1-9
            self.panel.onkey(self.tiles_played[move], str(move+1))    
        
    
    def play_soup(self):
        """Play soup is the computers play. inside this method are three for loops. 
        one for loop is to check if the computer can win with its next move inside 
        of the grid list. the next for loops checks if the player is going to 
        win and makes the computer block that move. the third loop places the 
        computer piece in the first available corner if there are no winable 
        moves available"""
        # using a nested for loop to check if o can win with it's next move
        
        for row in range(self.tile_row):
            for column in range(self.tile_column):
                # if a gird list tile is open then fill it with an o 
                if self.grid[row][column] == " ":
                    # temporarily make blank space a o
                    self.grid[row][column] = "o"
                    # input "o" in winner to check and see if o won, if it did
                    # then return and exit function
                    if self.winner("o"):
                        # stamp soup in the winning tile location
                        self.stamp_soup((-self.width/1.5) + (self.width/1.5) *\
                                        row, (self.height/1.5) - (self.height/1.5) * column)
                        return
                    else: # go back to being a blank space
                        self.grid[row][column] = " "
              
        # check where o should block x              
        for row in range(self.tile_row):
            for column in range(self.tile_column):
                if self.grid[row][column] == " ":
                    # temporarily make blank space an x
                    self.grid[row][column] = "x"
                    if self.winner("x"):
                        # add an "o" to the open spot in the grid list and then stamp a soup
                        self.grid[row][column] = "o"
                        self.stamp_soup((-self.width/1.5) + (self.width/1.5) *\
                                        row, (self.height/1.5) - (self.height/1.5) * column)
                        return
                    else: # go back to being a blank space
                        self.grid[row][column] = " "
                    
        # using nested for loop and the start (0), stop(3), and step(2) AKA  making 
        # the row and coloumns equal 0,0 and 2,0, and 0,2 and 2,2 values 
        # to make the comp choose any of the four playable corners            
        for row in range(self.base,self.tile_row,2):
            for column in range(self.base,self.tile_column,2):              
                if self.grid[row][column] == " ":
                    # if a corner is open, add an o to the first empty corner and
                    # then stamp a soup and add an o to that grid list position
                    self.grid[row][column] = "o"
                    self.stamp_soup((-self.width/1.5) + (self.width/1.5) * row,\
                                    (self.height/1.5) - (self.height/1.5) * column)
                    return

                  
    def play_warhol(self,row, column):
        """Play warhol is the method that will let the player stamp thier move
        in any open tile and allocate an x to that position in the grid list 
        created for the computer"""
        # do not allow the comp or the player to be allowed to play in any tile
        # in grid that is already taken by an x or an o
        if self.grid[row][column] == "x" or self.grid[row][column] == "o":
            self.ref.penup()
            self.ref.write(" ")
            self.panel.update()
        # if the tile is open and chosen by the player, stamp a warhol and add 
        # an x to the grid list
        else:
            # this sends the warhol turtle to the center of which ever tile the player
            # selects and stamps the warhol piece
            self.stamp_warhol((-self.width/1.5) + (self.width/1.5) * row,\
                              (self.height/1.5) - (self.height/1.5) * column)
            # this puts an "x" in this spot after the player move is stamped. this 
            # makes the comp know that spot is taken by player "x"
            self.grid[row][column] = "x"
            # check if x won by passing "x" inside of the winner method
            if self.winner("x"):
                self.ref.penup()
                self.ref.goto(-self.width/2, -self.height/8)
                # if x wins print winner winner chicken dinner
                self.ref.write("WINNER WINNER\nCHICKEN DINNER!!", font=('helvetica', 46))
                self.panel.update()
                turtle.done()
            else:
                # call play_soup at the end of play_warhol method so that once 
                # the player choses thier tile to play the computer immediate 
                # plays afer 
                self.play_soup()
            # check to see if o wins by passing the o in the winner method
            if self.winner("o"):
                self.ref.penup()
                # if o wins send the ref to the center of the screen and inform
                # player that they get no soup and they lose
                self.ref.goto(-self.width/2, -self.height/8)
                self.ref.write("NO SOUP FOR YOU,\nYOU LOSE!!", font=('helvetica', 46))
            elif self.tie():
                self.ref.penup()
                # if o wins send the ref to the center of the screen and inform
                # player that they get no soup and they lose
                self.ref.goto(-self.width/2, -self.height/8)
                self.play_soup()
                self.ref.write("NOBODY WINS, \nTIE GAME!!", font=('helvetica', 46))
        
                
    def winner(self,play):
        """This defines the winner of the game by comparing the tiles played, 
        seeing if they are equal to eachother in whether an x or o is in the space.
        this is done by replacing "play" with an x or an o when I call it in my 
        play warhol and play soup functions"""
        for move in range(self.tile_column):
            # this for loop runs to check all nine tiles and sees if there is an
            # x or an o in each spot for all vertical rows
            if self.grid[move][0] == self.grid[move][1] and self.grid[move][1]\
                == self.grid[move][2] and self.grid[move][0] == play:
                return True
            # this for loop runs to check all nine tiles and sees if there is an
            # x or an o in each spot for all horizontal rows
            if self.grid[0][move] == self.grid[1][move] and self.grid[1][move]\
                == self.grid[2][move] and self.grid[0][move] == play:
                return True
        # this for loop runs to check for a diagonal winner going from top left
        #  to bottom right and sees if the spaces are x or o 
        if self.grid[0][0] == self.grid[1][1] and self.grid[1][1] == self.grid[2][2] and\
            self.grid[0][0] == play:
            return True
        # this for loop runs to check for a diagonal winner going from top right
        #  to bottom left  and seeing if the spaces are x or o 
        if self.grid[0][2] == self.grid[1][1] and self.grid[1][1] == self.grid[2][0] and\
            self.grid[0][2] == play:
            return True  
        # if no one has won, return false so that nothing happens
        else:
            return False
    def tie(self):
        moves = 0
        for row in range(self.tile_row):
            for column in range(self.tile_column):
                if self.grid[row][column] == "x":
                    moves += 1
        if moves > self.tile_row:
            return True
        else:
            return False
        









        
# ========= DEFINE LOCAL VARIABLES =========
god = Manager()


# god.panel.listen()

# =========SET UP TURTLE(S) BELOW (color, size, shape, etc)=========


# CALLBACK FUNCTIONS BELOW 
# add onclick and onkey commands below. 




# =========ANIMATIONS BELOW=========
# code will execute in order within the loop
while god.running:
    
    # YOUR ANIMATION CODE HERE

    god.panel.update()


# =========LISTENERS & CLEANUP =========
god.panel.mainloop() # keep listeners listening DO NOT DELETE
turtle.done() # cleanup whenever we exit the loop DO NOT DELETE.





# instantiate Manager object here




# call Manager methods here:
# game = Manager()
    
# turtle.done()