from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CancelChequeWithNoteResponse200Metadata")


@_attrs_define
class CancelChequeWithNoteResponse200Metadata:
    """
    Attributes:
        postgrid_dashboard (Union[Unset, str]):
    """

    postgrid_dashboard: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        postgrid_dashboard = self.postgrid_dashboard

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if postgrid_dashboard is not UNSET:
            field_dict["postgrid_dashboard"] = postgrid_dashboard

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        postgrid_dashboard = d.pop("postgrid_dashboard", UNSET)

        cancel_cheque_with_note_response_200_metadata = cls(
            postgrid_dashboard=postgrid_dashboard,
        )

        cancel_cheque_with_note_response_200_metadata.additional_properties = d
        return cancel_cheque_with_note_response_200_metadata

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
