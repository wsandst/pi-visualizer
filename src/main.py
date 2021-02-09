import time
import decimal
import sys
import generate_image

def main():
    file = open("pi.txt")
    lines = file.readlines()
    print("File done")
    decimal.getcontext().prec = 10**10
    decimal.getcontext().Emin = -999999999999999
    decimal.getcontext().Emax = 0-decimal.getcontext().Emin

    nums = 10**8

    start = time.time()
    pi = lines[0][2:nums]
    pi = decimal.Decimal(pi)
    end = time.time()
    print(sys.getsizeof(pi))
    base = decimal.getcontext().power(2, 10 ** 8)
    i = 0
    start = time.time()
    while pi > base:
        print(i)
        pi -= pi % base
        pi //= base
        i += 1
    end = time.time()
    print(end - start)
    

if __name__ == "__main__":
    main()
    #generate_image.generate_image("pi1mil")