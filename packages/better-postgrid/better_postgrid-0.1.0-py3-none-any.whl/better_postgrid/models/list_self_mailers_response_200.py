from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_self_mailers_response_200_data_item import ListSelfMailersResponse200DataItem


T = TypeVar("T", bound="ListSelfMailersResponse200")


@_attrs_define
class ListSelfMailersResponse200:
    """
    Attributes:
        data (Union[Unset, list['ListSelfMailersResponse200DataItem']]):  Example: [{'createdAt':
            '2023-07-06T15:31:04.560Z', 'from': {'addressLine1': '145 MULBERRY ST', 'addressLine2': None, 'addressStatus':
            'verified', 'city': 'NEW YORK', 'country': 'UNITED STATES', 'countryCode': 'US', 'firstName': 'Ricky', 'id':
            'contact_tydRUvrZsw39Nc6guEccid', 'object': 'contact', 'postalOrZip': None, 'provinceOrState': 'NY'}, 'id':
            'self_mailer_5gQmDVDUMpQEYTuSxSf645', 'live': False, 'mailingClass': 'first_class', 'object': 'self_mailer',
            'pageCount': 2, 'sendDate': '2023-07-06T15:31:04.543Z', 'size': '8.5x11_bifold', 'status': 'ready', 'to':
            {'addressLine1': '20-20 BAY ST', 'addressLine2': None, 'addressStatus': 'verified', 'city': 'TORONTO',
            'country': 'CANADA', 'countryCode': 'CA', 'firstName': 'Kevin', 'id': 'contact_3BQJWhUfKQFGKLQF42YM5T',
            'object': 'contact', 'postalOrZip': None, 'provinceOrState': None}, 'updatedAt': '2023-07-06T15:31:07.651Z',
            'uploadedPDF': 'https://pg-prod-bucket-
            1.s3.amazonaws.com/test/pdf_nCZAkLeiS7x3vYZsSWkRc7?AWSAccessKeyId=AKIA5GFUILSULWTWCR64&Expires=1688658729&Signat
            ure=FdO0S8ozliUMQqKCooTXXHKC%2BX4%3D', 'url': 'https://pg-prod-bucket-
            1.s3.amazonaws.com/test/self_mailer_5gQmDVDUMpQEYTuSxSf645?AWSAccessKeyId=AKIA5GFUILSULWTWCR64&Expires=168865872
            9&Signature=rRzAXFtbk1UvE7lUTcgSjo9zMW8%3D'}].
        limit (Union[Unset, float]):  Example: 1.
        object_ (Union[Unset, str]):  Example: list.
        skip (Union[Unset, float]):
        total_count (Union[Unset, float]):  Example: 7.
    """

    data: Union[Unset, list["ListSelfMailersResponse200DataItem"]] = UNSET
    limit: Union[Unset, float] = UNSET
    object_: Union[Unset, str] = UNSET
    skip: Union[Unset, float] = UNSET
    total_count: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        limit = self.limit

        object_ = self.object_

        skip = self.skip

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if limit is not UNSET:
            field_dict["limit"] = limit
        if object_ is not UNSET:
            field_dict["object"] = object_
        if skip is not UNSET:
            field_dict["skip"] = skip
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.list_self_mailers_response_200_data_item import ListSelfMailersResponse200DataItem

        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = ListSelfMailersResponse200DataItem.from_dict(data_item_data)

            data.append(data_item)

        limit = d.pop("limit", UNSET)

        object_ = d.pop("object", UNSET)

        skip = d.pop("skip", UNSET)

        total_count = d.pop("totalCount", UNSET)

        list_self_mailers_response_200 = cls(
            data=data,
            limit=limit,
            object_=object_,
            skip=skip,
            total_count=total_count,
        )

        list_self_mailers_response_200.additional_properties = d
        return list_self_mailers_response_200

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
