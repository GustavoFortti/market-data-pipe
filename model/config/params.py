import json

def read_params(variables: str):
    params = json.load(open('./config/variables.json', 'r'))
    return params[variables]