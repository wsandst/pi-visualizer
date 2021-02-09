import time
import decimal
import sys
#import generate_image
#import comp_helper


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
    decimal.getcontext().prec = 10**10
    decimal.getcontext().Emin = -999999999999999
    decimal.getcontext().Emax = 0-decimal.getcontext().Emin
    file = open("pi.txt")
    lines = file.readlines()
    print("File done")
    nums = 10**7
    pi = '3' + lines[0][2:nums]
    pi = decimal.Decimal(pi)
    start_pow = 2**25
    #print(pi)

    print("start")
    start = time.time()
    binary = convert_base_2(pi, start_pow, dict())
    end = time.time()
    print("end: ", end - start)

    #val = sum([val << i for i, val in enumerate(binary)])
    #print(val)
    #print(binary)
    """
    binary = convert_base_2(decimal.Decimal(48), 2**(2**3))
    val = sum([val << i for i, val in enumerate(binary)])
    print(binary)
    print(val)
    print(48)"""
    

if __name__ == "__main__":
    main()
    #comp_helper.compare_bits([0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1])
    #generate_image.generate_image("pi1mil")