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
from . import outputs
from ... import core as _core
from ... import meta as _meta
from ._inputs import *

__all__ = ['ResourceClaimInitArgs', 'ResourceClaim']

@pulumi.input_type
class ResourceClaimInitArgs:
    def __init__(__self__, *,
                 spec: pulumi.Input['ResourceClaimSpecArgs'],
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']] = None):
        """
        The set of arguments for constructing a ResourceClaim resource.
        :param pulumi.Input['ResourceClaimSpecArgs'] spec: Spec describes the desired attributes of a resource that then needs to be allocated. It can only be set once when creating the ResourceClaim.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param pulumi.Input['_meta.v1.ObjectMetaArgs'] metadata: Standard object metadata
        """
        pulumi.set(__self__, "spec", spec)
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'resource.k8s.io/v1alpha1')
        if kind is not None:
            pulumi.set(__self__, "kind", 'ResourceClaim')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Input['ResourceClaimSpecArgs']:
        """
        Spec describes the desired attributes of a resource that then needs to be allocated. It can only be set once when creating the ResourceClaim.
        """
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: pulumi.Input['ResourceClaimSpecArgs']):
        pulumi.set(self, "spec", value)

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
        Standard object metadata
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']]):
        pulumi.set(self, "metadata", value)


class ResourceClaim(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Union['_meta.v1.ObjectMetaArgs', '_meta.v1.ObjectMetaArgsDict']]] = None,
                 spec: Optional[pulumi.Input[Union['ResourceClaimSpecArgs', 'ResourceClaimSpecArgsDict']]] = None,
                 __props__=None):
        """
        ResourceClaim describes which resources are needed by a resource consumer. Its status tracks whether the resource has been allocated and what the resulting attributes are.

        This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param pulumi.Input[Union['_meta.v1.ObjectMetaArgs', '_meta.v1.ObjectMetaArgsDict']] metadata: Standard object metadata
        :param pulumi.Input[Union['ResourceClaimSpecArgs', 'ResourceClaimSpecArgsDict']] spec: Spec describes the desired attributes of a resource that then needs to be allocated. It can only be set once when creating the ResourceClaim.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResourceClaimInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ResourceClaim describes which resources are needed by a resource consumer. Its status tracks whether the resource has been allocated and what the resulting attributes are.

        This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

        :param str resource_name: The name of the resource.
        :param ResourceClaimInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResourceClaimInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Union['_meta.v1.ObjectMetaArgs', '_meta.v1.ObjectMetaArgsDict']]] = None,
                 spec: Optional[pulumi.Input[Union['ResourceClaimSpecArgs', 'ResourceClaimSpecArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResourceClaimInitArgs.__new__(ResourceClaimInitArgs)

            __props__.__dict__["api_version"] = 'resource.k8s.io/v1alpha1'
            __props__.__dict__["kind"] = 'ResourceClaim'
            __props__.__dict__["metadata"] = metadata
            if spec is None and not opts.urn:
                raise TypeError("Missing required property 'spec'")
            __props__.__dict__["spec"] = spec
            __props__.__dict__["status"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="kubernetes:resource.k8s.io/v1alpha2:ResourceClaim"), pulumi.Alias(type_="kubernetes:resource.k8s.io/v1alpha3:ResourceClaim"), pulumi.Alias(type_="kubernetes:resource.k8s.io/v1beta1:ResourceClaim")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ResourceClaim, __self__).__init__(
            'kubernetes:resource.k8s.io/v1alpha1:ResourceClaim',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ResourceClaim':
        """
        Get an existing ResourceClaim resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ResourceClaimInitArgs.__new__(ResourceClaimInitArgs)

        __props__.__dict__["api_version"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["spec"] = None
        __props__.__dict__["status"] = None
        return ResourceClaim(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Output[str]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output['_meta.v1.outputs.ObjectMeta']:
        """
        Standard object metadata
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Output['outputs.ResourceClaimSpec']:
        """
        Spec describes the desired attributes of a resource that then needs to be allocated. It can only be set once when creating the ResourceClaim.
        """
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional['outputs.ResourceClaimStatus']]:
        """
        Status describes whether the resource is available and with which attributes.
        """
        return pulumi.get(self, "status")

