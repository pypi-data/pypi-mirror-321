from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.progress_test_self_mailer_response_200_from import ProgressTestSelfMailerResponse200From
    from ..models.progress_test_self_mailer_response_200_to import ProgressTestSelfMailerResponse200To


T = TypeVar("T", bound="ProgressTestSelfMailerResponse200")


@_attrs_define
class ProgressTestSelfMailerResponse200:
    """
    Attributes:
        created_at (Union[Unset, str]):  Example: 2023-06-28T18:20:56.435Z.
        description (Union[Unset, str]):  Example: My HTML self mailer.
        from_ (Union[Unset, ProgressTestSelfMailerResponse200From]):
        id (Union[Unset, str]):  Example: self_mailer_wx97UGTC7H3UaSfhunWLjt.
        inside_html (Union[Unset, str]):  Example: Hello, {{to.firstName}}.
        live (Union[Unset, bool]):
        mailing_class (Union[Unset, str]):  Example: first_class.
        object_ (Union[Unset, str]):  Example: self_mailer.
        outside_html (Union[Unset, str]):  Example: Hello again, {{to.firstName}}.
        page_count (Union[Unset, float]):  Example: 2.
        send_date (Union[Unset, str]):  Example: 2023-06-28T18:20:56.430Z.
        size (Union[Unset, str]):  Example: 8.5x11_bifold.
        status (Union[Unset, str]):  Example: printing.
        to (Union[Unset, ProgressTestSelfMailerResponse200To]):
        updated_at (Union[Unset, str]):  Example: 2023-07-06T16:36:27.559Z.
        url (Union[Unset, str]):  Example: https://pg-prod-bucket-
            1.s3.amazonaws.com/test/self_mailer_wx97UGTC7H3UaSfhunWLjt?AWSAccessKeyId=AKIA5GFUILSULWTWCR64&Expires=168866228
            7&Signature=ne6IZ45j2gvnHFVtFbb44VYdqu0%3D.
    """

    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    from_: Union[Unset, "ProgressTestSelfMailerResponse200From"] = UNSET
    id: Union[Unset, str] = UNSET
    inside_html: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    mailing_class: Union[Unset, str] = UNSET
    object_: Union[Unset, str] = UNSET
    outside_html: Union[Unset, str] = UNSET
    page_count: Union[Unset, float] = UNSET
    send_date: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    to: Union[Unset, "ProgressTestSelfMailerResponse200To"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        description = self.description

        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        id = self.id

        inside_html = self.inside_html

        live = self.live

        mailing_class = self.mailing_class

        object_ = self.object_

        outside_html = self.outside_html

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
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if from_ is not UNSET:
            field_dict["from"] = from_
        if id is not UNSET:
            field_dict["id"] = id
        if inside_html is not UNSET:
            field_dict["insideHTML"] = inside_html
        if live is not UNSET:
            field_dict["live"] = live
        if mailing_class is not UNSET:
            field_dict["mailingClass"] = mailing_class
        if object_ is not UNSET:
            field_dict["object"] = object_
        if outside_html is not UNSET:
            field_dict["outsideHTML"] = outside_html
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
        from ..models.progress_test_self_mailer_response_200_from import ProgressTestSelfMailerResponse200From
        from ..models.progress_test_self_mailer_response_200_to import ProgressTestSelfMailerResponse200To

        d = src_dict.copy()
        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, ProgressTestSelfMailerResponse200From]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = ProgressTestSelfMailerResponse200From.from_dict(_from_)

        id = d.pop("id", UNSET)

        inside_html = d.pop("insideHTML", UNSET)

        live = d.pop("live", UNSET)

        mailing_class = d.pop("mailingClass", UNSET)

        object_ = d.pop("object", UNSET)

        outside_html = d.pop("outsideHTML", UNSET)

        page_count = d.pop("pageCount", UNSET)

        send_date = d.pop("sendDate", UNSET)

        size = d.pop("size", UNSET)

        status = d.pop("status", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, ProgressTestSelfMailerResponse200To]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = ProgressTestSelfMailerResponse200To.from_dict(_to)

        updated_at = d.pop("updatedAt", UNSET)

        url = d.pop("url", UNSET)

        progress_test_self_mailer_response_200 = cls(
            created_at=created_at,
            description=description,
            from_=from_,
            id=id,
            inside_html=inside_html,
            live=live,
            mailing_class=mailing_class,
            object_=object_,
            outside_html=outside_html,
            page_count=page_count,
            send_date=send_date,
            size=size,
            status=status,
            to=to,
            updated_at=updated_at,
            url=url,
        )

        progress_test_self_mailer_response_200.additional_properties = d
        return progress_test_self_mailer_response_200

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
