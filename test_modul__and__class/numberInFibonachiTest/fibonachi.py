
def fibonachi(n,son1):
    n1=0
    n2=1
    fibonachilar=[]
    while n>0:
        son=n1+n2
        n1=n2
        n2=son
        n-=1
        fibonachilar.append(son)
    return True if son1 in fibonachilar else False

    
