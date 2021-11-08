
import sys
import os
import json
import time
import argparse

from src.premodel import premodel

PATH_PARAMS = '../config/params.json'
PATH_VARIABLES = '../config/variables.json'

def main(args: list):
    currency, variables = read_config(args.indicator, args.variables)
    premodel(currency, args.date, args.d_matrix, variables)

def read_config(indicator: str, variables: str) -> list:
    f_params = open(PATH_PARAMS)
    f_variables = open(PATH_VARIABLES)

    j_params = json.load(f_params)['indicator']['params_save'][indicator]['currency']
    j_variables = json.load(f_variables)[variables]

    return [j_params, j_variables]

if __name__ == '__main__':
    start_time = time.time()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-i" ,"--indicator", help="", required=True)
    parser.add_argument("-d" ,"--date", help="", required=True)
    parser.add_argument("-m" ,"--d_matrix", help="", required=True)
    parser.add_argument("-s" ,"--variables", help="", required=True)
    args = parser.parse_args()
    main(args)

    print(f"--- {str(time.time() - start_time)} seconds main ---")