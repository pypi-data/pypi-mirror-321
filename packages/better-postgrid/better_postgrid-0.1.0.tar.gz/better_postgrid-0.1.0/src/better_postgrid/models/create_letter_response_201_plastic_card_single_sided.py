from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLetterResponse201PlasticCardSingleSided")


@_attrs_define
class CreateLetterResponse201PlasticCardSingleSided:
    """
    Attributes:
        html (Union[Unset, str]):  Example: <h1>Example Plastic Card</h1>.
        template (Union[Unset, str]):  Example: template_nYuXaSsEKGKcCAT9ZM4Cz6.
        uploaded_pdf (Union[Unset, str]):  Example: https://pg-prod-bucket-
            1.s3.amazonaws.com/test/pdf_7WxY5LKM6k5g7zwLZAoLgD?AWSAccessKeyId=AKIA5GFUILSULWTWCR64&Expires=1724427602&Signat
            ure=LTGln466IoGpuSoNTnUKXLf1ge8%3D.
    """

    html: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    uploaded_pdf: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        html = self.html

        template = self.template

        uploaded_pdf = self.uploaded_pdf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if html is not UNSET:
            field_dict["html"] = html
        if template is not UNSET:
            field_dict["template"] = template
        if uploaded_pdf is not UNSET:
            field_dict["uploadedPDF"] = uploaded_pdf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        html = d.pop("html", UNSET)

        template = d.pop("template", UNSET)

        uploaded_pdf = d.pop("uploadedPDF", UNSET)

        create_letter_response_201_plastic_card_single_sided = cls(
            html=html,
            template=template,
            uploaded_pdf=uploaded_pdf,
        )

        create_letter_response_201_plastic_card_single_sided.additional_properties = d
        return create_letter_response_201_plastic_card_single_sided

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
