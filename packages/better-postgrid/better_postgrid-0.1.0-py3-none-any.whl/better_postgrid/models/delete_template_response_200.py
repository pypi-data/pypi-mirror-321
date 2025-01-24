from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteTemplateResponse200")


@_attrs_define
class DeleteTemplateResponse200:
    """
    Attributes:
        deleted (Union[Unset, bool]):  Example: True.
        id (Union[Unset, str]):  Example: template_c6HSqnsD1h2zoeHJ6Z9EEA.
        object_ (Union[Unset, str]):  Example: template.
    """

    deleted: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    object_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted = self.deleted

        id = self.id

        object_ = self.object_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if id is not UNSET:
            field_dict["id"] = id
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        deleted = d.pop("deleted", UNSET)

        id = d.pop("id", UNSET)

        object_ = d.pop("object", UNSET)

        delete_template_response_200 = cls(
            deleted=deleted,
            id=id,
            object_=object_,
        )

        delete_template_response_200.additional_properties = d
        return delete_template_response_200

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
