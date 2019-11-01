from random import shuffle


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def show(self):
        if self.rank == "Joker":
            return f"{self.suit} Joker"
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self._build()

    def _build(self):
        for s in ("Spades", "Clubs", "Diamonds", "Hearts"):
            for r in ("A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"):
                self.cards.append(Card(s, r))
        for c in ("Black", "Red"):
            self.cards.append(Card(c, "Joker"))
        shuffle(self.cards)

    def draw(self):
        card = self.cards.pop()
        return card.show()

    def isempty(self):
        return not bool(self.cards)
