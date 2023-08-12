def bin2dec():
    a = 0
    while(a == 0):
        binstr = input('Enter binary Number: ')
        prdec = 0
        dec = 0
        binlist = list(binstr)
        for i in range(len(binlist)):
            if(binlist[i] != '0' and binlist[i] != '1'):
                a = 0
                break
            else:
                a = 1
                if(binlist[i] == '1'):
                    prdec = 2**(len(binlist)-1-i)
                    dec = dec + prdec        
        if(a == 1):
            print('Decimal Number is: ', dec)
        else:
            print('Binary Number consists of either 0 or 1')
def dec2bin():
    W = ['0','1','2','3','4','5','6','7','8','9']
    a = 0
    while(a == 0):
        sdec = input('Enter Decimal Number: ')
        for i in list(sdec):
            if(i not in W):
                a = 0
                break
            else:
                a = 1
        if(a == 1):
            dec = int(sdec)
            rlist = []
            while(dec != 1):
                r = dec%2
                dec = dec//2
                rlist.append(r)
            rlist.append(1)
            rlist.reverse()
            bin = ''
            for i in rlist:
                bin += str(i)
            print('Binary Number is: ', bin)
        else:
            print('Decimal Number consists of 0 to 9')
