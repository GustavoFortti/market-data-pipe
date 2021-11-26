import os
from config.create_params import return_params

indicator, premodel, model = return_params('1-set')

# print(f'indicator params...\n\t{indicator}')
# os.system(f'python3 ./indicator/main.py {indicator}')

# print(f'premodel params...\n\t{premodel}')
# os.system(f'python3 ./premodel/main.py {premodel}')

print(f'premodel params...\n\t{model}')