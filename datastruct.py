from enum import Enum





class Table:
    def __init__(self, name, type, bb, ante):
        self.name = name
        self.type = type
        self.bb = bb
        self.ante = ante
        self.hands = []
        
    def __eq__(self, other):
        return self.name == other.name and self.type == other.type and self.bb == other.bb and self.ante == other.ante
    
    def __str__(self):
        return self.name + " " + self.type
     
class Hand:
    def __init__(self, id):
        self.id = id
        self.board = None
        self.players = [] #dealer is always first player in list
        self.actions = []
        self.winners = []
        self.showdown = False #does this hand go to showdown
        self.totalpot = 0
        
        
    def find_player_by_name(self, name):
        for player in self.players:
            if player.name == name:
                return player
        return None

class Board:
    def __init__(self, cards):
        self.cards = cards
        
class PlayerinHand:
    def __init__(self, name, stack, seat):
        self.name = name
        self.origstack = stack #original stack size used to calc the net in the hand
        self.stack = stack #will be modified by bets call raise
        self.seat = seat
        self.hand = None
           
    def __str__(self):
        return self.name
        
class Action:
    #Type will be Ante, Post?, Bet, Call, Fold, Raise, timeout
    #info is the amount of info available to player: Predeal, Preflop, Flop, Turn, River
    def __init__(self, type, info, amount, player):
        self.type = type
        self.info = info
        self.amount = amount
        self.player = player
        
        #TODO IMPLEMENT
        self.called = 0
        self.tocall = 0
        self.inhand = 0
        self.cashinpot = 0
        self.amounttocall = 0
        
        
    def __str__(self):
        return self.info.name + " " + str(self.player) + " " + self.type.name + " " + str(self.amount)


class ActionType(Enum):
    ANTE = 0
    POST = 1
    BET = 2
    CALL = 3
    FOLD = 4
    RAISE = 5
    CHECK = 6
    ALLIN = 7
    TIMEOUT = 8
    
    
class ActionInfo(Enum):
    PREDEAL = 0
    PREFLOP = 1
    FLOP = 2
    TURN = 3
    RIVER = 4 
    

    