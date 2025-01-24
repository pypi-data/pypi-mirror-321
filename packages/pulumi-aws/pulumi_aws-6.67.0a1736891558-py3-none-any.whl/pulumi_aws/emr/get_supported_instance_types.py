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
    'GetSupportedInstanceTypesResult',
    'AwaitableGetSupportedInstanceTypesResult',
    'get_supported_instance_types',
    'get_supported_instance_types_output',
]

@pulumi.output_type
class GetSupportedInstanceTypesResult:
    """
    A collection of values returned by getSupportedInstanceTypes.
    """
    def __init__(__self__, id=None, release_label=None, supported_instance_types=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if release_label and not isinstance(release_label, str):
            raise TypeError("Expected argument 'release_label' to be a str")
        pulumi.set(__self__, "release_label", release_label)
        if supported_instance_types and not isinstance(supported_instance_types, list):
            raise TypeError("Expected argument 'supported_instance_types' to be a list")
        pulumi.set(__self__, "supported_instance_types", supported_instance_types)

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="releaseLabel")
    def release_label(self) -> str:
        return pulumi.get(self, "release_label")

    @property
    @pulumi.getter(name="supportedInstanceTypes")
    def supported_instance_types(self) -> Optional[Sequence['outputs.GetSupportedInstanceTypesSupportedInstanceTypeResult']]:
        """
        List of supported instance types. See `supported_instance_types` below.
        """
        return pulumi.get(self, "supported_instance_types")


class AwaitableGetSupportedInstanceTypesResult(GetSupportedInstanceTypesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSupportedInstanceTypesResult(
            id=self.id,
            release_label=self.release_label,
            supported_instance_types=self.supported_instance_types)


def get_supported_instance_types(release_label: Optional[str] = None,
                                 supported_instance_types: Optional[Sequence[Union['GetSupportedInstanceTypesSupportedInstanceTypeArgs', 'GetSupportedInstanceTypesSupportedInstanceTypeArgsDict']]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSupportedInstanceTypesResult:
    """
    Data source for managing AWS EMR Supported Instance Types.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.emr.get_supported_instance_types(release_label="ebs-6.15.0")
    ```

    ### With a Lifecycle Pre-Condition

    This data source can be used with a lifecycle precondition to ensure a given instance type is supported by EMR.

    ```python
    import pulumi
    import pulumi_aws as aws

    instance_type = "r7g.large"
    release_label = "emr-6.15.0"
    test = aws.emr.get_supported_instance_types(release_label=release_label)
    test_cluster = aws.emr.Cluster("test",
        release_label=release_label,
        master_instance_group={
            "instance_type": instance_type,
        })
    ```


    :param str release_label: Amazon EMR release label. For more information about Amazon EMR releases and their included application versions and features, see the [Amazon EMR Release Guide](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-components.html).
    :param Sequence[Union['GetSupportedInstanceTypesSupportedInstanceTypeArgs', 'GetSupportedInstanceTypesSupportedInstanceTypeArgsDict']] supported_instance_types: List of supported instance types. See `supported_instance_types` below.
    """
    __args__ = dict()
    __args__['releaseLabel'] = release_label
    __args__['supportedInstanceTypes'] = supported_instance_types
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:emr/getSupportedInstanceTypes:getSupportedInstanceTypes', __args__, opts=opts, typ=GetSupportedInstanceTypesResult).value

    return AwaitableGetSupportedInstanceTypesResult(
        id=pulumi.get(__ret__, 'id'),
        release_label=pulumi.get(__ret__, 'release_label'),
        supported_instance_types=pulumi.get(__ret__, 'supported_instance_types'))
def get_supported_instance_types_output(release_label: Optional[pulumi.Input[str]] = None,
                                        supported_instance_types: Optional[pulumi.Input[Optional[Sequence[Union['GetSupportedInstanceTypesSupportedInstanceTypeArgs', 'GetSupportedInstanceTypesSupportedInstanceTypeArgsDict']]]]] = None,
                                        opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetSupportedInstanceTypesResult]:
    """
    Data source for managing AWS EMR Supported Instance Types.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.emr.get_supported_instance_types(release_label="ebs-6.15.0")
    ```

    ### With a Lifecycle Pre-Condition

    This data source can be used with a lifecycle precondition to ensure a given instance type is supported by EMR.

    ```python
    import pulumi
    import pulumi_aws as aws

    instance_type = "r7g.large"
    release_label = "emr-6.15.0"
    test = aws.emr.get_supported_instance_types(release_label=release_label)
    test_cluster = aws.emr.Cluster("test",
        release_label=release_label,
        master_instance_group={
            "instance_type": instance_type,
        })
    ```


    :param str release_label: Amazon EMR release label. For more information about Amazon EMR releases and their included application versions and features, see the [Amazon EMR Release Guide](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-components.html).
    :param Sequence[Union['GetSupportedInstanceTypesSupportedInstanceTypeArgs', 'GetSupportedInstanceTypesSupportedInstanceTypeArgsDict']] supported_instance_types: List of supported instance types. See `supported_instance_types` below.
    """
    __args__ = dict()
    __args__['releaseLabel'] = release_label
    __args__['supportedInstanceTypes'] = supported_instance_types
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:emr/getSupportedInstanceTypes:getSupportedInstanceTypes', __args__, opts=opts, typ=GetSupportedInstanceTypesResult)
    return __ret__.apply(lambda __response__: GetSupportedInstanceTypesResult(
        id=pulumi.get(__response__, 'id'),
        release_label=pulumi.get(__response__, 'release_label'),
        supported_instance_types=pulumi.get(__response__, 'supported_instance_types')))
