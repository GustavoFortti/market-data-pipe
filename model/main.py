import time
import argparse

from src.model import model
from config.params import read_params

def main(args: dict):
    model(args)

if __name__ == '__main__':
    start_time = time.time()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-c" ,"--currency", help="currency", required=True)
    parser.add_argument("-da" ,"--date", help="currency", required=True)
    parser.add_argument("-dm" ,"--d_matrix", help="d_matrix", required=True)
    parser.add_argument("-p" ,"--variables", help="variables", required=True)
    parser.add_argument("-ts" ,"--timestemp", help="timestemp", required=True)
    parser.add_argument("-ta" ,"--time_ahead", help="time_ahead", required=True)
    parser.add_argument("-tm" ,"--question", help="question", required=True)
    parser.add_argument("-g" ,"--group_methods", help="group_methods", required=True)
    parser.add_argument("-hi" ,"--hiperparams", help="hiperparams", required=True)
    parser.add_argument("-o" ,"--optimization", help="optimization", required=True)

    args = parser.parse_args()

    args = {
        'currency': args.currency,
        'date': args.date,
        'd_matrix': int(args.d_matrix),
        'variables': read_params(args.variables),
        'variables_set': args.variables,
        'timestemp': int(args.timestemp),
        'time_ahead': int(args.time_ahead),
        'question': args.question,
        'group_methods': args.group_methods,
        'hiperparams': args.hiperparams,
        'optimization': args.optimization
    }

    main(args)

    print(f"--- {str(time.time() - start_time)} seconds main ---")