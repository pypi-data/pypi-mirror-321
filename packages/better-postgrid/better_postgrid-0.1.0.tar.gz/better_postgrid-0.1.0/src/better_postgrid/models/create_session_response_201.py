from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSessionResponse201")


@_attrs_define
class CreateSessionResponse201:
    """
    Attributes:
        created_at (Union[Unset, str]):  Example: 2023-07-05T19:36:01.369Z.
        id (Union[Unset, str]):  Example:
            template_editor_session_bBYRQ5DKu3LJ5yNemoAQ7E3or6E7Yzd7FGNWJSXBRrAfcdoNXNGLvfZxAm2dJYiv9c.
        live (Union[Unset, bool]):
        object_ (Union[Unset, str]):  Example: template_editor_session.
        template (Union[Unset, str]):  Example: template_eYxcbMKPZEZPk71ZJPA6Yz.
        url (Union[Unset, str]):  Example: https://dashboard.postgrid.com/embed/template_editor_sessions/template_editor
            _session_bBYRQ5DKu3LJ5yNemoAQ7E3or6E7Yzd7FGNWJSXBRrAfcdoNXNGLvfZxAm2dJYiv9c.
    """

    created_at: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    object_: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        live = self.live

        object_ = self.object_

        template = self.template

        url = self.url

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
        if template is not UNSET:
            field_dict["template"] = template
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("createdAt", UNSET)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        object_ = d.pop("object", UNSET)

        template = d.pop("template", UNSET)

        url = d.pop("url", UNSET)

        create_session_response_201 = cls(
            created_at=created_at,
            id=id,
            live=live,
            object_=object_,
            template=template,
            url=url,
        )

        create_session_response_201.additional_properties = d
        return create_session_response_201

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
