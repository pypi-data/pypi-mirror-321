from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_events_response_200_data_item_data_from import ListEventsResponse200DataItemDataFrom
    from ..models.list_events_response_200_data_item_data_merge_variables import (
        ListEventsResponse200DataItemDataMergeVariables,
    )
    from ..models.list_events_response_200_data_item_data_metadata import ListEventsResponse200DataItemDataMetadata
    from ..models.list_events_response_200_data_item_data_to import ListEventsResponse200DataItemDataTo


T = TypeVar("T", bound="ListEventsResponse200DataItemData")


@_attrs_define
class ListEventsResponse200DataItemData:
    """
    Attributes:
        address_placement (Union[Unset, str]):  Example: top_first_page.
        color (Union[Unset, bool]):
        created_at (Union[Unset, str]):  Example: 2023-05-28T23:29:45.206Z.
        description (Union[Unset, str]):  Example: letter test 2.
        double_sided (Union[Unset, bool]):
        envelope_type (Union[Unset, str]):  Example: standard_double_window.
        express (Union[Unset, bool]):
        extra_service (Union[Unset, str]):  Example: certified.
        from_ (Union[Unset, ListEventsResponse200DataItemDataFrom]):
        id (Union[Unset, str]):  Example: letter_rqfnwvzq5TUsYR2r6L9V8X.
        live (Union[Unset, bool]):
        mailing_class (Union[Unset, str]):  Example: first_class.
        merge_variables (Union[Unset, ListEventsResponse200DataItemDataMergeVariables]):
        metadata (Union[Unset, ListEventsResponse200DataItemDataMetadata]):
        object_ (Union[Unset, str]):  Example: letter.
        page_count (Union[Unset, float]):  Example: 1.
        send_date (Union[Unset, str]):  Example: 2023-05-29T03:59:59.999Z.
        size (Union[Unset, str]):  Example: us_letter.
        status (Union[Unset, str]):  Example: ready.
        template (Union[Unset, str]):  Example: template_g37s8aKWcTA96YCanSwTe7.
        to (Union[Unset, ListEventsResponse200DataItemDataTo]):
        updated_at (Union[Unset, str]):  Example: 2023-05-29T05:30:31.404Z.
        url (Union[Unset, str]):  Example: https://pg-prod-bucket-
            1.s3.amazonaws.com/test/letter_rqfnwvzq5TUsYR2r6L9V8X?AWSAccessKeyId=AKIA5GFUILSULWTWCR64&Expires=1685374558&Sig
            nature=LfgizJyFWFcBilYV46nBtad%2Fwx8%3D.
    """

    address_placement: Union[Unset, str] = UNSET
    color: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    double_sided: Union[Unset, bool] = UNSET
    envelope_type: Union[Unset, str] = UNSET
    express: Union[Unset, bool] = UNSET
    extra_service: Union[Unset, str] = UNSET
    from_: Union[Unset, "ListEventsResponse200DataItemDataFrom"] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    mailing_class: Union[Unset, str] = UNSET
    merge_variables: Union[Unset, "ListEventsResponse200DataItemDataMergeVariables"] = UNSET
    metadata: Union[Unset, "ListEventsResponse200DataItemDataMetadata"] = UNSET
    object_: Union[Unset, str] = UNSET
    page_count: Union[Unset, float] = UNSET
    send_date: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    to: Union[Unset, "ListEventsResponse200DataItemDataTo"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_placement = self.address_placement

        color = self.color

        created_at = self.created_at

        description = self.description

        double_sided = self.double_sided

        envelope_type = self.envelope_type

        express = self.express

        extra_service = self.extra_service

        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        id = self.id

        live = self.live

        mailing_class = self.mailing_class

        merge_variables: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merge_variables, Unset):
            merge_variables = self.merge_variables.to_dict()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        object_ = self.object_

        page_count = self.page_count

        send_date = self.send_date

        size = self.size

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
        if color is not UNSET:
            field_dict["color"] = color
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if double_sided is not UNSET:
            field_dict["doubleSided"] = double_sided
        if envelope_type is not UNSET:
            field_dict["envelopeType"] = envelope_type
        if express is not UNSET:
            field_dict["express"] = express
        if extra_service is not UNSET:
            field_dict["extraService"] = extra_service
        if from_ is not UNSET:
            field_dict["from"] = from_
        if id is not UNSET:
            field_dict["id"] = id
        if live is not UNSET:
            field_dict["live"] = live
        if mailing_class is not UNSET:
            field_dict["mailingClass"] = mailing_class
        if merge_variables is not UNSET:
            field_dict["mergeVariables"] = merge_variables
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
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
        from ..models.list_events_response_200_data_item_data_from import ListEventsResponse200DataItemDataFrom
        from ..models.list_events_response_200_data_item_data_merge_variables import (
            ListEventsResponse200DataItemDataMergeVariables,
        )
        from ..models.list_events_response_200_data_item_data_metadata import ListEventsResponse200DataItemDataMetadata
        from ..models.list_events_response_200_data_item_data_to import ListEventsResponse200DataItemDataTo

        d = src_dict.copy()
        address_placement = d.pop("addressPlacement", UNSET)

        color = d.pop("color", UNSET)

        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

        double_sided = d.pop("doubleSided", UNSET)

        envelope_type = d.pop("envelopeType", UNSET)

        express = d.pop("express", UNSET)

        extra_service = d.pop("extraService", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, ListEventsResponse200DataItemDataFrom]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = ListEventsResponse200DataItemDataFrom.from_dict(_from_)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        mailing_class = d.pop("mailingClass", UNSET)

        _merge_variables = d.pop("mergeVariables", UNSET)
        merge_variables: Union[Unset, ListEventsResponse200DataItemDataMergeVariables]
        if isinstance(_merge_variables, Unset):
            merge_variables = UNSET
        else:
            merge_variables = ListEventsResponse200DataItemDataMergeVariables.from_dict(_merge_variables)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ListEventsResponse200DataItemDataMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ListEventsResponse200DataItemDataMetadata.from_dict(_metadata)

        object_ = d.pop("object", UNSET)

        page_count = d.pop("pageCount", UNSET)

        send_date = d.pop("sendDate", UNSET)

        size = d.pop("size", UNSET)

        status = d.pop("status", UNSET)

        template = d.pop("template", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, ListEventsResponse200DataItemDataTo]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = ListEventsResponse200DataItemDataTo.from_dict(_to)

        updated_at = d.pop("updatedAt", UNSET)

        url = d.pop("url", UNSET)

        list_events_response_200_data_item_data = cls(
            address_placement=address_placement,
            color=color,
            created_at=created_at,
            description=description,
            double_sided=double_sided,
            envelope_type=envelope_type,
            express=express,
            extra_service=extra_service,
            from_=from_,
            id=id,
            live=live,
            mailing_class=mailing_class,
            merge_variables=merge_variables,
            metadata=metadata,
            object_=object_,
            page_count=page_count,
            send_date=send_date,
            size=size,
            status=status,
            template=template,
            to=to,
            updated_at=updated_at,
            url=url,
        )

        list_events_response_200_data_item_data.additional_properties = d
        return list_events_response_200_data_item_data

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
