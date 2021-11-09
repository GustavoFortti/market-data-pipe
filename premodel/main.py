
import sys
import os
import json
import time
import argparse

from src.premodel import premodel

def main(args: list):
    premodel(currency=args.indicator, date=args.date, d_matrix=args.d_matrix, variables=args.variables, timestemp=args.timestemp)

if __name__ == '__main__':
    start_time = time.time()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-i" ,"--indicator", help="indicator", required=True)
    parser.add_argument("-d" ,"--date", help="date", required=True)
    parser.add_argument("-m" ,"--d_matrix", help="d_matrix", required=True)
    parser.add_argument("-v" ,"--variables", help="variables", required=True)
    parser.add_argument("-t" ,"--timestemp", help="timestemp", required=True)
    args = parser.parse_args()
    main(args)

    print(f"--- {str(time.time() - start_time)} seconds main ---")