from pathlib import Path
from typing import cast
from jinja2 import Environment
from dbt.node_types import NodeType

from dbt_markdoc.models.standard_manifest import StandardManifest, StandardSource


def generate_docs(env: Environment, manifest: StandardManifest, allowed_packages: list[str] | None = None) -> None:
    templates = {
        node_type: env.get_template(f"{node_type.value}.md")
        for node_type in (NodeType.Model, NodeType.Source, NodeType.Macro)
    }

    merged_manifest = manifest.nodes | manifest.macros

    for _, node in merged_manifest.items():
        node_type = node.resource_type

        if not isinstance(node, StandardSource) and not node.show_docs:
            continue

        if allowed_packages and node.package_name not in allowed_packages:
            continue

        template = templates[node_type]

        node_dependencies = (
            {
                dependency_type: [
                    {"name": dependency.name, "path": dependency.path}
                    for dependency_id in dependencies
                    if (dependency := merged_manifest[dependency_id])
                ]
                for dependency_type, dependencies in (
                    ("models", [node for node in node.depends_on.nodes if node.startswith("model")]),
                    ("sources", [node for node in node.depends_on.nodes if node.startswith("source")]),
                    ("macros", node.depends_on.macros),
                )
            }
            if not isinstance(node, StandardSource)
            else {}
        )

        template_dict = node.dict() | {"depends_on": node_dependencies}
        rendered_template = cast(str, template.render(**template_dict))

        file = Path("output") / f"{node_type.value}s" / f"{node.id}.md"
        file.parent.mkdir(exist_ok=True, parents=True)
        file.write_text(rendered_template)
