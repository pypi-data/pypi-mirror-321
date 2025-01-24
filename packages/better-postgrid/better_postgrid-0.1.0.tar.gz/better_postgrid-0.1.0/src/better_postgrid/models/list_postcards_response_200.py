from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_postcards_response_200_data_item import ListPostcardsResponse200DataItem


T = TypeVar("T", bound="ListPostcardsResponse200")


@_attrs_define
class ListPostcardsResponse200:
    """
    Attributes:
        data (Union[Unset, list['ListPostcardsResponse200DataItem']]):  Example: [{'createdAt':
            '2020-12-23T07:13:12.208Z', 'id': 'postcard_wwjVvf1epKSnC4vL1nyFSn', 'live': True, 'object': 'postcard',
            'pageCount': 2, 'sendDate': '2020-12-23T07:13:12.180Z', 'size': '9x6', 'status': 'ready', 'to': {'addressLine1':
            '20-20 BAY ST', 'addressLine2': '', 'addressStatus': 'corrected', 'city': 'TORONTO', 'country': 'CANADA',
            'countryCode': 'CA', 'firstName': 'Kevin', 'id': 'contact_6fMMFdvk7YSSKVgaKyJaQS', 'object': 'contact',
            'postalOrZip': 'M5J 2N8', 'provinceOrState': 'ON'}, 'updatedAt': '2020-12-23T07:13:15.195Z', 'uploadedPDF':
            'https://pg-prod-bucket-
            1.s3.amazonaws.com/live/pdf_teWMLA4XQjs4KHocpE8kEA?AWSAccessKeyId=AKIA5GFUILSUDYW4YKAG&Expires=1608708627&Signat
            ure=3HhXdlkk1meHmfGaDmY0GlxcWCE%3D', 'url': 'https://pg-prod-bucket-
            1.s3.amazonaws.com/live/postcard_wwjVvf1epKSnC4vL1nyFSn.pdf?AWSAccessKeyId=AKIA5GFUILSUDYW4YKAG&Expires=16087086
            27&Signature=OMhDcaCiAxMeMi0f5gNmHoUzsro%3D'}, {'createdAt': '2020-12-23T07:10:08.442Z', 'id':
            'postcard_rCbN9Tp1GndociRVmbXcfn', 'live': True, 'object': 'postcard', 'pageCount': 2, 'sendDate':
            '2020-12-23T07:10:08.413Z', 'size': '9x6', 'status': 'ready', 'to': {'addressLine1': '20-20 BAY ST',
            'addressLine2': '', 'addressStatus': 'corrected', 'city': 'TORONTO', 'country': 'CANADA', 'countryCode': 'CA',
            'firstName': 'Kevin', 'id': 'contact_6fMMFdvk7YSSKVgaKyJaQS', 'object': 'contact', 'postalOrZip': 'M5J 2N8',
            'provinceOrState': 'ON'}, 'updatedAt': '2020-12-23T07:10:12.028Z', 'uploadedPDF': 'https://pg-prod-bucket-
            1.s3.amazonaws.com/live/pdf_bsdhXXsrpPFtmnWsbkPBwp?AWSAccessKeyId=AKIA5GFUILSUDYW4YKAG&Expires=1608708627&Signat
            ure=AwaniGGCv6OPlCzmgw4E3KIdZH8%3D', 'url': 'https://pg-prod-bucket-
            1.s3.amazonaws.com/live/postcard_rCbN9Tp1GndociRVmbXcfn.pdf?AWSAccessKeyId=AKIA5GFUILSUDYW4YKAG&Expires=16087086
            27&Signature=ZMFVyJN2DtMUx9ArUN3c%2BtJj3gQ%3D'}, {'backHTML': 'Hello, world!', 'backTemplate':
            'template_gGF4jRzHBNogJrju2JHC2T', 'createdAt': '2020-12-23T07:08:17.178Z', 'frontHTML': 'Hello, world!',
            'frontTemplate': 'template_gGF4jRzHBNogJrju2JHC2T', 'id': 'postcard_xnSK1RPcqbYY7y6z8qoy7j', 'live': True,
            'object': 'postcard', 'pageCount': 2, 'sendDate': '2020-12-23T07:08:17.172Z', 'size': '6x4', 'status': 'ready',
            'to': {'addressLine1': '20-20 BAY ST', 'addressLine2': '', 'addressStatus': 'corrected', 'city': 'TORONTO',
            'country': 'CANADA', 'countryCode': 'CA', 'firstName': 'Kevin', 'id': 'contact_6fMMFdvk7YSSKVgaKyJaQS',
            'object': 'contact', 'postalOrZip': 'M5J 2N8', 'provinceOrState': 'ON'}, 'updatedAt':
            '2020-12-23T07:08:19.800Z', 'url': 'https://pg-prod-bucket-
            1.s3.amazonaws.com/live/postcard_xnSK1RPcqbYY7y6z8qoy7j.pdf?AWSAccessKeyId=AKIA5GFUILSUDYW4YKAG&Expires=16087086
            27&Signature=25vnQUZ02Nj8vr%2B8tvmWoxyAM04%3D'}, {'backHTML': 'Hello again, {{to.firstName}}', 'createdAt':
            '2020-12-23T07:06:57.549Z', 'frontHTML': 'Hello, {{to.firstName}}', 'id': 'postcard_mWZGkpb16fcdGKnZUk2WQv',
            'live': True, 'object': 'postcard', 'pageCount': 2, 'sendDate': '2020-12-23T07:06:57.519Z', 'size': '6x4',
            'status': 'ready', 'to': {'addressLine1': '22-20 BAY ST', 'addressLine2': '', 'addressStatus': 'corrected',
            'city': 'TORONTO', 'country': 'CANADA', 'countryCode': 'CA', 'firstName': 'Kevin', 'id':
            'contact_6vMttLnCDjFEBYZ77KjGPP', 'object': 'contact', 'postalOrZip': 'M5J 2N8', 'provinceOrState': 'ON'},
            'updatedAt': '2020-12-23T07:07:00.476Z', 'url': 'https://pg-prod-bucket-
            1.s3.amazonaws.com/live/postcard_mWZGkpb16fcdGKnZUk2WQv.pdf?AWSAccessKeyId=AKIA5GFUILSUDYW4YKAG&Expires=16087086
            27&Signature=O9VJ5y2qXJuiTg6H2UgJAPSdHcE%3D'}].
        limit (Union[Unset, float]):  Example: 10.
        object_ (Union[Unset, str]):  Example: list.
        skip (Union[Unset, float]):
        total_count (Union[Unset, float]):  Example: 4.
    """

    data: Union[Unset, list["ListPostcardsResponse200DataItem"]] = UNSET
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
        from ..models.list_postcards_response_200_data_item import ListPostcardsResponse200DataItem

        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = ListPostcardsResponse200DataItem.from_dict(data_item_data)

            data.append(data_item)

        limit = d.pop("limit", UNSET)

        object_ = d.pop("object", UNSET)

        skip = d.pop("skip", UNSET)

        total_count = d.pop("totalCount", UNSET)

        list_postcards_response_200 = cls(
            data=data,
            limit=limit,
            object_=object_,
            skip=skip,
            total_count=total_count,
        )

        list_postcards_response_200.additional_properties = d
        return list_postcards_response_200

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
