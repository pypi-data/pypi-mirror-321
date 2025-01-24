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
    'GetVpcIamPoolsResult',
    'AwaitableGetVpcIamPoolsResult',
    'get_vpc_iam_pools',
    'get_vpc_iam_pools_output',
]

warnings.warn("""aws.ec2/getvpciampools.getVpcIamPools has been deprecated in favor of aws.ec2/getvpcipampools.getVpcIpamPools""", DeprecationWarning)

@pulumi.output_type
class GetVpcIamPoolsResult:
    """
    A collection of values returned by getVpcIamPools.
    """
    def __init__(__self__, filters=None, id=None, ipam_pools=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipam_pools and not isinstance(ipam_pools, list):
            raise TypeError("Expected argument 'ipam_pools' to be a list")
        pulumi.set(__self__, "ipam_pools", ipam_pools)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetVpcIamPoolsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipamPools")
    def ipam_pools(self) -> Sequence['outputs.GetVpcIamPoolsIpamPoolResult']:
        """
        List of IPAM pools and their attributes. See below for details
        """
        return pulumi.get(self, "ipam_pools")


class AwaitableGetVpcIamPoolsResult(GetVpcIamPoolsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcIamPoolsResult(
            filters=self.filters,
            id=self.id,
            ipam_pools=self.ipam_pools)


def get_vpc_iam_pools(filters: Optional[Sequence[Union['GetVpcIamPoolsFilterArgs', 'GetVpcIamPoolsFilterArgsDict']]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpcIamPoolsResult:
    """
    `ec2_get_vpc_ipam_pools` provides details about IPAM pools.

    This resource can prove useful when IPAM pools are created in another root
    module and you need the pool ids as input variables. For example, pools
    can be shared via RAM and used to create vpcs with CIDRs from that pool.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    test = aws.ec2.get_vpc_ipam_pools(filters=[
        {
            "name": "description",
            "values": ["*test*"],
        },
        {
            "name": "address-family",
            "values": ["ipv4"],
        },
    ])
    ```


    :param Sequence[Union['GetVpcIamPoolsFilterArgs', 'GetVpcIamPoolsFilterArgsDict']] filters: Custom filter block as described below.
    """
    pulumi.log.warn("""get_vpc_iam_pools is deprecated: aws.ec2/getvpciampools.getVpcIamPools has been deprecated in favor of aws.ec2/getvpcipampools.getVpcIpamPools""")
    __args__ = dict()
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:ec2/getVpcIamPools:getVpcIamPools', __args__, opts=opts, typ=GetVpcIamPoolsResult).value

    return AwaitableGetVpcIamPoolsResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        ipam_pools=pulumi.get(__ret__, 'ipam_pools'))
def get_vpc_iam_pools_output(filters: Optional[pulumi.Input[Optional[Sequence[Union['GetVpcIamPoolsFilterArgs', 'GetVpcIamPoolsFilterArgsDict']]]]] = None,
                             opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetVpcIamPoolsResult]:
    """
    `ec2_get_vpc_ipam_pools` provides details about IPAM pools.

    This resource can prove useful when IPAM pools are created in another root
    module and you need the pool ids as input variables. For example, pools
    can be shared via RAM and used to create vpcs with CIDRs from that pool.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    test = aws.ec2.get_vpc_ipam_pools(filters=[
        {
            "name": "description",
            "values": ["*test*"],
        },
        {
            "name": "address-family",
            "values": ["ipv4"],
        },
    ])
    ```


    :param Sequence[Union['GetVpcIamPoolsFilterArgs', 'GetVpcIamPoolsFilterArgsDict']] filters: Custom filter block as described below.
    """
    pulumi.log.warn("""get_vpc_iam_pools is deprecated: aws.ec2/getvpciampools.getVpcIamPools has been deprecated in favor of aws.ec2/getvpcipampools.getVpcIpamPools""")
    __args__ = dict()
    __args__['filters'] = filters
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:ec2/getVpcIamPools:getVpcIamPools', __args__, opts=opts, typ=GetVpcIamPoolsResult)
    return __ret__.apply(lambda __response__: GetVpcIamPoolsResult(
        filters=pulumi.get(__response__, 'filters'),
        id=pulumi.get(__response__, 'id'),
        ipam_pools=pulumi.get(__response__, 'ipam_pools')))
