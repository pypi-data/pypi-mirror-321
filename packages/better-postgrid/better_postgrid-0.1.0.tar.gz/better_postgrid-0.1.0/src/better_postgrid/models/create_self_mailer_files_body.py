from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="CreateSelfMailerFilesBody")


@_attrs_define
class CreateSelfMailerFilesBody:
    """
    Attributes:
        fromaddress_line_1 (Union[Unset, str]):  Example: 145 Mulberry St.
        fromcity (Union[Unset, str]):  Example: New York.
        fromcountry_code (Union[Unset, str]):  Example: US.
        fromfirst_name (Union[Unset, str]):  Example: Ricky.
        fromprovince_or_state (Union[Unset, str]):  Example: NY.
        pdf (Union[Unset, File]):
        size (Union[Unset, str]):  Example: 8.5x11_bifold.
        toaddress_line_1 (Union[Unset, str]):  Example: 20-20 bay st.
        tocity (Union[Unset, str]):  Example: Toronto.
        tofirst_name (Union[Unset, str]):  Example: Kevin.
    """

    fromaddress_line_1: Union[Unset, str] = UNSET
    fromcity: Union[Unset, str] = UNSET
    fromcountry_code: Union[Unset, str] = UNSET
    fromfirst_name: Union[Unset, str] = UNSET
    fromprovince_or_state: Union[Unset, str] = UNSET
    pdf: Union[Unset, File] = UNSET
    size: Union[Unset, str] = UNSET
    toaddress_line_1: Union[Unset, str] = UNSET
    tocity: Union[Unset, str] = UNSET
    tofirst_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fromaddress_line_1 = self.fromaddress_line_1

        fromcity = self.fromcity

        fromcountry_code = self.fromcountry_code

        fromfirst_name = self.fromfirst_name

        fromprovince_or_state = self.fromprovince_or_state

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
        if fromaddress_line_1 is not UNSET:
            field_dict["from[addressLine1]"] = fromaddress_line_1
        if fromcity is not UNSET:
            field_dict["from[city]"] = fromcity
        if fromcountry_code is not UNSET:
            field_dict["from[countryCode]"] = fromcountry_code
        if fromfirst_name is not UNSET:
            field_dict["from[firstName]"] = fromfirst_name
        if fromprovince_or_state is not UNSET:
            field_dict["from[provinceOrState]"] = fromprovince_or_state
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
        fromaddress_line_1 = (
            self.fromaddress_line_1
            if isinstance(self.fromaddress_line_1, Unset)
            else (None, str(self.fromaddress_line_1).encode(), "text/plain")
        )

        fromcity = (
            self.fromcity if isinstance(self.fromcity, Unset) else (None, str(self.fromcity).encode(), "text/plain")
        )

        fromcountry_code = (
            self.fromcountry_code
            if isinstance(self.fromcountry_code, Unset)
            else (None, str(self.fromcountry_code).encode(), "text/plain")
        )

        fromfirst_name = (
            self.fromfirst_name
            if isinstance(self.fromfirst_name, Unset)
            else (None, str(self.fromfirst_name).encode(), "text/plain")
        )

        fromprovince_or_state = (
            self.fromprovince_or_state
            if isinstance(self.fromprovince_or_state, Unset)
            else (None, str(self.fromprovince_or_state).encode(), "text/plain")
        )

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
        if fromaddress_line_1 is not UNSET:
            field_dict["from[addressLine1]"] = fromaddress_line_1
        if fromcity is not UNSET:
            field_dict["from[city]"] = fromcity
        if fromcountry_code is not UNSET:
            field_dict["from[countryCode]"] = fromcountry_code
        if fromfirst_name is not UNSET:
            field_dict["from[firstName]"] = fromfirst_name
        if fromprovince_or_state is not UNSET:
            field_dict["from[provinceOrState]"] = fromprovince_or_state
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
        fromaddress_line_1 = d.pop("from[addressLine1]", UNSET)

        fromcity = d.pop("from[city]", UNSET)

        fromcountry_code = d.pop("from[countryCode]", UNSET)

        fromfirst_name = d.pop("from[firstName]", UNSET)

        fromprovince_or_state = d.pop("from[provinceOrState]", UNSET)

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

        create_self_mailer_files_body = cls(
            fromaddress_line_1=fromaddress_line_1,
            fromcity=fromcity,
            fromcountry_code=fromcountry_code,
            fromfirst_name=fromfirst_name,
            fromprovince_or_state=fromprovince_or_state,
            pdf=pdf,
            size=size,
            toaddress_line_1=toaddress_line_1,
            tocity=tocity,
            tofirst_name=tofirst_name,
        )

        create_self_mailer_files_body.additional_properties = d
        return create_self_mailer_files_body

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
