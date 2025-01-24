from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_postcard_response_200_to import GetPostcardResponse200To


T = TypeVar("T", bound="GetPostcardResponse200")


@_attrs_define
class GetPostcardResponse200:
    """
    Attributes:
        back_html (Union[Unset, str]):  Example: Hello again, {{to.firstName}}.
        created_at (Union[Unset, str]):  Example: 2020-12-23T07:06:57.549Z.
        front_html (Union[Unset, str]):  Example: Hello, {{to.firstName}}.
        id (Union[Unset, str]):  Example: postcard_mWZGkpb16fcdGKnZUk2WQv.
        live (Union[Unset, bool]):  Example: True.
        object_ (Union[Unset, str]):  Example: postcard.
        page_count (Union[Unset, float]):  Example: 2.
        send_date (Union[Unset, str]):  Example: 2020-12-23T07:06:57.519Z.
        size (Union[Unset, str]):  Example: 6x4.
        status (Union[Unset, str]):  Example: ready.
        to (Union[Unset, GetPostcardResponse200To]):
        updated_at (Union[Unset, str]):  Example: 2020-12-23T07:07:00.476Z.
        url (Union[Unset, str]):  Example: https://pg-prod-bucket-
            1.s3.amazonaws.com/live/postcard_mWZGkpb16fcdGKnZUk2WQv.pdf?AWSAccessKeyId=AKIA5GFUILSUDYW4YKAG&Expires=16087085
            99&Signature=sHND9sHNLadfwjMkmmCrxucNzTw%3D.
    """

    back_html: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    front_html: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    object_: Union[Unset, str] = UNSET
    page_count: Union[Unset, float] = UNSET
    send_date: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    to: Union[Unset, "GetPostcardResponse200To"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        back_html = self.back_html

        created_at = self.created_at

        front_html = self.front_html

        id = self.id

        live = self.live

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
        if back_html is not UNSET:
            field_dict["backHTML"] = back_html
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if front_html is not UNSET:
            field_dict["frontHTML"] = front_html
        if id is not UNSET:
            field_dict["id"] = id
        if live is not UNSET:
            field_dict["live"] = live
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
        from ..models.get_postcard_response_200_to import GetPostcardResponse200To

        d = src_dict.copy()
        back_html = d.pop("backHTML", UNSET)

        created_at = d.pop("createdAt", UNSET)

        front_html = d.pop("frontHTML", UNSET)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        object_ = d.pop("object", UNSET)

        page_count = d.pop("pageCount", UNSET)

        send_date = d.pop("sendDate", UNSET)

        size = d.pop("size", UNSET)

        status = d.pop("status", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, GetPostcardResponse200To]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = GetPostcardResponse200To.from_dict(_to)

        updated_at = d.pop("updatedAt", UNSET)

        url = d.pop("url", UNSET)

        get_postcard_response_200 = cls(
            back_html=back_html,
            created_at=created_at,
            front_html=front_html,
            id=id,
            live=live,
            object_=object_,
            page_count=page_count,
            send_date=send_date,
            size=size,
            status=status,
            to=to,
            updated_at=updated_at,
            url=url,
        )

        get_postcard_response_200.additional_properties = d
        return get_postcard_response_200

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
