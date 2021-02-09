from PIL import Image
import math
Image.MAX_IMAGE_PIXELS = None
import numpy as np

def read_bytes_from_file(name):
    with open(name, "rb") as infile:
        byte = infile.read(1)
        while byte:
            num = int.from_bytes(byte, "little")
            yield num
            byte = infile.read(1)

def generate_image(name, output_name="pi"):
    print(f"Loading bytes from file {name}")
    bitmap = [byte for byte in read_bytes_from_file(name)]
    side = math.sqrt(len(bitmap) / 3)
    int_side = math.floor(side)
    diff = math.ceil(side*side*3 - int_side*int_side*3)
    bitmap = bitmap[:-diff]

    print("Generating image")
    array = np.array(bitmap, dtype=np.uint8)
    array = array.reshape(int_side, int_side, 3)
    img = Image.fromarray(array)
    img.save(f'{output_name}.png')
    print(f"Image {output_name} saved")

if __name__ == "__main__":
    main()