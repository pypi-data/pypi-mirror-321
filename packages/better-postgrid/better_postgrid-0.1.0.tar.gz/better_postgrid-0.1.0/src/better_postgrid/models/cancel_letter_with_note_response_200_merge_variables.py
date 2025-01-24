from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cancel_letter_with_note_response_200_merge_variables_to import (
        CancelLetterWithNoteResponse200MergeVariablesTo,
    )


T = TypeVar("T", bound="CancelLetterWithNoteResponse200MergeVariables")


@_attrs_define
class CancelLetterWithNoteResponse200MergeVariables:
    """
    Attributes:
        qr_code (Union[Unset, str]):
        date (Union[Unset, str]):
        to (Union[Unset, CancelLetterWithNoteResponse200MergeVariablesTo]):
    """

    qr_code: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    to: Union[Unset, "CancelLetterWithNoteResponse200MergeVariablesTo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qr_code = self.qr_code

        date = self.date

        to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qr_code is not UNSET:
            field_dict["QR_code"] = qr_code
        if date is not UNSET:
            field_dict["date"] = date
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.cancel_letter_with_note_response_200_merge_variables_to import (
            CancelLetterWithNoteResponse200MergeVariablesTo,
        )

        d = src_dict.copy()
        qr_code = d.pop("QR_code", UNSET)

        date = d.pop("date", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, CancelLetterWithNoteResponse200MergeVariablesTo]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = CancelLetterWithNoteResponse200MergeVariablesTo.from_dict(_to)

        cancel_letter_with_note_response_200_merge_variables = cls(
            qr_code=qr_code,
            date=date,
            to=to,
        )

        cancel_letter_with_note_response_200_merge_variables.additional_properties = d
        return cancel_letter_with_note_response_200_merge_variables

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
