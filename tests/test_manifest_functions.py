from dbt.contracts.graph.manifest import Manifest
from dbt_markdoc.functions.manifest_functions import standardize_manifest


def test_standardize_manifest_full(manifest: Manifest) -> None:
    standardized_manifest = standardize_manifest(manifest)

    assert standardized_manifest is not None
