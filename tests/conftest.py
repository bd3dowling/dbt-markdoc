import json
from importlib.resources import path
from typing import Any

from dbt.contracts.graph.manifest import Manifest
from pytest import fixture

import tests.data as data


@fixture
def manifest() -> Any:
    with path(data, "manifest.json") as manifest_path:
        with open(manifest_path) as manifest_file:
            return Manifest.from_dict(json.load(manifest_file))
