from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTemplateResponse200")


@_attrs_define
class UpdateTemplateResponse200:
    """
    Attributes:
        created_at (Union[Unset, str]):  Example: 2020-11-12T23:23:47.974Z.
        description (Union[Unset, str]):  Example: Test.
        html (Union[Unset, str]):  Example: <b>Hello</b> updated world!.
        id (Union[Unset, str]):  Example: template_tBnVEzz878mXLbHQaz86j8.
        live (Union[Unset, bool]):
        object_ (Union[Unset, str]):  Example: template.
        updated_at (Union[Unset, str]):  Example: 2020-11-13T01:06:42.336Z.
    """

    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    html: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    object_: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        description = self.description

        html = self.html

        id = self.id

        live = self.live

        object_ = self.object_

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if html is not UNSET:
            field_dict["html"] = html
        if id is not UNSET:
            field_dict["id"] = id
        if live is not UNSET:
            field_dict["live"] = live
        if object_ is not UNSET:
            field_dict["object"] = object_
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

        html = d.pop("html", UNSET)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        object_ = d.pop("object", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        update_template_response_200 = cls(
            created_at=created_at,
            description=description,
            html=html,
            id=id,
            live=live,
            object_=object_,
            updated_at=updated_at,
        )

        update_template_response_200.additional_properties = d
        return update_template_response_200

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
