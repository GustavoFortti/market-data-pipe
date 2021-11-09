import os
from config.create_params import return_params

indicator, premodel = return_params('1-set')
print(indicator)
os.system(f'python3 ./indicator/main.py {indicator}')

print(premodel)
# -i INDICATOR -d DATE -m D_MATRIX -s VARIABLES
# os.system('python3 ./premodel/main.py')