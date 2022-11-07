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
    try:
        if rank>1 and rank <=9:
            SH=" "+str(rank)+suit[0].upper()

    except:
        SH=" "+rank[0]+suit[0].upper()

    return SH
print(make_card(3,"Diamonds"))





