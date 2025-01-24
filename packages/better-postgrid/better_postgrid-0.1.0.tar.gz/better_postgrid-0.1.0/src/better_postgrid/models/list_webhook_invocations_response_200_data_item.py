from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListWebhookInvocationsResponse200DataItem")


@_attrs_define
class ListWebhookInvocationsResponse200DataItem:
    """
    Attributes:
        created_at (Union[Unset, str]):  Example: 2021-04-02T02:09:32.066Z.
        id (Union[Unset, str]):  Example: webhook_invocation_6TAGtJezjUyGFnznTRdX37.
        object_ (Union[Unset, str]):  Example: webhook_invocation.
        status_code (Union[Unset, float]):  Example: 200.
        type_ (Union[Unset, str]):  Example: letter.created.
        updated_at (Union[Unset, str]):  Example: 2021-04-02T02:09:32.066Z.
        webhook (Union[Unset, str]):  Example: webhook_beA27GdjQvUUisCDwRTasK.
    """

    created_at: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    object_: Union[Unset, str] = UNSET
    status_code: Union[Unset, float] = UNSET
    type_: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    webhook: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        object_ = self.object_

        status_code = self.status_code

        type_ = self.type_

        updated_at = self.updated_at

        webhook = self.webhook

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if object_ is not UNSET:
            field_dict["object"] = object_
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if webhook is not UNSET:
            field_dict["webhook"] = webhook

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("createdAt", UNSET)

        id = d.pop("id", UNSET)

        object_ = d.pop("object", UNSET)

        status_code = d.pop("statusCode", UNSET)

        type_ = d.pop("type", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        webhook = d.pop("webhook", UNSET)

        list_webhook_invocations_response_200_data_item = cls(
            created_at=created_at,
            id=id,
            object_=object_,
            status_code=status_code,
            type_=type_,
            updated_at=updated_at,
            webhook=webhook,
        )

        list_webhook_invocations_response_200_data_item.additional_properties = d
        return list_webhook_invocations_response_200_data_item

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
