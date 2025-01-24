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
from scope_client.api_bindings.models.job_kind import JobKind
from scope_client.api_bindings.models.job_priority import JobPriority
from scope_client.api_bindings.models.job_spec import JobSpec
from typing import Optional, Set
from typing_extensions import Self

class PostJob(BaseModel):
    """
    PostJob
    """ # noqa: E501
    kind: JobKind = Field(description="Type of job.")
    job_spec: JobSpec
    schedule_id: Optional[StrictStr] = None
    ready_at: Optional[datetime] = None
    nonce: Optional[StrictStr] = None
    job_priority: Optional[JobPriority] = None
    __properties: ClassVar[List[str]] = ["kind", "job_spec", "schedule_id", "ready_at", "nonce", "job_priority"]

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
        """Create an instance of PostJob from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of job_spec
        if self.job_spec:
            _dict['job_spec'] = self.job_spec.to_dict()
        # set to None if schedule_id (nullable) is None
        # and model_fields_set contains the field
        if self.schedule_id is None and "schedule_id" in self.model_fields_set:
            _dict['schedule_id'] = None

        # set to None if ready_at (nullable) is None
        # and model_fields_set contains the field
        if self.ready_at is None and "ready_at" in self.model_fields_set:
            _dict['ready_at'] = None

        # set to None if nonce (nullable) is None
        # and model_fields_set contains the field
        if self.nonce is None and "nonce" in self.model_fields_set:
            _dict['nonce'] = None

        # set to None if job_priority (nullable) is None
        # and model_fields_set contains the field
        if self.job_priority is None and "job_priority" in self.model_fields_set:
            _dict['job_priority'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostJob from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "kind": obj.get("kind"),
            "job_spec": JobSpec.from_dict(obj["job_spec"]) if obj.get("job_spec") is not None else None,
            "schedule_id": obj.get("schedule_id"),
            "ready_at": obj.get("ready_at"),
            "nonce": obj.get("nonce"),
            "job_priority": obj.get("job_priority")
        })
        return _obj


