from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CancelPostcardWithNoteResponse200FromMetadata")


@_attrs_define
class CancelPostcardWithNoteResponse200FromMetadata:
    """
    Attributes:
        account_number (Union[Unset, str]):  Example: 2114.
        code (Union[Unset, str]):  Example: 78910.
        date_created (Union[Unset, str]):  Example: 20-Sep-21.
        date_due (Union[Unset, str]):  Example: 20-Sep-21.
        days (Union[Unset, str]):  Example: 90.
        invoice_number (Union[Unset, str]):  Example: 1002.
    """

    account_number: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    date_created: Union[Unset, str] = UNSET
    date_due: Union[Unset, str] = UNSET
    days: Union[Unset, str] = UNSET
    invoice_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_number = self.account_number

        code = self.code

        date_created = self.date_created

        date_due = self.date_due

        days = self.days

        invoice_number = self.invoice_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_number is not UNSET:
            field_dict["Account Number"] = account_number
        if code is not UNSET:
            field_dict["code"] = code
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if date_due is not UNSET:
            field_dict["dateDue"] = date_due
        if days is not UNSET:
            field_dict["days"] = days
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        account_number = d.pop("Account Number", UNSET)

        code = d.pop("code", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        date_due = d.pop("dateDue", UNSET)

        days = d.pop("days", UNSET)

        invoice_number = d.pop("invoiceNumber", UNSET)

        cancel_postcard_with_note_response_200_from_metadata = cls(
            account_number=account_number,
            code=code,
            date_created=date_created,
            date_due=date_due,
            days=days,
            invoice_number=invoice_number,
        )

        cancel_postcard_with_note_response_200_from_metadata.additional_properties = d
        return cancel_postcard_with_note_response_200_from_metadata

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
