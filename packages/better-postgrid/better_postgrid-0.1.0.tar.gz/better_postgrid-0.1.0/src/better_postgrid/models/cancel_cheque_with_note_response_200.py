from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cancel_cheque_with_note_response_200_cancellation import CancelChequeWithNoteResponse200Cancellation
    from ..models.cancel_cheque_with_note_response_200_from import CancelChequeWithNoteResponse200From
    from ..models.cancel_cheque_with_note_response_200_merge_variables import (
        CancelChequeWithNoteResponse200MergeVariables,
    )
    from ..models.cancel_cheque_with_note_response_200_metadata import CancelChequeWithNoteResponse200Metadata
    from ..models.cancel_cheque_with_note_response_200_to import CancelChequeWithNoteResponse200To


T = TypeVar("T", bound="CancelChequeWithNoteResponse200")


@_attrs_define
class CancelChequeWithNoteResponse200:
    """
    Attributes:
        amount (Union[Unset, float]):  Example: 500.
        bank_account (Union[Unset, str]):  Example: bank_wALJikLcPznEK3i8WhkVjo.
        cancellation (Union[Unset, CancelChequeWithNoteResponse200Cancellation]):
        carrier_tracking (Union[Unset, Any]):
        created_at (Union[Unset, str]):  Example: 2024-01-25T15:58:29.967Z.
        currency_code (Union[Unset, str]):  Example: USD.
        description (Union[Unset, str]):  Example: cancellation test 1.
        express (Union[Unset, bool]):
        from_ (Union[Unset, CancelChequeWithNoteResponse200From]):
        id (Union[Unset, str]):  Example: cheque_26Rm3FAizk6U8TUi8bokPj.
        live (Union[Unset, bool]):
        mailing_class (Union[Unset, str]):  Example: first_class.
        memo (Union[Unset, str]):
        merge_variables (Union[Unset, CancelChequeWithNoteResponse200MergeVariables]):
        message (Union[Unset, str]):
        metadata (Union[Unset, CancelChequeWithNoteResponse200Metadata]):
        number (Union[Unset, float]):  Example: 2049.
        object_ (Union[Unset, str]):  Example: cheque.
        page_count (Union[Unset, float]):  Example: 2.
        send_date (Union[Unset, str]):  Example: 2024-01-26T04:59:59.999Z.
        size (Union[Unset, str]):  Example: us_letter.
        status (Union[Unset, str]):  Example: cancelled.
        to (Union[Unset, CancelChequeWithNoteResponse200To]):
        updated_at (Union[Unset, str]):  Example: 2024-01-25T15:58:57.260Z.
        url (Union[Unset, str]):  Example: https://pg-prod-bucket-
            1.s3.amazonaws.com/test/cheque_26Rm3FAizk6U8TUi8bokPj.pdf?AWSAccessKeyId=AKIA5GFUILSULWTWCR64&Expires=1706199237
            &Signature=66BxqEUwNCilzgRWVg2nRsczCUw%3D.
    """

    amount: Union[Unset, float] = UNSET
    bank_account: Union[Unset, str] = UNSET
    cancellation: Union[Unset, "CancelChequeWithNoteResponse200Cancellation"] = UNSET
    carrier_tracking: Union[Unset, Any] = UNSET
    created_at: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    express: Union[Unset, bool] = UNSET
    from_: Union[Unset, "CancelChequeWithNoteResponse200From"] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    mailing_class: Union[Unset, str] = UNSET
    memo: Union[Unset, str] = UNSET
    merge_variables: Union[Unset, "CancelChequeWithNoteResponse200MergeVariables"] = UNSET
    message: Union[Unset, str] = UNSET
    metadata: Union[Unset, "CancelChequeWithNoteResponse200Metadata"] = UNSET
    number: Union[Unset, float] = UNSET
    object_: Union[Unset, str] = UNSET
    page_count: Union[Unset, float] = UNSET
    send_date: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    to: Union[Unset, "CancelChequeWithNoteResponse200To"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        bank_account = self.bank_account

        cancellation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cancellation, Unset):
            cancellation = self.cancellation.to_dict()

        carrier_tracking = self.carrier_tracking

        created_at = self.created_at

        currency_code = self.currency_code

        description = self.description

        express = self.express

        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        id = self.id

        live = self.live

        mailing_class = self.mailing_class

        memo = self.memo

        merge_variables: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merge_variables, Unset):
            merge_variables = self.merge_variables.to_dict()

        message = self.message

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        number = self.number

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
        if amount is not UNSET:
            field_dict["amount"] = amount
        if bank_account is not UNSET:
            field_dict["bankAccount"] = bank_account
        if cancellation is not UNSET:
            field_dict["cancellation"] = cancellation
        if carrier_tracking is not UNSET:
            field_dict["carrierTracking"] = carrier_tracking
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if description is not UNSET:
            field_dict["description"] = description
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
        if memo is not UNSET:
            field_dict["memo"] = memo
        if merge_variables is not UNSET:
            field_dict["mergeVariables"] = merge_variables
        if message is not UNSET:
            field_dict["message"] = message
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if number is not UNSET:
            field_dict["number"] = number
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
        from ..models.cancel_cheque_with_note_response_200_cancellation import (
            CancelChequeWithNoteResponse200Cancellation,
        )
        from ..models.cancel_cheque_with_note_response_200_from import CancelChequeWithNoteResponse200From
        from ..models.cancel_cheque_with_note_response_200_merge_variables import (
            CancelChequeWithNoteResponse200MergeVariables,
        )
        from ..models.cancel_cheque_with_note_response_200_metadata import CancelChequeWithNoteResponse200Metadata
        from ..models.cancel_cheque_with_note_response_200_to import CancelChequeWithNoteResponse200To

        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        bank_account = d.pop("bankAccount", UNSET)

        _cancellation = d.pop("cancellation", UNSET)
        cancellation: Union[Unset, CancelChequeWithNoteResponse200Cancellation]
        if isinstance(_cancellation, Unset):
            cancellation = UNSET
        else:
            cancellation = CancelChequeWithNoteResponse200Cancellation.from_dict(_cancellation)

        carrier_tracking = d.pop("carrierTracking", UNSET)

        created_at = d.pop("createdAt", UNSET)

        currency_code = d.pop("currencyCode", UNSET)

        description = d.pop("description", UNSET)

        express = d.pop("express", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, CancelChequeWithNoteResponse200From]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = CancelChequeWithNoteResponse200From.from_dict(_from_)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        mailing_class = d.pop("mailingClass", UNSET)

        memo = d.pop("memo", UNSET)

        _merge_variables = d.pop("mergeVariables", UNSET)
        merge_variables: Union[Unset, CancelChequeWithNoteResponse200MergeVariables]
        if isinstance(_merge_variables, Unset):
            merge_variables = UNSET
        else:
            merge_variables = CancelChequeWithNoteResponse200MergeVariables.from_dict(_merge_variables)

        message = d.pop("message", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CancelChequeWithNoteResponse200Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CancelChequeWithNoteResponse200Metadata.from_dict(_metadata)

        number = d.pop("number", UNSET)

        object_ = d.pop("object", UNSET)

        page_count = d.pop("pageCount", UNSET)

        send_date = d.pop("sendDate", UNSET)

        size = d.pop("size", UNSET)

        status = d.pop("status", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, CancelChequeWithNoteResponse200To]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = CancelChequeWithNoteResponse200To.from_dict(_to)

        updated_at = d.pop("updatedAt", UNSET)

        url = d.pop("url", UNSET)

        cancel_cheque_with_note_response_200 = cls(
            amount=amount,
            bank_account=bank_account,
            cancellation=cancellation,
            carrier_tracking=carrier_tracking,
            created_at=created_at,
            currency_code=currency_code,
            description=description,
            express=express,
            from_=from_,
            id=id,
            live=live,
            mailing_class=mailing_class,
            memo=memo,
            merge_variables=merge_variables,
            message=message,
            metadata=metadata,
            number=number,
            object_=object_,
            page_count=page_count,
            send_date=send_date,
            size=size,
            status=status,
            to=to,
            updated_at=updated_at,
            url=url,
        )

        cancel_cheque_with_note_response_200.additional_properties = d
        return cancel_cheque_with_note_response_200

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
