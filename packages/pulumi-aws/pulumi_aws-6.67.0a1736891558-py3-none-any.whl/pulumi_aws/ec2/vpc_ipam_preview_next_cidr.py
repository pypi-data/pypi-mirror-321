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

__all__ = ['VpcIpamPreviewNextCidrArgs', 'VpcIpamPreviewNextCidr']

@pulumi.input_type
class VpcIpamPreviewNextCidrArgs:
    def __init__(__self__, *,
                 ipam_pool_id: pulumi.Input[str],
                 disallowed_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 netmask_length: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a VpcIpamPreviewNextCidr resource.
        :param pulumi.Input[str] ipam_pool_id: The ID of the pool to which you want to assign a CIDR.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] disallowed_cidrs: Exclude a particular CIDR range from being returned by the pool.
        :param pulumi.Input[int] netmask_length: The netmask length of the CIDR you would like to preview from the IPAM pool.
        """
        pulumi.set(__self__, "ipam_pool_id", ipam_pool_id)
        if disallowed_cidrs is not None:
            pulumi.set(__self__, "disallowed_cidrs", disallowed_cidrs)
        if netmask_length is not None:
            pulumi.set(__self__, "netmask_length", netmask_length)

    @property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> pulumi.Input[str]:
        """
        The ID of the pool to which you want to assign a CIDR.
        """
        return pulumi.get(self, "ipam_pool_id")

    @ipam_pool_id.setter
    def ipam_pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "ipam_pool_id", value)

    @property
    @pulumi.getter(name="disallowedCidrs")
    def disallowed_cidrs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Exclude a particular CIDR range from being returned by the pool.
        """
        return pulumi.get(self, "disallowed_cidrs")

    @disallowed_cidrs.setter
    def disallowed_cidrs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "disallowed_cidrs", value)

    @property
    @pulumi.getter(name="netmaskLength")
    def netmask_length(self) -> Optional[pulumi.Input[int]]:
        """
        The netmask length of the CIDR you would like to preview from the IPAM pool.
        """
        return pulumi.get(self, "netmask_length")

    @netmask_length.setter
    def netmask_length(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "netmask_length", value)


