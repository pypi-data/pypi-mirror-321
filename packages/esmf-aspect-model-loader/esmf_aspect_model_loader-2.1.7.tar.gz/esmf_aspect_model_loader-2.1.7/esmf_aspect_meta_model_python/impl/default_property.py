#  Copyright (c) 2023 Robert Bosch Manufacturing Solutions GmbH
#
#  See the AUTHORS file(s) distributed with this work for additional
#  information regarding authorship.
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
#
#   SPDX-License-Identifier: MPL-2.0

from typing import Any, Dict, List, Optional

from esmf_aspect_meta_model_python.base.characteristics.characteristic import Characteristic
from esmf_aspect_meta_model_python.base.property import Property
from esmf_aspect_meta_model_python.impl.base_impl import BaseImpl
from esmf_aspect_meta_model_python.loader.meta_model_base_attributes import MetaModelBaseAttributes


class DefaultProperty(BaseImpl, Property):
    """Default Property class."""

    SCALAR_ATTR_NAMES = BaseImpl.SCALAR_ATTR_NAMES + [
        "characteristic",
        "example_value",
        "extends",
        "optional",
        "not_in_payload",
        "payload_name",
    ]

    def __init__(
        self,
        meta_model_base_attributes: MetaModelBaseAttributes,
        characteristic: Optional[Characteristic],
        example_value: Optional[Any],
        extends: Optional[Property] = None,
        abstract: bool = False,
        optional: bool = False,
        not_in_payload: bool = False,
        payload_name: Optional[str] = None,
    ):
        super().__init__(meta_model_base_attributes)

        if characteristic is not None:
            characteristic.append_parent_element(self)
        self._characteristic = characteristic
        self._example_value = example_value
        self._is_abstract = abstract
        self._extends = extends
        self._optional = optional
        self._not_in_payload = not_in_payload
        self._payload_name = payload_name

    @property
    def characteristic(self) -> Optional[Characteristic]:
        """Characteristic."""
        return self._characteristic

    @property
    def example_value(self) -> Optional[Any]:
        """Example of value."""
        return self._example_value

    @property
    def is_abstract(self) -> bool:
        """Is abstract flag."""
        return self._is_abstract

    @property
    def extends(self) -> Optional[Property]:
        """Extends."""
        return self._extends

    @property
    def is_optional(self) -> bool:
        """Is optional flag."""
        return self._optional

    @property
    def is_not_in_payload(self) -> bool:
        """Is not in payload flag."""
        return self._not_in_payload

    @property
    def payload_name(self) -> str:
        """Payload name."""
        return self.name if self._payload_name is None else self._payload_name

    @property
    def preferred_names(self) -> Dict[str, str]:
        """Preferred names.

        Returns a merged dictionary of preferred names of self and the extended abstract property if it exists.
        If both, the property and the abstract property have a preferred name for the same language,
        then the preferred name of the concrete property is used.
        """
        if self.extends is None:
            return self._preferred_names
        return self.extends.preferred_names | self._preferred_names

    @property
    def descriptions(self) -> Dict[str, str]:
        """Descriptions.

        Returns a merged dictionary of descriptions of self and the extended abstract property if it exists.
        If both, the property and the abstract property have a description for the same language,
        then the description of the concrete property is used.
        """
        if self.extends is None:
            return self._descriptions
        return self.extends.descriptions | self._descriptions

    @property
    def see(self) -> List[str]:
        """See.

        Returns a combined list of all see elements of self and the extended abstract property.
        """
        return self._see if self.extends is None else self._see + self.extends.see
