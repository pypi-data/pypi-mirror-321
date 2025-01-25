import sys
from .topsis import topsis

def main():
    if len(sys.argv) != 5:
        print("Usage: topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>")
    else:
        input_file = sys.argv[1]
        weights = sys.argv[2]
        impacts = sys.argv[3]
        output_file = sys.argv[4]
        try:
            topsis(input_file, weights, impacts, output_file)
            print(f"Results saved to '{output_file}'")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
