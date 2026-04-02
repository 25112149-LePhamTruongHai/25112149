import random
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
                  '8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}
        return values[self.rank]

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        suits = ['♥', '♦', '♣', '♠']
        ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.cards = [Card(r, s) for r in ranks for s in suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def value(self):
        return sum(card.value() for card in self.cards)

    def show(self):
        return " ".join(str(c) for c in self.cards)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def add_card(self, card):
        self.hand.add_card(card)

    def show_hand(self):
        print(f"{self.name}: {self.hand.show()} (all: {self.hand.value()})")

class HumanPlayer(Player):
    pass

class ComputerPlayer(Player):
    pass

class PokerGame:
    def __init__(self):
        self.deck = Deck()
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def start(self):
        self.deck.shuffle()

        for _ in range(2):
            for p in self.players:
                p.add_card(self.deck.deal())

        for p in self.players:
            p.show_hand()

        winner = max(self.players, key=lambda p: p.hand.value())
        print(f"\nwinner: {winner.name} ")

game = PokerGame()
p1 = HumanPlayer("you")
p2 = ComputerPlayer("bot")
game.add_player(p1)
game.add_player(p2)
game.start()
