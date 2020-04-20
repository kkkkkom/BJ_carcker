
class Player:
    def __init__(self, initial_fund=100):
        self.hands = []
        self.hand = []
        self.money = initial_fund
        self.win = 0
        self.lose = 0
        return

    def receive(self, card):
        self.hand.append(card)
        return

    def initial_two_cards(self, cards):
        self.hand = cards
        return

    def hit(self):
        #self.hand
        return

    def stay(self):
        #self.hand
        return

    def double(self):
        return

    def surrender(self):
        return

    def split(self):
        return

class Dealer(Player):
    pass



if __name__=='__main__':
    my_dealer = Dealer()
    print(my_dealer.money)
