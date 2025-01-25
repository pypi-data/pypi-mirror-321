from .topsis import topsis
import sys

def main():
    if len(sys.argv) != 5:
        print("Usage: topsis <inputFileName> <weights> <impacts> <resultFileName>")
        sys.exit(1)

    inputFileName = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    resultFileName = sys.argv[4]

    topsis(inputFileName, weights, impacts, resultFileName)
