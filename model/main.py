import time
import argparse

from src.model import model

def main(args: dict):
    model(args)

if __name__ == '__main__':
    start_time = time.time()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-c" ,"--currency", help="currency", required=True)
    parser.add_argument("-da" ,"--date", help="currency", required=True)
    parser.add_argument("-dm" ,"--d_matrix", help="d_matrix", required=True)
    parser.add_argument("-p" ,"--predictor", help="predictor", required=True)
    parser.add_argument("-t" ,"--target", help="target", required=True)
    parser.add_argument("-ts" ,"--timestemp", help="timestemp", required=True)
    parser.add_argument("-ta" ,"--time_ahead", help="time_ahead", required=True)
    parser.add_argument("-tm" ,"--question", help="question", required=True) # 1 = classification, 2 = regression, 3 clustering
    parser.add_argument("-g" ,"--group_methods", help="group_methods", required=True)
    parser.add_argument("-h" ,"--hiperparams", help="hiperparams", required=True)
    parser.add_argument("-i" ,"--index", help="index", required=True)
    parser.add_argument("-o" ,"--optimization", help="optimization", required=True)

    args = parser.parse_args()

    args = {
        'currency': args.currency,
        'date': args.date,
        'd_matrix': args.d_matrix,
        'predictor': args.predictor,
        'target': args.target,
        'timestemp': args.timestemp,
        'time_ahead': args.time_ahead,
        'question': args.question,
        'group_methods': args.group_methods,
        'hiperparams': args.hiperparams,
        'index': int(args.index),
        'optimization': args.optimization
    }

    main(args)

    print(f"--- {str(time.time() - start_time)} seconds main ---")