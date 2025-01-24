from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListTrackerVisitsResponse200DataItem")


@_attrs_define
class ListTrackerVisitsResponse200DataItem:
    """
    Attributes:
        created_at (Union[Unset, str]):  Example: 2020-11-12T23:30:12.581Z.
        device (Union[Unset, str]):  Example: Device Unknown.
        id (Union[Unset, str]):  Example: tracker_visit_123456789abcdefghijklmnopqrstuvwxyz.
        ip_address (Union[Unset, str]):  Example: Unknown IP Address.
        live (Union[Unset, bool]):
        object_ (Union[Unset, str]):  Example: tracker_visit.
        order_id (Union[Unset, str]):  Example: order_123456789abcdefghijklmnopqrstuvwxyz.
        tracker (Union[Unset, str]):  Example: tracker_123456789abcdefghijklmnopqrstuvwxyz.
        updated_at (Union[Unset, str]):  Example: 2020-11-12T23:31:12.581Z.
    """

    created_at: Union[Unset, str] = UNSET
    device: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    object_: Union[Unset, str] = UNSET
    order_id: Union[Unset, str] = UNSET
    tracker: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        device = self.device

        id = self.id

        ip_address = self.ip_address

        live = self.live

        object_ = self.object_

        order_id = self.order_id

        tracker = self.tracker

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if device is not UNSET:
            field_dict["device"] = device
        if id is not UNSET:
            field_dict["id"] = id
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if live is not UNSET:
            field_dict["live"] = live
        if object_ is not UNSET:
            field_dict["object"] = object_
        if order_id is not UNSET:
            field_dict["orderID"] = order_id
        if tracker is not UNSET:
            field_dict["tracker"] = tracker
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("createdAt", UNSET)

        device = d.pop("device", UNSET)

        id = d.pop("id", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        live = d.pop("live", UNSET)

        object_ = d.pop("object", UNSET)

        order_id = d.pop("orderID", UNSET)

        tracker = d.pop("tracker", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        list_tracker_visits_response_200_data_item = cls(
            created_at=created_at,
            device=device,
            id=id,
            ip_address=ip_address,
            live=live,
            object_=object_,
            order_id=order_id,
            tracker=tracker,
            updated_at=updated_at,
        )

        list_tracker_visits_response_200_data_item.additional_properties = d
        return list_tracker_visits_response_200_data_item

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
