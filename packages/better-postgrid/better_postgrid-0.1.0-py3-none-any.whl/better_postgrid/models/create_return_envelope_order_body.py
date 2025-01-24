from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateReturnEnvelopeOrderBody")


@_attrs_define
class CreateReturnEnvelopeOrderBody:
    """
    Attributes:
        quantity_ordered (Union[Unset, str]):  Example: 100.
    """

    quantity_ordered: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quantity_ordered = self.quantity_ordered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quantity_ordered is not UNSET:
            field_dict["quantityOrdered"] = quantity_ordered

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        quantity_ordered = d.pop("quantityOrdered", UNSET)

        create_return_envelope_order_body = cls(
            quantity_ordered=quantity_ordered,
        )

        create_return_envelope_order_body.additional_properties = d
        return create_return_envelope_order_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
