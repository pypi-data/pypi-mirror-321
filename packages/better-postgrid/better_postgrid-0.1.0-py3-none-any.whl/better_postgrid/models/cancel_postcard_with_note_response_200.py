from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cancel_postcard_with_note_response_200_cancellation import (
        CancelPostcardWithNoteResponse200Cancellation,
    )
    from ..models.cancel_postcard_with_note_response_200_from import CancelPostcardWithNoteResponse200From
    from ..models.cancel_postcard_with_note_response_200_metadata import CancelPostcardWithNoteResponse200Metadata
    from ..models.cancel_postcard_with_note_response_200_to import CancelPostcardWithNoteResponse200To


T = TypeVar("T", bound="CancelPostcardWithNoteResponse200")


@_attrs_define
class CancelPostcardWithNoteResponse200:
    """
    Attributes:
        back_template (Union[Unset, str]):  Example: template_39JBwJzymaqAx4RieG5XdG.
        cancellation (Union[Unset, CancelPostcardWithNoteResponse200Cancellation]):
        carrier_tracking (Union[Unset, Any]):
        created_at (Union[Unset, str]):  Example: 2024-01-25T15:45:42.470Z.
        description (Union[Unset, str]):  Example: cancellation test 3.
        express (Union[Unset, bool]):
        from_ (Union[Unset, CancelPostcardWithNoteResponse200From]):
        front_template (Union[Unset, str]):  Example: template_vae2fc9kEc5wmfBVKuEYE1.
        id (Union[Unset, str]):  Example: postcard_55yTG9Hjt7mg9UtkRDRNNz.
        live (Union[Unset, bool]):
        mailing_class (Union[Unset, str]):  Example: first_class.
        metadata (Union[Unset, CancelPostcardWithNoteResponse200Metadata]):
        object_ (Union[Unset, str]):  Example: postcard.
        page_count (Union[Unset, float]):  Example: 2.
        send_date (Union[Unset, str]):  Example: 2024-01-25T15:45:42.458Z.
        size (Union[Unset, str]):  Example: 9x6.
        status (Union[Unset, str]):  Example: cancelled.
        to (Union[Unset, CancelPostcardWithNoteResponse200To]):
        updated_at (Union[Unset, str]):  Example: 2024-01-25T15:46:09.244Z.
        url (Union[Unset, str]):  Example: https://pg-prod-bucket-
            1.s3.amazonaws.com/test/postcard_55yTG9Hjt7mg9UtkRDRNNz?AWSAccessKeyId=AKIA5GFUILSULWTWCR64&Expires=1706198469&S
            ignature=A7Irt4Uz%2FgT58MHSun5KS9C%2BTEc%3D.
    """

    back_template: Union[Unset, str] = UNSET
    cancellation: Union[Unset, "CancelPostcardWithNoteResponse200Cancellation"] = UNSET
    carrier_tracking: Union[Unset, Any] = UNSET
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    express: Union[Unset, bool] = UNSET
    from_: Union[Unset, "CancelPostcardWithNoteResponse200From"] = UNSET
    front_template: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    mailing_class: Union[Unset, str] = UNSET
    metadata: Union[Unset, "CancelPostcardWithNoteResponse200Metadata"] = UNSET
    object_: Union[Unset, str] = UNSET
    page_count: Union[Unset, float] = UNSET
    send_date: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    to: Union[Unset, "CancelPostcardWithNoteResponse200To"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        back_template = self.back_template

        cancellation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cancellation, Unset):
            cancellation = self.cancellation.to_dict()

        carrier_tracking = self.carrier_tracking

        created_at = self.created_at

        description = self.description

        express = self.express

        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        front_template = self.front_template

        id = self.id

        live = self.live

        mailing_class = self.mailing_class

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        object_ = self.object_

        page_count = self.page_count

        send_date = self.send_date

        size = self.size

        status = self.status

        to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if back_template is not UNSET:
            field_dict["backTemplate"] = back_template
        if cancellation is not UNSET:
            field_dict["cancellation"] = cancellation
        if carrier_tracking is not UNSET:
            field_dict["carrierTracking"] = carrier_tracking
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if express is not UNSET:
            field_dict["express"] = express
        if from_ is not UNSET:
            field_dict["from"] = from_
        if front_template is not UNSET:
            field_dict["frontTemplate"] = front_template
        if id is not UNSET:
            field_dict["id"] = id
        if live is not UNSET:
            field_dict["live"] = live
        if mailing_class is not UNSET:
            field_dict["mailingClass"] = mailing_class
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
        if to is not UNSET:
            field_dict["to"] = to
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.cancel_postcard_with_note_response_200_cancellation import (
            CancelPostcardWithNoteResponse200Cancellation,
        )
        from ..models.cancel_postcard_with_note_response_200_from import CancelPostcardWithNoteResponse200From
        from ..models.cancel_postcard_with_note_response_200_metadata import CancelPostcardWithNoteResponse200Metadata
        from ..models.cancel_postcard_with_note_response_200_to import CancelPostcardWithNoteResponse200To

        d = src_dict.copy()
        back_template = d.pop("backTemplate", UNSET)

        _cancellation = d.pop("cancellation", UNSET)
        cancellation: Union[Unset, CancelPostcardWithNoteResponse200Cancellation]
        if isinstance(_cancellation, Unset):
            cancellation = UNSET
        else:
            cancellation = CancelPostcardWithNoteResponse200Cancellation.from_dict(_cancellation)

        carrier_tracking = d.pop("carrierTracking", UNSET)

        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

        express = d.pop("express", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, CancelPostcardWithNoteResponse200From]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = CancelPostcardWithNoteResponse200From.from_dict(_from_)

        front_template = d.pop("frontTemplate", UNSET)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        mailing_class = d.pop("mailingClass", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CancelPostcardWithNoteResponse200Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CancelPostcardWithNoteResponse200Metadata.from_dict(_metadata)

        object_ = d.pop("object", UNSET)

        page_count = d.pop("pageCount", UNSET)

        send_date = d.pop("sendDate", UNSET)

        size = d.pop("size", UNSET)

        status = d.pop("status", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, CancelPostcardWithNoteResponse200To]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = CancelPostcardWithNoteResponse200To.from_dict(_to)

        updated_at = d.pop("updatedAt", UNSET)

        url = d.pop("url", UNSET)

        cancel_postcard_with_note_response_200 = cls(
            back_template=back_template,
            cancellation=cancellation,
            carrier_tracking=carrier_tracking,
            created_at=created_at,
            description=description,
            express=express,
            from_=from_,
            front_template=front_template,
            id=id,
            live=live,
            mailing_class=mailing_class,
            metadata=metadata,
            object_=object_,
            page_count=page_count,
            send_date=send_date,
            size=size,
            status=status,
            to=to,
            updated_at=updated_at,
            url=url,
        )

        cancel_postcard_with_note_response_200.additional_properties = d
        return cancel_postcard_with_note_response_200

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
