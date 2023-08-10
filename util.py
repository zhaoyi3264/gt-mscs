import json
import os

def get_title():
    return 'Georgia Tech MSCS Tracks'

def load_json(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data

def load_json_in(data_dir, file_name):
    return load_json(os.path.join(data_dir, file_name))

def to_json(file_name, obj):
    with open(file_name, 'w') as f:
        json.dump(obj, f, indent=4)

def to_json_in(data_dir, file_name, obj):
    to_json(os.path.join(data_dir, file_name), obj)

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
