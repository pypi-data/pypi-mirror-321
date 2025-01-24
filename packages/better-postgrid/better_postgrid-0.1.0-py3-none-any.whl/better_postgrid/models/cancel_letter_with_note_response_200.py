from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cancel_letter_with_note_response_200_cancellation import CancelLetterWithNoteResponse200Cancellation
    from ..models.cancel_letter_with_note_response_200_from import CancelLetterWithNoteResponse200From
    from ..models.cancel_letter_with_note_response_200_merge_variables import (
        CancelLetterWithNoteResponse200MergeVariables,
    )
    from ..models.cancel_letter_with_note_response_200_metadata import CancelLetterWithNoteResponse200Metadata
    from ..models.cancel_letter_with_note_response_200_to import CancelLetterWithNoteResponse200To


T = TypeVar("T", bound="CancelLetterWithNoteResponse200")


@_attrs_define
class CancelLetterWithNoteResponse200:
    """
    Attributes:
        address_placement (Union[Unset, str]):  Example: top_first_page.
        attached_pdf (Union[Unset, Any]):
        cancellation (Union[Unset, CancelLetterWithNoteResponse200Cancellation]):
        carrier_tracking (Union[Unset, Any]):
        color (Union[Unset, bool]):
        created_at (Union[Unset, str]):  Example: 2024-01-25T15:49:18.575Z.
        description (Union[Unset, str]):  Example: cancelled with note 6.
        double_sided (Union[Unset, bool]):
        envelope_type (Union[Unset, str]):  Example: standard_double_window.
        express (Union[Unset, bool]):
        from_ (Union[Unset, CancelLetterWithNoteResponse200From]):
        id (Union[Unset, str]):  Example: letter_cS61RTPrSvBKVyT7kenpjn.
        live (Union[Unset, bool]):
        mailing_class (Union[Unset, str]):  Example: first_class.
        merge_variables (Union[Unset, CancelLetterWithNoteResponse200MergeVariables]):
        metadata (Union[Unset, CancelLetterWithNoteResponse200Metadata]):
        object_ (Union[Unset, str]):  Example: letter.
        page_count (Union[Unset, float]):  Example: 1.
        send_date (Union[Unset, str]):  Example: 2024-01-25T15:49:18.572Z.
        size (Union[Unset, str]):  Example: us_letter.
        status (Union[Unset, str]):  Example: cancelled.
        template (Union[Unset, str]):  Example: template_fcxb4FEkwMiYYWTveqmmjr.
        to (Union[Unset, CancelLetterWithNoteResponse200To]):
        updated_at (Union[Unset, str]):  Example: 2024-01-25T15:49:30.319Z.
        url (Union[Unset, str]):  Example: https://pg-prod-bucket-
            1.s3.amazonaws.com/test/letter_cS61RTPrSvBKVyT7kenpjn?AWSAccessKeyId=AKIA5GFUILSULWTWCR64&Expires=1706198670&Sig
            nature=qM2netdP1U1BQ8A5Kgmg94WMIkU%3D.
    """

    address_placement: Union[Unset, str] = UNSET
    attached_pdf: Union[Unset, Any] = UNSET
    cancellation: Union[Unset, "CancelLetterWithNoteResponse200Cancellation"] = UNSET
    carrier_tracking: Union[Unset, Any] = UNSET
    color: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    double_sided: Union[Unset, bool] = UNSET
    envelope_type: Union[Unset, str] = UNSET
    express: Union[Unset, bool] = UNSET
    from_: Union[Unset, "CancelLetterWithNoteResponse200From"] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    mailing_class: Union[Unset, str] = UNSET
    merge_variables: Union[Unset, "CancelLetterWithNoteResponse200MergeVariables"] = UNSET
    metadata: Union[Unset, "CancelLetterWithNoteResponse200Metadata"] = UNSET
    object_: Union[Unset, str] = UNSET
    page_count: Union[Unset, float] = UNSET
    send_date: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    to: Union[Unset, "CancelLetterWithNoteResponse200To"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_placement = self.address_placement

        attached_pdf = self.attached_pdf

        cancellation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cancellation, Unset):
            cancellation = self.cancellation.to_dict()

        carrier_tracking = self.carrier_tracking

        color = self.color

        created_at = self.created_at

        description = self.description

        double_sided = self.double_sided

        envelope_type = self.envelope_type

        express = self.express

        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

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

        page_count = self.page_count

        send_date = self.send_date

        size = self.size

        status = self.status

        template = self.template

        to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_placement is not UNSET:
            field_dict["addressPlacement"] = address_placement
        if attached_pdf is not UNSET:
            field_dict["attachedPDF"] = attached_pdf
        if cancellation is not UNSET:
            field_dict["cancellation"] = cancellation
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
        if envelope_type is not UNSET:
            field_dict["envelopeType"] = envelope_type
        if express is not UNSET:
            field_dict["express"] = express
        if from_ is not UNSET:
            field_dict["from"] = from_
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
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
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
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.cancel_letter_with_note_response_200_cancellation import (
            CancelLetterWithNoteResponse200Cancellation,
        )
        from ..models.cancel_letter_with_note_response_200_from import CancelLetterWithNoteResponse200From
        from ..models.cancel_letter_with_note_response_200_merge_variables import (
            CancelLetterWithNoteResponse200MergeVariables,
        )
        from ..models.cancel_letter_with_note_response_200_metadata import CancelLetterWithNoteResponse200Metadata
        from ..models.cancel_letter_with_note_response_200_to import CancelLetterWithNoteResponse200To

        d = src_dict.copy()
        address_placement = d.pop("addressPlacement", UNSET)

        attached_pdf = d.pop("attachedPDF", UNSET)

        _cancellation = d.pop("cancellation", UNSET)
        cancellation: Union[Unset, CancelLetterWithNoteResponse200Cancellation]
        if isinstance(_cancellation, Unset):
            cancellation = UNSET
        else:
            cancellation = CancelLetterWithNoteResponse200Cancellation.from_dict(_cancellation)

        carrier_tracking = d.pop("carrierTracking", UNSET)

        color = d.pop("color", UNSET)

        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

        double_sided = d.pop("doubleSided", UNSET)

        envelope_type = d.pop("envelopeType", UNSET)

        express = d.pop("express", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, CancelLetterWithNoteResponse200From]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = CancelLetterWithNoteResponse200From.from_dict(_from_)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        mailing_class = d.pop("mailingClass", UNSET)

        _merge_variables = d.pop("mergeVariables", UNSET)
        merge_variables: Union[Unset, CancelLetterWithNoteResponse200MergeVariables]
        if isinstance(_merge_variables, Unset):
            merge_variables = UNSET
        else:
            merge_variables = CancelLetterWithNoteResponse200MergeVariables.from_dict(_merge_variables)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CancelLetterWithNoteResponse200Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CancelLetterWithNoteResponse200Metadata.from_dict(_metadata)

        object_ = d.pop("object", UNSET)

        page_count = d.pop("pageCount", UNSET)

        send_date = d.pop("sendDate", UNSET)

        size = d.pop("size", UNSET)

        status = d.pop("status", UNSET)

        template = d.pop("template", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, CancelLetterWithNoteResponse200To]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = CancelLetterWithNoteResponse200To.from_dict(_to)

        updated_at = d.pop("updatedAt", UNSET)

        url = d.pop("url", UNSET)

        cancel_letter_with_note_response_200 = cls(
            address_placement=address_placement,
            attached_pdf=attached_pdf,
            cancellation=cancellation,
            carrier_tracking=carrier_tracking,
            color=color,
            created_at=created_at,
            description=description,
            double_sided=double_sided,
            envelope_type=envelope_type,
            express=express,
            from_=from_,
            id=id,
            live=live,
            mailing_class=mailing_class,
            merge_variables=merge_variables,
            metadata=metadata,
            object_=object_,
            page_count=page_count,
            send_date=send_date,
            size=size,
            status=status,
            template=template,
            to=to,
            updated_at=updated_at,
            url=url,
        )

        cancel_letter_with_note_response_200.additional_properties = d
        return cancel_letter_with_note_response_200

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
