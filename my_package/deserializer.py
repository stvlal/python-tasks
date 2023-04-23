import pickle
import json
import yaml
from yaml.loader import SafeLoader


def from_pickle(file):
    with open(file, "rb") as f:
        obj = pickle.load(f)
    return obj
    

def from_json(file):
    with open(file, "rt") as f:
        obj = json.load(f)
    return obj



def from_yaml(file):
    with open(file, "rt") as f:
        obj = yaml.load(f, Loader=SafeLoader)
    return obj