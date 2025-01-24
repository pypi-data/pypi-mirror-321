from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateReturnEnvelopeOrderResponse201")


@_attrs_define
class CreateReturnEnvelopeOrderResponse201:
    """
    Attributes:
        created_at (Union[Unset, str]):  Example: 2021-12-16T03:23:22.617Z.
        id (Union[Unset, str]):  Example: return_envelope_order_cJhFxQhs69MGhxu3L5NvyA.
        live (Union[Unset, bool]):
        object_ (Union[Unset, str]):  Example: return_envelope_order.
        quantity_ordered (Union[Unset, float]):  Example: 100.
        return_envelope (Union[Unset, str]):  Example: return_envelope_7mhJUt25TnagyYzy1N81SJ.
        status (Union[Unset, str]):  Example: placed.
        updated_at (Union[Unset, str]):  Example: 2021-12-16T03:23:22.617Z.
    """

    created_at: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    object_: Union[Unset, str] = UNSET
    quantity_ordered: Union[Unset, float] = UNSET
    return_envelope: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        live = self.live

        object_ = self.object_

        quantity_ordered = self.quantity_ordered

        return_envelope = self.return_envelope

        status = self.status

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if live is not UNSET:
            field_dict["live"] = live
        if object_ is not UNSET:
            field_dict["object"] = object_
        if quantity_ordered is not UNSET:
            field_dict["quantityOrdered"] = quantity_ordered
        if return_envelope is not UNSET:
            field_dict["returnEnvelope"] = return_envelope
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("createdAt", UNSET)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        object_ = d.pop("object", UNSET)

        quantity_ordered = d.pop("quantityOrdered", UNSET)

        return_envelope = d.pop("returnEnvelope", UNSET)

        status = d.pop("status", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        create_return_envelope_order_response_201 = cls(
            created_at=created_at,
            id=id,
            live=live,
            object_=object_,
            quantity_ordered=quantity_ordered,
            return_envelope=return_envelope,
            status=status,
            updated_at=updated_at,
        )

        create_return_envelope_order_response_201.additional_properties = d
        return create_return_envelope_order_response_201

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
