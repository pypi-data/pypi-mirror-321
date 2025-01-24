from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_postcard_response_201_to import CreatePostcardResponse201To


T = TypeVar("T", bound="CreatePostcardResponse201")


@_attrs_define
class CreatePostcardResponse201:
    """
    Attributes:
        back_html (Union[Unset, str]):  Example: Hello again, {{to.firstName}}.
        back_template (Union[Unset, str]):  Example: template_gGF4jRzHBNogJrju2JHC2T.
        created_at (Union[Unset, str]):  Example: 2020-12-23T07:06:57.549Z.
        front_html (Union[Unset, str]):  Example: Hello, {{to.firstName}}.
        front_template (Union[Unset, str]):  Example: template_gGF4jRzHBNogJrju2JHC2T.
        id (Union[Unset, str]):  Example: postcard_mWZGkpb16fcdGKnZUk2WQv.
        live (Union[Unset, bool]):  Example: True.
        object_ (Union[Unset, str]):  Example: postcard.
        send_date (Union[Unset, str]):  Example: 2020-12-23T07:06:57.519Z.
        size (Union[Unset, str]):  Example: 6x4.
        status (Union[Unset, str]):  Example: ready.
        to (Union[Unset, CreatePostcardResponse201To]):
        updated_at (Union[Unset, str]):  Example: 2020-12-23T07:06:57.549Z.
        uploaded_pdf (Union[Unset, str]):  Example: https://pg-prod-bucket-
            1.s3.amazonaws.com/live/pdf_bsdhXXsrpPFtmnWsbkPBwp?AWSAccessKeyId=AKIA5GFUILSUDYW4YKAG&Expires=1608708308&Signat
            ure=sgqfUr4yMxa1Th%2FDD4%2B7IiQRiZo%3D.
    """

    back_html: Union[Unset, str] = UNSET
    back_template: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    front_html: Union[Unset, str] = UNSET
    front_template: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    object_: Union[Unset, str] = UNSET
    send_date: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    to: Union[Unset, "CreatePostcardResponse201To"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    uploaded_pdf: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        back_html = self.back_html

        back_template = self.back_template

        created_at = self.created_at

        front_html = self.front_html

        front_template = self.front_template

        id = self.id

        live = self.live

        object_ = self.object_

        send_date = self.send_date

        size = self.size

        status = self.status

        to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        updated_at = self.updated_at

        uploaded_pdf = self.uploaded_pdf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if back_html is not UNSET:
            field_dict["backHTML"] = back_html
        if back_template is not UNSET:
            field_dict["backTemplate"] = back_template
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if front_html is not UNSET:
            field_dict["frontHTML"] = front_html
        if front_template is not UNSET:
            field_dict["frontTemplate"] = front_template
        if id is not UNSET:
            field_dict["id"] = id
        if live is not UNSET:
            field_dict["live"] = live
        if object_ is not UNSET:
            field_dict["object"] = object_
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_postcard_response_201_to import CreatePostcardResponse201To

        d = src_dict.copy()
        back_html = d.pop("backHTML", UNSET)

        back_template = d.pop("backTemplate", UNSET)

        created_at = d.pop("createdAt", UNSET)

        front_html = d.pop("frontHTML", UNSET)

        front_template = d.pop("frontTemplate", UNSET)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        object_ = d.pop("object", UNSET)

        send_date = d.pop("sendDate", UNSET)

        size = d.pop("size", UNSET)

        status = d.pop("status", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, CreatePostcardResponse201To]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = CreatePostcardResponse201To.from_dict(_to)

        updated_at = d.pop("updatedAt", UNSET)

        uploaded_pdf = d.pop("uploadedPDF", UNSET)

        create_postcard_response_201 = cls(
            back_html=back_html,
            back_template=back_template,
            created_at=created_at,
            front_html=front_html,
            front_template=front_template,
            id=id,
            live=live,
            object_=object_,
            send_date=send_date,
            size=size,
            status=status,
            to=to,
            updated_at=updated_at,
            uploaded_pdf=uploaded_pdf,
        )

        create_postcard_response_201.additional_properties = d
        return create_postcard_response_201

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
