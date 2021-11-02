
import sys
import os
import time
import argparse

from src.indicator import indicator

def main(args: list):
    indicator(args.currency)

if __name__ == '__main__':
    start_time = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument("-c" ,"--currency", help="", required=True)
    args = parser.parse_args()
    main(args)

    print(f"--- {str(time.time() - start_time)} seconds main ---")