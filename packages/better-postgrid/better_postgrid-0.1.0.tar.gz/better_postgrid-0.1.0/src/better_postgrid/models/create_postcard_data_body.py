from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePostcardDataBody")


@_attrs_define
class CreatePostcardDataBody:
    """
    Attributes:
        pdf (Union[Unset, str]):  Example: https://pg-prod-bucket-1.s3.amazonaws.com/Postcard_Test_9x6.pdf.
        size (Union[Unset, str]):  Example: 9x6.
        toaddress_line_1 (Union[Unset, str]):  Example: 20-20 bay st.
        tocity (Union[Unset, str]):  Example: Toronto.
        tofirst_name (Union[Unset, str]):  Example: Kevin.
    """

    pdf: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    toaddress_line_1: Union[Unset, str] = UNSET
    tocity: Union[Unset, str] = UNSET
    tofirst_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pdf = self.pdf

        size = self.size

        toaddress_line_1 = self.toaddress_line_1

        tocity = self.tocity

        tofirst_name = self.tofirst_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pdf is not UNSET:
            field_dict["pdf"] = pdf
        if size is not UNSET:
            field_dict["size"] = size
        if toaddress_line_1 is not UNSET:
            field_dict["to[addressLine1]"] = toaddress_line_1
        if tocity is not UNSET:
            field_dict["to[city]"] = tocity
        if tofirst_name is not UNSET:
            field_dict["to[firstName]"] = tofirst_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        pdf = d.pop("pdf", UNSET)

        size = d.pop("size", UNSET)

        toaddress_line_1 = d.pop("to[addressLine1]", UNSET)

        tocity = d.pop("to[city]", UNSET)

        tofirst_name = d.pop("to[firstName]", UNSET)

        create_postcard_data_body = cls(
            pdf=pdf,
            size=size,
            toaddress_line_1=toaddress_line_1,
            tocity=tocity,
            tofirst_name=tofirst_name,
        )

        create_postcard_data_body.additional_properties = d
        return create_postcard_data_body

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
