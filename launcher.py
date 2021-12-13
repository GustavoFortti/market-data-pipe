import os
from config.create_params import return_params
import time

indicator, premodel, model = return_params(f'1-set')

print(f'indicator params...\n\t{indicator}')
os.system(f'python3 ./indicator/main.py {indicator}')

for i in range(1, 5):
    indicator, premodel, model = return_params(f'{i}-set')

    print(f'premodel params...\n\t{premodel}')
    os.system(f'python3 ./premodel/main.py {premodel}')
    time.sleep(1)

# print(f'model params...\n\t{model}')
# os.system(f'python3 ./model/main.py {model}')

