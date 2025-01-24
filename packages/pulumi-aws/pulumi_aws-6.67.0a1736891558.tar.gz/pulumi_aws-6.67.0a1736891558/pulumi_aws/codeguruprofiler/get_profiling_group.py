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
    'GetProfilingGroupResult',
    'AwaitableGetProfilingGroupResult',
    'get_profiling_group',
    'get_profiling_group_output',
]

@pulumi.output_type
class GetProfilingGroupResult:
    """
    A collection of values returned by getProfilingGroup.
    """
    def __init__(__self__, agent_orchestration_configs=None, arn=None, compute_platform=None, created_at=None, id=None, name=None, profiling_statuses=None, tags=None, updated_at=None):
        if agent_orchestration_configs and not isinstance(agent_orchestration_configs, list):
            raise TypeError("Expected argument 'agent_orchestration_configs' to be a list")
        pulumi.set(__self__, "agent_orchestration_configs", agent_orchestration_configs)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if compute_platform and not isinstance(compute_platform, str):
            raise TypeError("Expected argument 'compute_platform' to be a str")
        pulumi.set(__self__, "compute_platform", compute_platform)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if profiling_statuses and not isinstance(profiling_statuses, list):
            raise TypeError("Expected argument 'profiling_statuses' to be a list")
        pulumi.set(__self__, "profiling_statuses", profiling_statuses)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="agentOrchestrationConfigs")
    def agent_orchestration_configs(self) -> Sequence['outputs.GetProfilingGroupAgentOrchestrationConfigResult']:
        """
        Profiling Group agent orchestration config
        """
        return pulumi.get(self, "agent_orchestration_configs")

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the Profiling Group.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="computePlatform")
    def compute_platform(self) -> str:
        """
        The compute platform of the profiling group.
        """
        return pulumi.get(self, "compute_platform")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        Timestamp when Profiling Group was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="profilingStatuses")
    def profiling_statuses(self) -> Sequence['outputs.GetProfilingGroupProfilingStatusResult']:
        """
        The status of the Profiling Group.
        """
        return pulumi.get(self, "profiling_statuses")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Mapping of Key-Value tags for the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        Timestamp when Profiling Group was updated.
        """
        return pulumi.get(self, "updated_at")


class AwaitableGetProfilingGroupResult(GetProfilingGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProfilingGroupResult(
            agent_orchestration_configs=self.agent_orchestration_configs,
            arn=self.arn,
            compute_platform=self.compute_platform,
            created_at=self.created_at,
            id=self.id,
            name=self.name,
            profiling_statuses=self.profiling_statuses,
            tags=self.tags,
            updated_at=self.updated_at)


def get_profiling_group(name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProfilingGroupResult:
    """
    Data source for managing an AWS CodeGuru Profiler Profiling Group.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.codeguruprofiler.get_profiling_group(name="example")
    ```


    :param str name: The name of the profiling group.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:codeguruprofiler/getProfilingGroup:getProfilingGroup', __args__, opts=opts, typ=GetProfilingGroupResult).value

    return AwaitableGetProfilingGroupResult(
        agent_orchestration_configs=pulumi.get(__ret__, 'agent_orchestration_configs'),
        arn=pulumi.get(__ret__, 'arn'),
        compute_platform=pulumi.get(__ret__, 'compute_platform'),
        created_at=pulumi.get(__ret__, 'created_at'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        profiling_statuses=pulumi.get(__ret__, 'profiling_statuses'),
        tags=pulumi.get(__ret__, 'tags'),
        updated_at=pulumi.get(__ret__, 'updated_at'))
def get_profiling_group_output(name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetProfilingGroupResult]:
    """
    Data source for managing an AWS CodeGuru Profiler Profiling Group.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.codeguruprofiler.get_profiling_group(name="example")
    ```


    :param str name: The name of the profiling group.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:codeguruprofiler/getProfilingGroup:getProfilingGroup', __args__, opts=opts, typ=GetProfilingGroupResult)
    return __ret__.apply(lambda __response__: GetProfilingGroupResult(
        agent_orchestration_configs=pulumi.get(__response__, 'agent_orchestration_configs'),
        arn=pulumi.get(__response__, 'arn'),
        compute_platform=pulumi.get(__response__, 'compute_platform'),
        created_at=pulumi.get(__response__, 'created_at'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        profiling_statuses=pulumi.get(__response__, 'profiling_statuses'),
        tags=pulumi.get(__response__, 'tags'),
        updated_at=pulumi.get(__response__, 'updated_at')))
