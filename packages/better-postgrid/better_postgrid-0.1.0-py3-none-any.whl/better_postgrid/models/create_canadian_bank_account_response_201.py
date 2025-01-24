from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_canadian_bank_account_response_201_metadata import CreateCanadianBankAccountResponse201Metadata


T = TypeVar("T", bound="CreateCanadianBankAccountResponse201")


@_attrs_define
class CreateCanadianBankAccountResponse201:
    """
    Attributes:
        account_number_last_4 (Union[Unset, str]):  Example: 3211.
        bank_country_code (Union[Unset, str]):  Example: CA.
        bank_name (Union[Unset, str]):  Example: Example Bank.
        bank_primary_line (Union[Unset, str]):  Example: 100 Garden Street.
        bank_secondary_line (Union[Unset, str]):  Example: Gananoque, ON K7G 1H9.
        created_at (Union[Unset, str]):  Example: 2022-02-16T18:31:41.849Z.
        description (Union[Unset, str]):  Example: My canadian bank with a signature image.
        id (Union[Unset, str]):  Example: bank_fVgozkqb1omutdnZWzpLer.
        live (Union[Unset, bool]):
        metadata (Union[Unset, CreateCanadianBankAccountResponse201Metadata]):
        object_ (Union[Unset, str]):  Example: bank_account.
        route_number (Union[Unset, str]):  Example: 678.
        routing_number (Union[Unset, str]):  Example: 123456789.
        signature_image (Union[Unset, str]):  Example: https://pg-prod-bucket-
            1.s3.amazonaws.com/test/sign_iRiipTpwrDro5n5Td9srGF?AWSAccessKeyId=AKIA5GFUILSULWTWCR64&Expires=1645037201&Signa
            ture=feBEyT93YIEw2ju0Y4eWwa7%2FsEQ%3D.
        signature_text (Union[Unset, str]):  Example: Kevin Smith.
        transit_number (Union[Unset, str]):  Example: 12345.
        updated_at (Union[Unset, str]):  Example: 2022-02-16T18:31:41.849Z.
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
    metadata: Union[Unset, "CreateCanadianBankAccountResponse201Metadata"] = UNSET
    object_: Union[Unset, str] = UNSET
    route_number: Union[Unset, str] = UNSET
    routing_number: Union[Unset, str] = UNSET
    signature_image: Union[Unset, str] = UNSET
    signature_text: Union[Unset, str] = UNSET
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

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        object_ = self.object_

        route_number = self.route_number

        routing_number = self.routing_number

        signature_image = self.signature_image

        signature_text = self.signature_text

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
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if object_ is not UNSET:
            field_dict["object"] = object_
        if route_number is not UNSET:
            field_dict["routeNumber"] = route_number
        if routing_number is not UNSET:
            field_dict["routingNumber"] = routing_number
        if signature_image is not UNSET:
            field_dict["signatureImage"] = signature_image
        if signature_text is not UNSET:
            field_dict["signatureText"] = signature_text
        if transit_number is not UNSET:
            field_dict["transitNumber"] = transit_number
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_canadian_bank_account_response_201_metadata import (
            CreateCanadianBankAccountResponse201Metadata,
        )

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

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CreateCanadianBankAccountResponse201Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateCanadianBankAccountResponse201Metadata.from_dict(_metadata)

        object_ = d.pop("object", UNSET)

        route_number = d.pop("routeNumber", UNSET)

        routing_number = d.pop("routingNumber", UNSET)

        signature_image = d.pop("signatureImage", UNSET)

        signature_text = d.pop("signatureText", UNSET)

        transit_number = d.pop("transitNumber", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        create_canadian_bank_account_response_201 = cls(
            account_number_last_4=account_number_last_4,
            bank_country_code=bank_country_code,
            bank_name=bank_name,
            bank_primary_line=bank_primary_line,
            bank_secondary_line=bank_secondary_line,
            created_at=created_at,
            description=description,
            id=id,
            live=live,
            metadata=metadata,
            object_=object_,
            route_number=route_number,
            routing_number=routing_number,
            signature_image=signature_image,
            signature_text=signature_text,
            transit_number=transit_number,
            updated_at=updated_at,
        )

        create_canadian_bank_account_response_201.additional_properties = d
        return create_canadian_bank_account_response_201

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
