from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListWebhooksResponse200DataItem")


@_attrs_define
class ListWebhooksResponse200DataItem:
    """
    Attributes:
        created_at (Union[Unset, str]):  Example: 2021-04-02T03:11:01.158Z.
        description (Union[Unset, str]):  Example: Letter Created.
        enabled (Union[Unset, bool]):  Example: True.
        enabled_events (Union[Unset, list[str]]):  Example: ['letter.created'].
        id (Union[Unset, str]):  Example: webhook_f3gLJ57kutjvtb8HjCov5s.
        live (Union[Unset, bool]):
        object_ (Union[Unset, str]):  Example: webhook.
        secret (Union[Unset, str]):  Example: webhook_secret_u1R5HxPs8BduKzMn2FdZUV.
        updated_at (Union[Unset, str]):  Example: 2021-04-02T03:11:01.158Z.
        url (Union[Unset, str]):  Example: https://ac18f0aecb4a.ngrok.io.
    """

    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    enabled_events: Union[Unset, list[str]] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    object_: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        description = self.description

        enabled = self.enabled

        enabled_events: Union[Unset, list[str]] = UNSET
        if not isinstance(self.enabled_events, Unset):
            enabled_events = self.enabled_events

        id = self.id

        live = self.live

        object_ = self.object_

        secret = self.secret

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if enabled_events is not UNSET:
            field_dict["enabledEvents"] = enabled_events
        if id is not UNSET:
            field_dict["id"] = id
        if live is not UNSET:
            field_dict["live"] = live
        if object_ is not UNSET:
            field_dict["object"] = object_
        if secret is not UNSET:
            field_dict["secret"] = secret
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        enabled_events = cast(list[str], d.pop("enabledEvents", UNSET))

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        object_ = d.pop("object", UNSET)

        secret = d.pop("secret", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        url = d.pop("url", UNSET)

        list_webhooks_response_200_data_item = cls(
            created_at=created_at,
            description=description,
            enabled=enabled,
            enabled_events=enabled_events,
            id=id,
            live=live,
            object_=object_,
            secret=secret,
            updated_at=updated_at,
            url=url,
        )

        list_webhooks_response_200_data_item.additional_properties = d
        return list_webhooks_response_200_data_item

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
