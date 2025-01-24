from enum import Enum
from typing import Any, Dict, List, Optional, Type

from pydantic import BaseModel, Field

from utic_public_types.plugins.taxonomy import EncryptionMode
from utic_public_types.plugins.usage import UnstructuredUsageRecord

from .setting_types import PluginSettingsPresentationStructure, PluginSettingsRecipe


class PluginAPIVersion(str, Enum):
    V1 = "1"
    v20241022 = "2"


class PluginIOItemCardinality(str, Enum):
    EXACTLY_ZERO = "exactly-zero"
    EXACTLY_ONE = "exactly-one"
    EXACTLY_TWO = "exactly-two"
    ZERO_OR_ONE = "zero-or-one"  # AKA OPTIONAL ONE
    ZERO_OR_MORE = "zero-or-more"  # AKA ANY or OPTIONAL ANY
    ONE_OR_MORE = "one-or-more"  # AKA ANY BUT AT LEAST ONE


class PluginIOTypeDescriptor(BaseModel):
    name: str = Field(
        title="Input name",
        description="used for UI and observability",
        examples=["Input File", "Prompt Template", "Custom Bucket Reference"],
    )
    compatibility_specifier: str = Field(
        title="Compatibility Specifier",
        description="Follows format: /Structuredness/FormatType/Format/Schemas\n"
        "Any level can include either '*' or the word 'any' to indicate wildcard.\n"
        "The first two segments are otherwise constrained to a defined taxonomy. "
        "The latter two are more open-ended.\n\n"
        "Multiple schemas can be specified using space as delimiter in the last field.\n\n"
        "Any Schema item can begin with the special token 'data' which indicates "
        "RFC 2397 mode, which supports base64-encoded values.\n"
        "This is necessary to support URI-style schema specification.\n"
        "It has the side effect of allowing inline schema definitions!\n\n"
        "https://www.rfc-editor.org/rfc/rfc2397",
        examples=[
            "/structured/text/json/data:;base64,aHR0cHM6Ly9zY2hlbWEub3JnL1BlcnNvbgo=",
            "/*",
        ],
    )
    extra: dict[str, Any] = Field(
        title="Extra Properties",
        description="Given the nature of variety in file formats, this field left open. "
        "Expect future versions to provide more structure to encourage interoperability "
        "between various components that have limited scope.",
        examples=[{"foo": "bar"}],
        default_factory=dict,
    )
    cardinality: PluginIOItemCardinality = Field(
        title="Cardinality",
        description="Express the plugin's one-one, one-many, many-many, many-one character. "
        "This is not related to batching, which is expected to be supported regardless. "
        "Even in a batched setting, if the outputs have a 1-1 with the inputs, then express "
        "your cardinality as one-one. If your output items are a proper aggregation of inputs, "
        "then many-one or many-many as appropriate. Etc.",
    )


class UnstructuredPluginSignature(BaseModel):
    plugin_api_version: PluginAPIVersion = Field(
        title="Plugin API Version",
        description="Version of the Plugin OpenAPI Schema this plugin adheres to",
        default=PluginAPIVersion.V1,
    )
    inputs: List[PluginIOTypeDescriptor] = Field(
        title="Inputs",
        default_factory=list,
    )
    outputs: List[PluginIOTypeDescriptor] = Field(
        title="Outputs",
        default_factory=list,
    )

    @classmethod
    def one_to_one(
        cls,
        intype: str,
        outtype: str,
        plugin_api_version: PluginAPIVersion = PluginAPIVersion.V1,
    ) -> "UnstructuredPluginSignature":
        return cls(
            inputs=[
                PluginIOTypeDescriptor(
                    name="input",
                    compatibility_specifier=intype,
                    cardinality=PluginIOItemCardinality.EXACTLY_ONE,
                )
            ],
            outputs=[
                PluginIOTypeDescriptor(
                    name="output",
                    compatibility_specifier=outtype,
                    cardinality=PluginIOItemCardinality.EXACTLY_ONE,
                )
            ],
            plugin_api_version=plugin_api_version,
        )

    @classmethod
    def side_effect(cls) -> "UnstructuredPluginSignature":
        return cls(inputs=[], outputs=[])

    @classmethod
    def source(cls):
        return cls(
            inputs=[],
            outputs=[
                PluginIOTypeDescriptor(
                    name="files",
                    compatibility_specifier="*",
                    cardinality=PluginIOItemCardinality.ZERO_OR_MORE,
                )
            ],
        )

    @classmethod
    def destination(cls):
        return cls(
            inputs=[
                PluginIOTypeDescriptor(
                    name="files",
                    compatibility_specifier="*",
                    cardinality=PluginIOItemCardinality.ZERO_OR_MORE,
                )
            ],
            outputs=[],
        )


