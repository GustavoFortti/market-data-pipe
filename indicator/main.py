import time
import argparse
from src.indicator import indicator

def main(args:str=None):
    indicator()

if __name__ == '__main__':
    start_time = time.time()

    # parser = argparse.ArgumentParser()
    # parser.add_argument("-e" ,"--exemple", help="", required=True)
    # args = parser.parse_args()
    # if (not args.index): args.index = 0

    main()

    print("--- %s seconds main ---" % (time.time() - start_time))