from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWebhookBody")


@_attrs_define
class CreateWebhookBody:
    """
    Attributes:
        description (Union[Unset, str]):  Example: Letter Created.
        enabled_events (Union[Unset, str]):  Example: letter.created.
        url (Union[Unset, str]):  Example: https://ac18f0aecb4a.ngrok.io.
    """

    description: Union[Unset, str] = UNSET
    enabled_events: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        enabled_events = self.enabled_events

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if enabled_events is not UNSET:
            field_dict["enabledEvents[]"] = enabled_events
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        enabled_events = d.pop("enabledEvents[]", UNSET)

        url = d.pop("url", UNSET)

        create_webhook_body = cls(
            description=description,
            enabled_events=enabled_events,
            url=url,
        )

        create_webhook_body.additional_properties = d
        return create_webhook_body

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
