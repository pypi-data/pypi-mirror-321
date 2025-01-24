from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSessionBody")


@_attrs_define
class CreateSessionBody:
    """
    Attributes:
        back_url (Union[Unset, str]):  Example: https://postgrid.com.
        template (Union[Unset, str]):  Example: template_eYxcbMKPZEZPk71ZJPA6Yz.
        title (Union[Unset, str]):  Example: My Editor Session.
    """

    back_url: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        back_url = self.back_url

        template = self.template

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if back_url is not UNSET:
            field_dict["backURL"] = back_url
        if template is not UNSET:
            field_dict["template"] = template
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        back_url = d.pop("backURL", UNSET)

        template = d.pop("template", UNSET)

        title = d.pop("title", UNSET)

        create_session_body = cls(
            back_url=back_url,
            template=template,
            title=title,
        )

        create_session_body.additional_properties = d
        return create_session_body

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
