from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CancelChequeWithNoteResponse200From")


@_attrs_define
class CancelChequeWithNoteResponse200From:
    """
    Attributes:
        address_line_1 (Union[Unset, str]):  Example: 750 NORTH SAINT PAUL STREET.
        address_line_2 (Union[Unset, str]):
        address_status (Union[Unset, str]):  Example: verified.
        city (Union[Unset, str]):  Example: DALLAS.
        company_name (Union[Unset, str]):  Example: JANE DOE.
        country (Union[Unset, str]):  Example: UNITED STATES.
        country_code (Union[Unset, str]):  Example: US.
        id (Union[Unset, str]):  Example: contact_6cHJXmpSnAjQC4vgXvTQV2.
        object_ (Union[Unset, str]):  Example: contact.
        postal_or_zip (Union[Unset, str]):  Example: 75201.
        province_or_state (Union[Unset, str]):  Example: TX.
    """

    address_line_1: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    address_status: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    object_: Union[Unset, str] = UNSET
    postal_or_zip: Union[Unset, str] = UNSET
    province_or_state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_line_1 = self.address_line_1

        address_line_2 = self.address_line_2

        address_status = self.address_status

        city = self.city

        company_name = self.company_name

        country = self.country

        country_code = self.country_code

        id = self.id

        object_ = self.object_

        postal_or_zip = self.postal_or_zip

        province_or_state = self.province_or_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if address_status is not UNSET:
            field_dict["addressStatus"] = address_status
        if city is not UNSET:
            field_dict["city"] = city
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if country is not UNSET:
            field_dict["country"] = country
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if id is not UNSET:
            field_dict["id"] = id
        if object_ is not UNSET:
            field_dict["object"] = object_
        if postal_or_zip is not UNSET:
            field_dict["postalOrZip"] = postal_or_zip
        if province_or_state is not UNSET:
            field_dict["provinceOrState"] = province_or_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        address_line_1 = d.pop("addressLine1", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        address_status = d.pop("addressStatus", UNSET)

        city = d.pop("city", UNSET)

        company_name = d.pop("companyName", UNSET)

        country = d.pop("country", UNSET)

        country_code = d.pop("countryCode", UNSET)

        id = d.pop("id", UNSET)

        object_ = d.pop("object", UNSET)

        postal_or_zip = d.pop("postalOrZip", UNSET)

        province_or_state = d.pop("provinceOrState", UNSET)

        cancel_cheque_with_note_response_200_from = cls(
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            address_status=address_status,
            city=city,
            company_name=company_name,
            country=country,
            country_code=country_code,
            id=id,
            object_=object_,
            postal_or_zip=postal_or_zip,
            province_or_state=province_or_state,
        )

        cancel_cheque_with_note_response_200_from.additional_properties = d
        return cancel_cheque_with_note_response_200_from

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
