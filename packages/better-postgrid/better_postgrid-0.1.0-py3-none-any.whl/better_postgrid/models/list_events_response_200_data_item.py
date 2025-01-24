from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_events_response_200_data_item_data import ListEventsResponse200DataItemData


T = TypeVar("T", bound="ListEventsResponse200DataItem")


@_attrs_define
class ListEventsResponse200DataItem:
    """
    Attributes:
        data (Union[Unset, ListEventsResponse200DataItemData]):
        id (Union[Unset, str]):  Example: event_r1nfP4xAacyqMYtt7PeyFD.
        live (Union[Unset, bool]):
        object_ (Union[Unset, str]):  Example: event.
        type_ (Union[Unset, str]):  Example: letter.created.
    """

    data: Union[Unset, "ListEventsResponse200DataItemData"] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    object_: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        id = self.id

        live = self.live

        object_ = self.object_

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if id is not UNSET:
            field_dict["id"] = id
        if live is not UNSET:
            field_dict["live"] = live
        if object_ is not UNSET:
            field_dict["object"] = object_
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.list_events_response_200_data_item_data import ListEventsResponse200DataItemData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, ListEventsResponse200DataItemData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ListEventsResponse200DataItemData.from_dict(_data)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        object_ = d.pop("object", UNSET)

        type_ = d.pop("type", UNSET)

        list_events_response_200_data_item = cls(
            data=data,
            id=id,
            live=live,
            object_=object_,
            type_=type_,
        )

        list_events_response_200_data_item.additional_properties = d
        return list_events_response_200_data_item

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
