import time
import argparse

def main(args):
    pass    

if __name__ == '__main__':
    start_time = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument("-e" ,"--exemple", help="", required=True)
    args = parser.parse_args()
    if (not args.index): args.index = 0

    main(args)

    print("--- %s seconds main ---" % (time.time() - start_time))