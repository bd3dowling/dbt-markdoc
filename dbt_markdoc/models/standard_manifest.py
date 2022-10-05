from pydantic import BaseModel, Field


class StandardNodeConfig(BaseModel):
    enabled: bool
    post_hook: list[str]
    pre_hook: list[str]


class StandardSourceConfig(BaseModel):
    enabled: bool


class StandardDependencies(BaseModel):
    macros: list[str] = []
    nodes: list[str] = []
    sources: list[str] = []


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
    columns: dict[str, StandardColumnInfo]
    depends_on: StandardDependencies
    show_docs: bool
    database: str
    schema_: str = Field(aliases=["schema"])
    raw_sql: str
    path: str
    package_name: str


class StandardSource(BaseModel):
    id: str
    name: str
    config: StandardSourceConfig
    tags: list[str]
    description: str
    columns: dict[str, StandardColumnInfo]
    database: str
    schema_: str = Field(aliases=["schema"])
    identifier: str
    source_name: str
    source_description: str
    path: str
    package_name: str


class StandardMacro(BaseModel):
    id: str
    name: str
    macro_sql: str
    depends_on: StandardDependencies
    arguments: list[StandardMacroArg]
    description: str
    show_docs: bool
    path: str
    package_name: str


class StandardManifest(BaseModel):
    models: dict[str, StandardModel]
    sources: dict[str, StandardSource]
    macros: dict[str, StandardMacro]
