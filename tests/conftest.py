import json
from importlib.resources import path

from dbt.contracts.graph.manifest import Manifest
from dbt_markdoc.functions.manifest_functions import standardize_manifest
from dbt_markdoc.models.standard_manifest import StandardManifest
from jinja2 import Environment, PackageLoader
from pytest import fixture

import tests.data as data


@fixture
def manifest() -> Manifest:
    with path(data, "manifest.json") as manifest_path:
        with open(manifest_path) as manifest_file:
            return Manifest.from_dict(json.load(manifest_file))


@fixture
def std_manifest(manifest: Manifest) -> StandardManifest:
    return standardize_manifest(manifest)


@fixture
def jinja_env() -> Environment:
    return Environment(loader=PackageLoader("dbt_markdoc.data", "templates"))
