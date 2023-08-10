import json
import os

import streamlit as st

def set_title(subtitle=''):
    title = 'Georgia Tech MSCS Tracks' + (f': {subtitle}' if subtitle else '')
    st.set_page_config(page_title=title, page_icon=':computer:')
    st.markdown(f'# :computer: {title}')

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
