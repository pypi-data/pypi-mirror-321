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
    'GetVpcIpamPoolCidrsResult',
    'AwaitableGetVpcIpamPoolCidrsResult',
    'get_vpc_ipam_pool_cidrs',
    'get_vpc_ipam_pool_cidrs_output',
]

@pulumi.output_type
class GetVpcIpamPoolCidrsResult:
    """
    A collection of values returned by getVpcIpamPoolCidrs.
    """
    def __init__(__self__, filters=None, id=None, ipam_pool_cidrs=None, ipam_pool_id=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipam_pool_cidrs and not isinstance(ipam_pool_cidrs, list):
            raise TypeError("Expected argument 'ipam_pool_cidrs' to be a list")
        pulumi.set(__self__, "ipam_pool_cidrs", ipam_pool_cidrs)
        if ipam_pool_id and not isinstance(ipam_pool_id, str):
            raise TypeError("Expected argument 'ipam_pool_id' to be a str")
        pulumi.set(__self__, "ipam_pool_id", ipam_pool_id)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetVpcIpamPoolCidrsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipamPoolCidrs")
    def ipam_pool_cidrs(self) -> Sequence['outputs.GetVpcIpamPoolCidrsIpamPoolCidrResult']:
        """
        The CIDRs provisioned into the IPAM pool, described below.
        """
        return pulumi.get(self, "ipam_pool_cidrs")

    @property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> str:
        return pulumi.get(self, "ipam_pool_id")


class AwaitableGetVpcIpamPoolCidrsResult(GetVpcIpamPoolCidrsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcIpamPoolCidrsResult(
            filters=self.filters,
            id=self.id,
            ipam_pool_cidrs=self.ipam_pool_cidrs,
            ipam_pool_id=self.ipam_pool_id)


def get_vpc_ipam_pool_cidrs(filters: Optional[Sequence[Union['GetVpcIpamPoolCidrsFilterArgs', 'GetVpcIpamPoolCidrsFilterArgsDict']]] = None,
                            ipam_pool_id: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpcIpamPoolCidrsResult:
    """
    `ec2_get_vpc_ipam_pool_cidrs` provides details about an IPAM pool.

    This resource can prove useful when an ipam pool was shared to your account and you want to know all (or a filtered list) of the CIDRs that are provisioned into the pool.

    ## Example Usage

    Basic usage:

    ```python
    import pulumi
    import pulumi_aws as aws

    p = aws.ec2.get_vpc_ipam_pool(filters=[
        {
            "name": "description",
            "values": ["*mypool*"],
        },
        {
            "name": "address-family",
            "values": ["ipv4"],
        },
    ])
    c = aws.ec2.get_vpc_ipam_pool_cidrs(ipam_pool_id=p.id)
    ```

    Filtering:

    ```python
    import pulumi
    import pulumi_aws as aws

    c = aws.ec2.get_vpc_ipam_pool_cidrs(ipam_pool_id="ipam-pool-123",
        filters=[{
            "name": "cidr",
            "values": ["10.*"],
        }])
    mycidrs = [cidr.cidr for cidr in c.ipam_pool_cidrs if cidr.state == "provisioned"]
    pls = aws.ec2.ManagedPrefixList("pls",
        entries=[{
            "cidr": entry["value"],
            "description": entry["value"],
        } for entry in [{"key": k, "value": v} for k, v in mycidrs]],
        name=f"IPAM Pool ({test['id']}) Cidrs",
        address_family="IPv4",
        max_entries=len(mycidrs))
    ```


    :param Sequence[Union['GetVpcIpamPoolCidrsFilterArgs', 'GetVpcIpamPoolCidrsFilterArgsDict']] filters: Custom filter block as described below.
    :param str ipam_pool_id: ID of the IPAM pool you would like the list of provisioned CIDRs.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['ipamPoolId'] = ipam_pool_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:ec2/getVpcIpamPoolCidrs:getVpcIpamPoolCidrs', __args__, opts=opts, typ=GetVpcIpamPoolCidrsResult).value

    return AwaitableGetVpcIpamPoolCidrsResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        ipam_pool_cidrs=pulumi.get(__ret__, 'ipam_pool_cidrs'),
        ipam_pool_id=pulumi.get(__ret__, 'ipam_pool_id'))
def get_vpc_ipam_pool_cidrs_output(filters: Optional[pulumi.Input[Optional[Sequence[Union['GetVpcIpamPoolCidrsFilterArgs', 'GetVpcIpamPoolCidrsFilterArgsDict']]]]] = None,
                                   ipam_pool_id: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetVpcIpamPoolCidrsResult]:
    """
    `ec2_get_vpc_ipam_pool_cidrs` provides details about an IPAM pool.

    This resource can prove useful when an ipam pool was shared to your account and you want to know all (or a filtered list) of the CIDRs that are provisioned into the pool.

    ## Example Usage

    Basic usage:

    ```python
    import pulumi
    import pulumi_aws as aws

    p = aws.ec2.get_vpc_ipam_pool(filters=[
        {
            "name": "description",
            "values": ["*mypool*"],
        },
        {
            "name": "address-family",
            "values": ["ipv4"],
        },
    ])
    c = aws.ec2.get_vpc_ipam_pool_cidrs(ipam_pool_id=p.id)
    ```

    Filtering:

    ```python
    import pulumi
    import pulumi_aws as aws

    c = aws.ec2.get_vpc_ipam_pool_cidrs(ipam_pool_id="ipam-pool-123",
        filters=[{
            "name": "cidr",
            "values": ["10.*"],
        }])
    mycidrs = [cidr.cidr for cidr in c.ipam_pool_cidrs if cidr.state == "provisioned"]
    pls = aws.ec2.ManagedPrefixList("pls",
        entries=[{
            "cidr": entry["value"],
            "description": entry["value"],
        } for entry in [{"key": k, "value": v} for k, v in mycidrs]],
        name=f"IPAM Pool ({test['id']}) Cidrs",
        address_family="IPv4",
        max_entries=len(mycidrs))
    ```


    :param Sequence[Union['GetVpcIpamPoolCidrsFilterArgs', 'GetVpcIpamPoolCidrsFilterArgsDict']] filters: Custom filter block as described below.
    :param str ipam_pool_id: ID of the IPAM pool you would like the list of provisioned CIDRs.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['ipamPoolId'] = ipam_pool_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:ec2/getVpcIpamPoolCidrs:getVpcIpamPoolCidrs', __args__, opts=opts, typ=GetVpcIpamPoolCidrsResult)
    return __ret__.apply(lambda __response__: GetVpcIpamPoolCidrsResult(
        filters=pulumi.get(__response__, 'filters'),
        id=pulumi.get(__response__, 'id'),
        ipam_pool_cidrs=pulumi.get(__response__, 'ipam_pool_cidrs'),
        ipam_pool_id=pulumi.get(__response__, 'ipam_pool_id')))
