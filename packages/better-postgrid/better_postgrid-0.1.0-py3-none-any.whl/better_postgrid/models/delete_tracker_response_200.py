from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteTrackerResponse200")


@_attrs_define
class DeleteTrackerResponse200:
    """
    Attributes:
        deleted (Union[Unset, bool]):  Example: True.
        id (Union[Unset, str]):  Example: tracker_123456789abcdefghijklmnopqrstuvwxyz.
    """

    deleted: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted = self.deleted

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        deleted = d.pop("deleted", UNSET)

        id = d.pop("id", UNSET)

        delete_tracker_response_200 = cls(
            deleted=deleted,
            id=id,
        )

        delete_tracker_response_200.additional_properties = d
        return delete_tracker_response_200

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
