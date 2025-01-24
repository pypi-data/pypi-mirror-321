from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="CreatePostcardFilesBody")


@_attrs_define
class CreatePostcardFilesBody:
    """
    Attributes:
        pdf (Union[Unset, File]):
        size (Union[Unset, str]):  Example: 9x6.
        toaddress_line_1 (Union[Unset, str]):  Example: 20-20 bay st.
        tocity (Union[Unset, str]):  Example: Toronto.
        tofirst_name (Union[Unset, str]):  Example: Kevin.
    """

    pdf: Union[Unset, File] = UNSET
    size: Union[Unset, str] = UNSET
    toaddress_line_1: Union[Unset, str] = UNSET
    tocity: Union[Unset, str] = UNSET
    tofirst_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pdf: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.pdf, Unset):
            pdf = self.pdf.to_tuple()

        size = self.size

        toaddress_line_1 = self.toaddress_line_1

        tocity = self.tocity

        tofirst_name = self.tofirst_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pdf is not UNSET:
            field_dict["pdf"] = pdf
        if size is not UNSET:
            field_dict["size"] = size
        if toaddress_line_1 is not UNSET:
            field_dict["to[addressLine1]"] = toaddress_line_1
        if tocity is not UNSET:
            field_dict["to[city]"] = tocity
        if tofirst_name is not UNSET:
            field_dict["to[firstName]"] = tofirst_name

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        pdf: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.pdf, Unset):
            pdf = self.pdf.to_tuple()

        size = self.size if isinstance(self.size, Unset) else (None, str(self.size).encode(), "text/plain")

        toaddress_line_1 = (
            self.toaddress_line_1
            if isinstance(self.toaddress_line_1, Unset)
            else (None, str(self.toaddress_line_1).encode(), "text/plain")
        )

        tocity = self.tocity if isinstance(self.tocity, Unset) else (None, str(self.tocity).encode(), "text/plain")

        tofirst_name = (
            self.tofirst_name
            if isinstance(self.tofirst_name, Unset)
            else (None, str(self.tofirst_name).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if pdf is not UNSET:
            field_dict["pdf"] = pdf
        if size is not UNSET:
            field_dict["size"] = size
        if toaddress_line_1 is not UNSET:
            field_dict["to[addressLine1]"] = toaddress_line_1
        if tocity is not UNSET:
            field_dict["to[city]"] = tocity
        if tofirst_name is not UNSET:
            field_dict["to[firstName]"] = tofirst_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _pdf = d.pop("pdf", UNSET)
        pdf: Union[Unset, File]
        if isinstance(_pdf, Unset):
            pdf = UNSET
        else:
            pdf = File(payload=BytesIO(_pdf))

        size = d.pop("size", UNSET)

        toaddress_line_1 = d.pop("to[addressLine1]", UNSET)

        tocity = d.pop("to[city]", UNSET)

        tofirst_name = d.pop("to[firstName]", UNSET)

        create_postcard_files_body = cls(
            pdf=pdf,
            size=size,
            toaddress_line_1=toaddress_line_1,
            tocity=tocity,
            tofirst_name=tofirst_name,
        )

        create_postcard_files_body.additional_properties = d
        return create_postcard_files_body

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
