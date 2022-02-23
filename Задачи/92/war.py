# Однокарточная версия игры "Война"

class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = str(self.rank) + str(self.suit)
        return rep
    @property
    def value(self):
        val = Card.RANKS.index(self.rank) + 1
        return val
class Hand(object):
    def __init__(self):
        self.cards = []
    def __str__(self):
        for card in self.cards:
            rep += str(card) + "\t"
        return rep
    @property
    def total(self):
        r = 0
        for card in self.cards:
            r += card.value
        return r
    def clear(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def give(self, other_hund, card):
        self.cards.remove(card)
        other_hund.add(card)
class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands):
        for hand in hands:
            top_card = self.cards[0]
            self.give(hand, top_card)
class Player(Hand):
    def __init__(self, name, score = 0):
        super(Player, self).__init__()
        self.name = name
    def __str__(self):
        rep = str(self.name)
        return rep

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

class Game(object):
    def __init__(self):
        print("Создаю колоду.")
        self.deck = Deck()
        self.deck.populate()
        print("Перемешиваю колоду.")
        self.deck.shuffle()
        number = ask_number("Введите количество игроков(1-7): ", low = 1, high = 8)
        self.players = []
        for i in range(number):
            name = str(input("Введите имя игрока: "))
            gamer = Player(name)
            self.players.append(gamer)
    def play(self):
        self.deck.deal(self.players)
        print("Карты игроков и их счет:")
        score = 0
        for player in self.players:
            print(player, "\t", player.total)
            if player.total > score:
                score = player.total
            if player.total >= score:
                player_best = player
        print("Наивысший результат у игрока:")
        print(player_best, "\t", score)
def main():
    response = None
    while response not in ("y", "n"):
        
        response = input("Хотите начать новую игру?(y/n): ")
        if response == "y":
            game = Game()
            game.play()
        else:
            break

main()
input("\n\nНажмите Enter, чтобы выйти.")