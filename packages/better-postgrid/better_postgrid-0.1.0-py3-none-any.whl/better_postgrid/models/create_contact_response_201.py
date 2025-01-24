from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_contact_response_201_metadata import CreateContactResponse201Metadata


T = TypeVar("T", bound="CreateContactResponse201")


@_attrs_define
class CreateContactResponse201:
    """
    Attributes:
        address_line_1 (Union[Unset, str]):  Example: 20-20 BAY ST.
        address_line_2 (Union[Unset, str]):  Example: FLOOR 11.
        address_status (Union[Unset, str]):  Example: verified.
        city (Union[Unset, str]):  Example: TORONTO.
        company_name (Union[Unset, str]):  Example: PostGrid.
        country (Union[Unset, str]):  Example: CANADA.
        country_code (Union[Unset, str]):  Example: CA.
        created_at (Union[Unset, str]):  Example: 2022-02-16T15:08:41.052Z.
        description (Union[Unset, str]):  Example: Kevin Smith's contact information .
        email (Union[Unset, str]):  Example: kevinsmith@postgrid.com.
        first_name (Union[Unset, str]):  Example: Kevin.
        force_verified_status (Union[Unset, bool]):
        id (Union[Unset, str]):  Example: contact_pxd7wnnD1xY6H6etKNvjb4.
        job_title (Union[Unset, str]):  Example: Manager.
        last_name (Union[Unset, str]):  Example: Smith.
        live (Union[Unset, bool]):
        mailing_lists (Union[Unset, list[Any]]):
        metadata (Union[Unset, CreateContactResponse201Metadata]):
        object_ (Union[Unset, str]):  Example: contact.
        phone_number (Union[Unset, str]):  Example: 9059059059.
        postal_or_zip (Union[Unset, str]):  Example: M5J 2N8.
        province_or_state (Union[Unset, str]):  Example: ON.
        secret (Union[Unset, bool]):  Example: True.
        skip_verification (Union[Unset, bool]):
        updated_at (Union[Unset, str]):  Example: 2022-02-17T16:58:10.063Z.
    """

    address_line_1: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    address_status: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    force_verified_status: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    job_title: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    mailing_lists: Union[Unset, list[Any]] = UNSET
    metadata: Union[Unset, "CreateContactResponse201Metadata"] = UNSET
    object_: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    postal_or_zip: Union[Unset, str] = UNSET
    province_or_state: Union[Unset, str] = UNSET
    secret: Union[Unset, bool] = UNSET
    skip_verification: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_line_1 = self.address_line_1

        address_line_2 = self.address_line_2

        address_status = self.address_status

        city = self.city

        company_name = self.company_name

        country = self.country

        country_code = self.country_code

        created_at = self.created_at

        description = self.description

        email = self.email

        first_name = self.first_name

        force_verified_status = self.force_verified_status

        id = self.id

        job_title = self.job_title

        last_name = self.last_name

        live = self.live

        mailing_lists: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.mailing_lists, Unset):
            mailing_lists = self.mailing_lists

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        object_ = self.object_

        phone_number = self.phone_number

        postal_or_zip = self.postal_or_zip

        province_or_state = self.province_or_state

        secret = self.secret

        skip_verification = self.skip_verification

        updated_at = self.updated_at

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
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if force_verified_status is not UNSET:
            field_dict["forceVerifiedStatus"] = force_verified_status
        if id is not UNSET:
            field_dict["id"] = id
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if live is not UNSET:
            field_dict["live"] = live
        if mailing_lists is not UNSET:
            field_dict["mailingLists"] = mailing_lists
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
        if secret is not UNSET:
            field_dict["secret"] = secret
        if skip_verification is not UNSET:
            field_dict["skipVerification"] = skip_verification
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_contact_response_201_metadata import CreateContactResponse201Metadata

        d = src_dict.copy()
        address_line_1 = d.pop("addressLine1", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        address_status = d.pop("addressStatus", UNSET)

        city = d.pop("city", UNSET)

        company_name = d.pop("companyName", UNSET)

        country = d.pop("country", UNSET)

        country_code = d.pop("countryCode", UNSET)

        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

        email = d.pop("email", UNSET)

        first_name = d.pop("firstName", UNSET)

        force_verified_status = d.pop("forceVerifiedStatus", UNSET)

        id = d.pop("id", UNSET)

        job_title = d.pop("jobTitle", UNSET)

        last_name = d.pop("lastName", UNSET)

        live = d.pop("live", UNSET)

        mailing_lists = cast(list[Any], d.pop("mailingLists", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CreateContactResponse201Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateContactResponse201Metadata.from_dict(_metadata)

        object_ = d.pop("object", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        postal_or_zip = d.pop("postalOrZip", UNSET)

        province_or_state = d.pop("provinceOrState", UNSET)

        secret = d.pop("secret", UNSET)

        skip_verification = d.pop("skipVerification", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        create_contact_response_201 = cls(
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            address_status=address_status,
            city=city,
            company_name=company_name,
            country=country,
            country_code=country_code,
            created_at=created_at,
            description=description,
            email=email,
            first_name=first_name,
            force_verified_status=force_verified_status,
            id=id,
            job_title=job_title,
            last_name=last_name,
            live=live,
            mailing_lists=mailing_lists,
            metadata=metadata,
            object_=object_,
            phone_number=phone_number,
            postal_or_zip=postal_or_zip,
            province_or_state=province_or_state,
            secret=secret,
            skip_verification=skip_verification,
            updated_at=updated_at,
        )

        create_contact_response_201.additional_properties = d
        return create_contact_response_201

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
