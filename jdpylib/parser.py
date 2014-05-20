import yaml
import json

from collections import OrderedDict

from jdpylib.errors import InvalidYAML


def load_yaml_ordered(stream, Loader=yaml.Loader,
                        object_pairs_hook=OrderedDict):
    """
    Loads YAML into an ordered dict (maintaining original order)

    Based on http://stackoverflow.com/questions/5121931/in-python-how-can-you-load-yaml-mappings-as-ordereddicts
    """
    class OrderedLoader(yaml.Loader):
        pass

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        lambda loader, node: object_pairs_hook(
            loader.construct_pairs(node)))

    return yaml.load(stream, OrderedLoader)



def yaml_to_json(yaml_str):
    """
    Converts YAML to JSON - maintains order of original YAML
    """
    try:
        yaml_ordered = load_yaml_ordered(yaml_str)
        return json.dumps(yaml_ordered)
    except yaml.YAMLError, e:
        raise InvalidYAML(e)
