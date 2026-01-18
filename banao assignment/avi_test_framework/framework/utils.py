import yaml

def load_yaml_file(path ="config/config.yaml"):
    with open(path,"r+") as yaml_file:
        return yaml_file
