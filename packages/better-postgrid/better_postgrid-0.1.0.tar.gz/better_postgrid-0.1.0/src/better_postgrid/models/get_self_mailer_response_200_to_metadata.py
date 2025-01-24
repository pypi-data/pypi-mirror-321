from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSelfMailerResponse200ToMetadata")


@_attrs_define
class GetSelfMailerResponse200ToMetadata:
    """
    Attributes:
        county (Union[Unset, str]):  Example: Charlotte.
        property_address (Union[Unset, str]):  Example: 3381 Maple Ter.
        property_city (Union[Unset, str]):  Example: Port Charlotte.
        property_state (Union[Unset, str]):  Example: FL.
        zip_ (Union[Unset, str]):  Example: 33952.
    """

    county: Union[Unset, str] = UNSET
    property_address: Union[Unset, str] = UNSET
    property_city: Union[Unset, str] = UNSET
    property_state: Union[Unset, str] = UNSET
    zip_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        county = self.county

        property_address = self.property_address

        property_city = self.property_city

        property_state = self.property_state

        zip_ = self.zip_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if county is not UNSET:
            field_dict["County"] = county
        if property_address is not UNSET:
            field_dict["PropertyAddress"] = property_address
        if property_city is not UNSET:
            field_dict["PropertyCity"] = property_city
        if property_state is not UNSET:
            field_dict["PropertyState"] = property_state
        if zip_ is not UNSET:
            field_dict["Zip"] = zip_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        county = d.pop("County", UNSET)

        property_address = d.pop("PropertyAddress", UNSET)

        property_city = d.pop("PropertyCity", UNSET)

        property_state = d.pop("PropertyState", UNSET)

        zip_ = d.pop("Zip", UNSET)

        get_self_mailer_response_200_to_metadata = cls(
            county=county,
            property_address=property_address,
            property_city=property_city,
            property_state=property_state,
            zip_=zip_,
        )

        get_self_mailer_response_200_to_metadata.additional_properties = d
        return get_self_mailer_response_200_to_metadata

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
