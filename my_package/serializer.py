import pickle
import json
import yaml


def to_pickle(obj, file):
    with open(file, 'wb') as fd:
        pickle.dump(obj, fd, pickle.HIGHEST_PROTOCOL)
 

def to_json(obj, file):
    with open(file, 'wt') as fd:
        json.dump(obj, fd)


def to_yaml(obj, file):
    with open(file, 'wt') as fd:
        yaml.dump(obj, fd)