from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLetterResponse201PlasticCardDoubleSided")


@_attrs_define
class CreateLetterResponse201PlasticCardDoubleSided:
    """
    Attributes:
        back_html (Union[Unset, str]):  Example: <h1>Example Plastic Card Back</h1>.
        back_template (Union[Unset, str]):  Example: template_nYuXaSsEKGKcCAT9ZM4Cz6.
        front_html (Union[Unset, str]):  Example: <h1>Example Plastic Card</h1>.
        front_template (Union[Unset, str]):  Example: template_nYuXaSsEKGKcCAT9ZM4Cz6.
        uploaded_pdf (Union[Unset, str]):  Example: https://pg-prod-bucket-
            1.s3.amazonaws.com/test/pdf_vSf84UiX1eUp4aaQD42oep?AWSAccessKeyId=AKIA5GFUILSULWTWCR64&Expires=1724427793&Signat
            ure=%2B4L1S0NnKU7%2BKB5NRVyoW1IIf2w%3D.
    """

    back_html: Union[Unset, str] = UNSET
    back_template: Union[Unset, str] = UNSET
    front_html: Union[Unset, str] = UNSET
    front_template: Union[Unset, str] = UNSET
    uploaded_pdf: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        back_html = self.back_html

        back_template = self.back_template

        front_html = self.front_html

        front_template = self.front_template

        uploaded_pdf = self.uploaded_pdf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if back_html is not UNSET:
            field_dict["backHTML"] = back_html
        if back_template is not UNSET:
            field_dict["backTemplate"] = back_template
        if front_html is not UNSET:
            field_dict["frontHTML"] = front_html
        if front_template is not UNSET:
            field_dict["frontTemplate"] = front_template
        if uploaded_pdf is not UNSET:
            field_dict["uploadedPDF"] = uploaded_pdf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        back_html = d.pop("backHTML", UNSET)

        back_template = d.pop("backTemplate", UNSET)

        front_html = d.pop("frontHTML", UNSET)

        front_template = d.pop("frontTemplate", UNSET)

        uploaded_pdf = d.pop("uploadedPDF", UNSET)

        create_letter_response_201_plastic_card_double_sided = cls(
            back_html=back_html,
            back_template=back_template,
            front_html=front_html,
            front_template=front_template,
            uploaded_pdf=uploaded_pdf,
        )

        create_letter_response_201_plastic_card_double_sided.additional_properties = d
        return create_letter_response_201_plastic_card_double_sided

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
