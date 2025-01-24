# Generated by ariadne-codegen
# Source: queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetMacros(BaseModel):
    environment: "GetMacrosEnvironment"


class GetMacrosEnvironment(BaseModel):
    definition: Optional["GetMacrosEnvironmentDefinition"]


class GetMacrosEnvironmentDefinition(BaseModel):
    macros: "GetMacrosEnvironmentDefinitionMacros"


class GetMacrosEnvironmentDefinitionMacros(BaseModel):
    total_count: int = Field(alias="totalCount")
    page_info: "GetMacrosEnvironmentDefinitionMacrosPageInfo" = Field(alias="pageInfo")
    edges: List["GetMacrosEnvironmentDefinitionMacrosEdges"]


class GetMacrosEnvironmentDefinitionMacrosPageInfo(BaseModel):
    has_next_page: bool = Field(alias="hasNextPage")
    end_cursor: Optional[str] = Field(alias="endCursor")


class GetMacrosEnvironmentDefinitionMacrosEdges(BaseModel):
    node: "GetMacrosEnvironmentDefinitionMacrosEdgesNode"


class GetMacrosEnvironmentDefinitionMacrosEdgesNode(BaseModel):
    description: Optional[str]
    environment_id: Any = Field(alias="environmentId")
    macro_sql: str = Field(alias="macroSql")
    meta: Optional[Any]
    name: Optional[str]
    package_name: Optional[str] = Field(alias="packageName")
    unique_id: str = Field(alias="uniqueId")
    arguments: List["GetMacrosEnvironmentDefinitionMacrosEdgesNodeArguments"]


class GetMacrosEnvironmentDefinitionMacrosEdgesNodeArguments(BaseModel):
    description: Optional[str]
    name: Optional[str]
    type: Optional[str]


GetMacros.model_rebuild()
GetMacrosEnvironment.model_rebuild()
GetMacrosEnvironmentDefinition.model_rebuild()
GetMacrosEnvironmentDefinitionMacros.model_rebuild()
GetMacrosEnvironmentDefinitionMacrosEdges.model_rebuild()
GetMacrosEnvironmentDefinitionMacrosEdgesNode.model_rebuild()
