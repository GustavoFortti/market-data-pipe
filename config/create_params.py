import json

def return_params(set: str) -> str:
    read_json = lambda file: json.load(open(f'./config/{file}.json', 'r'))
    params, projects = read_json('params'), read_json('projects')
    params_set = params[set]

    ax_contruct_param = lambda project: contruct_param(project, projects, params_set)

    indicator = ax_contruct_param('indicator')
    premodel = ax_contruct_param('premodel')
    model = ax_contruct_param('model')

    return [indicator, premodel, model]

def contruct_param(name: str, projects: dict, params_set: dict):
    params = projects[name]['params_save'][params_set[name]]
    for i in params:
        value = params[i]
        if ('set' in value):
            if (i in projects.keys()): 
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