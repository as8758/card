'''Past 7'''
import cards 
def deal_hand():
    x=cards.make_deck()
    de1,de2,deck = cards.deal(x,4)
    return de1,de2,deck

x,y,z=deal_hand()
for i in (x):
    print(i)