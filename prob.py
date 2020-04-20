
### TODO ###
### 10,11,12,13 are all 10 ###
### 1 can be either 1 or 11 ###
class Cheater:
    def __init__(self):
        return

    def cal_next(self,count):
        prob = {}
        total_cnt = sum(count.values())
        for c in count.keys():
            prob[c] = count[c]/total_cnt
        return prob

    def convert(self,n):
        return 10 if n>=10 else n

    def win_p1(self, count, dealer_first_card, player_hand, stay=1):
        res = 0
        my_prob = self.cal_next(count)
        for i in range(1,14):
            count[i] -= 1
            dealer_hand = dealer_first_card+self.convert(i)
            res += my_prob[i]*self.win_p2(count, dealer_hand, player_hand, stay)
            count[i] += 1
        return res

    def win_p2(self, count, dealer_hand, player_hand, stay=1):
        if player_hand > 21: return 0
        ### if player stays ###
        if stay:
            if dealer_hand >= 17:
                if dealer_hand > 21:
                    return 1.0
                if player_hand < dealer_hand: 
                    return 0
                else:
                    return 1.0
            else:
                my_prob = self.cal_next(count)
                player_win_p = 0
                for i in range(1,14):
                    count[i] -= 1
                    player_win_p += my_prob[i]*self.win_p2(count, dealer_hand+self.convert(i), player_hand)
                    count[i] += 1
            return player_win_p
        else:
            ### if player hits ###
            my_prob = self.cal_next(count)
            player_win_p = 0
            for i in range(1,14):
                count[i] -= 1
                player_win_p += my_prob[i]*self.win_p2(count, dealer_hand, player_hand+self.convert(i))
                count[i] += 1
            return player_win_p

    def buster_prob(self, prob, player_hand):
        res = 0
        for i in range(1,14):
            if player_hand+self.convert(i) > 21:
                res+=prob[i]
        return res
