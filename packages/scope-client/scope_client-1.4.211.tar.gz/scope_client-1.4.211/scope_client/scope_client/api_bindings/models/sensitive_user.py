# coding: utf-8

"""
    Arthur Scope

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from scope_client.api_bindings.models.credentials import Credentials
from scope_client.api_bindings.models.user_type import UserType
from typing import Optional, Set
from typing_extensions import Self

class SensitiveUser(BaseModel):
    """
    SensitiveUser
    """ # noqa: E501
    id: StrictStr = Field(description="Unique user ID assigned by Arthur.")
    first_name: StrictStr = Field(description="The user's first name.")
    last_name: Optional[StrictStr]
    email: Optional[StrictStr] = None
    picture: Optional[StrictStr] = None
    user_type: UserType = Field(description="The type of user.")
    realm: StrictStr = Field(description="The realm the user belongs to.")
    data_plane_id: Optional[StrictStr] = None
    client_id: Optional[StrictStr] = None
    created_at: datetime = Field(description="Time of record creation.")
    updated_at: datetime = Field(description="Time of last record update.")
    organization_id: StrictStr = Field(description="The ID of the organization the user belongs to.")
    credentials: Credentials
    __properties: ClassVar[List[str]] = ["id", "first_name", "last_name", "email", "picture", "user_type", "realm", "data_plane_id", "client_id", "created_at", "updated_at", "organization_id", "credentials"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SensitiveUser from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of credentials
        if self.credentials:
            _dict['credentials'] = self.credentials.to_dict()
        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['last_name'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if picture (nullable) is None
        # and model_fields_set contains the field
        if self.picture is None and "picture" in self.model_fields_set:
            _dict['picture'] = None

        # set to None if data_plane_id (nullable) is None
        # and model_fields_set contains the field
        if self.data_plane_id is None and "data_plane_id" in self.model_fields_set:
            _dict['data_plane_id'] = None

        # set to None if client_id (nullable) is None
        # and model_fields_set contains the field
        if self.client_id is None and "client_id" in self.model_fields_set:
            _dict['client_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SensitiveUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "email": obj.get("email"),
            "picture": obj.get("picture"),
            "user_type": obj.get("user_type"),
            "realm": obj.get("realm"),
            "data_plane_id": obj.get("data_plane_id"),
            "client_id": obj.get("client_id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "organization_id": obj.get("organization_id"),
            "credentials": Credentials.from_dict(obj["credentials"]) if obj.get("credentials") is not None else None
        })
        return _obj


