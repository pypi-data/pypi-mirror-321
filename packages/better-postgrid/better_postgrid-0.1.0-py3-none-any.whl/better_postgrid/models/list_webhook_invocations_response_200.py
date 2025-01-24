from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_webhook_invocations_response_200_data_item import ListWebhookInvocationsResponse200DataItem


T = TypeVar("T", bound="ListWebhookInvocationsResponse200")


@_attrs_define
class ListWebhookInvocationsResponse200:
    """
    Attributes:
        data (Union[Unset, list['ListWebhookInvocationsResponse200DataItem']]):  Example: [{'createdAt':
            '2021-04-02T02:09:32.066Z', 'id': 'webhook_invocation_6TAGtJezjUyGFnznTRdX37', 'object': 'webhook_invocation',
            'statusCode': 200, 'type': 'letter.created', 'updatedAt': '2021-04-02T02:09:32.066Z', 'webhook':
            'webhook_beA27GdjQvUUisCDwRTasK'}, {'createdAt': '2021-04-02T02:08:55.707Z', 'id':
            'webhook_invocation_a1Znx4otAJkEeFYGWCL3G2', 'object': 'webhook_invocation', 'statusCode': 500, 'type':
            'letter.created', 'updatedAt': '2021-04-02T02:08:55.707Z', 'webhook': 'webhook_beA27GdjQvUUisCDwRTasK'}].
        limit (Union[Unset, float]):  Example: 10.
        object_ (Union[Unset, str]):  Example: list.
        skip (Union[Unset, float]):
        total_count (Union[Unset, float]):  Example: 2.
    """

    data: Union[Unset, list["ListWebhookInvocationsResponse200DataItem"]] = UNSET
    limit: Union[Unset, float] = UNSET
    object_: Union[Unset, str] = UNSET
    skip: Union[Unset, float] = UNSET
    total_count: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        limit = self.limit

        object_ = self.object_

        skip = self.skip

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if limit is not UNSET:
            field_dict["limit"] = limit
        if object_ is not UNSET:
            field_dict["object"] = object_
        if skip is not UNSET:
            field_dict["skip"] = skip
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.list_webhook_invocations_response_200_data_item import ListWebhookInvocationsResponse200DataItem

        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = ListWebhookInvocationsResponse200DataItem.from_dict(data_item_data)

            data.append(data_item)

        limit = d.pop("limit", UNSET)

        object_ = d.pop("object", UNSET)

        skip = d.pop("skip", UNSET)

        total_count = d.pop("totalCount", UNSET)

        list_webhook_invocations_response_200 = cls(
            data=data,
            limit=limit,
            object_=object_,
            skip=skip,
            total_count=total_count,
        )

        list_webhook_invocations_response_200.additional_properties = d
        return list_webhook_invocations_response_200

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
