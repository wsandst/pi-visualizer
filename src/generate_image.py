from PIL import Image
import math
Image.MAX_IMAGE_PIXELS = None
import numpy as np

def to_byte(nums: list):
    for i in range(0, len(nums)-8+1, 8):
        byte = ''.join([str(x) for x in nums[i:i+8]])
        yield int(byte, 2)

def read_bytes_from_file(name: str):
    """ Generator. Loads a binary file. Every 3 bytes becomes a color """
    with open(name, "rb") as infile:
        byte = infile.read(1)
        while byte:
            num = int.from_bytes(byte, "little")
            yield num
            byte = infile.read(1)

def generate_image_from_file(name, output_name="pi"):
    """ Generates and saves a png from a binary file """
    print(f"Loading bytes from file {name}")
    bitmap = [byte for byte in read_bytes_from_file(name)]
    # Calculate side length for perfect square, truncuate rest
    side = math.sqrt(len(bitmap) / 3)
    int_side = math.floor(side)
    diff = math.ceil(side*side*3 - int_side*int_side*3)
    bitmap = bitmap[:-diff]

    # Convert list into np array and then PIL image
    print("Generating image")
    array = np.array(bitmap, dtype=np.uint8)
    array = array.reshape(int_side, int_side, 3)
    img = Image.fromarray(array)
    img.save(f'{output_name}.png')
    print(f"Image {output_name} saved")

def generate_image_from_list(lst, output_name):
    """ Generates and saves a png from a binary file """
    print("Creating bitmap from list")
    bitmap = [byte for byte in to_byte(lst)]
    # Calculate side length for perfect square, truncuate rest
    side = math.sqrt(len(bitmap) / 3)
    int_side = math.floor(side)
    diff = math.ceil(side*side*3 - int_side*int_side*3)
    bitmap = bitmap[:-diff]

    # Convert list into np array and then PIL image
    print("Generating image")
    array = np.array(bitmap, dtype=np.uint8)
    array = array.reshape(int_side, int_side, 3)
    img = Image.fromarray(array)
    img.save(f'{output_name}.png')
    print(f"Image {output_name} saved")