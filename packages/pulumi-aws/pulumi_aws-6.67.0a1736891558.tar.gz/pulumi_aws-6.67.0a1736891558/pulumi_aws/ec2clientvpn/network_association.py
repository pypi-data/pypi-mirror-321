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

__all__ = ['NetworkAssociationArgs', 'NetworkAssociation']

@pulumi.input_type
class NetworkAssociationArgs:
    def __init__(__self__, *,
                 client_vpn_endpoint_id: pulumi.Input[str],
                 subnet_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a NetworkAssociation resource.
        :param pulumi.Input[str] client_vpn_endpoint_id: The ID of the Client VPN endpoint.
        :param pulumi.Input[str] subnet_id: The ID of the subnet to associate with the Client VPN endpoint.
        """
        pulumi.set(__self__, "client_vpn_endpoint_id", client_vpn_endpoint_id)
        pulumi.set(__self__, "subnet_id", subnet_id)

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
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        The ID of the subnet to associate with the Client VPN endpoint.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)


@pulumi.input_type
class _NetworkAssociationState:
    def __init__(__self__, *,
                 association_id: Optional[pulumi.Input[str]] = None,
                 client_vpn_endpoint_id: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering NetworkAssociation resources.
        :param pulumi.Input[str] association_id: The unique ID of the target network association.
        :param pulumi.Input[str] client_vpn_endpoint_id: The ID of the Client VPN endpoint.
        :param pulumi.Input[str] subnet_id: The ID of the subnet to associate with the Client VPN endpoint.
        :param pulumi.Input[str] vpc_id: The ID of the VPC in which the target subnet is located.
        """
        if association_id is not None:
            pulumi.set(__self__, "association_id", association_id)
        if client_vpn_endpoint_id is not None:
            pulumi.set(__self__, "client_vpn_endpoint_id", client_vpn_endpoint_id)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="associationId")
    def association_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique ID of the target network association.
        """
        return pulumi.get(self, "association_id")

    @association_id.setter
    def association_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "association_id", value)

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
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the subnet to associate with the Client VPN endpoint.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the VPC in which the target subnet is located.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


class NetworkAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_vpn_endpoint_id: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides network associations for AWS Client VPN endpoints. For more information on usage, please see the
        [AWS Client VPN Administrator's Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2clientvpn.NetworkAssociation("example",
            client_vpn_endpoint_id=example_aws_ec2_client_vpn_endpoint["id"],
            subnet_id=example_aws_subnet["id"])
        ```

        ## Import

        Using `pulumi import`, import AWS Client VPN network associations using the endpoint ID and the association ID. Values are separated by a `,`. For example:

        ```sh
        $ pulumi import aws:ec2clientvpn/networkAssociation:NetworkAssociation example cvpn-endpoint-0ac3a1abbccddd666,cvpn-assoc-0b8db902465d069ad
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_vpn_endpoint_id: The ID of the Client VPN endpoint.
        :param pulumi.Input[str] subnet_id: The ID of the subnet to associate with the Client VPN endpoint.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides network associations for AWS Client VPN endpoints. For more information on usage, please see the
        [AWS Client VPN Administrator's Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2clientvpn.NetworkAssociation("example",
            client_vpn_endpoint_id=example_aws_ec2_client_vpn_endpoint["id"],
            subnet_id=example_aws_subnet["id"])
        ```

        ## Import

        Using `pulumi import`, import AWS Client VPN network associations using the endpoint ID and the association ID. Values are separated by a `,`. For example:

        ```sh
        $ pulumi import aws:ec2clientvpn/networkAssociation:NetworkAssociation example cvpn-endpoint-0ac3a1abbccddd666,cvpn-assoc-0b8db902465d069ad
        ```

        :param str resource_name: The name of the resource.
        :param NetworkAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_vpn_endpoint_id: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkAssociationArgs.__new__(NetworkAssociationArgs)

            if client_vpn_endpoint_id is None and not opts.urn:
                raise TypeError("Missing required property 'client_vpn_endpoint_id'")
            __props__.__dict__["client_vpn_endpoint_id"] = client_vpn_endpoint_id
            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__.__dict__["subnet_id"] = subnet_id
            __props__.__dict__["association_id"] = None
            __props__.__dict__["vpc_id"] = None
        super(NetworkAssociation, __self__).__init__(
            'aws:ec2clientvpn/networkAssociation:NetworkAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            association_id: Optional[pulumi.Input[str]] = None,
            client_vpn_endpoint_id: Optional[pulumi.Input[str]] = None,
            subnet_id: Optional[pulumi.Input[str]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None) -> 'NetworkAssociation':
        """
        Get an existing NetworkAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] association_id: The unique ID of the target network association.
        :param pulumi.Input[str] client_vpn_endpoint_id: The ID of the Client VPN endpoint.
        :param pulumi.Input[str] subnet_id: The ID of the subnet to associate with the Client VPN endpoint.
        :param pulumi.Input[str] vpc_id: The ID of the VPC in which the target subnet is located.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NetworkAssociationState.__new__(_NetworkAssociationState)

        __props__.__dict__["association_id"] = association_id
        __props__.__dict__["client_vpn_endpoint_id"] = client_vpn_endpoint_id
        __props__.__dict__["subnet_id"] = subnet_id
        __props__.__dict__["vpc_id"] = vpc_id
        return NetworkAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="associationId")
    def association_id(self) -> pulumi.Output[str]:
        """
        The unique ID of the target network association.
        """
        return pulumi.get(self, "association_id")

    @property
    @pulumi.getter(name="clientVpnEndpointId")
    def client_vpn_endpoint_id(self) -> pulumi.Output[str]:
        """
        The ID of the Client VPN endpoint.
        """
        return pulumi.get(self, "client_vpn_endpoint_id")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        The ID of the subnet to associate with the Client VPN endpoint.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        The ID of the VPC in which the target subnet is located.
        """
        return pulumi.get(self, "vpc_id")

