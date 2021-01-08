import scipy.special as sci

def almost_everywhere_zero(n,k,i=0):
    length = len(str(n)) - 1

    if len(str(n)) + i < k or k-i == 0:
        return 0
    elif len(str(n)) == 1:
        if i +1 ==k:
            return n
        else:
            return 0
    else:

        vals = (9 ** (k-i)) * sci.comb(length, k-i, exact=True)
        mult = int(str(n)[0]) -1

        if k-i != 1 and mult != 0:
            vals += mult*((9 ** (k-i-1)) * sci.comb(length, k-i-1, exact=True))
        elif k-i == 1:
            vals += mult+1
        new_num = int(str(mult+1) +(length * str(0)))
        i+=1
        return int(vals + almost_everywhere_zero((n-new_num),k,i))


print(almost_everywhere_zero(10000000000000000000000,21))
