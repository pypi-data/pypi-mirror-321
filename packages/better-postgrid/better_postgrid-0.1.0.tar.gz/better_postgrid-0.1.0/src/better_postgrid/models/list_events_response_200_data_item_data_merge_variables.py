from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListEventsResponse200DataItemDataMergeVariables")


@_attrs_define
class ListEventsResponse200DataItemDataMergeVariables:
    """
    Attributes:
        amount (Union[Unset, float]):  Example: 732.11.
        cheque_number (Union[Unset, Any]):
        memo (Union[Unset, str]):  Example: David Becker Distribution.
        variable1 (Union[Unset, str]):
        variable2 (Union[Unset, str]):
    """

    amount: Union[Unset, float] = UNSET
    cheque_number: Union[Unset, Any] = UNSET
    memo: Union[Unset, str] = UNSET
    variable1: Union[Unset, str] = UNSET
    variable2: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        cheque_number = self.cheque_number

        memo = self.memo

        variable1 = self.variable1

        variable2 = self.variable2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if cheque_number is not UNSET:
            field_dict["chequeNumber"] = cheque_number
        if memo is not UNSET:
            field_dict["memo"] = memo
        if variable1 is not UNSET:
            field_dict["variable1"] = variable1
        if variable2 is not UNSET:
            field_dict["variable2"] = variable2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        cheque_number = d.pop("chequeNumber", UNSET)

        memo = d.pop("memo", UNSET)

        variable1 = d.pop("variable1", UNSET)

        variable2 = d.pop("variable2", UNSET)

        list_events_response_200_data_item_data_merge_variables = cls(
            amount=amount,
            cheque_number=cheque_number,
            memo=memo,
            variable1=variable1,
            variable2=variable2,
        )

        list_events_response_200_data_item_data_merge_variables.additional_properties = d
        return list_events_response_200_data_item_data_merge_variables

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
