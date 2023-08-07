import json

def load_json(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data

def to_json(file_name, obj):
    with open(file_name, 'w') as f:
        json.dump(obj, f, indent=4)

def map_dict_value(d, func, *args):
    return dict(map(lambda k: (k, func(d[k], *args)), d))

def flatten(l):
    flat = []
    for e in l:
        if type(e) == list:
            for nested_e in flatten(e):
                flat.append(nested_e)
        else:
            flat.append(e)
    return flat