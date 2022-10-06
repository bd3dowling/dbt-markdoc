from jinja2 import Environment

from dbt_markdoc.models.standard_manifest import StandardManifest
from dbt_markdoc.functions.markdown_functions import generate_docs


def test_generate_docs(jinja_env: Environment, std_manifest: StandardManifest) -> None:
    assert generate_docs(jinja_env, std_manifest, ["conjura"]) is None
