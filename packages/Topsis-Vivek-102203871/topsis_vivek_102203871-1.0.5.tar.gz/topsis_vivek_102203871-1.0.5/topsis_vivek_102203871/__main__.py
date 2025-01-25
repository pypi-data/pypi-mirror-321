from .topsis import topsis
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python -m topsis_vivek_102203871 <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    topsis(input_file, weights, impacts, output_file)