class Presentation(BaseModel):
    narrative_guidance: str = Field(
        "",
        description="Tell the story to the user of what they are about to "
        "do with configuring the plugin.",
        examples=[
            "After selecting the vendor and model, be sure to customize your prompt!",
            "Configure your PII settings here, including which types of data to redact.",
        ],
    )
    structures: Dict[str, PluginSettingsPresentationStructure] = Field(
        title="Presentation Structures",
        description="A dictionary that maps presentation-structure identifiers to those structures. "
        "If there is only one, or if one has the key default, it will be default",
    )
    recipes: Dict[str, PluginSettingsRecipe] = Field(title="Recipes")


class PluginType(BaseModel):
    name: str
    type: str
    subtype: str
    version: str
    image_name: str
    signature: UnstructuredPluginSignature

    settings: Type[BaseModel]
    presentation: Presentation
    metadata: dict[str, str] = {}


class PluginIOLocationType(str, Enum):
    PATH = "path"
    INLINE = "inline"


class PluginInvocationIODescriptor(BaseModel):
    location_type: PluginIOLocationType = Field(
        title="Location Type",
        description="Determines the meaning of the data field. When location_type=path, "
        "data is a path or URL that the recipient is responsible for dereferencing. "
        "When location_type=inline, the data field is the data itself base64 encoded. "
        "Note that additional encoding/processing may be indicated by attributes (example: compression)",
        examples=list(PluginIOLocationType),
    )
    attributes: Dict[str, str] = Field(
        title="Attributes",
        description="For inputs, may indicate information such as compression or other information which "
        "may impact reading the file. For outputs, may indicate desired attributes.",
        examples=[{"compression-level": "9"}, {"encoding": "base64-url"}],
    )
    data: str = Field(
        title="Data",
        description="Either base64 date, or a locator/uri/path the receiver is expected to understand.",
        examples=["/tmp/foo/bar.json", "eyJuYW1lIjoiQ2hyaXMifQo="],
    )


