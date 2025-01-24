# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from ... import _utilities
from ... import meta as _meta

__all__ = [
    'PriorityClassArgs',
    'PriorityClassArgsDict',
]

MYPY = False

if not MYPY:
    class PriorityClassArgsDict(TypedDict):
        """
        PriorityClass defines mapping from a priority class name to the priority integer value. The value can be any valid integer.
        """
        value: pulumi.Input[int]
        """
        value represents the integer value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec.
        """
        api_version: NotRequired[pulumi.Input[str]]
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        description: NotRequired[pulumi.Input[str]]
        """
        description is an arbitrary string that usually provides guidelines on when this priority class should be used.
        """
        global_default: NotRequired[pulumi.Input[bool]]
        """
        globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority.
        """
        kind: NotRequired[pulumi.Input[str]]
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        metadata: NotRequired[pulumi.Input['_meta.v1.ObjectMetaArgsDict']]
        """
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        preemption_policy: NotRequired[pulumi.Input[str]]
        """
        preemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.
        """
elif False:
    PriorityClassArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PriorityClassArgs:
    def __init__(__self__, *,
                 value: pulumi.Input[int],
                 api_version: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 global_default: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']] = None,
                 preemption_policy: Optional[pulumi.Input[str]] = None):
        """
        PriorityClass defines mapping from a priority class name to the priority integer value. The value can be any valid integer.
        :param pulumi.Input[int] value: value represents the integer value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[str] description: description is an arbitrary string that usually provides guidelines on when this priority class should be used.
        :param pulumi.Input[bool] global_default: globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority.
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param pulumi.Input['_meta.v1.ObjectMetaArgs'] metadata: Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        :param pulumi.Input[str] preemption_policy: preemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.
        """
        pulumi.set(__self__, "value", value)
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'scheduling.k8s.io/v1')
        if description is not None:
            pulumi.set(__self__, "description", description)
        if global_default is not None:
            pulumi.set(__self__, "global_default", global_default)
        if kind is not None:
            pulumi.set(__self__, "kind", 'PriorityClass')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if preemption_policy is not None:
            pulumi.set(__self__, "preemption_policy", preemption_policy)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[int]:
        """
        value represents the integer value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[int]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[str]]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_version", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        description is an arbitrary string that usually provides guidelines on when this priority class should be used.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="globalDefault")
    def global_default(self) -> Optional[pulumi.Input[bool]]:
        """
        globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority.
        """
        return pulumi.get(self, "global_default")

    @global_default.setter
    def global_default(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "global_default", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']]:
        """
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="preemptionPolicy")
    def preemption_policy(self) -> Optional[pulumi.Input[str]]:
        """
        preemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.
        """
        return pulumi.get(self, "preemption_policy")

    @preemption_policy.setter
    def preemption_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preemption_policy", value)


