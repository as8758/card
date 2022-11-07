import random
'''Part 1 & 2'''
def make_card(rank,suit):

    if rank==11:
        rank="jack"
    elif rank==12:
        rank="Queen"
    elif rank==13:
        rank="King"
    elif rank==14:
        rank="Ace"
    name=str(rank)+" of "+suit

    SHsuit=suit[0].upper()

    try:
        if rank>1 and rank <=10:
            SH=" "+str(rank)+SHsuit

    except:
        SH=" "+rank[0]+SHsuit

    if SHsuit == "D" : 
        return "\033[31m"+SH
    elif SHsuit=="H":
        return  "\033[31m"+SH
    else:
       return "\033[34m"+SH


'''Part 3'''
def make_deck():
    l=[]
    for i in range(4):
            if i==0:
                name="Diamonds"
            elif i==1:
                name="Clubs"
            elif i==2:
                name="Hearts"
            else:
                name="Spades"
            
            for i in range(2,15):
                x=make_card(i,name)
                l.append(x)
    tup=tuple(l)  
    return tup

'''Part 4'''
def shuffle(deck):
    length=52
    l=list(deck)
    o=0
    for i in range(0,length-1):
            j=random.randint(i,length-1) 
            a=l[i]
            b=l[j]
            l[i]=b
            l[j]=a
    return tuple(l)

'''Part 5'''
def draw(deck,hand=[]):
    length=len(deck)
    l=list(deck)
    if length <= 0:
        return None
    else:
        hand.append(deck[0])
    print (hand)



x=make_deck()


s=shuffle(x)
S=tuple()

d=draw(s)
