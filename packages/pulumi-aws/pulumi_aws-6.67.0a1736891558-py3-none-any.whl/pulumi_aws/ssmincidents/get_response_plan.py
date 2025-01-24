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
    'GetResponsePlanResult',
    'AwaitableGetResponsePlanResult',
    'get_response_plan',
    'get_response_plan_output',
]

@pulumi.output_type
class GetResponsePlanResult:
    """
    A collection of values returned by getResponsePlan.
    """
    def __init__(__self__, actions=None, arn=None, chat_channels=None, display_name=None, engagements=None, id=None, incident_templates=None, integrations=None, name=None, tags=None):
        if actions and not isinstance(actions, list):
            raise TypeError("Expected argument 'actions' to be a list")
        pulumi.set(__self__, "actions", actions)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if chat_channels and not isinstance(chat_channels, list):
            raise TypeError("Expected argument 'chat_channels' to be a list")
        pulumi.set(__self__, "chat_channels", chat_channels)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if engagements and not isinstance(engagements, list):
            raise TypeError("Expected argument 'engagements' to be a list")
        pulumi.set(__self__, "engagements", engagements)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if incident_templates and not isinstance(incident_templates, list):
            raise TypeError("Expected argument 'incident_templates' to be a list")
        pulumi.set(__self__, "incident_templates", incident_templates)
        if integrations and not isinstance(integrations, list):
            raise TypeError("Expected argument 'integrations' to be a list")
        pulumi.set(__self__, "integrations", integrations)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def actions(self) -> Sequence['outputs.GetResponsePlanActionResult']:
        """
        (Optional) The actions that the response plan starts at the beginning of an incident.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def arn(self) -> str:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="chatChannels")
    def chat_channels(self) -> Sequence[str]:
        """
        The Chatbot chat channel used for collaboration during an incident.
        """
        return pulumi.get(self, "chat_channels")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The long format of the response plan name. This field can contain spaces.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def engagements(self) -> Sequence[str]:
        """
        The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident.
        """
        return pulumi.get(self, "engagements")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="incidentTemplates")
    def incident_templates(self) -> Sequence['outputs.GetResponsePlanIncidentTemplateResult']:
        return pulumi.get(self, "incident_templates")

    @property
    @pulumi.getter
    def integrations(self) -> Sequence['outputs.GetResponsePlanIntegrationResult']:
        """
        Information about third-party services integrated into the response plan. The following values are supported:
        """
        return pulumi.get(self, "integrations")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the PagerDuty configuration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        The tags applied to the response plan.
        """
        return pulumi.get(self, "tags")


class AwaitableGetResponsePlanResult(GetResponsePlanResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResponsePlanResult(
            actions=self.actions,
            arn=self.arn,
            chat_channels=self.chat_channels,
            display_name=self.display_name,
            engagements=self.engagements,
            id=self.id,
            incident_templates=self.incident_templates,
            integrations=self.integrations,
            name=self.name,
            tags=self.tags)


def get_response_plan(arn: Optional[str] = None,
                      tags: Optional[Mapping[str, str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResponsePlanResult:
    """
    Use this data source to manage a response plan in AWS Systems Manager Incident Manager.

    ## Example Usage


    :param str arn: The Amazon Resource Name (ARN) of the response plan.
    :param Mapping[str, str] tags: The tags applied to the response plan.
    """
    __args__ = dict()
    __args__['arn'] = arn
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:ssmincidents/getResponsePlan:getResponsePlan', __args__, opts=opts, typ=GetResponsePlanResult).value

    return AwaitableGetResponsePlanResult(
        actions=pulumi.get(__ret__, 'actions'),
        arn=pulumi.get(__ret__, 'arn'),
        chat_channels=pulumi.get(__ret__, 'chat_channels'),
        display_name=pulumi.get(__ret__, 'display_name'),
        engagements=pulumi.get(__ret__, 'engagements'),
        id=pulumi.get(__ret__, 'id'),
        incident_templates=pulumi.get(__ret__, 'incident_templates'),
        integrations=pulumi.get(__ret__, 'integrations'),
        name=pulumi.get(__ret__, 'name'),
        tags=pulumi.get(__ret__, 'tags'))
def get_response_plan_output(arn: Optional[pulumi.Input[str]] = None,
                             tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                             opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetResponsePlanResult]:
    """
    Use this data source to manage a response plan in AWS Systems Manager Incident Manager.

    ## Example Usage


    :param str arn: The Amazon Resource Name (ARN) of the response plan.
    :param Mapping[str, str] tags: The tags applied to the response plan.
    """
    __args__ = dict()
    __args__['arn'] = arn
    __args__['tags'] = tags
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:ssmincidents/getResponsePlan:getResponsePlan', __args__, opts=opts, typ=GetResponsePlanResult)
    return __ret__.apply(lambda __response__: GetResponsePlanResult(
        actions=pulumi.get(__response__, 'actions'),
        arn=pulumi.get(__response__, 'arn'),
        chat_channels=pulumi.get(__response__, 'chat_channels'),
        display_name=pulumi.get(__response__, 'display_name'),
        engagements=pulumi.get(__response__, 'engagements'),
        id=pulumi.get(__response__, 'id'),
        incident_templates=pulumi.get(__response__, 'incident_templates'),
        integrations=pulumi.get(__response__, 'integrations'),
        name=pulumi.get(__response__, 'name'),
        tags=pulumi.get(__response__, 'tags')))
