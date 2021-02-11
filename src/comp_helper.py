import generate_image

def read_bits_from_file(name: str):
    """ Generator. Loads a binary file """
    with open(name, "rb") as infile:
        byte = infile.read(1)
        while byte:
            num = int.from_bytes(byte, "little")
            for i in range(8):
                yield num % 2
                num >>= 1
            byte = infile.read(1)

def getbytes(bits):
    done = False
    while not done:
        byte = 0
        for _ in range(0, 8):
            try:
                bit = next(bits)
            except StopIteration:
                bit = 0
                done = True
            byte = (byte << 1) | bit
        yield byte

def compare_bits(bit_array):
    pi_bits = read_bits_from_file("pi1mil")
    i = 0
    for (bit1, bit2) in zip(bit_array, pi_bits):
        if bit1 != bit2:
            print(f"Bits are not equal at bit {i}")
            break
        #print(bit1, bit2)
        #if i > 100:
            #break
        i += 1

def

