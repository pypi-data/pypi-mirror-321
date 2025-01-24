from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cancel_postcard_with_note_response_200_from_metadata import (
        CancelPostcardWithNoteResponse200FromMetadata,
    )


T = TypeVar("T", bound="CancelPostcardWithNoteResponse200From")


@_attrs_define
class CancelPostcardWithNoteResponse200From:
    """
    Attributes:
        address_line_1 (Union[Unset, str]):  Example: 145 MULBERRY ST.
        address_line_2 (Union[Unset, str]):  Example: FLOOR 11.
        address_status (Union[Unset, str]):  Example: verified.
        city (Union[Unset, str]):  Example: TORONTO.
        company_name (Union[Unset, str]):  Example: PostGrid.
        country (Union[Unset, str]):  Example: UNITED STATES.
        country_code (Union[Unset, str]):  Example: US.
        description (Union[Unset, str]):  Example: This is a recipient with metadata/merge variables added.
        email (Union[Unset, str]):  Example: jane@postgrid.com.
        first_name (Union[Unset, str]):  Example: Jane.
        id (Union[Unset, str]):  Example: contact_85MdVnizzQpDaV5LCBMrzY.
        job_title (Union[Unset, str]):  Example: Software Engineer.
        last_name (Union[Unset, str]):  Example: Doe.
        metadata (Union[Unset, CancelPostcardWithNoteResponse200FromMetadata]):
        object_ (Union[Unset, str]):  Example: contact.
        phone_number (Union[Unset, str]):
        postal_or_zip (Union[Unset, str]):
        province_or_state (Union[Unset, str]):  Example: ON.
    """

    address_line_1: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    address_status: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    job_title: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    metadata: Union[Unset, "CancelPostcardWithNoteResponse200FromMetadata"] = UNSET
    object_: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
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

        description = self.description

        email = self.email

        first_name = self.first_name

        id = self.id

        job_title = self.job_title

        last_name = self.last_name

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        object_ = self.object_

        phone_number = self.phone_number

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
        if description is not UNSET:
            field_dict["description"] = description
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if object_ is not UNSET:
            field_dict["object"] = object_
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if postal_or_zip is not UNSET:
            field_dict["postalOrZip"] = postal_or_zip
        if province_or_state is not UNSET:
            field_dict["provinceOrState"] = province_or_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.cancel_postcard_with_note_response_200_from_metadata import (
            CancelPostcardWithNoteResponse200FromMetadata,
        )

        d = src_dict.copy()
        address_line_1 = d.pop("addressLine1", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        address_status = d.pop("addressStatus", UNSET)

        city = d.pop("city", UNSET)

        company_name = d.pop("companyName", UNSET)

        country = d.pop("country", UNSET)

        country_code = d.pop("countryCode", UNSET)

        description = d.pop("description", UNSET)

        email = d.pop("email", UNSET)

        first_name = d.pop("firstName", UNSET)

        id = d.pop("id", UNSET)

        job_title = d.pop("jobTitle", UNSET)

        last_name = d.pop("lastName", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CancelPostcardWithNoteResponse200FromMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CancelPostcardWithNoteResponse200FromMetadata.from_dict(_metadata)

        object_ = d.pop("object", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        postal_or_zip = d.pop("postalOrZip", UNSET)

        province_or_state = d.pop("provinceOrState", UNSET)

        cancel_postcard_with_note_response_200_from = cls(
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            address_status=address_status,
            city=city,
            company_name=company_name,
            country=country,
            country_code=country_code,
            description=description,
            email=email,
            first_name=first_name,
            id=id,
            job_title=job_title,
            last_name=last_name,
            metadata=metadata,
            object_=object_,
            phone_number=phone_number,
            postal_or_zip=postal_or_zip,
            province_or_state=province_or_state,
        )

        cancel_postcard_with_note_response_200_from.additional_properties = d
        return cancel_postcard_with_note_response_200_from

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
