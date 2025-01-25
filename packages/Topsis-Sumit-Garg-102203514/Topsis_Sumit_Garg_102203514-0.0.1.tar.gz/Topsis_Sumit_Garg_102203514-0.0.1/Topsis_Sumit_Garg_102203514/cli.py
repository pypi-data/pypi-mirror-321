import sys
import pandas as pd
from topsisg import topsis

def main():
    if len(sys.argv) != 4:
        print("Usage: topsis-sg3514 <input.csv> <weights> <impacts>")
        print("Example: topsis-sg3514 data.csv '0.25,0.25,0.25,0.25' '+,+,-,+'")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = list(map(float, sys.argv[2].split(',')))
    impacts = sys.argv[3].split(',')

    try:
        data = pd.read_csv(input_file)
        matrix = data.values
        rankings = topsis(matrix, weights, impacts)
        print("Rankings:", rankings)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
