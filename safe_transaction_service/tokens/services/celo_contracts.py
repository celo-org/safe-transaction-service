import json
import os

module_dir = os.path.dirname(__file__)  # get current directory

registry_abi = json.loads(open(os.path.join(module_dir, "Registry.json"), "r").read())
