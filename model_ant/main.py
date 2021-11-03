
import sys
import os
import time
import argparse

from src.model_ant import model_ant

def main(args: list):
    model_ant(args.currency)

if __name__ == '__main__':
    start_time = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument("-c" ,"--currency", help="", required=True)
    parser.add_argument("-c" ,"--currency", help="", required=True)
    args = parser.parse_args()
    main(args)

    print(f"--- {str(time.time() - start_time)} seconds main ---")