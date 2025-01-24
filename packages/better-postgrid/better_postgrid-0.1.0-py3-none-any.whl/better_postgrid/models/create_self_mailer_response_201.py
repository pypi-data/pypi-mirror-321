from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_self_mailer_response_201_from import CreateSelfMailerResponse201From
    from ..models.create_self_mailer_response_201_to import CreateSelfMailerResponse201To


T = TypeVar("T", bound="CreateSelfMailerResponse201")


@_attrs_define
class CreateSelfMailerResponse201:
    """
    Attributes:
        created_at (Union[Unset, str]):  Example: 2023-07-06T15:10:09.769Z.
        from_ (Union[Unset, CreateSelfMailerResponse201From]):
        id (Union[Unset, str]):  Example: self_mailer_6XS5cDqkUZdNmQ2tAcqGnA.
        inside_html (Union[Unset, str]):  Example: Hello, {{to.firstName}}.
        inside_template (Union[Unset, str]):  Example: template_6biMkm1TwghYFHaRwyoXmS.
        live (Union[Unset, bool]):
        mailing_class (Union[Unset, str]):  Example: first_class.
        object_ (Union[Unset, str]):  Example: self_mailer.
        outside_html (Union[Unset, str]):  Example: Hello again, {{to.firstName}}.
        outside_template (Union[Unset, str]):  Example: template_8CHnHN1yhkSCynA1dsZaGc.
        send_date (Union[Unset, str]):  Example: 2023-07-06T15:10:09.761Z.
        size (Union[Unset, str]):  Example: 8.5x11_bifold.
        status (Union[Unset, str]):  Example: ready.
        to (Union[Unset, CreateSelfMailerResponse201To]):
        updated_at (Union[Unset, str]):  Example: 2023-07-06T15:10:09.769Z.
        uploaded_pdf (Union[Unset, str]):  Example: https://pg-prod-bucket-
            1.s3.amazonaws.com/test/pdf_95cRWVX23pXyTKHBYDaoQi?AWSAccessKeyId=AKIA5GFUILSULWTWCR64&Expires=1688658078&Signat
            ure=2RkvE86LbBet%2F9DTZ7NxWMSGxEU%3D.
    """

    created_at: Union[Unset, str] = UNSET
    from_: Union[Unset, "CreateSelfMailerResponse201From"] = UNSET
    id: Union[Unset, str] = UNSET
    inside_html: Union[Unset, str] = UNSET
    inside_template: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    mailing_class: Union[Unset, str] = UNSET
    object_: Union[Unset, str] = UNSET
    outside_html: Union[Unset, str] = UNSET
    outside_template: Union[Unset, str] = UNSET
    send_date: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    to: Union[Unset, "CreateSelfMailerResponse201To"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    uploaded_pdf: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        id = self.id

        inside_html = self.inside_html

        inside_template = self.inside_template

        live = self.live

        mailing_class = self.mailing_class

        object_ = self.object_

        outside_html = self.outside_html

        outside_template = self.outside_template

        send_date = self.send_date

        size = self.size

        status = self.status

        to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        updated_at = self.updated_at

        uploaded_pdf = self.uploaded_pdf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if from_ is not UNSET:
            field_dict["from"] = from_
        if id is not UNSET:
            field_dict["id"] = id
        if inside_html is not UNSET:
            field_dict["insideHTML"] = inside_html
        if inside_template is not UNSET:
            field_dict["insideTemplate"] = inside_template
        if live is not UNSET:
            field_dict["live"] = live
        if mailing_class is not UNSET:
            field_dict["mailingClass"] = mailing_class
        if object_ is not UNSET:
            field_dict["object"] = object_
        if outside_html is not UNSET:
            field_dict["outsideHTML"] = outside_html
        if outside_template is not UNSET:
            field_dict["outsideTemplate"] = outside_template
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
        if uploaded_pdf is not UNSET:
            field_dict["uploadedPDF"] = uploaded_pdf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_self_mailer_response_201_from import CreateSelfMailerResponse201From
        from ..models.create_self_mailer_response_201_to import CreateSelfMailerResponse201To

        d = src_dict.copy()
        created_at = d.pop("createdAt", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, CreateSelfMailerResponse201From]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = CreateSelfMailerResponse201From.from_dict(_from_)

        id = d.pop("id", UNSET)

        inside_html = d.pop("insideHTML", UNSET)

        inside_template = d.pop("insideTemplate", UNSET)

        live = d.pop("live", UNSET)

        mailing_class = d.pop("mailingClass", UNSET)

        object_ = d.pop("object", UNSET)

        outside_html = d.pop("outsideHTML", UNSET)

        outside_template = d.pop("outsideTemplate", UNSET)

        send_date = d.pop("sendDate", UNSET)

        size = d.pop("size", UNSET)

        status = d.pop("status", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, CreateSelfMailerResponse201To]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = CreateSelfMailerResponse201To.from_dict(_to)

        updated_at = d.pop("updatedAt", UNSET)

        uploaded_pdf = d.pop("uploadedPDF", UNSET)

        create_self_mailer_response_201 = cls(
            created_at=created_at,
            from_=from_,
            id=id,
            inside_html=inside_html,
            inside_template=inside_template,
            live=live,
            mailing_class=mailing_class,
            object_=object_,
            outside_html=outside_html,
            outside_template=outside_template,
            send_date=send_date,
            size=size,
            status=status,
            to=to,
            updated_at=updated_at,
            uploaded_pdf=uploaded_pdf,
        )

        create_self_mailer_response_201.additional_properties = d
        return create_self_mailer_response_201

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
