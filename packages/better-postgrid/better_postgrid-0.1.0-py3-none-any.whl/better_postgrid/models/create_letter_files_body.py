from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="CreateLetterFilesBody")


@_attrs_define
class CreateLetterFilesBody:
    """
    Attributes:
        address_placement (Union[Unset, str]): The location where the address will be placed. Must be either
            `top_first_page` or `insert_blank_page`.
            `optional` Example: top_first_page.
        color (Union[Unset, str]): Indicates whether the letter will be printed in color or not.
            `optional` Example: false.
        description (Union[Unset, str]): A description for the letter.

            `optional` Example: Template with attached PDF.
        double_sided (Union[Unset, str]): Indicates if the letter is double sided or not.
            `optional`
            Default: `false` Example: true.
        envelope_type (Union[Unset, str]): Indicates the envelope type for the letter. Must be either
            `standard_double_window` or `flat`.
            `optional` Example: flat.
        express (Union[Unset, str]): See [express shipping](#express-shipping). Example: false.
        extra_service (Union[Unset, str]): Indicates extra services for the letter. See [certified and registered
            mail](#certified-and-registered-mail).
            `optional` Example: certified.
        from_ (Union[Unset, str]): The `id` or [contact](#contact) `object` of the sender. You can either pass a contact
            `object` or a contact's `id`.
            `required` Example: contact_8v1mibdKkpK8Si6vz7xBVi.
        mailing_class (Union[Unset, str]): Defaults to `first_class`. See [mailing class](#mailing-class).
            `optional` Example: first_class.
        merge_variableslanguage (Union[Unset, str]):  Example: english.
        metadatacompany (Union[Unset, str]):  Example: PostGrid.
        perforated_page (Union[Unset, str]): Indicates which page should be perforated. If supplied, the value must be
            `1` meaning perforate the first page.

            `optional` Example: 1.
        plastic_carddouble_sidedpdf (Union[Unset, str]): The link to the PDF to be used for the plastic card.

            `required` Example: https://eksandbox.s3.amazonaws.com/files/2_page_plastic_card_ex.pdf.
        plastic_cardsingle_sidedpdf (Union[Unset, File]): The uploaded PDF to be used for the plastic card.

            `required`
        plastic_cardsize (Union[Unset, str]): Size of plastic card

            `required` Example: standard.
        return_envelope (Union[Unset, str]): The `id` of the [return envelope](#return-envelope) to be used.
            `optional` Example: return_envelope_97Tcv1LxhWWLPUvn58CuVJ.
        send_date (Union[Unset, str]): The desired date for the letter to be sent out.

            `optional` Example: 2023-02-16T15:40:35.873Z.
        size (Union[Unset, str]): Default size will be chosen based on the destination country, if not provided.
            Indicates the letter size for the letter being created. See [letter size](#letter-size)

            `optional` Example: us_letter.
        template (Union[Unset, str]): The template's `id` to be used for the letter.
            `required` Example: template_5n7fprLVnDDsULzhguWBaZ.
        to (Union[Unset, str]): The `id` or [contact](#contact) `object` of the receiver. You can either pass a contact
            `object` or a contact's `id`.
            `required` Example: contact_8v1mibdKkpK8Si6vz7xBVi.
    """

    address_placement: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    double_sided: Union[Unset, str] = UNSET
    envelope_type: Union[Unset, str] = UNSET
    express: Union[Unset, str] = UNSET
    extra_service: Union[Unset, str] = UNSET
    from_: Union[Unset, str] = UNSET
    mailing_class: Union[Unset, str] = UNSET
    merge_variableslanguage: Union[Unset, str] = UNSET
    metadatacompany: Union[Unset, str] = UNSET
    perforated_page: Union[Unset, str] = UNSET
    plastic_carddouble_sidedpdf: Union[Unset, str] = UNSET
    plastic_cardsingle_sidedpdf: Union[Unset, File] = UNSET
    plastic_cardsize: Union[Unset, str] = UNSET
    return_envelope: Union[Unset, str] = UNSET
    send_date: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
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

        mailing_class = self.mailing_class

        merge_variableslanguage = self.merge_variableslanguage

        metadatacompany = self.metadatacompany

        perforated_page = self.perforated_page

        plastic_carddouble_sidedpdf = self.plastic_carddouble_sidedpdf

        plastic_cardsingle_sidedpdf: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.plastic_cardsingle_sidedpdf, Unset):
            plastic_cardsingle_sidedpdf = self.plastic_cardsingle_sidedpdf.to_tuple()

        plastic_cardsize = self.plastic_cardsize

        return_envelope = self.return_envelope

        send_date = self.send_date

        size = self.size

        template = self.template

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
        if mailing_class is not UNSET:
            field_dict["mailingClass"] = mailing_class
        if merge_variableslanguage is not UNSET:
            field_dict["mergeVariables[language]"] = merge_variableslanguage
        if metadatacompany is not UNSET:
            field_dict["metadata[company]"] = metadatacompany
        if perforated_page is not UNSET:
            field_dict["perforatedPage"] = perforated_page
        if plastic_carddouble_sidedpdf is not UNSET:
            field_dict["plasticCard[doubleSided][pdf]"] = plastic_carddouble_sidedpdf
        if plastic_cardsingle_sidedpdf is not UNSET:
            field_dict["plasticCard[singleSided][pdf]"] = plastic_cardsingle_sidedpdf
        if plastic_cardsize is not UNSET:
            field_dict["plasticCard[size]"] = plastic_cardsize
        if return_envelope is not UNSET:
            field_dict["returnEnvelope"] = return_envelope
        if send_date is not UNSET:
            field_dict["sendDate"] = send_date
        if size is not UNSET:
            field_dict["size"] = size
        if template is not UNSET:
            field_dict["template"] = template
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        address_placement = (
            self.address_placement
            if isinstance(self.address_placement, Unset)
            else (None, str(self.address_placement).encode(), "text/plain")
        )

        color = self.color if isinstance(self.color, Unset) else (None, str(self.color).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        double_sided = (
            self.double_sided
            if isinstance(self.double_sided, Unset)
            else (None, str(self.double_sided).encode(), "text/plain")
        )

        envelope_type = (
            self.envelope_type
            if isinstance(self.envelope_type, Unset)
            else (None, str(self.envelope_type).encode(), "text/plain")
        )

        express = self.express if isinstance(self.express, Unset) else (None, str(self.express).encode(), "text/plain")

        extra_service = (
            self.extra_service
            if isinstance(self.extra_service, Unset)
            else (None, str(self.extra_service).encode(), "text/plain")
        )

        from_ = self.from_ if isinstance(self.from_, Unset) else (None, str(self.from_).encode(), "text/plain")

        mailing_class = (
            self.mailing_class
            if isinstance(self.mailing_class, Unset)
            else (None, str(self.mailing_class).encode(), "text/plain")
        )

        merge_variableslanguage = (
            self.merge_variableslanguage
            if isinstance(self.merge_variableslanguage, Unset)
            else (None, str(self.merge_variableslanguage).encode(), "text/plain")
        )

        metadatacompany = (
            self.metadatacompany
            if isinstance(self.metadatacompany, Unset)
            else (None, str(self.metadatacompany).encode(), "text/plain")
        )

        perforated_page = (
            self.perforated_page
            if isinstance(self.perforated_page, Unset)
            else (None, str(self.perforated_page).encode(), "text/plain")
        )

        plastic_carddouble_sidedpdf = (
            self.plastic_carddouble_sidedpdf
            if isinstance(self.plastic_carddouble_sidedpdf, Unset)
            else (None, str(self.plastic_carddouble_sidedpdf).encode(), "text/plain")
        )

        plastic_cardsingle_sidedpdf: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.plastic_cardsingle_sidedpdf, Unset):
            plastic_cardsingle_sidedpdf = self.plastic_cardsingle_sidedpdf.to_tuple()

        plastic_cardsize = (
            self.plastic_cardsize
            if isinstance(self.plastic_cardsize, Unset)
            else (None, str(self.plastic_cardsize).encode(), "text/plain")
        )

        return_envelope = (
            self.return_envelope
            if isinstance(self.return_envelope, Unset)
            else (None, str(self.return_envelope).encode(), "text/plain")
        )

        send_date = (
            self.send_date if isinstance(self.send_date, Unset) else (None, str(self.send_date).encode(), "text/plain")
        )

        size = self.size if isinstance(self.size, Unset) else (None, str(self.size).encode(), "text/plain")

        template = (
            self.template if isinstance(self.template, Unset) else (None, str(self.template).encode(), "text/plain")
        )

        to = self.to if isinstance(self.to, Unset) else (None, str(self.to).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

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
        if mailing_class is not UNSET:
            field_dict["mailingClass"] = mailing_class
        if merge_variableslanguage is not UNSET:
            field_dict["mergeVariables[language]"] = merge_variableslanguage
        if metadatacompany is not UNSET:
            field_dict["metadata[company]"] = metadatacompany
        if perforated_page is not UNSET:
            field_dict["perforatedPage"] = perforated_page
        if plastic_carddouble_sidedpdf is not UNSET:
            field_dict["plasticCard[doubleSided][pdf]"] = plastic_carddouble_sidedpdf
        if plastic_cardsingle_sidedpdf is not UNSET:
            field_dict["plasticCard[singleSided][pdf]"] = plastic_cardsingle_sidedpdf
        if plastic_cardsize is not UNSET:
            field_dict["plasticCard[size]"] = plastic_cardsize
        if return_envelope is not UNSET:
            field_dict["returnEnvelope"] = return_envelope
        if send_date is not UNSET:
            field_dict["sendDate"] = send_date
        if size is not UNSET:
            field_dict["size"] = size
        if template is not UNSET:
            field_dict["template"] = template
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

        mailing_class = d.pop("mailingClass", UNSET)

        merge_variableslanguage = d.pop("mergeVariables[language]", UNSET)

        metadatacompany = d.pop("metadata[company]", UNSET)

        perforated_page = d.pop("perforatedPage", UNSET)

        plastic_carddouble_sidedpdf = d.pop("plasticCard[doubleSided][pdf]", UNSET)

        _plastic_cardsingle_sidedpdf = d.pop("plasticCard[singleSided][pdf]", UNSET)
        plastic_cardsingle_sidedpdf: Union[Unset, File]
        if isinstance(_plastic_cardsingle_sidedpdf, Unset):
            plastic_cardsingle_sidedpdf = UNSET
        else:
            plastic_cardsingle_sidedpdf = File(payload=BytesIO(_plastic_cardsingle_sidedpdf))

        plastic_cardsize = d.pop("plasticCard[size]", UNSET)

        return_envelope = d.pop("returnEnvelope", UNSET)

        send_date = d.pop("sendDate", UNSET)

        size = d.pop("size", UNSET)

        template = d.pop("template", UNSET)

        to = d.pop("to", UNSET)

        create_letter_files_body = cls(
            address_placement=address_placement,
            color=color,
            description=description,
            double_sided=double_sided,
            envelope_type=envelope_type,
            express=express,
            extra_service=extra_service,
            from_=from_,
            mailing_class=mailing_class,
            merge_variableslanguage=merge_variableslanguage,
            metadatacompany=metadatacompany,
            perforated_page=perforated_page,
            plastic_carddouble_sidedpdf=plastic_carddouble_sidedpdf,
            plastic_cardsingle_sidedpdf=plastic_cardsingle_sidedpdf,
            plastic_cardsize=plastic_cardsize,
            return_envelope=return_envelope,
            send_date=send_date,
            size=size,
            template=template,
            to=to,
        )

        create_letter_files_body.additional_properties = d
        return create_letter_files_body

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
