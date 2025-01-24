from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CancelChequeWithNoteResponse200ToMetadata")


@_attrs_define
class CancelChequeWithNoteResponse200ToMetadata:
    """
    Attributes:
        company_name (Union[Unset, str]):  Example: Axiom Space.
    """

    company_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_name = self.company_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_name is not UNSET:
            field_dict["Company name"] = company_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        company_name = d.pop("Company name", UNSET)

        cancel_cheque_with_note_response_200_to_metadata = cls(
            company_name=company_name,
        )

        cancel_cheque_with_note_response_200_to_metadata.additional_properties = d
        return cancel_cheque_with_note_response_200_to_metadata

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
