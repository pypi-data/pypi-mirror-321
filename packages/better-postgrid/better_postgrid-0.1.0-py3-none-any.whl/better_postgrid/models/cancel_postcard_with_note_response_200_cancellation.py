from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CancelPostcardWithNoteResponse200Cancellation")


@_attrs_define
class CancelPostcardWithNoteResponse200Cancellation:
    """
    Attributes:
        cancelled_by_user (Union[Unset, str]):  Example: user_epXvQvRpfsx5rWQnQu7YSA.
        note (Union[Unset, str]):  Example: Cancelled due to template changes.
        reason (Union[Unset, str]):  Example: user_initiated.
    """

    cancelled_by_user: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancelled_by_user = self.cancelled_by_user

        note = self.note

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancelled_by_user is not UNSET:
            field_dict["cancelledByUser"] = cancelled_by_user
        if note is not UNSET:
            field_dict["note"] = note
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        cancelled_by_user = d.pop("cancelledByUser", UNSET)

        note = d.pop("note", UNSET)

        reason = d.pop("reason", UNSET)

        cancel_postcard_with_note_response_200_cancellation = cls(
            cancelled_by_user=cancelled_by_user,
            note=note,
            reason=reason,
        )

        cancel_postcard_with_note_response_200_cancellation.additional_properties = d
        return cancel_postcard_with_note_response_200_cancellation

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
