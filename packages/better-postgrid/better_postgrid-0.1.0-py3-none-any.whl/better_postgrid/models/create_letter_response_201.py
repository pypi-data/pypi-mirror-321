from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_letter_response_201_attached_pdf_type_0 import CreateLetterResponse201AttachedPDFType0
    from ..models.create_letter_response_201_from import CreateLetterResponse201From
    from ..models.create_letter_response_201_merge_variables import CreateLetterResponse201MergeVariables
    from ..models.create_letter_response_201_metadata import CreateLetterResponse201Metadata
    from ..models.create_letter_response_201_plastic_card import CreateLetterResponse201PlasticCard
    from ..models.create_letter_response_201_to import CreateLetterResponse201To


T = TypeVar("T", bound="CreateLetterResponse201")


@_attrs_define
class CreateLetterResponse201:
    """
    Attributes:
        address_placement (Union[Unset, str]):  Example: top_first_page.
        attached_pdf (Union['CreateLetterResponse201AttachedPDFType0', None, Unset]):
        carrier_tracking (Union[Unset, Any]):
        color (Union[Unset, bool]):
        created_at (Union[Unset, str]):  Example: 2020-11-12T23:30:12.581Z.
        description (Union[Unset, str]):  Example: Template with attached PDF.
        double_sided (Union[Unset, bool]):  Example: True.
        envelope (Union[Unset, str]):  Example: standard.
        envelope_type (Union[Unset, str]):  Example: standard_double_window.
        express (Union[Unset, bool]):
        extra_service (Union[Unset, str]):  Example: certified.
        from_ (Union[Unset, CreateLetterResponse201From]):
        html (Union[Unset, str]):  Example: <b>Hello</b>, {{to.firstName}}!.
        id (Union[Unset, str]):  Example: letter_b2friz2FYMzHAUmDuZfy1F.
        live (Union[Unset, bool]):
        mailing_class (Union[Unset, str]):  Example: first_class.
        merge_variables (Union[Unset, CreateLetterResponse201MergeVariables]):
        metadata (Union[Unset, CreateLetterResponse201Metadata]):
        object_ (Union[Unset, str]):  Example: letter.
        perforated_page (Union[Unset, float]):  Example: 1.
        plastic_card (Union[Unset, CreateLetterResponse201PlasticCard]):
        send_date (Union[Unset, str]):  Example: Thu Nov 12 2020.
        size (Union[Unset, str]):  Example: us_letter.
        status (Union[Unset, str]):  Example: ready.
        template (Union[Unset, str]):  Example: template_tBnVEzz878mXLbHQaz86j8.
        to (Union[Unset, CreateLetterResponse201To]):
        updated_at (Union[Unset, str]):  Example: 2020-11-12T23:30:12.581Z.
    """

    address_placement: Union[Unset, str] = UNSET
    attached_pdf: Union["CreateLetterResponse201AttachedPDFType0", None, Unset] = UNSET
    carrier_tracking: Union[Unset, Any] = UNSET
    color: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    double_sided: Union[Unset, bool] = UNSET
    envelope: Union[Unset, str] = UNSET
    envelope_type: Union[Unset, str] = UNSET
    express: Union[Unset, bool] = UNSET
    extra_service: Union[Unset, str] = UNSET
    from_: Union[Unset, "CreateLetterResponse201From"] = UNSET
    html: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    mailing_class: Union[Unset, str] = UNSET
    merge_variables: Union[Unset, "CreateLetterResponse201MergeVariables"] = UNSET
    metadata: Union[Unset, "CreateLetterResponse201Metadata"] = UNSET
    object_: Union[Unset, str] = UNSET
    perforated_page: Union[Unset, float] = UNSET
    plastic_card: Union[Unset, "CreateLetterResponse201PlasticCard"] = UNSET
    send_date: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    to: Union[Unset, "CreateLetterResponse201To"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_letter_response_201_attached_pdf_type_0 import CreateLetterResponse201AttachedPDFType0

        address_placement = self.address_placement

        attached_pdf: Union[None, Unset, dict[str, Any]]
        if isinstance(self.attached_pdf, Unset):
            attached_pdf = UNSET
        elif isinstance(self.attached_pdf, CreateLetterResponse201AttachedPDFType0):
            attached_pdf = self.attached_pdf.to_dict()
        else:
            attached_pdf = self.attached_pdf

        carrier_tracking = self.carrier_tracking

        color = self.color

        created_at = self.created_at

        description = self.description

        double_sided = self.double_sided

        envelope = self.envelope

        envelope_type = self.envelope_type

        express = self.express

        extra_service = self.extra_service

        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        html = self.html

        id = self.id

        live = self.live

        mailing_class = self.mailing_class

        merge_variables: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merge_variables, Unset):
            merge_variables = self.merge_variables.to_dict()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        object_ = self.object_

        perforated_page = self.perforated_page

        plastic_card: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.plastic_card, Unset):
            plastic_card = self.plastic_card.to_dict()

        send_date = self.send_date

        size = self.size

        status = self.status

        template = self.template

        to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_placement is not UNSET:
            field_dict["addressPlacement"] = address_placement
        if attached_pdf is not UNSET:
            field_dict["attachedPDF"] = attached_pdf
        if carrier_tracking is not UNSET:
            field_dict["carrierTracking"] = carrier_tracking
        if color is not UNSET:
            field_dict["color"] = color
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if double_sided is not UNSET:
            field_dict["doubleSided"] = double_sided
        if envelope is not UNSET:
            field_dict["envelope"] = envelope
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
        if id is not UNSET:
            field_dict["id"] = id
        if live is not UNSET:
            field_dict["live"] = live
        if mailing_class is not UNSET:
            field_dict["mailingClass"] = mailing_class
        if merge_variables is not UNSET:
            field_dict["mergeVariables"] = merge_variables
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if object_ is not UNSET:
            field_dict["object"] = object_
        if perforated_page is not UNSET:
            field_dict["perforatedPage"] = perforated_page
        if plastic_card is not UNSET:
            field_dict["plasticCard"] = plastic_card
        if send_date is not UNSET:
            field_dict["sendDate"] = send_date
        if size is not UNSET:
            field_dict["size"] = size
        if status is not UNSET:
            field_dict["status"] = status
        if template is not UNSET:
            field_dict["template"] = template
        if to is not UNSET:
            field_dict["to"] = to
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_letter_response_201_attached_pdf_type_0 import CreateLetterResponse201AttachedPDFType0
        from ..models.create_letter_response_201_from import CreateLetterResponse201From
        from ..models.create_letter_response_201_merge_variables import CreateLetterResponse201MergeVariables
        from ..models.create_letter_response_201_metadata import CreateLetterResponse201Metadata
        from ..models.create_letter_response_201_plastic_card import CreateLetterResponse201PlasticCard
        from ..models.create_letter_response_201_to import CreateLetterResponse201To

        d = src_dict.copy()
        address_placement = d.pop("addressPlacement", UNSET)

        def _parse_attached_pdf(data: object) -> Union["CreateLetterResponse201AttachedPDFType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attached_pdf_type_0 = CreateLetterResponse201AttachedPDFType0.from_dict(data)

                return attached_pdf_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CreateLetterResponse201AttachedPDFType0", None, Unset], data)

        attached_pdf = _parse_attached_pdf(d.pop("attachedPDF", UNSET))

        carrier_tracking = d.pop("carrierTracking", UNSET)

        color = d.pop("color", UNSET)

        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

        double_sided = d.pop("doubleSided", UNSET)

        envelope = d.pop("envelope", UNSET)

        envelope_type = d.pop("envelopeType", UNSET)

        express = d.pop("express", UNSET)

        extra_service = d.pop("extraService", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, CreateLetterResponse201From]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = CreateLetterResponse201From.from_dict(_from_)

        html = d.pop("html", UNSET)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        mailing_class = d.pop("mailingClass", UNSET)

        _merge_variables = d.pop("mergeVariables", UNSET)
        merge_variables: Union[Unset, CreateLetterResponse201MergeVariables]
        if isinstance(_merge_variables, Unset):
            merge_variables = UNSET
        else:
            merge_variables = CreateLetterResponse201MergeVariables.from_dict(_merge_variables)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CreateLetterResponse201Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateLetterResponse201Metadata.from_dict(_metadata)

        object_ = d.pop("object", UNSET)

        perforated_page = d.pop("perforatedPage", UNSET)

        _plastic_card = d.pop("plasticCard", UNSET)
        plastic_card: Union[Unset, CreateLetterResponse201PlasticCard]
        if isinstance(_plastic_card, Unset):
            plastic_card = UNSET
        else:
            plastic_card = CreateLetterResponse201PlasticCard.from_dict(_plastic_card)

        send_date = d.pop("sendDate", UNSET)

        size = d.pop("size", UNSET)

        status = d.pop("status", UNSET)

        template = d.pop("template", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, CreateLetterResponse201To]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = CreateLetterResponse201To.from_dict(_to)

        updated_at = d.pop("updatedAt", UNSET)

        create_letter_response_201 = cls(
            address_placement=address_placement,
            attached_pdf=attached_pdf,
            carrier_tracking=carrier_tracking,
            color=color,
            created_at=created_at,
            description=description,
            double_sided=double_sided,
            envelope=envelope,
            envelope_type=envelope_type,
            express=express,
            extra_service=extra_service,
            from_=from_,
            html=html,
            id=id,
            live=live,
            mailing_class=mailing_class,
            merge_variables=merge_variables,
            metadata=metadata,
            object_=object_,
            perforated_page=perforated_page,
            plastic_card=plastic_card,
            send_date=send_date,
            size=size,
            status=status,
            template=template,
            to=to,
            updated_at=updated_at,
        )

        create_letter_response_201.additional_properties = d
        return create_letter_response_201

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
