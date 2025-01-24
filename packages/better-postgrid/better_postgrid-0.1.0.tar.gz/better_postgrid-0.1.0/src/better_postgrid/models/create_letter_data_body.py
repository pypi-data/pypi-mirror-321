from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLetterDataBody")


@_attrs_define
class CreateLetterDataBody:
    """
    Attributes:
        address_placement (Union[Unset, str]):  Example: top_first_page.
        color (Union[Unset, str]):  Example: false.
        description (Union[Unset, str]):  Example: My HTML letter.
        double_sided (Union[Unset, str]):  Example: true.
        envelope_type (Union[Unset, str]):  Example: flat.
        express (Union[Unset, str]):  Example: false.
        extra_service (Union[Unset, str]):  Example: certified.
        from_ (Union[Unset, str]):  Example: contact_fFh9tg3SgD8LRXxatVAWt2.
        html (Union[Unset, str]):  Example: <b>Hello</b>, {{to.firstName}}!.
        mailing_class (Union[Unset, str]):  Example: first_class.
        merge_variableslanguage (Union[Unset, str]):  Example: english.
        metadatacompany (Union[Unset, str]):  Example: PostGrid.
        perforated_page (Union[Unset, str]):  Example: 1.
        plastic_carddouble_sidedback_html (Union[Unset, str]):  Example: <h1>Example Plastic Card Back</h1>.
        plastic_carddouble_sidedfront_html (Union[Unset, str]):  Example: <h1>Example Plastic Card</h1>.
        plastic_cardsize (Union[Unset, str]):  Example: standard.
        return_envelope (Union[Unset, str]):  Example: return_envelope_97Tcv1LxhWWLPUvn58CuVJ.
        send_date (Union[Unset, str]):  Example: 2023-02-16T15:40:35.873Z.
        size (Union[Unset, str]):  Example: us_letter.
        to (Union[Unset, str]):  Example: contact_fFh9tg3SgD8LRXxatVAWt2.
    """

    address_placement: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    double_sided: Union[Unset, str] = UNSET
    envelope_type: Union[Unset, str] = UNSET
    express: Union[Unset, str] = UNSET
    extra_service: Union[Unset, str] = UNSET
    from_: Union[Unset, str] = UNSET
    html: Union[Unset, str] = UNSET
    mailing_class: Union[Unset, str] = UNSET
    merge_variableslanguage: Union[Unset, str] = UNSET
    metadatacompany: Union[Unset, str] = UNSET
    perforated_page: Union[Unset, str] = UNSET
    plastic_carddouble_sidedback_html: Union[Unset, str] = UNSET
    plastic_carddouble_sidedfront_html: Union[Unset, str] = UNSET
    plastic_cardsize: Union[Unset, str] = UNSET
    return_envelope: Union[Unset, str] = UNSET
    send_date: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    to: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_placement = self.address_placement

        color = self.color

        description = self.description

        double_sided = self.double_sided

        envelope_type = self.envelope_type

        express = self.express

        extra_service = self.extra_service

        from_ = self.from_

        html = self.html

        mailing_class = self.mailing_class

        merge_variableslanguage = self.merge_variableslanguage

        metadatacompany = self.metadatacompany

        perforated_page = self.perforated_page

        plastic_carddouble_sidedback_html = self.plastic_carddouble_sidedback_html

        plastic_carddouble_sidedfront_html = self.plastic_carddouble_sidedfront_html

        plastic_cardsize = self.plastic_cardsize

        return_envelope = self.return_envelope

        send_date = self.send_date

        size = self.size

        to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_placement is not UNSET:
            field_dict["addressPlacement"] = address_placement
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description
        if double_sided is not UNSET:
            field_dict["doubleSided"] = double_sided
        if envelope_type is not UNSET:
            field_dict["envelopeType"] = envelope_type
        if express is not UNSET:
            field_dict["express"] = express
        if extra_service is not UNSET:
            field_dict["extraService"] = extra_service
        if from_ is not UNSET:
            field_dict["from"] = from_
        if html is not UNSET:
            field_dict["html"] = html
        if mailing_class is not UNSET:
            field_dict["mailingClass"] = mailing_class
        if merge_variableslanguage is not UNSET:
            field_dict["mergeVariables[language]"] = merge_variableslanguage
        if metadatacompany is not UNSET:
            field_dict["metadata[company]"] = metadatacompany
        if perforated_page is not UNSET:
            field_dict["perforatedPage"] = perforated_page
        if plastic_carddouble_sidedback_html is not UNSET:
            field_dict["plasticCard[doubleSided][backHTML]"] = plastic_carddouble_sidedback_html
        if plastic_carddouble_sidedfront_html is not UNSET:
            field_dict["plasticCard[doubleSided][frontHTML]"] = plastic_carddouble_sidedfront_html
        if plastic_cardsize is not UNSET:
            field_dict["plasticCard[size]"] = plastic_cardsize
        if return_envelope is not UNSET:
            field_dict["returnEnvelope"] = return_envelope
        if send_date is not UNSET:
            field_dict["sendDate"] = send_date
        if size is not UNSET:
            field_dict["size"] = size
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        address_placement = d.pop("addressPlacement", UNSET)

        color = d.pop("color", UNSET)

        description = d.pop("description", UNSET)

        double_sided = d.pop("doubleSided", UNSET)

        envelope_type = d.pop("envelopeType", UNSET)

        express = d.pop("express", UNSET)

        extra_service = d.pop("extraService", UNSET)

        from_ = d.pop("from", UNSET)

        html = d.pop("html", UNSET)

        mailing_class = d.pop("mailingClass", UNSET)

        merge_variableslanguage = d.pop("mergeVariables[language]", UNSET)

        metadatacompany = d.pop("metadata[company]", UNSET)

        perforated_page = d.pop("perforatedPage", UNSET)

        plastic_carddouble_sidedback_html = d.pop("plasticCard[doubleSided][backHTML]", UNSET)

        plastic_carddouble_sidedfront_html = d.pop("plasticCard[doubleSided][frontHTML]", UNSET)

        plastic_cardsize = d.pop("plasticCard[size]", UNSET)

        return_envelope = d.pop("returnEnvelope", UNSET)

        send_date = d.pop("sendDate", UNSET)

        size = d.pop("size", UNSET)

        to = d.pop("to", UNSET)

        create_letter_data_body = cls(
            address_placement=address_placement,
            color=color,
            description=description,
            double_sided=double_sided,
            envelope_type=envelope_type,
            express=express,
            extra_service=extra_service,
            from_=from_,
            html=html,
            mailing_class=mailing_class,
            merge_variableslanguage=merge_variableslanguage,
            metadatacompany=metadatacompany,
            perforated_page=perforated_page,
            plastic_carddouble_sidedback_html=plastic_carddouble_sidedback_html,
            plastic_carddouble_sidedfront_html=plastic_carddouble_sidedfront_html,
            plastic_cardsize=plastic_cardsize,
            return_envelope=return_envelope,
            send_date=send_date,
            size=size,
            to=to,
        )

        create_letter_data_body.additional_properties = d
        return create_letter_data_body

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
