from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWebhookBody")


@_attrs_define
class UpdateWebhookBody:
    """
    Attributes:
        description (Union[Unset, str]):  Example: Letter creates and updates.
        enabled (Union[Unset, str]):  Example: true.
        enabled_events (Union[Unset, str]):  Example: letter.updated.
        metadatahooks (Union[Unset, str]):  Example: update.
        url (Union[Unset, str]):  Example: https://1cca5bfb3056.ngrok.io.
    """

    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, str] = UNSET
    enabled_events: Union[Unset, str] = UNSET
    metadatahooks: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        enabled = self.enabled

        enabled_events = self.enabled_events

        metadatahooks = self.metadatahooks

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if enabled_events is not UNSET:
            field_dict["enabledEvents[]"] = enabled_events
        if metadatahooks is not UNSET:
            field_dict["metadata[hooks]"] = metadatahooks
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        enabled_events = d.pop("enabledEvents[]", UNSET)

        metadatahooks = d.pop("metadata[hooks]", UNSET)

        url = d.pop("url", UNSET)

        update_webhook_body = cls(
            description=description,
            enabled=enabled,
            enabled_events=enabled_events,
            metadatahooks=metadatahooks,
            url=url,
        )

        update_webhook_body.additional_properties = d
        return update_webhook_body

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
