import time
import decimal
import sys
import math
#import generate_image
#import comp_helper
def to_hex(num: list):
    symbols = '0123456789ABCDEF'
    ind = 0
    for i, val in enumerate(num):
        ind = ind * 2 + val
        if i % 4 == 3:
            yield symbols[ind]
            ind = 0
    while i % 4 != 3:
        i += 1
        ind *= 2
    yield symbols[ind]

    

def flip_number(num: list):
    first_val_found = False
    ret_val = []
    for val in reversed(num):
        if first_val_found:
            ret_val.append(val)
        elif val != 0:
            ret_val.append(val)
            first_val_found = True
    return ret_val

def convert_base_2(num: decimal.Decimal, cur_pow: int, lookup: dict):
    if cur_pow < 1:
        return [int(num)]
    else:
        if cur_pow in lookup:
            base = lookup[cur_pow]
        else:
            base = decimal.getcontext().power(2, cur_pow)
            lookup[cur_pow] = base
        digits = []
        if num == 0:
            digits = [0]
            return digits
        while num:
            digit = num % base
            digits.append(digit)
            
            num = num // base
        dummy = 0
        digits = [convert_base_2(n, cur_pow // 2, lookup) for n in digits]
        digits_n = []
        for digit in digits:
            digits_n.extend(digit)
            digits_n.extend([0] * (cur_pow - len(digit)))
        return digits_n

def main():
    nums = 10**6
    decimal.getcontext().prec = 10**9
    decimal.getcontext().Emin = -999999999999999
    decimal.getcontext().Emax = 0-decimal.getcontext().Emin
    file = open("pi.txt")
    lines = file.readlines()
    print("File done")

    pi = '3' + lines[0][2:nums + 1]
    pi = decimal.Decimal(pi)
    print(sys.getsizeof(pi))
    context = decimal.getcontext()
    k = context.logb(pi)   #pi has been multiplied by 10^k (we removed the .)
        #We want to remove the factor 5 ^ k in order to preserve binary order of digits
        #To do this and preserve an integer we can work with we need to mulitply by 2 ^ m / 5 ^ k
        #for some m such that 2 ^ m is of a greater magnitude than 5 ^ k
    denum_part = context.power(5, k)
    num_part = context.power(2, int(int(k) * math.log2(5)) + 1)
    pi = (pi * num_part) // denum_part
    
    pi = decimal.Decimal(pi)
    start_exp = int(math.log2(float(int(context.logb(pi)) * (1/math.log10(2)))))
    del denum_part
    del num_part
    start_pow = 2**start_exp

    print(context.logb(pi), k)
    print("start")
    start = time.time()
    binary = convert_base_2(pi, start_pow, dict())
    binary = flip_number(binary)
    end = time.time()
    print("end: ", end - start)


    hx_partion = binary[2:]
    hx_partion = list(to_hex(hx_partion))
    st = ''
    for i in range(50):
        st += hx_partion[10**6 - 50 + i]
    print(st)

    #val = sum([val << i for i, val in enumerate(binary)])
    #print(val)
    #print(binary)
    

if __name__ == "__main__":
    main()
    #comp_helper.compare_bits([0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1])
    #generate_image.generate_image("pi1mil")