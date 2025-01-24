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
    'GetRouteTableResult',
    'AwaitableGetRouteTableResult',
    'get_route_table',
    'get_route_table_output',
]

@pulumi.output_type
class GetRouteTableResult:
    """
    A collection of values returned by getRouteTable.
    """
    def __init__(__self__, arn=None, default_association_route_table=None, default_propagation_route_table=None, filters=None, id=None, tags=None, transit_gateway_id=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if default_association_route_table and not isinstance(default_association_route_table, bool):
            raise TypeError("Expected argument 'default_association_route_table' to be a bool")
        pulumi.set(__self__, "default_association_route_table", default_association_route_table)
        if default_propagation_route_table and not isinstance(default_propagation_route_table, bool):
            raise TypeError("Expected argument 'default_propagation_route_table' to be a bool")
        pulumi.set(__self__, "default_propagation_route_table", default_propagation_route_table)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if transit_gateway_id and not isinstance(transit_gateway_id, str):
            raise TypeError("Expected argument 'transit_gateway_id' to be a str")
        pulumi.set(__self__, "transit_gateway_id", transit_gateway_id)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        EC2 Transit Gateway Route Table ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="defaultAssociationRouteTable")
    def default_association_route_table(self) -> bool:
        """
        Boolean whether this is the default association route table for the EC2 Transit Gateway
        """
        return pulumi.get(self, "default_association_route_table")

    @property
    @pulumi.getter(name="defaultPropagationRouteTable")
    def default_propagation_route_table(self) -> bool:
        """
        Boolean whether this is the default propagation route table for the EC2 Transit Gateway
        """
        return pulumi.get(self, "default_propagation_route_table")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetRouteTableFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        EC2 Transit Gateway Route Table identifier
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Key-value tags for the EC2 Transit Gateway Route Table
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> str:
        """
        EC2 Transit Gateway identifier
        """
        return pulumi.get(self, "transit_gateway_id")


class AwaitableGetRouteTableResult(GetRouteTableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRouteTableResult(
            arn=self.arn,
            default_association_route_table=self.default_association_route_table,
            default_propagation_route_table=self.default_propagation_route_table,
            filters=self.filters,
            id=self.id,
            tags=self.tags,
            transit_gateway_id=self.transit_gateway_id)


def get_route_table(filters: Optional[Sequence[Union['GetRouteTableFilterArgs', 'GetRouteTableFilterArgsDict']]] = None,
                    id: Optional[str] = None,
                    tags: Optional[Mapping[str, str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRouteTableResult:
    """
    Get information on an EC2 Transit Gateway Route Table.

    ## Example Usage

    ### By Filter

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2transitgateway.get_route_table(filters=[
        {
            "name": "default-association-route-table",
            "values": ["true"],
        },
        {
            "name": "transit-gateway-id",
            "values": ["tgw-12345678"],
        },
    ])
    ```

    ### By Identifier

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2transitgateway.get_route_table(id="tgw-rtb-12345678")
    ```


    :param Sequence[Union['GetRouteTableFilterArgs', 'GetRouteTableFilterArgsDict']] filters: One or more configuration blocks containing name-values filters. Detailed below.
    :param str id: Identifier of the EC2 Transit Gateway Route Table.
    :param Mapping[str, str] tags: Key-value tags for the EC2 Transit Gateway Route Table
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:ec2transitgateway/getRouteTable:getRouteTable', __args__, opts=opts, typ=GetRouteTableResult).value

    return AwaitableGetRouteTableResult(
        arn=pulumi.get(__ret__, 'arn'),
        default_association_route_table=pulumi.get(__ret__, 'default_association_route_table'),
        default_propagation_route_table=pulumi.get(__ret__, 'default_propagation_route_table'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        tags=pulumi.get(__ret__, 'tags'),
        transit_gateway_id=pulumi.get(__ret__, 'transit_gateway_id'))
def get_route_table_output(filters: Optional[pulumi.Input[Optional[Sequence[Union['GetRouteTableFilterArgs', 'GetRouteTableFilterArgsDict']]]]] = None,
                           id: Optional[pulumi.Input[Optional[str]]] = None,
                           tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                           opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetRouteTableResult]:
    """
    Get information on an EC2 Transit Gateway Route Table.

    ## Example Usage

    ### By Filter

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2transitgateway.get_route_table(filters=[
        {
            "name": "default-association-route-table",
            "values": ["true"],
        },
        {
            "name": "transit-gateway-id",
            "values": ["tgw-12345678"],
        },
    ])
    ```

    ### By Identifier

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2transitgateway.get_route_table(id="tgw-rtb-12345678")
    ```


    :param Sequence[Union['GetRouteTableFilterArgs', 'GetRouteTableFilterArgsDict']] filters: One or more configuration blocks containing name-values filters. Detailed below.
    :param str id: Identifier of the EC2 Transit Gateway Route Table.
    :param Mapping[str, str] tags: Key-value tags for the EC2 Transit Gateway Route Table
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['tags'] = tags
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:ec2transitgateway/getRouteTable:getRouteTable', __args__, opts=opts, typ=GetRouteTableResult)
    return __ret__.apply(lambda __response__: GetRouteTableResult(
        arn=pulumi.get(__response__, 'arn'),
        default_association_route_table=pulumi.get(__response__, 'default_association_route_table'),
        default_propagation_route_table=pulumi.get(__response__, 'default_propagation_route_table'),
        filters=pulumi.get(__response__, 'filters'),
        id=pulumi.get(__response__, 'id'),
        tags=pulumi.get(__response__, 'tags'),
        transit_gateway_id=pulumi.get(__response__, 'transit_gateway_id')))
