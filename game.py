
import decks,prob,players
from collections import Counter
class Game:
    def __init__(self):
        self.deck = decks.Deck()
        self.cheater = prob.Cheater()
        self.player = players.Player() 
        self.dealer = players.Dealer()
        return

    def flatten(self, card):
        return int(card[1:])

    def flatten_count(self, count):
        res = Counter()
        for i in range(1,14):
            for s in ['S','H','C','D']:
                res[i] += count[f'{s}{i}']
        return res

    def convert(self,n):
        return 10 if n>=10 else n

    def __test__(self):
        while self.deck.cards:
            card = self.deck.deal()
            p = self.cheater.cal_next(self.deck.count)
            print(f'Dealing {card}')
            print(sorted(p.items(), reverse=True, key=lambda x:(x[1],int(x[0][1:]))))
            input("Press Enter to continue...")
        return

    def __simulate__(self,deal_n):
        ### deal n cards before simulate ###
        for i in range(deal_n):
            self.deck.deal()

        ### simulation starts ###
        ### deal cards ###
        card = self.deck.deal()
        self.player.receive(card)
        card = self.deck.deal()
        dealer_first_card = card
        self.dealer.receive(card)
        card = self.deck.deal()
        self.player.receive(card)
        
        ### calculate win probability ###
        my_prob = self.cheater.cal_next(self.flatten_count(self.deck.count))
        win_stay = self.cheater.win_p1(self.flatten_count(self.deck.count), self.convert(self.flatten(dealer_first_card)), sum(map(self.convert,map(self.flatten,self.player.hand))), 1)
        win_hit = self.cheater.win_p1(self.flatten_count(self.deck.count), self.convert(self.flatten(dealer_first_card)), sum(map(self.convert,map(self.flatten,self.player.hand))), 0)
        print(f'Dealer has {dealer_first_card}')
        print(f'Player has {self.player.hand}')
        print(f'Probability of winning if stay: {win_stay}')
        print(f'Probability of winning if hit: {win_hit}')
        print(f'Next hit: {sorted(my_prob.items(), reverse=True, key=lambda x:(x[1],x[0]))}')
        print(f'Hit to buster: {self.cheater.buster_prob(my_prob, sum(map(self.convert,map(self.flatten,self.player.hand))))}')
        return



if __name__=='__main__':
    my_game = Game()
    #my_game.__test__()
    my_game.__simulate__(300)

