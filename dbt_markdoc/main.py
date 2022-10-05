import json
from jinja2 import Environment, PackageLoader
from dbt.contracts.graph.manifest import Manifest

from dbt_markdoc.functions.manifest_functions import standardize_manifest


def main(path: str) -> None:
    # Create Jinja2 environment
    env = Environment(loader=PackageLoader("dbt_markdoc", "templates"))

    # Load and parse manifest JSON
    with open(path, "r+", encoding="utf-8") as stream:
        manifest = Manifest.from_dict(json.load(stream))

    # Standardize and tidy manifest
    standard_manifest = standardize_manifest(manifest)

    print(standard_manifest, env)

    # Filter out DBT nodes
    # models = (
    #     seq(*nodes)
    #     .filter(lambda n: n["package_name"] != "dbt")
    #     .filter(lambda n: not n["package_name"].startswith("dbt_"))
    #     .to_list()
    # )

    # {"markdoc": templates[node.resource_type].render(**node.__dict__)}

    # with open("test_output.md", "w+") as stream:
    #     stream.write(flat_docs["macro.conjura.flag_metric_outliers"])
