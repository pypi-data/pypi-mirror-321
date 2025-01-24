from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateContactBody")


@_attrs_define
class CreateContactBody:
    """
    Attributes:
        address_line_1 (Union[Unset, str]):  Example: 20-20 bay st toronto on m9v 4v1.
        company_name (Union[Unset, str]):  Example: PostGrid.
        first_name (Union[Unset, str]):  Example: Kevin.
    """

    address_line_1: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_line_1 = self.address_line_1

        company_name = self.company_name

        first_name = self.first_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if first_name is not UNSET:
            field_dict["firstName"] = first_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        address_line_1 = d.pop("addressLine1", UNSET)

        company_name = d.pop("companyName", UNSET)

        first_name = d.pop("firstName", UNSET)

        create_contact_body = cls(
            address_line_1=address_line_1,
            company_name=company_name,
            first_name=first_name,
        )

        create_contact_body.additional_properties = d
        return create_contact_body

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
