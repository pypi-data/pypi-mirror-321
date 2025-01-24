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

__all__ = [
    'GetAccessPointsResult',
    'AwaitableGetAccessPointsResult',
    'get_access_points',
    'get_access_points_output',
]

@pulumi.output_type
class GetAccessPointsResult:
    """
    A collection of values returned by getAccessPoints.
    """
    def __init__(__self__, arns=None, file_system_id=None, id=None, ids=None):
        if arns and not isinstance(arns, list):
            raise TypeError("Expected argument 'arns' to be a list")
        pulumi.set(__self__, "arns", arns)
        if file_system_id and not isinstance(file_system_id, str):
            raise TypeError("Expected argument 'file_system_id' to be a str")
        pulumi.set(__self__, "file_system_id", file_system_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def arns(self) -> Sequence[str]:
        """
        Set of Amazon Resource Names (ARNs).
        """
        return pulumi.get(self, "arns")

    @property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> str:
        return pulumi.get(self, "file_system_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        Set of identifiers.
        """
        return pulumi.get(self, "ids")


class AwaitableGetAccessPointsResult(GetAccessPointsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccessPointsResult(
            arns=self.arns,
            file_system_id=self.file_system_id,
            id=self.id,
            ids=self.ids)


def get_access_points(file_system_id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccessPointsResult:
    """
    Provides information about multiple Elastic File System (EFS) Access Points.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    test = aws.efs.get_access_points(file_system_id="fs-12345678")
    ```


    :param str file_system_id: EFS File System identifier.
    """
    __args__ = dict()
    __args__['fileSystemId'] = file_system_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:efs/getAccessPoints:getAccessPoints', __args__, opts=opts, typ=GetAccessPointsResult).value

    return AwaitableGetAccessPointsResult(
        arns=pulumi.get(__ret__, 'arns'),
        file_system_id=pulumi.get(__ret__, 'file_system_id'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'))
def get_access_points_output(file_system_id: Optional[pulumi.Input[str]] = None,
                             opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetAccessPointsResult]:
    """
    Provides information about multiple Elastic File System (EFS) Access Points.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    test = aws.efs.get_access_points(file_system_id="fs-12345678")
    ```


    :param str file_system_id: EFS File System identifier.
    """
    __args__ = dict()
    __args__['fileSystemId'] = file_system_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:efs/getAccessPoints:getAccessPoints', __args__, opts=opts, typ=GetAccessPointsResult)
    return __ret__.apply(lambda __response__: GetAccessPointsResult(
        arns=pulumi.get(__response__, 'arns'),
        file_system_id=pulumi.get(__response__, 'file_system_id'),
        id=pulumi.get(__response__, 'id'),
        ids=pulumi.get(__response__, 'ids')))
