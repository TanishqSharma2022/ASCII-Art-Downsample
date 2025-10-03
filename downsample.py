
import argparse


def load_ascii_art(file_path):
    with open(file_path, 'r') as f:
        # Read all lines and strip newline characters
        ascii_art = [line.rstrip('\n') for line in f]
    return ascii_art


parser = argparse.ArgumentParser(prog="ASCIIArtDownsampler", 
                                 description="Downsamples ascii arts by an integer factor")

parser.add_argument("ascii", help="add ascii filepath...")


args = parser.parse_args()
# Example usage
file_path = args.ascii # replace with your file path
ascii_art = load_ascii_art(file_path)


def downsample_ascii(binary_art, new_h, new_w):
    H, W = len(binary_art), len(binary_art[0])
    block_h = new_h
    block_w = new_w
    new_art = []
    j = W
    for i in range(0, H, 2):
        row = ''        # new_art += binary_art[i]
        for j in range(0, W, 2):
            
            row+=binary_art[i][j]

        new_art.append(row)            
    return new_art


downsample_art = downsample_ascii(ascii_art, 2, 2)

# Assume downsample_art is a list of strings (each row of ASCII art)
with open("output.txt", "w") as f:
    for row in downsample_art:
        f.write(row + "\n")


