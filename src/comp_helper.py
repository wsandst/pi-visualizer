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

def compare_bits(bit_array):
    pi_bits = read_bits_from_file("pi1mil")
    i = 0
    for (bit1, bit2) in zip(bit_array, pi_bits):
        if bit1 != bit2:
            print(f"Bits are not equal at bit {i}")
        #print(bit1, bit2)
        #if i > 100:
            #break
        i += 1

