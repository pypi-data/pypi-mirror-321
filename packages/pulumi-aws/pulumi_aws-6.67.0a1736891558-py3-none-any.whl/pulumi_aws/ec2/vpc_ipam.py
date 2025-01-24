# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
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
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['VpcIpamArgs', 'VpcIpam']

@pulumi.input_type
class VpcIpamArgs:
    def __init__(__self__, *,
                 operating_regions: pulumi.Input[Sequence[pulumi.Input['VpcIpamOperatingRegionArgs']]],
                 cascade: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_private_gua: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tier: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VpcIpam resource.
        :param pulumi.Input[Sequence[pulumi.Input['VpcIpamOperatingRegionArgs']]] operating_regions: Determines which locales can be chosen when you create pools. Locale is the Region where you want to make an IPAM pool available for allocations. You can only create pools with locales that match the operating Regions of the IPAM. You can only create VPCs from a pool whose locale matches the VPC's Region. You specify a region using the region_name parameter. You **must** set your provider block region as an operating_region.
        :param pulumi.Input[bool] cascade: Enables you to quickly delete an IPAM, private scopes, pools in private scopes, and any allocations in the pools in private scopes.
        :param pulumi.Input[str] description: A description for the IPAM.
        :param pulumi.Input[bool] enable_private_gua: Enable this option to use your own GUA ranges as private IPv6 addresses. Default: `false`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] tier: specifies the IPAM tier. Valid options include `free` and `advanced`. Default is `advanced`.
        """
        pulumi.set(__self__, "operating_regions", operating_regions)
        if cascade is not None:
            pulumi.set(__self__, "cascade", cascade)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable_private_gua is not None:
            pulumi.set(__self__, "enable_private_gua", enable_private_gua)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter(name="operatingRegions")
    def operating_regions(self) -> pulumi.Input[Sequence[pulumi.Input['VpcIpamOperatingRegionArgs']]]:
        """
        Determines which locales can be chosen when you create pools. Locale is the Region where you want to make an IPAM pool available for allocations. You can only create pools with locales that match the operating Regions of the IPAM. You can only create VPCs from a pool whose locale matches the VPC's Region. You specify a region using the region_name parameter. You **must** set your provider block region as an operating_region.
        """
        return pulumi.get(self, "operating_regions")

    @operating_regions.setter
    def operating_regions(self, value: pulumi.Input[Sequence[pulumi.Input['VpcIpamOperatingRegionArgs']]]):
        pulumi.set(self, "operating_regions", value)

    @property
    @pulumi.getter
    def cascade(self) -> Optional[pulumi.Input[bool]]:
        """
        Enables you to quickly delete an IPAM, private scopes, pools in private scopes, and any allocations in the pools in private scopes.
        """
        return pulumi.get(self, "cascade")

    @cascade.setter
    def cascade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cascade", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the IPAM.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="enablePrivateGua")
    def enable_private_gua(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable this option to use your own GUA ranges as private IPv6 addresses. Default: `false`.
        """
        return pulumi.get(self, "enable_private_gua")

    @enable_private_gua.setter
    def enable_private_gua(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_private_gua", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[str]]:
        """
        specifies the IPAM tier. Valid options include `free` and `advanced`. Default is `advanced`.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tier", value)


@pulumi.input_type
class _VpcIpamState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 cascade: Optional[pulumi.Input[bool]] = None,
                 default_resource_discovery_association_id: Optional[pulumi.Input[str]] = None,
                 default_resource_discovery_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_private_gua: Optional[pulumi.Input[bool]] = None,
                 operating_regions: Optional[pulumi.Input[Sequence[pulumi.Input['VpcIpamOperatingRegionArgs']]]] = None,
                 private_default_scope_id: Optional[pulumi.Input[str]] = None,
                 public_default_scope_id: Optional[pulumi.Input[str]] = None,
                 scope_count: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tier: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VpcIpam resources.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of IPAM
        :param pulumi.Input[bool] cascade: Enables you to quickly delete an IPAM, private scopes, pools in private scopes, and any allocations in the pools in private scopes.
        :param pulumi.Input[str] default_resource_discovery_association_id: The IPAM's default resource discovery association ID.
        :param pulumi.Input[str] default_resource_discovery_id: The IPAM's default resource discovery ID.
        :param pulumi.Input[str] description: A description for the IPAM.
        :param pulumi.Input[bool] enable_private_gua: Enable this option to use your own GUA ranges as private IPv6 addresses. Default: `false`.
        :param pulumi.Input[Sequence[pulumi.Input['VpcIpamOperatingRegionArgs']]] operating_regions: Determines which locales can be chosen when you create pools. Locale is the Region where you want to make an IPAM pool available for allocations. You can only create pools with locales that match the operating Regions of the IPAM. You can only create VPCs from a pool whose locale matches the VPC's Region. You specify a region using the region_name parameter. You **must** set your provider block region as an operating_region.
        :param pulumi.Input[str] private_default_scope_id: The ID of the IPAM's private scope. A scope is a top-level container in IPAM. Each scope represents an IP-independent network. Scopes enable you to represent networks where you have overlapping IP space. When you create an IPAM, IPAM automatically creates two scopes: public and private. The private scope is intended for private IP space. The public scope is intended for all internet-routable IP space.
        :param pulumi.Input[str] public_default_scope_id: The ID of the IPAM's public scope. A scope is a top-level container in IPAM. Each scope represents an IP-independent network. Scopes enable you to represent networks where you have overlapping IP space. When you create an IPAM, IPAM automatically creates two scopes: public and private. The private scope is intended for private
               IP space. The public scope is intended for all internet-routable IP space.
        :param pulumi.Input[int] scope_count: The number of scopes in the IPAM.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] tier: specifies the IPAM tier. Valid options include `free` and `advanced`. Default is `advanced`.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if cascade is not None:
            pulumi.set(__self__, "cascade", cascade)
        if default_resource_discovery_association_id is not None:
            pulumi.set(__self__, "default_resource_discovery_association_id", default_resource_discovery_association_id)
        if default_resource_discovery_id is not None:
            pulumi.set(__self__, "default_resource_discovery_id", default_resource_discovery_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable_private_gua is not None:
            pulumi.set(__self__, "enable_private_gua", enable_private_gua)
        if operating_regions is not None:
            pulumi.set(__self__, "operating_regions", operating_regions)
        if private_default_scope_id is not None:
            pulumi.set(__self__, "private_default_scope_id", private_default_scope_id)
        if public_default_scope_id is not None:
            pulumi.set(__self__, "public_default_scope_id", public_default_scope_id)
        if scope_count is not None:
            pulumi.set(__self__, "scope_count", scope_count)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
            pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of IPAM
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def cascade(self) -> Optional[pulumi.Input[bool]]:
        """
        Enables you to quickly delete an IPAM, private scopes, pools in private scopes, and any allocations in the pools in private scopes.
        """
        return pulumi.get(self, "cascade")

    @cascade.setter
    def cascade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cascade", value)

    @property
    @pulumi.getter(name="defaultResourceDiscoveryAssociationId")
    def default_resource_discovery_association_id(self) -> Optional[pulumi.Input[str]]:
        """
        The IPAM's default resource discovery association ID.
        """
        return pulumi.get(self, "default_resource_discovery_association_id")

    @default_resource_discovery_association_id.setter
    def default_resource_discovery_association_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_resource_discovery_association_id", value)

    @property
    @pulumi.getter(name="defaultResourceDiscoveryId")
    def default_resource_discovery_id(self) -> Optional[pulumi.Input[str]]:
        """
        The IPAM's default resource discovery ID.
        """
        return pulumi.get(self, "default_resource_discovery_id")

    @default_resource_discovery_id.setter
    def default_resource_discovery_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_resource_discovery_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the IPAM.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="enablePrivateGua")
    def enable_private_gua(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable this option to use your own GUA ranges as private IPv6 addresses. Default: `false`.
        """
        return pulumi.get(self, "enable_private_gua")

    @enable_private_gua.setter
    def enable_private_gua(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_private_gua", value)

    @property
    @pulumi.getter(name="operatingRegions")
    def operating_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpcIpamOperatingRegionArgs']]]]:
        """
        Determines which locales can be chosen when you create pools. Locale is the Region where you want to make an IPAM pool available for allocations. You can only create pools with locales that match the operating Regions of the IPAM. You can only create VPCs from a pool whose locale matches the VPC's Region. You specify a region using the region_name parameter. You **must** set your provider block region as an operating_region.
        """
        return pulumi.get(self, "operating_regions")

    @operating_regions.setter
    def operating_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpcIpamOperatingRegionArgs']]]]):
        pulumi.set(self, "operating_regions", value)

    @property
    @pulumi.getter(name="privateDefaultScopeId")
    def private_default_scope_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the IPAM's private scope. A scope is a top-level container in IPAM. Each scope represents an IP-independent network. Scopes enable you to represent networks where you have overlapping IP space. When you create an IPAM, IPAM automatically creates two scopes: public and private. The private scope is intended for private IP space. The public scope is intended for all internet-routable IP space.
        """
        return pulumi.get(self, "private_default_scope_id")

    @private_default_scope_id.setter
    def private_default_scope_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_default_scope_id", value)

    @property
    @pulumi.getter(name="publicDefaultScopeId")
    def public_default_scope_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the IPAM's public scope. A scope is a top-level container in IPAM. Each scope represents an IP-independent network. Scopes enable you to represent networks where you have overlapping IP space. When you create an IPAM, IPAM automatically creates two scopes: public and private. The private scope is intended for private
        IP space. The public scope is intended for all internet-routable IP space.
        """
        return pulumi.get(self, "public_default_scope_id")

    @public_default_scope_id.setter
    def public_default_scope_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_default_scope_id", value)

    @property
    @pulumi.getter(name="scopeCount")
    def scope_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of scopes in the IPAM.
        """
        return pulumi.get(self, "scope_count")

    @scope_count.setter
    def scope_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "scope_count", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    @_utilities.deprecated("""Please use `tags` instead.""")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[str]]:
        """
        specifies the IPAM tier. Valid options include `free` and `advanced`. Default is `advanced`.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tier", value)


class VpcIpam(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cascade: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_private_gua: Optional[pulumi.Input[bool]] = None,
                 operating_regions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['VpcIpamOperatingRegionArgs', 'VpcIpamOperatingRegionArgsDict']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tier: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an IPAM resource.

        ## Example Usage

        Basic usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        current = aws.get_region()
        main = aws.ec2.VpcIpam("main",
            description="My IPAM",
            operating_regions=[{
                "region_name": current.name,
            }],
            tags={
                "Test": "Main",
            })
        ```

        Shared with multiple operating_regions:

        ## Import

        Using `pulumi import`, import IPAMs using the IPAM `id`. For example:

        ```sh
        $ pulumi import aws:ec2/vpcIpam:VpcIpam example ipam-0178368ad2146a492
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] cascade: Enables you to quickly delete an IPAM, private scopes, pools in private scopes, and any allocations in the pools in private scopes.
        :param pulumi.Input[str] description: A description for the IPAM.
        :param pulumi.Input[bool] enable_private_gua: Enable this option to use your own GUA ranges as private IPv6 addresses. Default: `false`.
        :param pulumi.Input[Sequence[pulumi.Input[Union['VpcIpamOperatingRegionArgs', 'VpcIpamOperatingRegionArgsDict']]]] operating_regions: Determines which locales can be chosen when you create pools. Locale is the Region where you want to make an IPAM pool available for allocations. You can only create pools with locales that match the operating Regions of the IPAM. You can only create VPCs from a pool whose locale matches the VPC's Region. You specify a region using the region_name parameter. You **must** set your provider block region as an operating_region.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] tier: specifies the IPAM tier. Valid options include `free` and `advanced`. Default is `advanced`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpcIpamArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an IPAM resource.

        ## Example Usage

        Basic usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        current = aws.get_region()
        main = aws.ec2.VpcIpam("main",
            description="My IPAM",
            operating_regions=[{
                "region_name": current.name,
            }],
            tags={
                "Test": "Main",
            })
        ```

        Shared with multiple operating_regions:

        ## Import

        Using `pulumi import`, import IPAMs using the IPAM `id`. For example:

        ```sh
        $ pulumi import aws:ec2/vpcIpam:VpcIpam example ipam-0178368ad2146a492
        ```

        :param str resource_name: The name of the resource.
        :param VpcIpamArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpcIpamArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cascade: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_private_gua: Optional[pulumi.Input[bool]] = None,
                 operating_regions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['VpcIpamOperatingRegionArgs', 'VpcIpamOperatingRegionArgsDict']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tier: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpcIpamArgs.__new__(VpcIpamArgs)

            __props__.__dict__["cascade"] = cascade
            __props__.__dict__["description"] = description
            __props__.__dict__["enable_private_gua"] = enable_private_gua
            if operating_regions is None and not opts.urn:
                raise TypeError("Missing required property 'operating_regions'")
            __props__.__dict__["operating_regions"] = operating_regions
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tier"] = tier
            __props__.__dict__["arn"] = None
            __props__.__dict__["default_resource_discovery_association_id"] = None
            __props__.__dict__["default_resource_discovery_id"] = None
            __props__.__dict__["private_default_scope_id"] = None
            __props__.__dict__["public_default_scope_id"] = None
            __props__.__dict__["scope_count"] = None
            __props__.__dict__["tags_all"] = None
        super(VpcIpam, __self__).__init__(
            'aws:ec2/vpcIpam:VpcIpam',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            cascade: Optional[pulumi.Input[bool]] = None,
            default_resource_discovery_association_id: Optional[pulumi.Input[str]] = None,
            default_resource_discovery_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            enable_private_gua: Optional[pulumi.Input[bool]] = None,
            operating_regions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['VpcIpamOperatingRegionArgs', 'VpcIpamOperatingRegionArgsDict']]]]] = None,
            private_default_scope_id: Optional[pulumi.Input[str]] = None,
            public_default_scope_id: Optional[pulumi.Input[str]] = None,
            scope_count: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tier: Optional[pulumi.Input[str]] = None) -> 'VpcIpam':
        """
        Get an existing VpcIpam resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of IPAM
        :param pulumi.Input[bool] cascade: Enables you to quickly delete an IPAM, private scopes, pools in private scopes, and any allocations in the pools in private scopes.
        :param pulumi.Input[str] default_resource_discovery_association_id: The IPAM's default resource discovery association ID.
        :param pulumi.Input[str] default_resource_discovery_id: The IPAM's default resource discovery ID.
        :param pulumi.Input[str] description: A description for the IPAM.
        :param pulumi.Input[bool] enable_private_gua: Enable this option to use your own GUA ranges as private IPv6 addresses. Default: `false`.
        :param pulumi.Input[Sequence[pulumi.Input[Union['VpcIpamOperatingRegionArgs', 'VpcIpamOperatingRegionArgsDict']]]] operating_regions: Determines which locales can be chosen when you create pools. Locale is the Region where you want to make an IPAM pool available for allocations. You can only create pools with locales that match the operating Regions of the IPAM. You can only create VPCs from a pool whose locale matches the VPC's Region. You specify a region using the region_name parameter. You **must** set your provider block region as an operating_region.
        :param pulumi.Input[str] private_default_scope_id: The ID of the IPAM's private scope. A scope is a top-level container in IPAM. Each scope represents an IP-independent network. Scopes enable you to represent networks where you have overlapping IP space. When you create an IPAM, IPAM automatically creates two scopes: public and private. The private scope is intended for private IP space. The public scope is intended for all internet-routable IP space.
        :param pulumi.Input[str] public_default_scope_id: The ID of the IPAM's public scope. A scope is a top-level container in IPAM. Each scope represents an IP-independent network. Scopes enable you to represent networks where you have overlapping IP space. When you create an IPAM, IPAM automatically creates two scopes: public and private. The private scope is intended for private
               IP space. The public scope is intended for all internet-routable IP space.
        :param pulumi.Input[int] scope_count: The number of scopes in the IPAM.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] tier: specifies the IPAM tier. Valid options include `free` and `advanced`. Default is `advanced`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VpcIpamState.__new__(_VpcIpamState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["cascade"] = cascade
        __props__.__dict__["default_resource_discovery_association_id"] = default_resource_discovery_association_id
        __props__.__dict__["default_resource_discovery_id"] = default_resource_discovery_id
        __props__.__dict__["description"] = description
        __props__.__dict__["enable_private_gua"] = enable_private_gua
        __props__.__dict__["operating_regions"] = operating_regions
        __props__.__dict__["private_default_scope_id"] = private_default_scope_id
        __props__.__dict__["public_default_scope_id"] = public_default_scope_id
        __props__.__dict__["scope_count"] = scope_count
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["tier"] = tier
        return VpcIpam(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of IPAM
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def cascade(self) -> pulumi.Output[Optional[bool]]:
        """
        Enables you to quickly delete an IPAM, private scopes, pools in private scopes, and any allocations in the pools in private scopes.
        """
        return pulumi.get(self, "cascade")

    @property
    @pulumi.getter(name="defaultResourceDiscoveryAssociationId")
    def default_resource_discovery_association_id(self) -> pulumi.Output[str]:
        """
        The IPAM's default resource discovery association ID.
        """
        return pulumi.get(self, "default_resource_discovery_association_id")

    @property
    @pulumi.getter(name="defaultResourceDiscoveryId")
    def default_resource_discovery_id(self) -> pulumi.Output[str]:
        """
        The IPAM's default resource discovery ID.
        """
        return pulumi.get(self, "default_resource_discovery_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the IPAM.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="enablePrivateGua")
    def enable_private_gua(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable this option to use your own GUA ranges as private IPv6 addresses. Default: `false`.
        """
        return pulumi.get(self, "enable_private_gua")

    @property
    @pulumi.getter(name="operatingRegions")
    def operating_regions(self) -> pulumi.Output[Sequence['outputs.VpcIpamOperatingRegion']]:
        """
        Determines which locales can be chosen when you create pools. Locale is the Region where you want to make an IPAM pool available for allocations. You can only create pools with locales that match the operating Regions of the IPAM. You can only create VPCs from a pool whose locale matches the VPC's Region. You specify a region using the region_name parameter. You **must** set your provider block region as an operating_region.
        """
        return pulumi.get(self, "operating_regions")

    @property
    @pulumi.getter(name="privateDefaultScopeId")
    def private_default_scope_id(self) -> pulumi.Output[str]:
        """
        The ID of the IPAM's private scope. A scope is a top-level container in IPAM. Each scope represents an IP-independent network. Scopes enable you to represent networks where you have overlapping IP space. When you create an IPAM, IPAM automatically creates two scopes: public and private. The private scope is intended for private IP space. The public scope is intended for all internet-routable IP space.
        """
        return pulumi.get(self, "private_default_scope_id")

    @property
    @pulumi.getter(name="publicDefaultScopeId")
    def public_default_scope_id(self) -> pulumi.Output[str]:
        """
        The ID of the IPAM's public scope. A scope is a top-level container in IPAM. Each scope represents an IP-independent network. Scopes enable you to represent networks where you have overlapping IP space. When you create an IPAM, IPAM automatically creates two scopes: public and private. The private scope is intended for private
        IP space. The public scope is intended for all internet-routable IP space.
        """
        return pulumi.get(self, "public_default_scope_id")

    @property
    @pulumi.getter(name="scopeCount")
    def scope_count(self) -> pulumi.Output[int]:
        """
        The number of scopes in the IPAM.
        """
        return pulumi.get(self, "scope_count")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    @_utilities.deprecated("""Please use `tags` instead.""")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Output[Optional[str]]:
        """
        specifies the IPAM tier. Valid options include `free` and `advanced`. Default is `advanced`.
        """
        return pulumi.get(self, "tier")

