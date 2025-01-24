from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLetterResponse201AttachedPDFType0")


@_attrs_define
class CreateLetterResponse201AttachedPDFType0:
    """
    Attributes:
        file (Union[Unset, str]):  Example: https://pg-prod-bucket-
            1.s3.amazonaws.com/test/pdf_9FHvwkDfFSJa2yWQXfzDtP?AWSAccessKeyId=AKIA5GFUILSULWTWCR64&Expires=1697489724&Signat
            ure=Dt3iFFPY9K0P01jxedNZIpupQ8E%3D.
        placement (Union[Unset, str]):  Example: after_template.
    """

    file: Union[Unset, str] = UNSET
    placement: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        placement = self.placement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file
        if placement is not UNSET:
            field_dict["placement"] = placement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        file = d.pop("file", UNSET)

        placement = d.pop("placement", UNSET)

        create_letter_response_201_attached_pdf_type_0 = cls(
            file=file,
            placement=placement,
        )

        create_letter_response_201_attached_pdf_type_0.additional_properties = d
        return create_letter_response_201_attached_pdf_type_0

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
