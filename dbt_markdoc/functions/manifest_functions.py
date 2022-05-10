from dataclasses import dataclass
from functools import reduce
from typing import MutableMapping
from jinja2 import Environment
from dbt.contracts.graph.manifest import Manifest
from dbt.contracts.graph.parsed import ParsedNode, ParsedSourceDefinition, ParsedMacro

NODE_TYPE_MAP = {"macro": "macros", "model": "nodes", "source": "sources"}

GeneralParsedNode = ParsedNode | ParsedSourceDefinition | ParsedMacro

# ParsedNode does not encompass all props of sources and macros...
# TODO: Make own complete wrapper class to import here
@dataclass
class AugNode(ParsedNode):
    markdoc: str = ""


def standardize_nodes(manifest: Manifest, env: Environment) -> dict[str, dict[str, AugNode]]:
    docs = {
        node_type: standardize_sub_manifest_nodes(
            getattr(manifest, NODE_TYPE_MAP[node_type]), env
        )
        for node_type in NODE_TYPE_MAP.keys()
    }

    return docs


def standardize_sub_manifest_nodes(
    sub_manifest: MutableMapping[str, GeneralParsedNode], env: Environment
) -> dict[str, AugNode]:
    sub_manifest_resource_types = {node.resource_type for node in sub_manifest.values()}

    # TODO: Reparse node into AugNode once definition made
    node_type_docs = {
        node_id: node
        for node_id, node in sub_manifest.items()
    }

    return node_type_docs


def flatten_manifest_nodes(
    standard_manifest: dict[str, dict[str, AugNode]]
) -> list[dict[str, AugNode]]:
    return [*reduce(lambda a, b: a | b, standard_manifest.values()).values()]
