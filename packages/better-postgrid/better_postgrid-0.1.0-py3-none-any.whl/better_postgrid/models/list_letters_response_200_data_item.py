from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_letters_response_200_data_item_from import ListLettersResponse200DataItemFrom
    from ..models.list_letters_response_200_data_item_to import ListLettersResponse200DataItemTo


T = TypeVar("T", bound="ListLettersResponse200DataItem")


@_attrs_define
class ListLettersResponse200DataItem:
    """
    Attributes:
        address_placement (Union[Unset, str]):  Example: top_first_page.
        created_at (Union[Unset, str]):  Example: 2020-11-13T01:34:44.117Z.
        from_ (Union[Unset, ListLettersResponse200DataItemFrom]):
        html (Union[Unset, str]):  Example: <b>Hello</b> updated world!.
        id (Union[Unset, str]):  Example: letter_qVtvoLzZ4qurmUSDNAShTj.
        live (Union[Unset, bool]):
        object_ (Union[Unset, str]):  Example: letter.
        page_count (Union[Unset, float]):  Example: 1.
        send_date (Union[Unset, str]):  Example: 2020-11-12.
        status (Union[Unset, str]):  Example: ready.
        template (Union[Unset, str]):  Example: template_tBnVEzz878mXLbHQaz86j8.
        to (Union[Unset, ListLettersResponse200DataItemTo]):
        updated_at (Union[Unset, str]):  Example: 2020-11-13T01:34:47.052Z.
        url (Union[Unset, str]):  Example: https://eksandbox.s3.amazonaws.com/test/letter_qVtvoLzZ4qurmUSDNAShTj.pdf?AWS
            AccessKeyId=AKIA5GFUILSUDYW4YKAG&Expires=1605232448&Signature=n2MOJ2gBClJRPj7Iu2LOhMzuNBk%3D.
    """

    address_placement: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    from_: Union[Unset, "ListLettersResponse200DataItemFrom"] = UNSET
    html: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    object_: Union[Unset, str] = UNSET
    page_count: Union[Unset, float] = UNSET
    send_date: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    to: Union[Unset, "ListLettersResponse200DataItemTo"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_placement = self.address_placement

        created_at = self.created_at

        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        html = self.html

        id = self.id

        live = self.live

        object_ = self.object_

        page_count = self.page_count

        send_date = self.send_date

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
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if from_ is not UNSET:
            field_dict["from"] = from_
        if html is not UNSET:
            field_dict["html"] = html
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
        from ..models.list_letters_response_200_data_item_from import ListLettersResponse200DataItemFrom
        from ..models.list_letters_response_200_data_item_to import ListLettersResponse200DataItemTo

        d = src_dict.copy()
        address_placement = d.pop("addressPlacement", UNSET)

        created_at = d.pop("createdAt", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, ListLettersResponse200DataItemFrom]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = ListLettersResponse200DataItemFrom.from_dict(_from_)

        html = d.pop("html", UNSET)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        object_ = d.pop("object", UNSET)

        page_count = d.pop("pageCount", UNSET)

        send_date = d.pop("sendDate", UNSET)

        status = d.pop("status", UNSET)

        template = d.pop("template", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, ListLettersResponse200DataItemTo]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = ListLettersResponse200DataItemTo.from_dict(_to)

        updated_at = d.pop("updatedAt", UNSET)

        url = d.pop("url", UNSET)

        list_letters_response_200_data_item = cls(
            address_placement=address_placement,
            created_at=created_at,
            from_=from_,
            html=html,
            id=id,
            live=live,
            object_=object_,
            page_count=page_count,
            send_date=send_date,
            status=status,
            template=template,
            to=to,
            updated_at=updated_at,
            url=url,
        )

        list_letters_response_200_data_item.additional_properties = d
        return list_letters_response_200_data_item

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
