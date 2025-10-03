
import argparse


def load_ascii_art(file_path):
    with open(file_path, 'r') as f:
        # Read all lines and strip newline characters
        ascii_art = [line.rstrip('\n') for line in f]
    return ascii_art


parser = argparse.ArgumentParser(prog="ASCIIArtDownsampler", 
                                 description="Downsamples ascii arts by an integer factor")

parser.add_argument("ascii", help="add ascii filepath...")
parser.add_argument("-f", "--factor", help="scaling factor (1, 2, 4)...")

args = parser.parse_args()
# Example usage
file_path = args.ascii # replace with your file path
ascii_art = load_ascii_art(file_path)

scaling_factor = int(args.factor)
def downsample_ascii(binary_art):
    H, W = len(binary_art), len(binary_art[0])
    new_art = []
    j = W
    for i in range(0, H, scaling_factor):
        row = ''    
        for j in range(0, W, scaling_factor):
            row+=binary_art[i][j]
        new_art.append(row)            
    return new_art


downsample_art = downsample_ascii(ascii_art)

for row in downsample_art:
    print(row)



# with open("output.txt", "w") as f:
#     for row in downsample_art:
#         f.write(row + "\n")



