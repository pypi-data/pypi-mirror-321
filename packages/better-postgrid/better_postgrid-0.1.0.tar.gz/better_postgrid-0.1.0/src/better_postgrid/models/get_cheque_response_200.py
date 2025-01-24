from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_cheque_response_200_bank_account import GetChequeResponse200BankAccount
    from ..models.get_cheque_response_200_from import GetChequeResponse200From
    from ..models.get_cheque_response_200_to import GetChequeResponse200To


T = TypeVar("T", bound="GetChequeResponse200")


@_attrs_define
class GetChequeResponse200:
    """
    Attributes:
        amount (Union[Unset, float]):  Example: 10000.
        bank_account (Union[Unset, GetChequeResponse200BankAccount]):
        created_at (Union[Unset, str]):  Example: 2020-11-18T05:10:52.994Z.
        description (Union[Unset, str]):  Example: Test.
        from_ (Union[Unset, GetChequeResponse200From]):
        id (Union[Unset, str]):  Example: cheque_mK8PfefU41ZQnKBRCaUayh.
        live (Union[Unset, bool]):
        memo (Union[Unset, str]):  Example: A short memo..
        number (Union[Unset, float]):  Example: 5049.
        object_ (Union[Unset, str]):  Example: cheque.
        send_date (Union[Unset, str]):  Example: 2020-11-18.
        status (Union[Unset, str]):  Example: ready.
        to (Union[Unset, GetChequeResponse200To]):
        updated_at (Union[Unset, str]):  Example: 2020-11-18T05:10:52.994Z.
    """

    amount: Union[Unset, float] = UNSET
    bank_account: Union[Unset, "GetChequeResponse200BankAccount"] = UNSET
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    from_: Union[Unset, "GetChequeResponse200From"] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    memo: Union[Unset, str] = UNSET
    number: Union[Unset, float] = UNSET
    object_: Union[Unset, str] = UNSET
    send_date: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    to: Union[Unset, "GetChequeResponse200To"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        bank_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bank_account, Unset):
            bank_account = self.bank_account.to_dict()

        created_at = self.created_at

        description = self.description

        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        id = self.id

        live = self.live

        memo = self.memo

        number = self.number

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
        if amount is not UNSET:
            field_dict["amount"] = amount
        if bank_account is not UNSET:
            field_dict["bankAccount"] = bank_account
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if from_ is not UNSET:
            field_dict["from"] = from_
        if id is not UNSET:
            field_dict["id"] = id
        if live is not UNSET:
            field_dict["live"] = live
        if memo is not UNSET:
            field_dict["memo"] = memo
        if number is not UNSET:
            field_dict["number"] = number
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
        from ..models.get_cheque_response_200_bank_account import GetChequeResponse200BankAccount
        from ..models.get_cheque_response_200_from import GetChequeResponse200From
        from ..models.get_cheque_response_200_to import GetChequeResponse200To

        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        _bank_account = d.pop("bankAccount", UNSET)
        bank_account: Union[Unset, GetChequeResponse200BankAccount]
        if isinstance(_bank_account, Unset):
            bank_account = UNSET
        else:
            bank_account = GetChequeResponse200BankAccount.from_dict(_bank_account)

        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, GetChequeResponse200From]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = GetChequeResponse200From.from_dict(_from_)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        memo = d.pop("memo", UNSET)

        number = d.pop("number", UNSET)

        object_ = d.pop("object", UNSET)

        send_date = d.pop("sendDate", UNSET)

        status = d.pop("status", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, GetChequeResponse200To]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = GetChequeResponse200To.from_dict(_to)

        updated_at = d.pop("updatedAt", UNSET)

        get_cheque_response_200 = cls(
            amount=amount,
            bank_account=bank_account,
            created_at=created_at,
            description=description,
            from_=from_,
            id=id,
            live=live,
            memo=memo,
            number=number,
            object_=object_,
            send_date=send_date,
            status=status,
            to=to,
            updated_at=updated_at,
        )

        get_cheque_response_200.additional_properties = d
        return get_cheque_response_200

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
