from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .label_location import LabelLocation

from .label_location import LabelLocation

@dataclass
class LabelInView(LabelLocation, Parsable):
    # The componentId property
    component_id: Optional[int] = None
    # The header property
    header: Optional[str] = None
    # The viewId property
    view_id: Optional[int] = None
    # The viewName property
    view_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LabelInView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LabelInView
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LabelInView()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .label_location import LabelLocation

        from .label_location import LabelLocation

        fields: dict[str, Callable[[Any], None]] = {
            "componentId": lambda n : setattr(self, 'component_id', n.get_int_value()),
            "header": lambda n : setattr(self, 'header', n.get_str_value()),
            "viewId": lambda n : setattr(self, 'view_id', n.get_int_value()),
            "viewName": lambda n : setattr(self, 'view_name', n.get_str_value()),
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
        writer.write_int_value("componentId", self.component_id)
        writer.write_str_value("header", self.header)
        writer.write_int_value("viewId", self.view_id)
        writer.write_str_value("viewName", self.view_name)
    

