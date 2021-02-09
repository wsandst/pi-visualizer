import time
import decimal
import sys

def convert_base_2(num: decimal.Decimal, cur_pow: int):
    if cur_pow < 1:
        return [int(num)]
    else:
        base = decimal.getcontext().power(2, cur_pow)
        digits = []
        if num == 0:
            digits = [0] * cur_pow
            return digits
        while num:
            digit = num % base
            digits.append(digit)
            
            num = num // base
        dummy = 0
        digits = [convert_base_2(n, cur_pow // 2) for n in digits]
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
    nums = 10**1
    pi = '3' + lines[0][2:nums]
    pi = decimal.Decimal(pi)
    pi = decimal.Decimal(123)
    start_pow = 5
    print(pi)
    binary = convert_base_2(pi, start_pow)

    val = sum([val << i for i, val in enumerate(binary)])
    print(val)
    print(binary)
    

if __name__ == "__main__":
    main()