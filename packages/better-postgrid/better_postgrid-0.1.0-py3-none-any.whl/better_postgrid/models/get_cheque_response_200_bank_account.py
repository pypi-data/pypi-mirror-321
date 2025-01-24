from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetChequeResponse200BankAccount")


@_attrs_define
class GetChequeResponse200BankAccount:
    """
    Attributes:
        account_number_last_4 (Union[Unset, str]):  Example: 3211.
        bank_country_code (Union[Unset, str]):  Example: CA.
        bank_name (Union[Unset, str]):  Example: CIBC.
        bank_primary_line (Union[Unset, str]):  Example: 100 Bank Street.
        bank_secondary_line (Union[Unset, str]):  Example: Toronto, ON M9V4V1.
        created_at (Union[Unset, str]):  Example: 2020-11-13T08:28:42.509Z.
        description (Union[Unset, str]):  Example: Example Bank Account.
        id (Union[Unset, str]):  Example: bank_3yXGjQ6ee4pHkLhb3a7keu.
        live (Union[Unset, bool]):
        object_ (Union[Unset, str]):  Example: bank_account.
        route_number (Union[Unset, str]):  Example: 123.
        transit_number (Union[Unset, str]):  Example: 12345.
        updated_at (Union[Unset, str]):  Example: 2020-11-13T08:28:42.509Z.
    """

    account_number_last_4: Union[Unset, str] = UNSET
    bank_country_code: Union[Unset, str] = UNSET
    bank_name: Union[Unset, str] = UNSET
    bank_primary_line: Union[Unset, str] = UNSET
    bank_secondary_line: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    object_: Union[Unset, str] = UNSET
    route_number: Union[Unset, str] = UNSET
    transit_number: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_number_last_4 = self.account_number_last_4

        bank_country_code = self.bank_country_code

        bank_name = self.bank_name

        bank_primary_line = self.bank_primary_line

        bank_secondary_line = self.bank_secondary_line

        created_at = self.created_at

        description = self.description

        id = self.id

        live = self.live

        object_ = self.object_

        route_number = self.route_number

        transit_number = self.transit_number

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_number_last_4 is not UNSET:
            field_dict["accountNumberLast4"] = account_number_last_4
        if bank_country_code is not UNSET:
            field_dict["bankCountryCode"] = bank_country_code
        if bank_name is not UNSET:
            field_dict["bankName"] = bank_name
        if bank_primary_line is not UNSET:
            field_dict["bankPrimaryLine"] = bank_primary_line
        if bank_secondary_line is not UNSET:
            field_dict["bankSecondaryLine"] = bank_secondary_line
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if live is not UNSET:
            field_dict["live"] = live
        if object_ is not UNSET:
            field_dict["object"] = object_
        if route_number is not UNSET:
            field_dict["routeNumber"] = route_number
        if transit_number is not UNSET:
            field_dict["transitNumber"] = transit_number
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        account_number_last_4 = d.pop("accountNumberLast4", UNSET)

        bank_country_code = d.pop("bankCountryCode", UNSET)

        bank_name = d.pop("bankName", UNSET)

        bank_primary_line = d.pop("bankPrimaryLine", UNSET)

        bank_secondary_line = d.pop("bankSecondaryLine", UNSET)

        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        object_ = d.pop("object", UNSET)

        route_number = d.pop("routeNumber", UNSET)

        transit_number = d.pop("transitNumber", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        get_cheque_response_200_bank_account = cls(
            account_number_last_4=account_number_last_4,
            bank_country_code=bank_country_code,
            bank_name=bank_name,
            bank_primary_line=bank_primary_line,
            bank_secondary_line=bank_secondary_line,
            created_at=created_at,
            description=description,
            id=id,
            live=live,
            object_=object_,
            route_number=route_number,
            transit_number=transit_number,
            updated_at=updated_at,
        )

        get_cheque_response_200_bank_account.additional_properties = d
        return get_cheque_response_200_bank_account

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
