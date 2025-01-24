from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_return_envelope_response_201_to import CreateReturnEnvelopeResponse201To


T = TypeVar("T", bound="CreateReturnEnvelopeResponse201")


@_attrs_define
class CreateReturnEnvelopeResponse201:
    """
    Attributes:
        available (Union[Unset, float]):
        created_at (Union[Unset, str]):  Example: 2021-12-16T03:06:17.419Z.
        id (Union[Unset, str]):  Example: return_envelope_7mhJUt25TnagyYzy1N81SJ.
        live (Union[Unset, bool]):
        object_ (Union[Unset, str]):  Example: return_envelope.
        to (Union[Unset, CreateReturnEnvelopeResponse201To]):
        updated_at (Union[Unset, str]):  Example: 2021-12-16T03:06:17.419Z.
    """

    available: Union[Unset, float] = UNSET
    created_at: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    object_: Union[Unset, str] = UNSET
    to: Union[Unset, "CreateReturnEnvelopeResponse201To"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available = self.available

        created_at = self.created_at

        id = self.id

        live = self.live

        object_ = self.object_

        to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available is not UNSET:
            field_dict["available"] = available
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if live is not UNSET:
            field_dict["live"] = live
        if object_ is not UNSET:
            field_dict["object"] = object_
        if to is not UNSET:
            field_dict["to"] = to
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_return_envelope_response_201_to import CreateReturnEnvelopeResponse201To

        d = src_dict.copy()
        available = d.pop("available", UNSET)

        created_at = d.pop("createdAt", UNSET)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        object_ = d.pop("object", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, CreateReturnEnvelopeResponse201To]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = CreateReturnEnvelopeResponse201To.from_dict(_to)

        updated_at = d.pop("updatedAt", UNSET)

        create_return_envelope_response_201 = cls(
            available=available,
            created_at=created_at,
            id=id,
            live=live,
            object_=object_,
            to=to,
            updated_at=updated_at,
        )

        create_return_envelope_response_201.additional_properties = d
        return create_return_envelope_response_201

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
