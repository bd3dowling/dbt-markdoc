from typing import cast, MutableMapping

from dbt.contracts.graph.manifest import Manifest
from dbt.contracts.graph.compiled import ManifestNode
from dbt.contracts.graph.parsed import ParsedModelNode, ParsedSourceDefinition, ParsedMacro
from dbt.node_types import NodeType

from dbt_markdoc.models.standard_manifest import (
    StandardColumnInfo,
    StandardDependencies,
    StandardMacroArg,
    StandardManifest,
    StandardModel,
    StandardNodeConfig,
    StandardSource,
    StandardMacro,
    StandardSourceConfig,
)


def standardize_manifest(manifest: Manifest) -> StandardManifest:
    return StandardManifest(
        nodes=standardize_models(manifest.nodes) | standardize_sources(manifest.sources),
        macros=standardize_macros(manifest.macros),
    )


def standardize_models(manifest_nodes: MutableMapping[str, ManifestNode]) -> dict[str, StandardModel]:
    model_nodes = cast(
        dict[str, ParsedModelNode],
        {node_id: node for node_id, node in manifest_nodes.items() if node.resource_type == NodeType.Model},
    )

    return {
        node_id: StandardModel(
            id=node.unique_id,
            name=node.name,
            config=StandardNodeConfig(
                enabled=node.config.enabled,
                post_hook=[hook.sql for hook in node.config.post_hook],
                pre_hook=[hook.sql for hook in node.config.pre_hook],
            ),
            tags=node.tags,
            description=node.description,
            columns=[
                StandardColumnInfo(
                    name=col.name,
                    description=col.description,
                    data_type=col.data_type or "",
                    tags=col.tags,
                )
                for col in node.columns.values()
            ],
            depends_on=StandardDependencies(
                nodes=node.depends_on.nodes,
                macros=node.depends_on.macros,
            ),
            show_docs=node.docs.show,
            database=node.database or "",
            schema_=node.schema,
            raw_sql=node.raw_sql,
            path=node.path,
            package_name=node.package_name,
        )
        for node_id, node in model_nodes.items()
    }


def standardize_sources(manifest_sources: MutableMapping[str, ParsedSourceDefinition]) -> dict[str, StandardSource]:
    return {
        source_id: StandardSource(
            id=source.unique_id,
            name=source.name,
            config=StandardSourceConfig(enabled=source.config.enabled),
            tags=source.tags,
            description=source.description,
            columns=[
                StandardColumnInfo(
                    name=col.name,
                    description=col.description,
                    data_type=col.data_type or "",
                    tags=col.tags,
                )
                for col in source.columns.values()
            ],
            database=source.database or "",
            schema_=source.schema,
            identifier=source.identifier,
            source_name=source.source_name,
            source_description=source.source_description,
            path=source.path,
            package_name=source.package_name,
        )
        for source_id, source in manifest_sources.items()
    }


def standardize_macros(manifest_macros: MutableMapping[str, ParsedMacro]) -> dict[str, StandardMacro]:
    return {
        macro_id: StandardMacro(
            id=macro.unique_id,
            name=macro.name,
            macro_sql=macro.macro_sql,
            depends_on=StandardDependencies(macros=macro.depends_on.macros),
            arguments=[
                StandardMacroArg(name=arg.name, type=arg.type or "", description=arg.description)
                for arg in macro.arguments
            ],
            description=macro.description,
            usage_info=macro.meta.get("usage", ""),
            show_docs=macro.docs.show,
            path=macro.path,
            package_name=macro.package_name,
        )
        for macro_id, macro in manifest_macros.items()
    }
