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

__all__ = [
    'GetDedicatedIpPoolResult',
    'AwaitableGetDedicatedIpPoolResult',
    'get_dedicated_ip_pool',
    'get_dedicated_ip_pool_output',
]

@pulumi.output_type
class GetDedicatedIpPoolResult:
    """
    A collection of values returned by getDedicatedIpPool.
    """
    def __init__(__self__, arn=None, dedicated_ips=None, id=None, pool_name=None, scaling_mode=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if dedicated_ips and not isinstance(dedicated_ips, list):
            raise TypeError("Expected argument 'dedicated_ips' to be a list")
        pulumi.set(__self__, "dedicated_ips", dedicated_ips)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if pool_name and not isinstance(pool_name, str):
            raise TypeError("Expected argument 'pool_name' to be a str")
        pulumi.set(__self__, "pool_name", pool_name)
        if scaling_mode and not isinstance(scaling_mode, str):
            raise TypeError("Expected argument 'scaling_mode' to be a str")
        pulumi.set(__self__, "scaling_mode", scaling_mode)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the Dedicated IP Pool.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="dedicatedIps")
    def dedicated_ips(self) -> Sequence['outputs.GetDedicatedIpPoolDedicatedIpResult']:
        """
        A list of objects describing the pool's dedicated IP's. See `dedicated_ips`.
        """
        return pulumi.get(self, "dedicated_ips")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> str:
        return pulumi.get(self, "pool_name")

    @property
    @pulumi.getter(name="scalingMode")
    def scaling_mode(self) -> str:
        """
        (Optional) IP pool scaling mode. Valid values: `STANDARD`, `MANAGED`.
        """
        return pulumi.get(self, "scaling_mode")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A map of tags attached to the pool.
        """
        return pulumi.get(self, "tags")


class AwaitableGetDedicatedIpPoolResult(GetDedicatedIpPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDedicatedIpPoolResult(
            arn=self.arn,
            dedicated_ips=self.dedicated_ips,
            id=self.id,
            pool_name=self.pool_name,
            scaling_mode=self.scaling_mode,
            tags=self.tags)


def get_dedicated_ip_pool(pool_name: Optional[str] = None,
                          tags: Optional[Mapping[str, str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDedicatedIpPoolResult:
    """
    Data source for managing an AWS SESv2 (Simple Email V2) Dedicated IP Pool.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.sesv2.get_dedicated_ip_pool(pool_name="my-pool")
    ```


    :param str pool_name: Name of the dedicated IP pool.
    :param Mapping[str, str] tags: A map of tags attached to the pool.
    """
    __args__ = dict()
    __args__['poolName'] = pool_name
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:sesv2/getDedicatedIpPool:getDedicatedIpPool', __args__, opts=opts, typ=GetDedicatedIpPoolResult).value

    return AwaitableGetDedicatedIpPoolResult(
        arn=pulumi.get(__ret__, 'arn'),
        dedicated_ips=pulumi.get(__ret__, 'dedicated_ips'),
        id=pulumi.get(__ret__, 'id'),
        pool_name=pulumi.get(__ret__, 'pool_name'),
        scaling_mode=pulumi.get(__ret__, 'scaling_mode'),
        tags=pulumi.get(__ret__, 'tags'))
def get_dedicated_ip_pool_output(pool_name: Optional[pulumi.Input[str]] = None,
                                 tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                 opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDedicatedIpPoolResult]:
    """
    Data source for managing an AWS SESv2 (Simple Email V2) Dedicated IP Pool.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.sesv2.get_dedicated_ip_pool(pool_name="my-pool")
    ```


    :param str pool_name: Name of the dedicated IP pool.
    :param Mapping[str, str] tags: A map of tags attached to the pool.
    """
    __args__ = dict()
    __args__['poolName'] = pool_name
    __args__['tags'] = tags
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:sesv2/getDedicatedIpPool:getDedicatedIpPool', __args__, opts=opts, typ=GetDedicatedIpPoolResult)
    return __ret__.apply(lambda __response__: GetDedicatedIpPoolResult(
        arn=pulumi.get(__response__, 'arn'),
        dedicated_ips=pulumi.get(__response__, 'dedicated_ips'),
        id=pulumi.get(__response__, 'id'),
        pool_name=pulumi.get(__response__, 'pool_name'),
        scaling_mode=pulumi.get(__response__, 'scaling_mode'),
        tags=pulumi.get(__response__, 'tags')))
