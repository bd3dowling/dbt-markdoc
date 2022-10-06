from pydantic import BaseModel, Field
from dbt.node_types import NodeType


class StandardNodeConfig(BaseModel):
    enabled: bool
    post_hook: list[str]
    pre_hook: list[str]


class StandardSourceConfig(BaseModel):
    enabled: bool


class StandardDependencies(BaseModel):
    macros: list[str] = []
    nodes: list[str] = []


class StandardColumnInfo(BaseModel):
    name: str
    description: str
    data_type: str
    tags: list[str]


class StandardMacroArg(BaseModel):
    name: str
    type: str
    description: str


class StandardModel(BaseModel):
    id: str
    name: str
    config: StandardNodeConfig
    tags: list[str]
    description: str
    columns: list[StandardColumnInfo]
    depends_on: StandardDependencies
    show_docs: bool
    database: str
    schema_: str = Field(aliases=["schema"])
    raw_sql: str
    path: str
    package_name: str
    resource_type: NodeType = NodeType.Model


class StandardSource(BaseModel):
    id: str
    name: str
    config: StandardSourceConfig
    tags: list[str]
    description: str
    columns: list[StandardColumnInfo]
    database: str
    schema_: str = Field(aliases=["schema"])
    identifier: str
    source_name: str
    source_description: str
    path: str
    package_name: str
    resource_type: NodeType = NodeType.Source


class StandardMacro(BaseModel):
    id: str
    name: str
    macro_sql: str
    depends_on: StandardDependencies
    arguments: list[StandardMacroArg]
    description: str
    show_docs: bool
    usage_info: str
    path: str
    package_name: str
    resource_type: NodeType = NodeType.Macro


class StandardManifest(BaseModel):
    nodes: dict[str, StandardModel | StandardSource]
    macros: dict[str, StandardMacro]