class PluginInvocationInput(BaseModel):
    invocation_settings: dict
    input_descriptors: Dict[str, PluginInvocationIODescriptor] = Field(
        title="Input pointers",
        description="Keys are named inputs, values are a structure indicate location of file and any access attributes",
        examples=[
            {
                "unstructured-document": PluginInvocationIODescriptor(
                    location_type=PluginIOLocationType.INLINE,
                    attributes={},
                    data="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XwEGADGgjcsNZW5kc3RyZWFtDWVuZG9iag0xIDAgb2JqDTw8L0ZpbHRlci9GbGF0ZURlY29kZS9GaXJzdCAxNC9MZW5ndGggMTI2L04gMy9UeXBlL09ialN0bT4+c3RyZWFtDQpo3jJTMFAwVzCxVLBQsDRSsLHRd84vzStRMNR3yywqLgFKGSgE6fskwpkhlQWp+v6lJTmZeanFdnZADY5ArSCZgMSiVKBOM4iyzJKcVA2nnMS8bIWAxPRUTbBSl2hDY7B0RGQUyF6gjXmlOTmx+sH67vkh+XZ2AAEGAKanJzYNZW5kc3RyZWFtDWVuZG9iag0yIDAgb2JqDTw8L0xlbmd0aCAzMTcwL1N1YnR5cGUvWE1ML1R5cGUvTWV0YWRhdGE+PnN0cmVhbQ0KPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgOS4xLWMwMDEgNzkuNjc1ZDBmNywgMjAyMy8wNi8xMS0xOToyMToxNiAgICAgICAgIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIgogICAgICAgICAgICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgICAgICAgICAgIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIgogICAgICAgICAgICB4bWxuczpwZGY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGRmLzEuMy8iPgogICAgICAgICA8eG1wOk1vZGlmeURhdGU+MjAyNC0xMC0yMVQxNzo1NDoyMC0wNzowMDwveG1wOk1vZGlmeURhdGU+CiAgICAgICAgIDx4bXA6Q3JlYXRlRGF0ZT4yMDI0LTEwLTIxVDE3OjUxOjQ0LTA3OjAwPC94bXA6Q3JlYXRlRGF0ZT4KICAgICAgICAgPHhtcDpNZXRhZGF0YURhdGU+MjAyNC0xMC0yMVQxNzo1NDoyMC0wNzowMDwveG1wOk1ldGFkYXRhRGF0ZT4KICAgICAgICAgPHhtcDpDcmVhdG9yVG9vbD5BY3JvYmF0IFBybyAyNC4zLjIwMTgwPC94bXA6Q3JlYXRvclRvb2w+CiAgICAgICAgIDxkYzpmb3JtYXQ+YXBwbGljYXRpb24vcGRmPC9kYzpmb3JtYXQ+CiAgICAgICAgIDx4bXBNTTpEb2N1bWVudElEPnV1aWQ6MmQxMzc4YzItOGJkZS1lNTQ0LThiYjAtZDE1NTUxYzBhM2NiPC94bXBNTTpEb2N1bWVudElEPgogICAgICAgICA8eG1wTU06SW5zdGFuY2VJRD51dWlkOmE0YmRhYWExLWMxNWEtNzE0OC05MzFlLTgxYzFlNTM2ZGYwNTwveG1wTU06SW5zdGFuY2VJRD4KICAgICAgICAgPHBkZjpQcm9kdWNlcj5BY3JvYmF0IFBybyAyNC4zLjIwMTgwPC9wZGY6UHJvZHVjZXI+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz4NZW5kc3RyZWFtDWVuZG9iag0zIDAgb2JqDTw8L0ZpbHRlci9GbGF0ZURlY29kZS9GaXJzdCA0L0xlbmd0aCA0OS9OIDEvVHlwZS9PYmpTdG0+PnN0cmVhbQ0KaN6yVDBQsLHRd84vzStRMNT3zkwpjjY0BgoGxeqHVBak6gckpqcW29kBBBgA4DULrw1lbmRzdHJlYW0NZW5kb2JqDTQgMCBvYmoNPDwvRmlsdGVyL0ZsYXRlRGVjb2RlL0ZpcnN0IDUvTGVuZ3RoIDEwNS9OIDEvVHlwZS9PYmpTdG0+PnN0cmVhbQ0KaN4yNFAwULCx0XcuSk0syczPc0ksSdVwsTIyMDIxNDAyNDQ3NTQx0TUwVzcwUNeEqMov0nBMLspPSixRCCjKVzAy0TPWMzIwtDDQ1PfNT8E0wMTIAG4AUENKaXIqThPs7AACDAD7nSZmDWVuZHN0cmVhbQ1lbmRvYmoNNSAwIG9iag08PC9EZWNvZGVQYXJtczw8L0NvbHVtbnMgNC9QcmVkaWN0b3IgMTI+Pi9GaWx0ZXIvRmxhdGVEZWNvZGUvSURbPDMyRUJDMTFEOTFFRTRBNTBCRUJCRDFBQUFBRUVCOEUxPjxFMEE5OTFFOUUzNUU0MzEyOTAyRUFFRDNDMTUzNEIwQz5dL0luZm8gMTAgMCBSL0xlbmd0aCA0OC9Sb290IDEyIDAgUi9TaXplIDExL1R5cGUvWFJlZi9XWzEgMiAxXT4+c3RyZWFtDQpo3mJiAAImRoltDEwMjLeBBO86IMHQA+IeBUrcLARxGRhhBNM/IMHIABBgALHiBh0NZW5kc3RyZWFtDWVuZG9iag1zdGFydHhyZWYNMTE2DSUlRU9GDQ==",
                )
            }
        ],
    )
    output_descriptors: Dict[str, PluginInvocationIODescriptor] = Field(
        title="Output pointers",
        description="Keys are output names, "
        "values are a structure indicating where plugin should place the file.",
    )


class PluginEncryptionProfile(BaseModel):
    policy: EncryptionMode = Field(
        title="Encryption Mode", description="If encryption is required or disabled."
    )
    encryption_certificate_chain: str = Field(
        title="Encryption Certificate with Chain",
        description="Encryption Certificate in PEM format, including chain through a root trusted by Platform. "
        "Do NOT include private key in the value! "
        "Order the certificates with leaf first and topmost last. "
        "You are not required to include the root certificate, but the last cert "
        "in your chain should be directly signed by it.",
        examples=["-----BEGIN CERTIFICATE-----\n....\n-----END CERTIFICATE-----"],
    )


class PluginInvocationOutput(BaseModel):
    usage: list[UnstructuredUsageRecord]
    status_code: int = Field(
        200, ge=100, lt=600, description="Indicate any upstream status"
    )
    status_code_text: Optional[str] = None
    output: Dict[str, PluginInvocationIODescriptor] = Field(
        description="Output of the plugin. Keys are the corresponding output names (per Schema) and values "
        "are structures indicating if the result was placed in a local file or is inline"
    )
