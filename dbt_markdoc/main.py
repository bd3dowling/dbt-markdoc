import json
from jinja2 import Environment, PackageLoader
from dbt.contracts.graph.manifest import Manifest
from dbt_markdoc.functions.manifest_functions import flatten_manifest_nodes, standardize_nodes


def main(path):
    # Create Jinja2 environment
    env = Environment(loader=PackageLoader("dbt_markdoc", "templates"))

    # Load and parse manifest JSON
    with open(path, "r+") as stream:
        manifest = Manifest.from_dict(json.load(stream))

    # Add documentation to manifest nodes
    standard_manifest = standardize_nodes(manifest, env)

    # Flatten node hierarchy to list of nodes
    nodes = flatten_manifest_nodes(standard_manifest)

    # Filter out DBT nodes
    # models = (
    #     seq(*nodes)
    #     .filter(lambda n: n["package_name"] != "dbt")
    #     .filter(lambda n: not n["package_name"].startswith("dbt_"))
    #     .to_list()
    # )

    return nodes

    # {"markdoc": templates[node.resource_type].render(**node.__dict__)}

    # with open("test_output.md", "w+") as stream:
    #     stream.write(flat_docs["macro.conjura.flag_metric_outliers"])
