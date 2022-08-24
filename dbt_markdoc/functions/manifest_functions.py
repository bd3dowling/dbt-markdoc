# from dataclasses import dataclass
from functools import reduce
from typing import Any, MutableMapping, TypeAlias
from dbt.contracts.graph.manifest import Manifest
from dbt.contracts.graph.parsed import ParsedNode, ParsedSourceDefinition, ParsedMacro

NODE_TYPE_MAP = {"macro": "macros", "model": "nodes", "source": "sources"}

GeneralParsedNode: TypeAlias = ParsedNode | ParsedSourceDefinition | ParsedMacro


# @dataclass
# class AugNode:
#     config: NodeConfig
#     tags: list[str]
#     refs: list[list[str]]
#     sources: list[list[str]]
#     depends_on: DependsOn
#     description: str
#     meta: dict[str, Any]
#     columns: dict[str, ColumnInfo]
#     docs: Docs
#     markdoc: str = ""


def standardize_nodes(manifest: Manifest) -> dict[str, dict[str, GeneralParsedNode]]:
    docs = {
        node_type: standardize_sub_manifest_nodes(getattr(manifest, node_orig_type))
        for node_type, node_orig_type in NODE_TYPE_MAP.items()
    }

    return docs


def standardize_sub_manifest_nodes(
    sub_manifest: MutableMapping[str, GeneralParsedNode],
) -> dict[str, GeneralParsedNode]:
    node_type_docs = dict(sub_manifest.items())

    return node_type_docs


def flatten_manifest_nodes(
    standard_manifest: dict[str, dict[str, dict[str, Any]]]
) -> list[dict[str, GeneralParsedNode]]:
    return [*reduce(lambda a, b: a | b, standard_manifest.values()).values()]
