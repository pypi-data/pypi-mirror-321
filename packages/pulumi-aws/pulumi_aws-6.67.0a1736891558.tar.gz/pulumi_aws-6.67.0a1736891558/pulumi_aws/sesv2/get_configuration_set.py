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
    'GetConfigurationSetResult',
    'AwaitableGetConfigurationSetResult',
    'get_configuration_set',
    'get_configuration_set_output',
]

@pulumi.output_type
class GetConfigurationSetResult:
    """
    A collection of values returned by getConfigurationSet.
    """
    def __init__(__self__, arn=None, configuration_set_name=None, delivery_options=None, id=None, reputation_options=None, sending_options=None, suppression_options=None, tags=None, tracking_options=None, vdm_options=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if configuration_set_name and not isinstance(configuration_set_name, str):
            raise TypeError("Expected argument 'configuration_set_name' to be a str")
        pulumi.set(__self__, "configuration_set_name", configuration_set_name)
        if delivery_options and not isinstance(delivery_options, list):
            raise TypeError("Expected argument 'delivery_options' to be a list")
        pulumi.set(__self__, "delivery_options", delivery_options)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if reputation_options and not isinstance(reputation_options, list):
            raise TypeError("Expected argument 'reputation_options' to be a list")
        pulumi.set(__self__, "reputation_options", reputation_options)
        if sending_options and not isinstance(sending_options, list):
            raise TypeError("Expected argument 'sending_options' to be a list")
        pulumi.set(__self__, "sending_options", sending_options)
        if suppression_options and not isinstance(suppression_options, list):
            raise TypeError("Expected argument 'suppression_options' to be a list")
        pulumi.set(__self__, "suppression_options", suppression_options)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tracking_options and not isinstance(tracking_options, list):
            raise TypeError("Expected argument 'tracking_options' to be a list")
        pulumi.set(__self__, "tracking_options", tracking_options)
        if vdm_options and not isinstance(vdm_options, list):
            raise TypeError("Expected argument 'vdm_options' to be a list")
        pulumi.set(__self__, "vdm_options", vdm_options)

    @property
    @pulumi.getter
    def arn(self) -> str:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="configurationSetName")
    def configuration_set_name(self) -> str:
        return pulumi.get(self, "configuration_set_name")

    @property
    @pulumi.getter(name="deliveryOptions")
    def delivery_options(self) -> Sequence['outputs.GetConfigurationSetDeliveryOptionResult']:
        """
        An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.
        """
        return pulumi.get(self, "delivery_options")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="reputationOptions")
    def reputation_options(self) -> Sequence['outputs.GetConfigurationSetReputationOptionResult']:
        """
        An object that defines whether or not Amazon SES collects reputation metrics for the emails that you send that use the configuration set.
        """
        return pulumi.get(self, "reputation_options")

    @property
    @pulumi.getter(name="sendingOptions")
    def sending_options(self) -> Sequence['outputs.GetConfigurationSetSendingOptionResult']:
        """
        An object that defines whether or not Amazon SES can send email that you send using the configuration set.
        """
        return pulumi.get(self, "sending_options")

    @property
    @pulumi.getter(name="suppressionOptions")
    def suppression_options(self) -> Sequence['outputs.GetConfigurationSetSuppressionOptionResult']:
        """
        An object that contains information about the suppression list preferences for your account.
        """
        return pulumi.get(self, "suppression_options")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Key-value map of resource tags for the container recipe.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trackingOptions")
    def tracking_options(self) -> Sequence['outputs.GetConfigurationSetTrackingOptionResult']:
        """
        An object that defines the open and click tracking options for emails that you send using the configuration set.
        """
        return pulumi.get(self, "tracking_options")

    @property
    @pulumi.getter(name="vdmOptions")
    def vdm_options(self) -> Sequence['outputs.GetConfigurationSetVdmOptionResult']:
        """
        An object that contains information about the VDM preferences for your configuration set.
        """
        return pulumi.get(self, "vdm_options")


class AwaitableGetConfigurationSetResult(GetConfigurationSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigurationSetResult(
            arn=self.arn,
            configuration_set_name=self.configuration_set_name,
            delivery_options=self.delivery_options,
            id=self.id,
            reputation_options=self.reputation_options,
            sending_options=self.sending_options,
            suppression_options=self.suppression_options,
            tags=self.tags,
            tracking_options=self.tracking_options,
            vdm_options=self.vdm_options)


def get_configuration_set(configuration_set_name: Optional[str] = None,
                          tags: Optional[Mapping[str, str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigurationSetResult:
    """
    Data source for managing an AWS SESv2 (Simple Email V2) Configuration Set.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.sesv2.get_configuration_set(configuration_set_name="example")
    ```


    :param str configuration_set_name: The name of the configuration set.
    :param Mapping[str, str] tags: Key-value map of resource tags for the container recipe.
    """
    __args__ = dict()
    __args__['configurationSetName'] = configuration_set_name
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:sesv2/getConfigurationSet:getConfigurationSet', __args__, opts=opts, typ=GetConfigurationSetResult).value

    return AwaitableGetConfigurationSetResult(
        arn=pulumi.get(__ret__, 'arn'),
        configuration_set_name=pulumi.get(__ret__, 'configuration_set_name'),
        delivery_options=pulumi.get(__ret__, 'delivery_options'),
        id=pulumi.get(__ret__, 'id'),
        reputation_options=pulumi.get(__ret__, 'reputation_options'),
        sending_options=pulumi.get(__ret__, 'sending_options'),
        suppression_options=pulumi.get(__ret__, 'suppression_options'),
        tags=pulumi.get(__ret__, 'tags'),
        tracking_options=pulumi.get(__ret__, 'tracking_options'),
        vdm_options=pulumi.get(__ret__, 'vdm_options'))
def get_configuration_set_output(configuration_set_name: Optional[pulumi.Input[str]] = None,
                                 tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                 opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetConfigurationSetResult]:
    """
    Data source for managing an AWS SESv2 (Simple Email V2) Configuration Set.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.sesv2.get_configuration_set(configuration_set_name="example")
    ```


    :param str configuration_set_name: The name of the configuration set.
    :param Mapping[str, str] tags: Key-value map of resource tags for the container recipe.
    """
    __args__ = dict()
    __args__['configurationSetName'] = configuration_set_name
    __args__['tags'] = tags
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:sesv2/getConfigurationSet:getConfigurationSet', __args__, opts=opts, typ=GetConfigurationSetResult)
    return __ret__.apply(lambda __response__: GetConfigurationSetResult(
        arn=pulumi.get(__response__, 'arn'),
        configuration_set_name=pulumi.get(__response__, 'configuration_set_name'),
        delivery_options=pulumi.get(__response__, 'delivery_options'),
        id=pulumi.get(__response__, 'id'),
        reputation_options=pulumi.get(__response__, 'reputation_options'),
        sending_options=pulumi.get(__response__, 'sending_options'),
        suppression_options=pulumi.get(__response__, 'suppression_options'),
        tags=pulumi.get(__response__, 'tags'),
        tracking_options=pulumi.get(__response__, 'tracking_options'),
        vdm_options=pulumi.get(__response__, 'vdm_options')))
