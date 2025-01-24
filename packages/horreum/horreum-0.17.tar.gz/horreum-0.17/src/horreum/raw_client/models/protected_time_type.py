from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .protected_time_type_access import ProtectedTimeType_access

@dataclass
class ProtectedTimeType(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Access rights for the test. This defines the visibility of the Test in the UI
    access: Optional[ProtectedTimeType_access] = None
    # Name of the team that owns the test. Users must belong to the team that owns a test to make modifications
    owner: Optional[str] = None
    # Run Start timestamp
    start: Optional[int] = None
    # Run Stop timestamp
    stop: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProtectedTimeType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProtectedTimeType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProtectedTimeType()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .protected_time_type_access import ProtectedTimeType_access

        from .protected_time_type_access import ProtectedTimeType_access

        fields: dict[str, Callable[[Any], None]] = {
            "access": lambda n : setattr(self, 'access', n.get_enum_value(ProtectedTimeType_access)),
            "owner": lambda n : setattr(self, 'owner', n.get_str_value()),
            "start": lambda n : setattr(self, 'start', n.get_int_value()),
            "stop": lambda n : setattr(self, 'stop', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("access", self.access)
        writer.write_str_value("owner", self.owner)
        writer.write_int_value("start", self.start)
        writer.write_int_value("stop", self.stop)
        writer.write_additional_data_value(self.additional_data)
    

