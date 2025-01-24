from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_letter_response_201_plastic_card_double_sided import (
        CreateLetterResponse201PlasticCardDoubleSided,
    )
    from ..models.create_letter_response_201_plastic_card_single_sided import (
        CreateLetterResponse201PlasticCardSingleSided,
    )


T = TypeVar("T", bound="CreateLetterResponse201PlasticCard")


@_attrs_define
class CreateLetterResponse201PlasticCard:
    """
    Attributes:
        double_sided (Union[Unset, CreateLetterResponse201PlasticCardDoubleSided]):
        single_sided (Union[Unset, CreateLetterResponse201PlasticCardSingleSided]):
        size (Union[Unset, str]):  Example: standard.
    """

    double_sided: Union[Unset, "CreateLetterResponse201PlasticCardDoubleSided"] = UNSET
    single_sided: Union[Unset, "CreateLetterResponse201PlasticCardSingleSided"] = UNSET
    size: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        double_sided: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.double_sided, Unset):
            double_sided = self.double_sided.to_dict()

        single_sided: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.single_sided, Unset):
            single_sided = self.single_sided.to_dict()

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if double_sided is not UNSET:
            field_dict["doubleSided"] = double_sided
        if single_sided is not UNSET:
            field_dict["singleSided"] = single_sided
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_letter_response_201_plastic_card_double_sided import (
            CreateLetterResponse201PlasticCardDoubleSided,
        )
        from ..models.create_letter_response_201_plastic_card_single_sided import (
            CreateLetterResponse201PlasticCardSingleSided,
        )

        d = src_dict.copy()
        _double_sided = d.pop("doubleSided", UNSET)
        double_sided: Union[Unset, CreateLetterResponse201PlasticCardDoubleSided]
        if isinstance(_double_sided, Unset):
            double_sided = UNSET
        else:
            double_sided = CreateLetterResponse201PlasticCardDoubleSided.from_dict(_double_sided)

        _single_sided = d.pop("singleSided", UNSET)
        single_sided: Union[Unset, CreateLetterResponse201PlasticCardSingleSided]
        if isinstance(_single_sided, Unset):
            single_sided = UNSET
        else:
            single_sided = CreateLetterResponse201PlasticCardSingleSided.from_dict(_single_sided)

        size = d.pop("size", UNSET)

        create_letter_response_201_plastic_card = cls(
            double_sided=double_sided,
            single_sided=single_sided,
            size=size,
        )

        create_letter_response_201_plastic_card.additional_properties = d
        return create_letter_response_201_plastic_card

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
