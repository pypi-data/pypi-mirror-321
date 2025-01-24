from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTrackerResponse200")


@_attrs_define
class GetTrackerResponse200:
    """
    Attributes:
        created_at (Union[Unset, str]):  Example: 2020-11-12T23:30:12.581Z.
        id (Union[Unset, str]):  Example: tracker_123456789abcdefghijklmnopqrstuvwxyz.
        live (Union[Unset, bool]):
        object_ (Union[Unset, str]):  Example: tracker.
        redirect_url_template (Union[Unset, str]):  Example: https://postgrid.com?name={{to.firstName}}.
        unique_visit_count (Union[Unset, float]):
        updated_at (Union[Unset, str]):  Example: 2020-11-12T23:31:12.581Z.
        url_expire_after_days (Union[Unset, float]):  Example: 90.
        visit_count (Union[Unset, float]):
    """

    created_at: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    object_: Union[Unset, str] = UNSET
    redirect_url_template: Union[Unset, str] = UNSET
    unique_visit_count: Union[Unset, float] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url_expire_after_days: Union[Unset, float] = UNSET
    visit_count: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        live = self.live

        object_ = self.object_

        redirect_url_template = self.redirect_url_template

        unique_visit_count = self.unique_visit_count

        updated_at = self.updated_at

        url_expire_after_days = self.url_expire_after_days

        visit_count = self.visit_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if live is not UNSET:
            field_dict["live"] = live
        if object_ is not UNSET:
            field_dict["object"] = object_
        if redirect_url_template is not UNSET:
            field_dict["redirectURLTemplate"] = redirect_url_template
        if unique_visit_count is not UNSET:
            field_dict["uniqueVisitCount"] = unique_visit_count
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if url_expire_after_days is not UNSET:
            field_dict["urlExpireAfterDays"] = url_expire_after_days
        if visit_count is not UNSET:
            field_dict["visitCount"] = visit_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("createdAt", UNSET)

        id = d.pop("id", UNSET)

        live = d.pop("live", UNSET)

        object_ = d.pop("object", UNSET)

        redirect_url_template = d.pop("redirectURLTemplate", UNSET)

        unique_visit_count = d.pop("uniqueVisitCount", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        url_expire_after_days = d.pop("urlExpireAfterDays", UNSET)

        visit_count = d.pop("visitCount", UNSET)

        get_tracker_response_200 = cls(
            created_at=created_at,
            id=id,
            live=live,
            object_=object_,
            redirect_url_template=redirect_url_template,
            unique_visit_count=unique_visit_count,
            updated_at=updated_at,
            url_expire_after_days=url_expire_after_days,
            visit_count=visit_count,
        )

        get_tracker_response_200.additional_properties = d
        return get_tracker_response_200

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
