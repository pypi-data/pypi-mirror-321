from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cancel_self_mailers_response_200_cancellation import CancelSelfMailersResponse200Cancellation
    from ..models.cancel_self_mailers_response_200_from import CancelSelfMailersResponse200From
    from ..models.cancel_self_mailers_response_200_to import CancelSelfMailersResponse200To


T = TypeVar("T", bound="CancelSelfMailersResponse200")


@_attrs_define
class CancelSelfMailersResponse200:
    """
    Attributes:
        cancellation (Union[Unset, CancelSelfMailersResponse200Cancellation]):
        created_at (Union[Unset, str]):  Example: 2023-07-06T15:31:04.560Z.
        from_ (Union[Unset, CancelSelfMailersResponse200From]):
        id (Union[Unset, str]):  Example: self_mailer_5gQmDVDUMpQEYTuSxSf645.
        live (Union[Unset, bool]):
        mailing_class (Union[Unset, str]):  Example: first_class.
        object_ (Union[Unset, str]):  Example: self_mailer.
        page_count (Union[Unset, float]):  Example: 2.
        send_date (Union[Unset, str]):  Example: 2023-07-06T15:31:04.543Z.
        size (Union[Unset, str]):  Example: 8.5x11_bifold.
        status (Union[Unset, str]):  Example: cancelled.
        to (Union[Unset, CancelSelfMailersResponse200To]):
        updated_at (Union[Unset, str]):  Example: 2023-07-06T16:35:53.946Z.
        uploaded_pdf (Union[Unset, str]):  Example: https://pg-prod-bucket-
            1.s3.amazonaws.com/test/pdf_nCZAkLeiS7x3vYZsSWkRc7?AWSAccessKeyId=AKIA5GFUILSULWTWCR64&Expires=1688662253&Signat
            ure=6reGm5FHQBn8ih4i%2BB1zS%2Bg8%2B%2FM%3D.
        url (Union[Unset, str]):  Example: https://pg-prod-bucket-
            1.s3.amazonaws.com/test/self_mailer_5gQmDVDUMpQEYTuSxSf645?AWSAccessKeyId=AKIA5GFUILSULWTWCR64&Expires=168866225
            3&Signature=8Un4TRW0kRipeU0SwHP3TfLVFok%3D.
    """

    cancellation: Union[Unset, "CancelSelfMailersResponse200Cancellation"] = UNSET
    created_at: Union[Unset, str] = UNSET
    from_: Union[Unset, "CancelSelfMailersResponse200From"] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    mailing_class: Union[Unset, str] = UNSET
    object_: Union[Unset, str] = UNSET
    page_count: Union[Unset, float] = UNSET
    send_date: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    to: Union[Unset, "CancelSelfMailersResponse200To"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    uploaded_pdf: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancellation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cancellation, Unset):
            cancellation = self.cancellation.to_dict()

        created_at = self.created_at

        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        id = self.id

        live = self.live

        mailing_class = self.mailing_class

        object_ = self.object_

        page_count = self.page_count

        send_date = self.send_date

        size = self.size

        status = self.status

        to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        updated_at = self.updated_at

        uploaded_pdf = self.uploaded_pdf

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancellation is not UNSET:
            field_dict["cancellation"] = cancellation
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if from_ is not UNSET:
            field_dict["from"] = from_
        if id is not UNSET:
            field_dict["id"] = id
        if live is not UNSET:
            field_dict["live"] = live
        if mailing_class is not UNSET:
            field_dict["mailingClass"] = mailing_class
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
        if uploaded_pdf is not UNSET:
            field_dict["uploadedPDF"] = uploaded_pdf
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.cancel_self_mailers_response_200_cancellation import CancelSelfMailersResponse200Cancellation
        from ..models.cancel_self_mailers_response_200_from import CancelSelfMailersResponse200From
        from ..models.cancel_self_mailers_response_200_to import CancelSelfMailersResponse200To

        d = src_dict.copy()
        _cancellation = d.pop("cancellation", UNSET)
        cancellation: Union[Unset, CancelSelfMailersResponse200Cancellation]
        if isinstance(_cancellation, Unset):
            cancellation = UNSET
        else:
            cancellation = CancelSelfMailersResponse200Cancellation.from_dict(_cancellation)

        created_at = d.pop("createdAt", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, CancelSelfMailersResponse200From]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = CancelSelfMailersResponse200From.from_dict(_from_)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        mailing_class = d.pop("mailingClass", UNSET)

        object_ = d.pop("object", UNSET)

        page_count = d.pop("pageCount", UNSET)

        send_date = d.pop("sendDate", UNSET)

        size = d.pop("size", UNSET)

        status = d.pop("status", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, CancelSelfMailersResponse200To]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = CancelSelfMailersResponse200To.from_dict(_to)

        updated_at = d.pop("updatedAt", UNSET)

        uploaded_pdf = d.pop("uploadedPDF", UNSET)

        url = d.pop("url", UNSET)

        cancel_self_mailers_response_200 = cls(
            cancellation=cancellation,
            created_at=created_at,
            from_=from_,
            id=id,
            live=live,
            mailing_class=mailing_class,
            object_=object_,
            page_count=page_count,
            send_date=send_date,
            size=size,
            status=status,
            to=to,
            updated_at=updated_at,
            uploaded_pdf=uploaded_pdf,
            url=url,
        )

        cancel_self_mailers_response_200.additional_properties = d
        return cancel_self_mailers_response_200

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
