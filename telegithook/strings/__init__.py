import os
import yaml

with open(os.path.join(os.path.dirname(__file__), 'strings.yml')) as f:
    STR = yaml.safe_load(f.read())

