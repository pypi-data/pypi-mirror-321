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

__all__ = ['TransitGatewayRegistrationArgs', 'TransitGatewayRegistration']

@pulumi.input_type
class TransitGatewayRegistrationArgs:
    def __init__(__self__, *,
                 global_network_id: pulumi.Input[str],
                 transit_gateway_arn: pulumi.Input[str]):
        """
        The set of arguments for constructing a TransitGatewayRegistration resource.
        :param pulumi.Input[str] global_network_id: The ID of the Global Network to register to.
        :param pulumi.Input[str] transit_gateway_arn: The ARN of the Transit Gateway to register.
        """
        pulumi.set(__self__, "global_network_id", global_network_id)
        pulumi.set(__self__, "transit_gateway_arn", transit_gateway_arn)

    @property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> pulumi.Input[str]:
        """
        The ID of the Global Network to register to.
        """
        return pulumi.get(self, "global_network_id")

    @global_network_id.setter
    def global_network_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "global_network_id", value)

    @property
    @pulumi.getter(name="transitGatewayArn")
    def transit_gateway_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the Transit Gateway to register.
        """
        return pulumi.get(self, "transit_gateway_arn")

    @transit_gateway_arn.setter
    def transit_gateway_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "transit_gateway_arn", value)


@pulumi.input_type
class _TransitGatewayRegistrationState:
    def __init__(__self__, *,
                 global_network_id: Optional[pulumi.Input[str]] = None,
                 transit_gateway_arn: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TransitGatewayRegistration resources.
        :param pulumi.Input[str] global_network_id: The ID of the Global Network to register to.
        :param pulumi.Input[str] transit_gateway_arn: The ARN of the Transit Gateway to register.
        """
        if global_network_id is not None:
            pulumi.set(__self__, "global_network_id", global_network_id)
        if transit_gateway_arn is not None:
            pulumi.set(__self__, "transit_gateway_arn", transit_gateway_arn)

    @property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Global Network to register to.
        """
        return pulumi.get(self, "global_network_id")

    @global_network_id.setter
    def global_network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "global_network_id", value)

    @property
    @pulumi.getter(name="transitGatewayArn")
    def transit_gateway_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the Transit Gateway to register.
        """
        return pulumi.get(self, "transit_gateway_arn")

    @transit_gateway_arn.setter
    def transit_gateway_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transit_gateway_arn", value)


class TransitGatewayRegistration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 global_network_id: Optional[pulumi.Input[str]] = None,
                 transit_gateway_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Registers a transit gateway to a global network. The transit gateway can be in any AWS Region,
        but it must be owned by the same AWS account that owns the global network.
        You cannot register a transit gateway in more than one global network.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.networkmanager.GlobalNetwork("example", description="example")
        example_transit_gateway = aws.ec2transitgateway.TransitGateway("example")
        example_transit_gateway_registration = aws.networkmanager.TransitGatewayRegistration("example",
            global_network_id=example.id,
            transit_gateway_arn=example_transit_gateway.arn)
        ```

        ## Import

        Using `pulumi import`, import `aws_networkmanager_transit_gateway_registration` using the global network ID and transit gateway ARN. For example:

        ```sh
        $ pulumi import aws:networkmanager/transitGatewayRegistration:TransitGatewayRegistration example global-network-0d47f6t230mz46dy4,arn:aws:ec2:us-west-2:123456789012:transit-gateway/tgw-123abc05e04123abc
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] global_network_id: The ID of the Global Network to register to.
        :param pulumi.Input[str] transit_gateway_arn: The ARN of the Transit Gateway to register.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TransitGatewayRegistrationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Registers a transit gateway to a global network. The transit gateway can be in any AWS Region,
        but it must be owned by the same AWS account that owns the global network.
        You cannot register a transit gateway in more than one global network.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.networkmanager.GlobalNetwork("example", description="example")
        example_transit_gateway = aws.ec2transitgateway.TransitGateway("example")
        example_transit_gateway_registration = aws.networkmanager.TransitGatewayRegistration("example",
            global_network_id=example.id,
            transit_gateway_arn=example_transit_gateway.arn)
        ```

        ## Import

        Using `pulumi import`, import `aws_networkmanager_transit_gateway_registration` using the global network ID and transit gateway ARN. For example:

        ```sh
        $ pulumi import aws:networkmanager/transitGatewayRegistration:TransitGatewayRegistration example global-network-0d47f6t230mz46dy4,arn:aws:ec2:us-west-2:123456789012:transit-gateway/tgw-123abc05e04123abc
        ```

        :param str resource_name: The name of the resource.
        :param TransitGatewayRegistrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TransitGatewayRegistrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 global_network_id: Optional[pulumi.Input[str]] = None,
                 transit_gateway_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TransitGatewayRegistrationArgs.__new__(TransitGatewayRegistrationArgs)

            if global_network_id is None and not opts.urn:
                raise TypeError("Missing required property 'global_network_id'")
            __props__.__dict__["global_network_id"] = global_network_id
            if transit_gateway_arn is None and not opts.urn:
                raise TypeError("Missing required property 'transit_gateway_arn'")
            __props__.__dict__["transit_gateway_arn"] = transit_gateway_arn
        super(TransitGatewayRegistration, __self__).__init__(
            'aws:networkmanager/transitGatewayRegistration:TransitGatewayRegistration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            global_network_id: Optional[pulumi.Input[str]] = None,
            transit_gateway_arn: Optional[pulumi.Input[str]] = None) -> 'TransitGatewayRegistration':
        """
        Get an existing TransitGatewayRegistration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] global_network_id: The ID of the Global Network to register to.
        :param pulumi.Input[str] transit_gateway_arn: The ARN of the Transit Gateway to register.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TransitGatewayRegistrationState.__new__(_TransitGatewayRegistrationState)

        __props__.__dict__["global_network_id"] = global_network_id
        __props__.__dict__["transit_gateway_arn"] = transit_gateway_arn
        return TransitGatewayRegistration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> pulumi.Output[str]:
        """
        The ID of the Global Network to register to.
        """
        return pulumi.get(self, "global_network_id")

    @property
    @pulumi.getter(name="transitGatewayArn")
    def transit_gateway_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the Transit Gateway to register.
        """
        return pulumi.get(self, "transit_gateway_arn")

