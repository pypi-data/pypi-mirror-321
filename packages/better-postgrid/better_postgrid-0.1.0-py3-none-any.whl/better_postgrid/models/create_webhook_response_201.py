from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_webhook_response_201_metadata import CreateWebhookResponse201Metadata


T = TypeVar("T", bound="CreateWebhookResponse201")


@_attrs_define
class CreateWebhookResponse201:
    """
    Attributes:
        created_at (Union[Unset, str]):  Example: 2022-02-16T18:37:02.048Z.
        description (Union[Unset, str]):  Example: Letter Created.
        enabled (Union[Unset, bool]):  Example: True.
        enabled_events (Union[Unset, list[str]]):  Example: ['letter.created'].
        id (Union[Unset, str]):  Example: webhook_skN2ZTvFwS62oc5tJY1gzw.
        live (Union[Unset, bool]):
        metadata (Union[Unset, CreateWebhookResponse201Metadata]):
        object_ (Union[Unset, str]):  Example: webhook.
        secret (Union[Unset, str]):  Example: webhook_secret_xkNXtQ4jHevFdkTG3mSf1Q.
        updated_at (Union[Unset, str]):  Example: 2022-02-16T18:37:02.048Z.
        url (Union[Unset, str]):  Example: https://ac18f0aecb4a.ngrok.io.
    """

    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    enabled_events: Union[Unset, list[str]] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    metadata: Union[Unset, "CreateWebhookResponse201Metadata"] = UNSET
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

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

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
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
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
        from ..models.create_webhook_response_201_metadata import CreateWebhookResponse201Metadata

        d = src_dict.copy()
        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        enabled_events = cast(list[str], d.pop("enabledEvents", UNSET))

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CreateWebhookResponse201Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateWebhookResponse201Metadata.from_dict(_metadata)

        object_ = d.pop("object", UNSET)

        secret = d.pop("secret", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        url = d.pop("url", UNSET)

        create_webhook_response_201 = cls(
            created_at=created_at,
            description=description,
            enabled=enabled,
            enabled_events=enabled_events,
            id=id,
            live=live,
            metadata=metadata,
            object_=object_,
            secret=secret,
            updated_at=updated_at,
            url=url,
        )

        create_webhook_response_201.additional_properties = d
        return create_webhook_response_201

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
