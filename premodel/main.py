
import time
import argparse

from config.params import read_params
from src.premodel import premodel

def main(args: list) -> None:
    variables = read_params(args.variables)
    premodel(currency=args.currency, date=args.date, d_matrix=args.d_matrix, variables=variables, variables_set=args.variables, timestemp=args.timestemp, time_ahead=args.time_ahead)

if __name__ == '__main__':
    start_time = time.time()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-c" ,"--currency", help="currency", required=True)
    parser.add_argument("-d" ,"--date", help="date", required=True)
    parser.add_argument("-m" ,"--d_matrix", help="d_matrix", required=True)
    parser.add_argument("-p" ,"--variables", help="variables", required=True)
    parser.add_argument("-T" ,"--timestemp", help="timestemp", required=True)
    parser.add_argument("-ta" ,"--time_ahead", help="time_ahead", required=True)
    args = parser.parse_args()
    main(args)

    print(f"--- {str(time.time() - start_time)} seconds main ---")