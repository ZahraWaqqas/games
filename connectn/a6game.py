"""
The controller class to run the game

This module provides tha class that handles the basic game loop. Once this class is
completed, you can start to play with the connectn program.

# Zahra Waqqas 291234050
# DATE COMPLETED HERE
"""
import a6board
import a6player


#### TASK 3 ####
class Game:
    """
    A class representing a game of Connect-N

    Instances of this class contain both a board and a list of players. They play the
    game by calling chooseMove() for each player, and making the corresponding play in
    the game board. They also check for wins or ties.
ack feature supported by the method take_back().  This is
    used in AI play to undo sp
    The game also has a takebeculative moves,
    """
    # HIDDEN ATTRIBUTES
    # Attribute _board: The game board
    # Invariant: _board is a Board object
    #
    # Attribute _players: The game players
    # Attribute _players: The game players
    # Invariant: _players is a (possibly empty) list of Player objects, each 
    #            with distinct colors
    #
    # Attribute _current: The index of the current player
    # Invariant: _current is an int >= 0 and < len(_players), or -1 if _players 
    #            is empty
    #
    # Attribute _winner: The (color of) the winner of the game
    # Invariant: _winner is either None (no winner) or a color of one of the
    #            Players in _players

    #### PART A ####
    def getBoard(self):
        """
        Returns the game board
        """
        return self._board
    
    def getPlayers(self):
        """
        Returns a list of players in the game
        """
        return self._players
    
    def addPlayer(self, player):
        """
        Adds the given player to the game.
        
        If the list of players was currently empty, this makes this player the
        current player.
        
        Parameter player: the Player to add
        Precondition: player is a Player object with a different color than any
        of the current players.
        """
        assert isinstance(player, a6player.Player) # precondition to ensure player is a Player object
        assert is_new_player(self._players, player) # precondition to ensure it is a new player and doesn't have same color using helper function

        self._players.append(player) # add to list
        if len(self._players) == 1:
            self._current = 0 # change index to show a new player has been added at index 0

    def clearPlayers(self):
        """
        Removes all the players from the game
        """
        self._players = [] # initialize list
        self._current = -1 # initialize current index
    
    def getCurrent(self):
        """
        Returns the current player object in the game. If there are no players, it
        returns None.
        """
        if self._current == -1: # condition to check it current index is -1, if so then it means no players
            return None # return as required
        return self._players[self._current] # otherwise just return the player at the current index

    
    def getWinner(self):
        """
        Returns the (color of) the winner of the game (or None if there is no winner)
        """
        return self._winner
    
    def __init__(self,width,height,streak):
        """
        Initializes a new game with the given width, height, and streak.
        
        This method should start out with no players. Read the invariant closely 
        to see how to do this.
        
        Parameter width: The board width
        Precondition: width is an int > 0
        
        Parameter height: The board height
        Precondition: height is an int > 0
        
        Parameter streak: The number of pieces in a line necessary to win
        Precondition: streak is an int > 0 and <= min(width,height)
        """
        assert isinstance(width, int) and width > 0 # precondition for width
        assert isinstance(height, int) and height > 0 # precondition for height
        assert isinstance(streak, int) and 0 < streak <= min(width, height) # precondition for streak

        self._board = a6board.Board(height, width, streak) # make a new board using given height, width and streak
        self._players = [] # initialize an empty list for players
        self._current = -1 # initialize current as given in instructions
        self._winner = None # initialize winner too

    #### PART B ####
    def advance(self):
        """
        Advances the game to the next player.
        
        This increments the current player index by 1 (or resets it to 0 when 
        all players have had a chance.
        """
        if len(self._players) == 0: # condition to check if list isn't already empty
            return # if so then just return nothing
        if self._current+1 >= len(self._players): # condition to check by going to the next increment it shouldn't be last one or if all players have had a chance yet
            self._current = 0 # if the index was at the last player then reset
        else:
            self._current += 1 # else increment
    
    def takeTurn(self,player):
        """
        Returns the column chosen by the given player.
        
        This method processes a turn for the current player. That means choosing a
        column AND placing the player's color in that column.
        
        If the player is unable to make a move, this method returns -1.
        
        Parameter player: The current player
        Precondition: player is a Player object
        """
        assert isinstance(player, a6player.Player) # precondition

        col = player.chooseMove(self._board) # use function to see which move is made
        row = self._board.place(col, player.getColor()) # use place function from Board class to see which row it was placed in
        if row == -1:
            return -1 # return -1 if no row had been available in that column
        return col # else just return the col in which the player placed their color in

    def run(self):
        """
        Runs the game until completion.
        
        This method contains a while loop that runs until either there is a 
        winner or the game board fills up.
        """
        while self._winner is None and self._board.isFullBoard() != True: # conditions to keep the game going unless met
            current_player = self.getCurrent() # get current player
            column = self.takeTurn(current_player) # let that player take their turn using function we just made
            if column != -1: # now if that function returns -1 that means no row was available meaning board full
                last_r, last_c = self._board.getLastMove() # get the most recent move made by the player
                win_result = self._board.findWins(last_r, last_c) # check to see if any wins can be found
                if win_result is not None: # condition to check if there are wins
                    self._winner = current_player.getColor() # update winner
                else:
                    self.advance() # otherwise just continue the game


#### HELPER FUNCTION ####
# DO NOT MODIFY
def is_new_player(players,p):
    """
    Returns True if p is a different color than the objects in players
    
    Parameter players: The existing players
    Precondition: players is a list of Player objects
    
    Parameter p: The player to test
    Precondition: p is a Player object
    """
    result = True
    for opponent in players:
        if opponent.getColor() == p.getColor():
            return False
    return True
