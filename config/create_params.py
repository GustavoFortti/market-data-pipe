import json

def return_params(set: str) -> str:
    params, projects, variables = open('./config/params.json', 'r'), open('./config/projects.json', 'r'), open('./config/variables.json', 'r')
    params, projects, variables = json.load(params), json.load(projects), json.load(variables)

    params_set = params[set]
    indicator = contruct_param('indicator', projects, params_set, variables)
    premodel = contruct_param('premodel', projects, params_set, variables)
    return [indicator, premodel]

def contruct_param(name: str, projects: dict, params_set: dict, variables: dict):
    params = projects[name]['params_save'][params_set[name]]
    for i in params:
        value = params[i]
        if ('set' in value):
            if (i == 'variables'): params[i] = variables[value]
            elif (i in projects.keys()): 
                params[i] = projects[i]['params_save'][value]
        
    params = [destruct_dict(i, j) for i, j in zip(params.keys(), params.values())]
    params = destruct_list(params)

    for i in projects[name]["params"]: 
        params = params.replace(i, f'|--{i}')
    
    def ax_replace(x, y): 
        for i in x: y = y.replace(i, '')
        return y

    ax_params = []
    for i in f' {params}'.split(' |')[1:]:
        ax_value = i.split(' ')[1:]
        ax_key = i.split(' ')[0]
        ax_params.append(ax_key)
        if (len(ax_value) > 1): 
            ax_params.append(ax_replace([' ', ']', '[', "'"], str(ax_value)))
        else: ax_params.append(str(ax_value[0]))
    params = destruct_list(ax_params)
    return params

def destruct_dict(key: str, value: any):
    if (type(value) == dict): return [destruct_dict(i, j) for i, j in zip(value.keys(), value.values())]
    return [key, value]

def destruct_list(vector: list):
    return ' '.join([destruct_list(i) if (type(i) == list) else i for i in vector])