
from collections import Counter
from random import shuffle
class Deck:
    def __init__(self):
        one_set = [f'{s}{i}' for i in range(1,14) for s in ['S','H','C','D']]
        self.cards = []
        for i in range(8):
            self.cards += one_set
        shuffle(self.cards)
        self.count = Counter(self.cards)
        return

    def deal(self, card=None):
        if not card:
            card = self.cards.pop()
            self.count[card]-=1
        else:
            self.cards.remove(card)
            self.count[card]-=1
        return card

    def reset(self):
        self.__init__()
        return



if __name__=='__main__':
    my_deck = Deck()
    print(my_deck.cards)
    print(my_deck.count)
    print(sum(my_deck.count.values()))
