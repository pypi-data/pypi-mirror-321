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

__all__ = ['RouteArgs', 'Route']

@pulumi.input_type
class RouteArgs:
    def __init__(__self__, *,
                 client_vpn_endpoint_id: pulumi.Input[str],
                 destination_cidr_block: pulumi.Input[str],
                 target_vpc_subnet_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Route resource.
        :param pulumi.Input[str] client_vpn_endpoint_id: The ID of the Client VPN endpoint.
        :param pulumi.Input[str] destination_cidr_block: The IPv4 address range, in CIDR notation, of the route destination.
        :param pulumi.Input[str] target_vpc_subnet_id: The ID of the Subnet to route the traffic through. It must already be attached to the Client VPN.
        :param pulumi.Input[str] description: A brief description of the route.
        """
        pulumi.set(__self__, "client_vpn_endpoint_id", client_vpn_endpoint_id)
        pulumi.set(__self__, "destination_cidr_block", destination_cidr_block)
        pulumi.set(__self__, "target_vpc_subnet_id", target_vpc_subnet_id)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="clientVpnEndpointId")
    def client_vpn_endpoint_id(self) -> pulumi.Input[str]:
        """
        The ID of the Client VPN endpoint.
        """
        return pulumi.get(self, "client_vpn_endpoint_id")

    @client_vpn_endpoint_id.setter
    def client_vpn_endpoint_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_vpn_endpoint_id", value)

    @property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> pulumi.Input[str]:
        """
        The IPv4 address range, in CIDR notation, of the route destination.
        """
        return pulumi.get(self, "destination_cidr_block")

    @destination_cidr_block.setter
    def destination_cidr_block(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination_cidr_block", value)

    @property
    @pulumi.getter(name="targetVpcSubnetId")
    def target_vpc_subnet_id(self) -> pulumi.Input[str]:
        """
        The ID of the Subnet to route the traffic through. It must already be attached to the Client VPN.
        """
        return pulumi.get(self, "target_vpc_subnet_id")

    @target_vpc_subnet_id.setter
    def target_vpc_subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_vpc_subnet_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A brief description of the route.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class _RouteState:
    def __init__(__self__, *,
                 client_vpn_endpoint_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_cidr_block: Optional[pulumi.Input[str]] = None,
                 origin: Optional[pulumi.Input[str]] = None,
                 target_vpc_subnet_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Route resources.
        :param pulumi.Input[str] client_vpn_endpoint_id: The ID of the Client VPN endpoint.
        :param pulumi.Input[str] description: A brief description of the route.
        :param pulumi.Input[str] destination_cidr_block: The IPv4 address range, in CIDR notation, of the route destination.
        :param pulumi.Input[str] origin: Indicates how the Client VPN route was added. Will be `add-route` for routes created by this resource.
        :param pulumi.Input[str] target_vpc_subnet_id: The ID of the Subnet to route the traffic through. It must already be attached to the Client VPN.
        :param pulumi.Input[str] type: The type of the route.
        """
        if client_vpn_endpoint_id is not None:
            pulumi.set(__self__, "client_vpn_endpoint_id", client_vpn_endpoint_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if destination_cidr_block is not None:
            pulumi.set(__self__, "destination_cidr_block", destination_cidr_block)
        if origin is not None:
            pulumi.set(__self__, "origin", origin)
        if target_vpc_subnet_id is not None:
            pulumi.set(__self__, "target_vpc_subnet_id", target_vpc_subnet_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="clientVpnEndpointId")
    def client_vpn_endpoint_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Client VPN endpoint.
        """
        return pulumi.get(self, "client_vpn_endpoint_id")

    @client_vpn_endpoint_id.setter
    def client_vpn_endpoint_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_vpn_endpoint_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A brief description of the route.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 address range, in CIDR notation, of the route destination.
        """
        return pulumi.get(self, "destination_cidr_block")

    @destination_cidr_block.setter
    def destination_cidr_block(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_cidr_block", value)

    @property
    @pulumi.getter
    def origin(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates how the Client VPN route was added. Will be `add-route` for routes created by this resource.
        """
        return pulumi.get(self, "origin")

    @origin.setter
    def origin(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "origin", value)

    @property
    @pulumi.getter(name="targetVpcSubnetId")
    def target_vpc_subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Subnet to route the traffic through. It must already be attached to the Client VPN.
        """
        return pulumi.get(self, "target_vpc_subnet_id")

    @target_vpc_subnet_id.setter
    def target_vpc_subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_vpc_subnet_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the route.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Route(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_vpn_endpoint_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_cidr_block: Optional[pulumi.Input[str]] = None,
                 target_vpc_subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides additional routes for AWS Client VPN endpoints. For more information on usage, please see the
        [AWS Client VPN Administrator's Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_endpoint = aws.ec2clientvpn.Endpoint("example",
            description="Example Client VPN endpoint",
            server_certificate_arn=example_aws_acm_certificate["arn"],
            client_cidr_block="10.0.0.0/16",
            authentication_options=[{
                "type": "certificate-authentication",
                "root_certificate_chain_arn": example_aws_acm_certificate["arn"],
            }],
            connection_log_options={
                "enabled": False,
            })
        example_network_association = aws.ec2clientvpn.NetworkAssociation("example",
            client_vpn_endpoint_id=example_endpoint.id,
            subnet_id=example_aws_subnet["id"])
        example = aws.ec2clientvpn.Route("example",
            client_vpn_endpoint_id=example_endpoint.id,
            destination_cidr_block="0.0.0.0/0",
            target_vpc_subnet_id=example_network_association.subnet_id)
        ```

        ## Import

        Using `pulumi import`, import AWS Client VPN routes using the endpoint ID, target subnet ID, and destination CIDR block. All values are separated by a `,`. For example:

        ```sh
        $ pulumi import aws:ec2clientvpn/route:Route example cvpn-endpoint-1234567890abcdef,subnet-9876543210fedcba,10.1.0.0/24
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_vpn_endpoint_id: The ID of the Client VPN endpoint.
        :param pulumi.Input[str] description: A brief description of the route.
        :param pulumi.Input[str] destination_cidr_block: The IPv4 address range, in CIDR notation, of the route destination.
        :param pulumi.Input[str] target_vpc_subnet_id: The ID of the Subnet to route the traffic through. It must already be attached to the Client VPN.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RouteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides additional routes for AWS Client VPN endpoints. For more information on usage, please see the
        [AWS Client VPN Administrator's Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_endpoint = aws.ec2clientvpn.Endpoint("example",
            description="Example Client VPN endpoint",
            server_certificate_arn=example_aws_acm_certificate["arn"],
            client_cidr_block="10.0.0.0/16",
            authentication_options=[{
                "type": "certificate-authentication",
                "root_certificate_chain_arn": example_aws_acm_certificate["arn"],
            }],
            connection_log_options={
                "enabled": False,
            })
        example_network_association = aws.ec2clientvpn.NetworkAssociation("example",
            client_vpn_endpoint_id=example_endpoint.id,
            subnet_id=example_aws_subnet["id"])
        example = aws.ec2clientvpn.Route("example",
            client_vpn_endpoint_id=example_endpoint.id,
            destination_cidr_block="0.0.0.0/0",
            target_vpc_subnet_id=example_network_association.subnet_id)
        ```

        ## Import

        Using `pulumi import`, import AWS Client VPN routes using the endpoint ID, target subnet ID, and destination CIDR block. All values are separated by a `,`. For example:

        ```sh
        $ pulumi import aws:ec2clientvpn/route:Route example cvpn-endpoint-1234567890abcdef,subnet-9876543210fedcba,10.1.0.0/24
        ```

        :param str resource_name: The name of the resource.
        :param RouteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RouteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_vpn_endpoint_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_cidr_block: Optional[pulumi.Input[str]] = None,
                 target_vpc_subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RouteArgs.__new__(RouteArgs)

            if client_vpn_endpoint_id is None and not opts.urn:
                raise TypeError("Missing required property 'client_vpn_endpoint_id'")
            __props__.__dict__["client_vpn_endpoint_id"] = client_vpn_endpoint_id
            __props__.__dict__["description"] = description
            if destination_cidr_block is None and not opts.urn:
                raise TypeError("Missing required property 'destination_cidr_block'")
            __props__.__dict__["destination_cidr_block"] = destination_cidr_block
            if target_vpc_subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'target_vpc_subnet_id'")
            __props__.__dict__["target_vpc_subnet_id"] = target_vpc_subnet_id
            __props__.__dict__["origin"] = None
            __props__.__dict__["type"] = None
        super(Route, __self__).__init__(
            'aws:ec2clientvpn/route:Route',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            client_vpn_endpoint_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            destination_cidr_block: Optional[pulumi.Input[str]] = None,
            origin: Optional[pulumi.Input[str]] = None,
            target_vpc_subnet_id: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Route':
        """
        Get an existing Route resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_vpn_endpoint_id: The ID of the Client VPN endpoint.
        :param pulumi.Input[str] description: A brief description of the route.
        :param pulumi.Input[str] destination_cidr_block: The IPv4 address range, in CIDR notation, of the route destination.
        :param pulumi.Input[str] origin: Indicates how the Client VPN route was added. Will be `add-route` for routes created by this resource.
        :param pulumi.Input[str] target_vpc_subnet_id: The ID of the Subnet to route the traffic through. It must already be attached to the Client VPN.
        :param pulumi.Input[str] type: The type of the route.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RouteState.__new__(_RouteState)

        __props__.__dict__["client_vpn_endpoint_id"] = client_vpn_endpoint_id
        __props__.__dict__["description"] = description
        __props__.__dict__["destination_cidr_block"] = destination_cidr_block
        __props__.__dict__["origin"] = origin
        __props__.__dict__["target_vpc_subnet_id"] = target_vpc_subnet_id
        __props__.__dict__["type"] = type
        return Route(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientVpnEndpointId")
    def client_vpn_endpoint_id(self) -> pulumi.Output[str]:
        """
        The ID of the Client VPN endpoint.
        """
        return pulumi.get(self, "client_vpn_endpoint_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A brief description of the route.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> pulumi.Output[str]:
        """
        The IPv4 address range, in CIDR notation, of the route destination.
        """
        return pulumi.get(self, "destination_cidr_block")

    @property
    @pulumi.getter
    def origin(self) -> pulumi.Output[str]:
        """
        Indicates how the Client VPN route was added. Will be `add-route` for routes created by this resource.
        """
        return pulumi.get(self, "origin")

    @property
    @pulumi.getter(name="targetVpcSubnetId")
    def target_vpc_subnet_id(self) -> pulumi.Output[str]:
        """
        The ID of the Subnet to route the traffic through. It must already be attached to the Client VPN.
        """
        return pulumi.get(self, "target_vpc_subnet_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the route.
        """
        return pulumi.get(self, "type")

