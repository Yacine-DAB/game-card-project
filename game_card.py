from random import shuffle

class Card:
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    values = [None, None, "2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen", "King", "Ace"]
    
    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __It__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        v = self.values[self.value] +\
        " Of "+\
        self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards\
                .append(Card(i, j))
                shuffle(self.cards)
    def random_card(self):
        if len(self.cards) == 0:
            return 
        return self.cards.pop()
    
deck = Deck()
for card in deck.cards:
    print(card)

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name
    
class Game:
    def __init__(self):
        name1 = input("player 1 name: ")
        name2 = input("Player 2 name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    
    def wins(self, winners):
        w = "{} wins this round"
        w = w.format(winners)
        print(w)
        
    def darw(self, p1n,
             p1c,
             p2n,
             p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n,
                     p1c,
                     p2n,
                     p2c)
        print(d)

    def paly_game(self):
        cards = self.deck.cards
        print("Beginning War")
        while len(cards) >= 2:
            m = "q to quit, Any" +\
            "key to play: "
            response = input(m).lower()
            if response == "q":
                break
            p1n = self.deck.random_card
            p1c = self.deck.random_card
            p2n = self.p1.name
            p2c = self.p2.name
            self.draw(p1n,
                      p1c,
                      p2n,
                      p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print("War is Over. {} wins".format(win))
    
    def winner (self, p1, p2):
        if p1.wins > p2.wins:
            return p2.name
        return "It was +A Tie!!!"

game = Game()
game.paly_game()
