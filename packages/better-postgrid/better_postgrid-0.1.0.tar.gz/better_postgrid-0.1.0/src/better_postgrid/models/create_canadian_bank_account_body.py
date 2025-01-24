from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="CreateCanadianBankAccountBody")


@_attrs_define
class CreateCanadianBankAccountBody:
    """
    Attributes:
        account_number (Union[Unset, str]):  Example: 9876543211.
        bank_country_code (Union[Unset, str]):  Example: CA.
        bank_name (Union[Unset, str]):  Example: Example Bank.
        bank_primary_line (Union[Unset, str]):  Example: 100 Garden Street.
        bank_secondary_line (Union[Unset, str]):  Example: Gananoque, ON K7G 1H9.
        route_number (Union[Unset, str]):  Example: 678.
        signature_image (Union[Unset, File]):
        transit_number (Union[Unset, str]):  Example: 12345.
    """

    account_number: Union[Unset, str] = UNSET
    bank_country_code: Union[Unset, str] = UNSET
    bank_name: Union[Unset, str] = UNSET
    bank_primary_line: Union[Unset, str] = UNSET
    bank_secondary_line: Union[Unset, str] = UNSET
    route_number: Union[Unset, str] = UNSET
    signature_image: Union[Unset, File] = UNSET
    transit_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_number = self.account_number

        bank_country_code = self.bank_country_code

        bank_name = self.bank_name

        bank_primary_line = self.bank_primary_line

        bank_secondary_line = self.bank_secondary_line

        route_number = self.route_number

        signature_image: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.signature_image, Unset):
            signature_image = self.signature_image.to_tuple()

        transit_number = self.transit_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number
        if bank_country_code is not UNSET:
            field_dict["bankCountryCode"] = bank_country_code
        if bank_name is not UNSET:
            field_dict["bankName"] = bank_name
        if bank_primary_line is not UNSET:
            field_dict["bankPrimaryLine"] = bank_primary_line
        if bank_secondary_line is not UNSET:
            field_dict["bankSecondaryLine"] = bank_secondary_line
        if route_number is not UNSET:
            field_dict["routeNumber"] = route_number
        if signature_image is not UNSET:
            field_dict["signatureImage"] = signature_image
        if transit_number is not UNSET:
            field_dict["transitNumber"] = transit_number

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        account_number = (
            self.account_number
            if isinstance(self.account_number, Unset)
            else (None, str(self.account_number).encode(), "text/plain")
        )

        bank_country_code = (
            self.bank_country_code
            if isinstance(self.bank_country_code, Unset)
            else (None, str(self.bank_country_code).encode(), "text/plain")
        )

        bank_name = (
            self.bank_name if isinstance(self.bank_name, Unset) else (None, str(self.bank_name).encode(), "text/plain")
        )

        bank_primary_line = (
            self.bank_primary_line
            if isinstance(self.bank_primary_line, Unset)
            else (None, str(self.bank_primary_line).encode(), "text/plain")
        )

        bank_secondary_line = (
            self.bank_secondary_line
            if isinstance(self.bank_secondary_line, Unset)
            else (None, str(self.bank_secondary_line).encode(), "text/plain")
        )

        route_number = (
            self.route_number
            if isinstance(self.route_number, Unset)
            else (None, str(self.route_number).encode(), "text/plain")
        )

        signature_image: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.signature_image, Unset):
            signature_image = self.signature_image.to_tuple()

        transit_number = (
            self.transit_number
            if isinstance(self.transit_number, Unset)
            else (None, str(self.transit_number).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number
        if bank_country_code is not UNSET:
            field_dict["bankCountryCode"] = bank_country_code
        if bank_name is not UNSET:
            field_dict["bankName"] = bank_name
        if bank_primary_line is not UNSET:
            field_dict["bankPrimaryLine"] = bank_primary_line
        if bank_secondary_line is not UNSET:
            field_dict["bankSecondaryLine"] = bank_secondary_line
        if route_number is not UNSET:
            field_dict["routeNumber"] = route_number
        if signature_image is not UNSET:
            field_dict["signatureImage"] = signature_image
        if transit_number is not UNSET:
            field_dict["transitNumber"] = transit_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        account_number = d.pop("accountNumber", UNSET)

        bank_country_code = d.pop("bankCountryCode", UNSET)

        bank_name = d.pop("bankName", UNSET)

        bank_primary_line = d.pop("bankPrimaryLine", UNSET)

        bank_secondary_line = d.pop("bankSecondaryLine", UNSET)

        route_number = d.pop("routeNumber", UNSET)

        _signature_image = d.pop("signatureImage", UNSET)
        signature_image: Union[Unset, File]
        if isinstance(_signature_image, Unset):
            signature_image = UNSET
        else:
            signature_image = File(payload=BytesIO(_signature_image))

        transit_number = d.pop("transitNumber", UNSET)

        create_canadian_bank_account_body = cls(
            account_number=account_number,
            bank_country_code=bank_country_code,
            bank_name=bank_name,
            bank_primary_line=bank_primary_line,
            bank_secondary_line=bank_secondary_line,
            route_number=route_number,
            signature_image=signature_image,
            transit_number=transit_number,
        )

        create_canadian_bank_account_body.additional_properties = d
        return create_canadian_bank_account_body

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
