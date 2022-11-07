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
    if SH[2]=="D": 
        print("\033[31m",end="")
    elif SH[2]=="H":
        print("\033[31m",end="")
    else:
        print("\033[34m",end="")
    print(SH,end="")
    print("\033[37m")    
make_card(12,"Diamonds")





