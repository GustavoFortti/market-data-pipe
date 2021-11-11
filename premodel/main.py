
import time
import argparse

from src.premodel import premodel

def main(args: list) -> None:
    premodel(currency=args.currency, date=args.date, d_matrix=args.d_matrix, predictor=args.predictor, target=args.target, timestemp=args.timestemp, time_ahead=args.time_ahead)

if __name__ == '__main__':
    start_time = time.time()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-c" ,"--currency", help="currency", required=True)
    parser.add_argument("-d" ,"--date", help="date", required=True)
    parser.add_argument("-m" ,"--d_matrix", help="d_matrix", required=True)
    parser.add_argument("-p" ,"--predictor", help="predictor", required=True)
    parser.add_argument("-t" ,"--target", help="target", required=True)
    parser.add_argument("-T" ,"--timestemp", help="timestemp", required=True)
    parser.add_argument("-ta" ,"--time_ahead", help="time_ahead", required=True)
    args = parser.parse_args()
    main(args)

    print(f"--- {str(time.time() - start_time)} seconds main ---")