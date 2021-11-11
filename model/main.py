import time
import argparse

from src.model import model

def main(args: list):
    model()

if __name__ == '__main__':
    start_time = time.time()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-c" ,"--currency", help="currency", required=True)
    parser.add_argument("-m" ,"--d_matrix", help="d_matrix", required=True)
    parser.add_argument("-M" ,"--type_model", help="type_model", required=True) # 1 = classification, 2 = regression, 3 clustering
    parser.add_argument("-l" ,"--type_learning", help="type_learning", required=True) # 1 = machine learning, 2 = deep learning
    parser.add_argument("-a" ,"--algorithm", help="algorithm", required=True)
    parser.add_argument("-h" ,"--hiperparams", help="hiperparams", required=True)
    parser.add_argument("-i" ,"--index", help="index", required=True)
    # k-fold
    # genetic algorith

    args = parser.parse_args()
    main(args)

    print(f"--- {str(time.time() - start_time)} seconds main ---")