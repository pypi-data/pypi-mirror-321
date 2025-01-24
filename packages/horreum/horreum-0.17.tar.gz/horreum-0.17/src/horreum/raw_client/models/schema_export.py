from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .label import Label
    from .schema import Schema
    from .transformer import Transformer

from .schema import Schema

@dataclass
class SchemaExport(Schema, Parsable):
    """
    Represents a Schema with all associated data used for export/import operations.
    """
    # Array of Labels associated with schema
    labels: Optional[list[Label]] = None
    # Array of Transformers associated with schema
    transformers: Optional[list[Transformer]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SchemaExport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SchemaExport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SchemaExport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .label import Label
        from .schema import Schema
        from .transformer import Transformer

        from .label import Label
        from .schema import Schema
        from .transformer import Transformer

        fields: dict[str, Callable[[Any], None]] = {
            "labels": lambda n : setattr(self, 'labels', n.get_collection_of_object_values(Label)),
            "transformers": lambda n : setattr(self, 'transformers', n.get_collection_of_object_values(Transformer)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("labels", self.labels)
        writer.write_collection_of_object_values("transformers", self.transformers)
    

