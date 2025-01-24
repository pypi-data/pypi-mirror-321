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

__all__ = ['VpcDhcpOptionsAssociationArgs', 'VpcDhcpOptionsAssociation']

@pulumi.input_type
class VpcDhcpOptionsAssociationArgs:
    def __init__(__self__, *,
                 dhcp_options_id: pulumi.Input[str],
                 vpc_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a VpcDhcpOptionsAssociation resource.
        :param pulumi.Input[str] dhcp_options_id: The ID of the DHCP Options Set to associate to the VPC.
        :param pulumi.Input[str] vpc_id: The ID of the VPC to which we would like to associate a DHCP Options Set.
        """
        pulumi.set(__self__, "dhcp_options_id", dhcp_options_id)
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="dhcpOptionsId")
    def dhcp_options_id(self) -> pulumi.Input[str]:
        """
        The ID of the DHCP Options Set to associate to the VPC.
        """
        return pulumi.get(self, "dhcp_options_id")

    @dhcp_options_id.setter
    def dhcp_options_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "dhcp_options_id", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        """
        The ID of the VPC to which we would like to associate a DHCP Options Set.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)


@pulumi.input_type
class _VpcDhcpOptionsAssociationState:
    def __init__(__self__, *,
                 dhcp_options_id: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VpcDhcpOptionsAssociation resources.
        :param pulumi.Input[str] dhcp_options_id: The ID of the DHCP Options Set to associate to the VPC.
        :param pulumi.Input[str] vpc_id: The ID of the VPC to which we would like to associate a DHCP Options Set.
        """
        if dhcp_options_id is not None:
            pulumi.set(__self__, "dhcp_options_id", dhcp_options_id)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="dhcpOptionsId")
    def dhcp_options_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the DHCP Options Set to associate to the VPC.
        """
        return pulumi.get(self, "dhcp_options_id")

    @dhcp_options_id.setter
    def dhcp_options_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dhcp_options_id", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the VPC to which we would like to associate a DHCP Options Set.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


class VpcDhcpOptionsAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dhcp_options_id: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a VPC DHCP Options Association resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        dns_resolver = aws.ec2.VpcDhcpOptionsAssociation("dns_resolver",
            vpc_id=foo_aws_vpc["id"],
            dhcp_options_id=foo["id"])
        ```

        ## Remarks

        * You can only associate one DHCP Options Set to a given VPC ID.
        * Removing the DHCP Options Association automatically sets AWS's `default` DHCP Options Set to the VPC.

        ## Import

        Using `pulumi import`, import DHCP associations using the VPC ID associated with the options. For example:

        ```sh
        $ pulumi import aws:ec2/vpcDhcpOptionsAssociation:VpcDhcpOptionsAssociation imported vpc-0f001273ec18911b1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dhcp_options_id: The ID of the DHCP Options Set to associate to the VPC.
        :param pulumi.Input[str] vpc_id: The ID of the VPC to which we would like to associate a DHCP Options Set.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpcDhcpOptionsAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a VPC DHCP Options Association resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        dns_resolver = aws.ec2.VpcDhcpOptionsAssociation("dns_resolver",
            vpc_id=foo_aws_vpc["id"],
            dhcp_options_id=foo["id"])
        ```

        ## Remarks

        * You can only associate one DHCP Options Set to a given VPC ID.
        * Removing the DHCP Options Association automatically sets AWS's `default` DHCP Options Set to the VPC.

        ## Import

        Using `pulumi import`, import DHCP associations using the VPC ID associated with the options. For example:

        ```sh
        $ pulumi import aws:ec2/vpcDhcpOptionsAssociation:VpcDhcpOptionsAssociation imported vpc-0f001273ec18911b1
        ```

        :param str resource_name: The name of the resource.
        :param VpcDhcpOptionsAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpcDhcpOptionsAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dhcp_options_id: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpcDhcpOptionsAssociationArgs.__new__(VpcDhcpOptionsAssociationArgs)

            if dhcp_options_id is None and not opts.urn:
                raise TypeError("Missing required property 'dhcp_options_id'")
            __props__.__dict__["dhcp_options_id"] = dhcp_options_id
            if vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_id'")
            __props__.__dict__["vpc_id"] = vpc_id
        super(VpcDhcpOptionsAssociation, __self__).__init__(
            'aws:ec2/vpcDhcpOptionsAssociation:VpcDhcpOptionsAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dhcp_options_id: Optional[pulumi.Input[str]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None) -> 'VpcDhcpOptionsAssociation':
        """
        Get an existing VpcDhcpOptionsAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dhcp_options_id: The ID of the DHCP Options Set to associate to the VPC.
        :param pulumi.Input[str] vpc_id: The ID of the VPC to which we would like to associate a DHCP Options Set.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VpcDhcpOptionsAssociationState.__new__(_VpcDhcpOptionsAssociationState)

        __props__.__dict__["dhcp_options_id"] = dhcp_options_id
        __props__.__dict__["vpc_id"] = vpc_id
        return VpcDhcpOptionsAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dhcpOptionsId")
    def dhcp_options_id(self) -> pulumi.Output[str]:
        """
        The ID of the DHCP Options Set to associate to the VPC.
        """
        return pulumi.get(self, "dhcp_options_id")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        The ID of the VPC to which we would like to associate a DHCP Options Set.
        """
        return pulumi.get(self, "vpc_id")

