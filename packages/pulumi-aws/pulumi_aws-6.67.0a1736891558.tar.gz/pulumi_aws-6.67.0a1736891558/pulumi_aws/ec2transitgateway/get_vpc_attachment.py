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

__all__ = [
    'GetVpcAttachmentResult',
    'AwaitableGetVpcAttachmentResult',
    'get_vpc_attachment',
    'get_vpc_attachment_output',
]

@pulumi.output_type
class GetVpcAttachmentResult:
    """
    A collection of values returned by getVpcAttachment.
    """
    def __init__(__self__, appliance_mode_support=None, dns_support=None, filters=None, id=None, ipv6_support=None, security_group_referencing_support=None, subnet_ids=None, tags=None, transit_gateway_id=None, vpc_id=None, vpc_owner_id=None):
        if appliance_mode_support and not isinstance(appliance_mode_support, str):
            raise TypeError("Expected argument 'appliance_mode_support' to be a str")
        pulumi.set(__self__, "appliance_mode_support", appliance_mode_support)
        if dns_support and not isinstance(dns_support, str):
            raise TypeError("Expected argument 'dns_support' to be a str")
        pulumi.set(__self__, "dns_support", dns_support)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipv6_support and not isinstance(ipv6_support, str):
            raise TypeError("Expected argument 'ipv6_support' to be a str")
        pulumi.set(__self__, "ipv6_support", ipv6_support)
        if security_group_referencing_support and not isinstance(security_group_referencing_support, str):
            raise TypeError("Expected argument 'security_group_referencing_support' to be a str")
        pulumi.set(__self__, "security_group_referencing_support", security_group_referencing_support)
        if subnet_ids and not isinstance(subnet_ids, list):
            raise TypeError("Expected argument 'subnet_ids' to be a list")
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if transit_gateway_id and not isinstance(transit_gateway_id, str):
            raise TypeError("Expected argument 'transit_gateway_id' to be a str")
        pulumi.set(__self__, "transit_gateway_id", transit_gateway_id)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)
        if vpc_owner_id and not isinstance(vpc_owner_id, str):
            raise TypeError("Expected argument 'vpc_owner_id' to be a str")
        pulumi.set(__self__, "vpc_owner_id", vpc_owner_id)

    @property
    @pulumi.getter(name="applianceModeSupport")
    def appliance_mode_support(self) -> str:
        """
        Whether Appliance Mode support is enabled.
        """
        return pulumi.get(self, "appliance_mode_support")

    @property
    @pulumi.getter(name="dnsSupport")
    def dns_support(self) -> str:
        """
        Whether DNS support is enabled.
        """
        return pulumi.get(self, "dns_support")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetVpcAttachmentFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        EC2 Transit Gateway VPC Attachment identifier
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipv6Support")
    def ipv6_support(self) -> str:
        """
        Whether IPv6 support is enabled.
        """
        return pulumi.get(self, "ipv6_support")

    @property
    @pulumi.getter(name="securityGroupReferencingSupport")
    def security_group_referencing_support(self) -> str:
        """
        Whether Security Group Referencing Support is enabled.
        """
        return pulumi.get(self, "security_group_referencing_support")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[str]:
        """
        Identifiers of EC2 Subnets.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Key-value tags for the EC2 Transit Gateway VPC Attachment
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> str:
        """
        EC2 Transit Gateway identifier
        """
        return pulumi.get(self, "transit_gateway_id")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        Identifier of EC2 VPC.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="vpcOwnerId")
    def vpc_owner_id(self) -> str:
        """
        Identifier of the AWS account that owns the EC2 VPC.
        """
        return pulumi.get(self, "vpc_owner_id")


class AwaitableGetVpcAttachmentResult(GetVpcAttachmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcAttachmentResult(
            appliance_mode_support=self.appliance_mode_support,
            dns_support=self.dns_support,
            filters=self.filters,
            id=self.id,
            ipv6_support=self.ipv6_support,
            security_group_referencing_support=self.security_group_referencing_support,
            subnet_ids=self.subnet_ids,
            tags=self.tags,
            transit_gateway_id=self.transit_gateway_id,
            vpc_id=self.vpc_id,
            vpc_owner_id=self.vpc_owner_id)


def get_vpc_attachment(filters: Optional[Sequence[Union['GetVpcAttachmentFilterArgs', 'GetVpcAttachmentFilterArgsDict']]] = None,
                       id: Optional[str] = None,
                       tags: Optional[Mapping[str, str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpcAttachmentResult:
    """
    Get information on an EC2 Transit Gateway VPC Attachment.

    ## Example Usage

    ### By Filter

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2transitgateway.get_vpc_attachment(filters=[{
        "name": "vpc-id",
        "values": ["vpc-12345678"],
    }])
    ```

    ### By Identifier

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2transitgateway.get_vpc_attachment(id="tgw-attach-12345678")
    ```


    :param Sequence[Union['GetVpcAttachmentFilterArgs', 'GetVpcAttachmentFilterArgsDict']] filters: One or more configuration blocks containing name-values filters. Detailed below.
    :param str id: Identifier of the EC2 Transit Gateway VPC Attachment.
    :param Mapping[str, str] tags: Key-value tags for the EC2 Transit Gateway VPC Attachment
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:ec2transitgateway/getVpcAttachment:getVpcAttachment', __args__, opts=opts, typ=GetVpcAttachmentResult).value

    return AwaitableGetVpcAttachmentResult(
        appliance_mode_support=pulumi.get(__ret__, 'appliance_mode_support'),
        dns_support=pulumi.get(__ret__, 'dns_support'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        ipv6_support=pulumi.get(__ret__, 'ipv6_support'),
        security_group_referencing_support=pulumi.get(__ret__, 'security_group_referencing_support'),
        subnet_ids=pulumi.get(__ret__, 'subnet_ids'),
        tags=pulumi.get(__ret__, 'tags'),
        transit_gateway_id=pulumi.get(__ret__, 'transit_gateway_id'),
        vpc_id=pulumi.get(__ret__, 'vpc_id'),
        vpc_owner_id=pulumi.get(__ret__, 'vpc_owner_id'))
def get_vpc_attachment_output(filters: Optional[pulumi.Input[Optional[Sequence[Union['GetVpcAttachmentFilterArgs', 'GetVpcAttachmentFilterArgsDict']]]]] = None,
                              id: Optional[pulumi.Input[Optional[str]]] = None,
                              tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                              opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetVpcAttachmentResult]:
    """
    Get information on an EC2 Transit Gateway VPC Attachment.

    ## Example Usage

    ### By Filter

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2transitgateway.get_vpc_attachment(filters=[{
        "name": "vpc-id",
        "values": ["vpc-12345678"],
    }])
    ```

    ### By Identifier

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2transitgateway.get_vpc_attachment(id="tgw-attach-12345678")
    ```


    :param Sequence[Union['GetVpcAttachmentFilterArgs', 'GetVpcAttachmentFilterArgsDict']] filters: One or more configuration blocks containing name-values filters. Detailed below.
    :param str id: Identifier of the EC2 Transit Gateway VPC Attachment.
    :param Mapping[str, str] tags: Key-value tags for the EC2 Transit Gateway VPC Attachment
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['tags'] = tags
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:ec2transitgateway/getVpcAttachment:getVpcAttachment', __args__, opts=opts, typ=GetVpcAttachmentResult)
    return __ret__.apply(lambda __response__: GetVpcAttachmentResult(
        appliance_mode_support=pulumi.get(__response__, 'appliance_mode_support'),
        dns_support=pulumi.get(__response__, 'dns_support'),
        filters=pulumi.get(__response__, 'filters'),
        id=pulumi.get(__response__, 'id'),
        ipv6_support=pulumi.get(__response__, 'ipv6_support'),
        security_group_referencing_support=pulumi.get(__response__, 'security_group_referencing_support'),
        subnet_ids=pulumi.get(__response__, 'subnet_ids'),
        tags=pulumi.get(__response__, 'tags'),
        transit_gateway_id=pulumi.get(__response__, 'transit_gateway_id'),
        vpc_id=pulumi.get(__response__, 'vpc_id'),
        vpc_owner_id=pulumi.get(__response__, 'vpc_owner_id')))
