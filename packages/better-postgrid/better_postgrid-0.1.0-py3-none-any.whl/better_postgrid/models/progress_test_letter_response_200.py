from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.progress_test_letter_response_200_from import ProgressTestLetterResponse200From
    from ..models.progress_test_letter_response_200_to import ProgressTestLetterResponse200To


T = TypeVar("T", bound="ProgressTestLetterResponse200")


@_attrs_define
class ProgressTestLetterResponse200:
    """
    Attributes:
        address_placement (Union[Unset, str]):  Example: top_first_page.
        color (Union[Unset, bool]):
        created_at (Union[Unset, str]):  Example: 2021-05-03T14:42:20.796Z.
        double_sided (Union[Unset, bool]):  Example: True.
        from_ (Union[Unset, ProgressTestLetterResponse200From]):
        html (Union[Unset, str]):  Example: <b>Hello</b>, {{to.firstName}}!.
        id (Union[Unset, str]):  Example: letter_oNrxnVvpyKwbcHtJinF5cm.
        live (Union[Unset, bool]):
        object_ (Union[Unset, str]):  Example: letter.
        send_date (Union[Unset, str]):  Example: 2021-05-03T14:42:20.785Z.
        status (Union[Unset, str]):  Example: printing.
        to (Union[Unset, ProgressTestLetterResponse200To]):
        updated_at (Union[Unset, str]):  Example: 2021-05-03T14:42:27.880Z.
    """

    address_placement: Union[Unset, str] = UNSET
    color: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    double_sided: Union[Unset, bool] = UNSET
    from_: Union[Unset, "ProgressTestLetterResponse200From"] = UNSET
    html: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    object_: Union[Unset, str] = UNSET
    send_date: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    to: Union[Unset, "ProgressTestLetterResponse200To"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_placement = self.address_placement

        color = self.color

        created_at = self.created_at

        double_sided = self.double_sided

        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        html = self.html

        id = self.id

        live = self.live

        object_ = self.object_

        send_date = self.send_date

        status = self.status

        to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_placement is not UNSET:
            field_dict["addressPlacement"] = address_placement
        if color is not UNSET:
            field_dict["color"] = color
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if double_sided is not UNSET:
            field_dict["doubleSided"] = double_sided
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
        if send_date is not UNSET:
            field_dict["sendDate"] = send_date
        if status is not UNSET:
            field_dict["status"] = status
        if to is not UNSET:
            field_dict["to"] = to
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.progress_test_letter_response_200_from import ProgressTestLetterResponse200From
        from ..models.progress_test_letter_response_200_to import ProgressTestLetterResponse200To

        d = src_dict.copy()
        address_placement = d.pop("addressPlacement", UNSET)

        color = d.pop("color", UNSET)

        created_at = d.pop("createdAt", UNSET)

        double_sided = d.pop("doubleSided", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, ProgressTestLetterResponse200From]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = ProgressTestLetterResponse200From.from_dict(_from_)

        html = d.pop("html", UNSET)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        object_ = d.pop("object", UNSET)

        send_date = d.pop("sendDate", UNSET)

        status = d.pop("status", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, ProgressTestLetterResponse200To]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = ProgressTestLetterResponse200To.from_dict(_to)

        updated_at = d.pop("updatedAt", UNSET)

        progress_test_letter_response_200 = cls(
            address_placement=address_placement,
            color=color,
            created_at=created_at,
            double_sided=double_sided,
            from_=from_,
            html=html,
            id=id,
            live=live,
            object_=object_,
            send_date=send_date,
            status=status,
            to=to,
            updated_at=updated_at,
        )

        progress_test_letter_response_200.additional_properties = d
        return progress_test_letter_response_200

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
