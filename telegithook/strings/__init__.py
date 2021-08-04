import os
import yaml

from typing import Dict, Union

with open(os.path.join(os.path.dirname(__file__), 'strings.yml')) as f:
    STR : Dict[str, Union[dict,str]] = yaml.safe_load(f.read())

