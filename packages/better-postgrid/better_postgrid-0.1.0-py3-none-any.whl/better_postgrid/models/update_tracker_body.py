from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTrackerBody")


@_attrs_define
class UpdateTrackerBody:
    """
    Attributes:
        redirect_url_template (Union[Unset, str]):  Example: https://postgrid.com?firstName={{to.firstName}}.
        url_expire_after_days (Union[Unset, str]):  Example: 90.
    """

    redirect_url_template: Union[Unset, str] = UNSET
    url_expire_after_days: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        redirect_url_template = self.redirect_url_template

        url_expire_after_days = self.url_expire_after_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if redirect_url_template is not UNSET:
            field_dict["redirectURLTemplate"] = redirect_url_template
        if url_expire_after_days is not UNSET:
            field_dict["urlExpireAfterDays"] = url_expire_after_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        redirect_url_template = d.pop("redirectURLTemplate", UNSET)

        url_expire_after_days = d.pop("urlExpireAfterDays", UNSET)

        update_tracker_body = cls(
            redirect_url_template=redirect_url_template,
            url_expire_after_days=url_expire_after_days,
        )

        update_tracker_body.additional_properties = d
        return update_tracker_body

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