@pulumi.input_type
class _VpcIpamPreviewNextCidrState:
    def __init__(__self__, *,
                 cidr: Optional[pulumi.Input[str]] = None,
                 disallowed_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 netmask_length: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering VpcIpamPreviewNextCidr resources.
        :param pulumi.Input[str] cidr: The previewed CIDR from the pool.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] disallowed_cidrs: Exclude a particular CIDR range from being returned by the pool.
        :param pulumi.Input[str] ipam_pool_id: The ID of the pool to which you want to assign a CIDR.
        :param pulumi.Input[int] netmask_length: The netmask length of the CIDR you would like to preview from the IPAM pool.
        """
        if cidr is not None:
            pulumi.set(__self__, "cidr", cidr)
        if disallowed_cidrs is not None:
            pulumi.set(__self__, "disallowed_cidrs", disallowed_cidrs)
        if ipam_pool_id is not None:
            pulumi.set(__self__, "ipam_pool_id", ipam_pool_id)
        if netmask_length is not None:
            pulumi.set(__self__, "netmask_length", netmask_length)

    @property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[str]]:
        """
        The previewed CIDR from the pool.
        """
        return pulumi.get(self, "cidr")

    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr", value)

    @property
    @pulumi.getter(name="disallowedCidrs")
    def disallowed_cidrs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Exclude a particular CIDR range from being returned by the pool.
        """
        return pulumi.get(self, "disallowed_cidrs")

    @disallowed_cidrs.setter
    def disallowed_cidrs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "disallowed_cidrs", value)

    @property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the pool to which you want to assign a CIDR.
        """
        return pulumi.get(self, "ipam_pool_id")

    @ipam_pool_id.setter
    def ipam_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipam_pool_id", value)

    @property
    @pulumi.getter(name="netmaskLength")
    def netmask_length(self) -> Optional[pulumi.Input[int]]:
        """
        The netmask length of the CIDR you would like to preview from the IPAM pool.
        """
        return pulumi.get(self, "netmask_length")

    @netmask_length.setter
    def netmask_length(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "netmask_length", value)


class VpcIpamPreviewNextCidr(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disallowed_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 netmask_length: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Previews a CIDR from an IPAM address pool. Only works for private IPv4.

        ## Example Usage

        Basic usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        current = aws.get_region()
        example_vpc_ipam = aws.ec2.VpcIpam("example", operating_regions=[{
            "region_name": current.name,
        }])
        example_vpc_ipam_pool = aws.ec2.VpcIpamPool("example",
            address_family="ipv4",
            ipam_scope_id=example_vpc_ipam.private_default_scope_id,
            locale=current.name)
        example_vpc_ipam_pool_cidr = aws.ec2.VpcIpamPoolCidr("example",
            ipam_pool_id=example_vpc_ipam_pool.id,
            cidr="172.20.0.0/16")
        example = aws.ec2.VpcIpamPreviewNextCidr("example",
            ipam_pool_id=example_vpc_ipam_pool.id,
            netmask_length=28,
            disallowed_cidrs=["172.2.0.0/32"],
            opts = pulumi.ResourceOptions(depends_on=[example_vpc_ipam_pool_cidr]))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] disallowed_cidrs: Exclude a particular CIDR range from being returned by the pool.
        :param pulumi.Input[str] ipam_pool_id: The ID of the pool to which you want to assign a CIDR.
        :param pulumi.Input[int] netmask_length: The netmask length of the CIDR you would like to preview from the IPAM pool.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpcIpamPreviewNextCidrArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Previews a CIDR from an IPAM address pool. Only works for private IPv4.

        ## Example Usage

        Basic usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        current = aws.get_region()
        example_vpc_ipam = aws.ec2.VpcIpam("example", operating_regions=[{
            "region_name": current.name,
        }])
        example_vpc_ipam_pool = aws.ec2.VpcIpamPool("example",
            address_family="ipv4",
            ipam_scope_id=example_vpc_ipam.private_default_scope_id,
            locale=current.name)
        example_vpc_ipam_pool_cidr = aws.ec2.VpcIpamPoolCidr("example",
            ipam_pool_id=example_vpc_ipam_pool.id,
            cidr="172.20.0.0/16")
        example = aws.ec2.VpcIpamPreviewNextCidr("example",
            ipam_pool_id=example_vpc_ipam_pool.id,
            netmask_length=28,
            disallowed_cidrs=["172.2.0.0/32"],
            opts = pulumi.ResourceOptions(depends_on=[example_vpc_ipam_pool_cidr]))
        ```

        :param str resource_name: The name of the resource.
        :param VpcIpamPreviewNextCidrArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpcIpamPreviewNextCidrArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disallowed_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 netmask_length: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpcIpamPreviewNextCidrArgs.__new__(VpcIpamPreviewNextCidrArgs)

            __props__.__dict__["disallowed_cidrs"] = disallowed_cidrs
            if ipam_pool_id is None and not opts.urn:
                raise TypeError("Missing required property 'ipam_pool_id'")
            __props__.__dict__["ipam_pool_id"] = ipam_pool_id
            __props__.__dict__["netmask_length"] = netmask_length
            __props__.__dict__["cidr"] = None
        super(VpcIpamPreviewNextCidr, __self__).__init__(
            'aws:ec2/vpcIpamPreviewNextCidr:VpcIpamPreviewNextCidr',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cidr: Optional[pulumi.Input[str]] = None,
            disallowed_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            ipam_pool_id: Optional[pulumi.Input[str]] = None,
            netmask_length: Optional[pulumi.Input[int]] = None) -> 'VpcIpamPreviewNextCidr':
        """
        Get an existing VpcIpamPreviewNextCidr resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cidr: The previewed CIDR from the pool.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] disallowed_cidrs: Exclude a particular CIDR range from being returned by the pool.
        :param pulumi.Input[str] ipam_pool_id: The ID of the pool to which you want to assign a CIDR.
        :param pulumi.Input[int] netmask_length: The netmask length of the CIDR you would like to preview from the IPAM pool.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VpcIpamPreviewNextCidrState.__new__(_VpcIpamPreviewNextCidrState)

        __props__.__dict__["cidr"] = cidr
        __props__.__dict__["disallowed_cidrs"] = disallowed_cidrs
        __props__.__dict__["ipam_pool_id"] = ipam_pool_id
        __props__.__dict__["netmask_length"] = netmask_length
        return VpcIpamPreviewNextCidr(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cidr(self) -> pulumi.Output[str]:
        """
        The previewed CIDR from the pool.
        """
        return pulumi.get(self, "cidr")

    @property
    @pulumi.getter(name="disallowedCidrs")
    def disallowed_cidrs(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Exclude a particular CIDR range from being returned by the pool.
        """
        return pulumi.get(self, "disallowed_cidrs")

    @property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> pulumi.Output[str]:
        """
        The ID of the pool to which you want to assign a CIDR.
        """
        return pulumi.get(self, "ipam_pool_id")

    @property
    @pulumi.getter(name="netmaskLength")
    def netmask_length(self) -> pulumi.Output[Optional[int]]:
        """
        The netmask length of the CIDR you would like to preview from the IPAM pool.
        """
        return pulumi.get(self, "netmask_length")

