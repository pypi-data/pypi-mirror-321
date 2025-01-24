from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_events_response_200_data_item import ListEventsResponse200DataItem


T = TypeVar("T", bound="ListEventsResponse200")


@_attrs_define
class ListEventsResponse200:
    """
    Attributes:
        data (Union[Unset, list['ListEventsResponse200DataItem']]):  Example: [{'data': {'addressPlacement':
            'top_first_page', 'color': False, 'createdAt': '2023-05-28T23:29:45.206Z', 'description': 'letter test 2',
            'doubleSided': False, 'envelopeType': 'standard_double_window', 'express': False, 'extraService': 'certified',
            'from': {'addressLine1': '2 PICKWICK PLAZA', 'addressLine2': '', 'addressStatus': 'verified', 'city':
            'GREENWICH', 'companyName': 'Interactive Brokers LLC', 'country': 'UNITED STATES', 'countryCode': 'US',
            'description': '1097916', 'email': '', 'firstName': '', 'id': 'contact_wCVRSWWYjx6QHF8Z2kisUA', 'jobTitle': '',
            'lastName': '', 'metadata': {'amount': 2071.28, 'chequeNumber': None, 'memo': 'FBO Daniel Devore Roth IRA
            U5039335', 'variable1': '', 'variable2': ''}, 'object': 'contact', 'phoneNumber': '', 'postalOrZip': '6831',
            'provinceOrState': 'CT'}, 'id': 'letter_rqfnwvzq5TUsYR2r6L9V8X', 'live': False, 'mailingClass': 'first_class',
            'mergeVariables': {'amount': 732.11, 'chequeNumber': None, 'memo': 'David Becker Distribution', 'variable1': '',
            'variable2': ''}, 'metadata': {'postgrid_dashboard': ''}, 'object': 'letter', 'pageCount': 1, 'sendDate':
            '2023-05-29T03:59:59.999Z', 'size': 'us_letter', 'status': 'ready', 'template':
            'template_g37s8aKWcTA96YCanSwTe7', 'to': {'addressLine1': '27571 SANDY SHORES DR SW', 'addressLine2': '',
            'addressStatus': 'verified', 'city': 'VASHON', 'companyName': '', 'country': 'UNITED STATES', 'countryCode':
            'US', 'description': '', 'email': '', 'firstName': 'David', 'id': 'contact_j4UQMhBkq6mz2Vvj2coLwX', 'jobTitle':
            '', 'lastName': 'Becker', 'metadata': {'amount': 732.11, 'chequeNumber': None, 'memo': 'David Becker
            Distribution', 'variable1': '', 'variable2': ''}, 'object': 'contact', 'phoneNumber': '', 'postalOrZip':
            '98070', 'provinceOrState': 'WA'}, 'updatedAt': '2023-05-29T05:30:31.404Z', 'url': 'https://pg-prod-bucket-
            1.s3.amazonaws.com/test/letter_rqfnwvzq5TUsYR2r6L9V8X?AWSAccessKeyId=AKIA5GFUILSULWTWCR64&Expires=1685374558&Sig
            nature=LfgizJyFWFcBilYV46nBtad%2Fwx8%3D'}, 'id': 'event_r1nfP4xAacyqMYtt7PeyFD', 'live': False, 'object':
            'event', 'type': 'letter.created'}, {'data': {'addressPlacement': 'top_first_page', 'color': False, 'createdAt':
            '2023-05-28T23:29:45.206Z', 'description': 'letter test 2', 'doubleSided': False, 'envelopeType':
            'standard_double_window', 'express': False, 'extraService': 'certified', 'from': {'addressLine1': '2 PICKWICK
            PLAZA', 'addressLine2': '', 'addressStatus': 'verified', 'city': 'GREENWICH', 'companyName': 'Interactive
            Brokers LLC', 'country': 'UNITED STATES', 'countryCode': 'US', 'description': '1097916', 'email': '',
            'firstName': '', 'id': 'contact_wCVRSWWYjx6QHF8Z2kisUA', 'jobTitle': '', 'lastName': '', 'metadata': {'amount':
            2071.28, 'chequeNumber': None, 'memo': 'FBO Daniel Devore Roth IRA U5039335', 'variable1': '', 'variable2': ''},
            'object': 'contact', 'phoneNumber': '', 'postalOrZip': '6831', 'provinceOrState': 'CT'}, 'id':
            'letter_rqfnwvzq5TUsYR2r6L9V8X', 'live': False, 'mailingClass': 'first_class', 'mergeVariables': {'amount':
            732.11, 'chequeNumber': None, 'memo': 'David Becker Distribution', 'variable1': '', 'variable2': ''},
            'metadata': {'postgrid_dashboard': ''}, 'object': 'letter', 'pageCount': 1, 'sendDate':
            '2023-05-29T03:59:59.999Z', 'size': 'us_letter', 'status': 'ready', 'template':
            'template_g37s8aKWcTA96YCanSwTe7', 'to': {'addressLine1': '27571 SANDY SHORES DR SW', 'addressLine2': '',
            'addressStatus': 'verified', 'city': 'VASHON', 'companyName': '', 'country': 'UNITED STATES', 'countryCode':
            'US', 'description': '', 'email': '', 'firstName': 'David', 'id': 'contact_j4UQMhBkq6mz2Vvj2coLwX', 'jobTitle':
            '', 'lastName': 'Becker', 'metadata': {'amount': 732.11, 'chequeNumber': None, 'memo': 'David Becker
            Distribution', 'variable1': '', 'variable2': ''}, 'object': 'contact', 'phoneNumber': '', 'postalOrZip':
            '98070', 'provinceOrState': 'WA'}, 'updatedAt': '2023-05-29T05:30:31.404Z', 'url': 'https://pg-prod-bucket-
            1.s3.amazonaws.com/test/letter_rqfnwvzq5TUsYR2r6L9V8X?AWSAccessKeyId=AKIA5GFUILSULWTWCR64&Expires=1685374558&Sig
            nature=LfgizJyFWFcBilYV46nBtad%2Fwx8%3D'}, 'id': 'event_8Gv6ekFotgQn2BQ15MhNgk', 'live': False, 'object':
            'event', 'type': 'letter.created'}].
        limit (Union[Unset, float]):  Example: 2.
        object_ (Union[Unset, str]):  Example: list.
        skip (Union[Unset, float]):  Example: 1.
        total_count (Union[Unset, float]):  Example: 196111.
    """

    data: Union[Unset, list["ListEventsResponse200DataItem"]] = UNSET
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
        from ..models.list_events_response_200_data_item import ListEventsResponse200DataItem

        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = ListEventsResponse200DataItem.from_dict(data_item_data)

            data.append(data_item)

        limit = d.pop("limit", UNSET)

        object_ = d.pop("object", UNSET)

        skip = d.pop("skip", UNSET)

        total_count = d.pop("totalCount", UNSET)

        list_events_response_200 = cls(
            data=data,
            limit=limit,
            object_=object_,
            skip=skip,
            total_count=total_count,
        )

        list_events_response_200.additional_properties = d
        return list_events_response_200

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
