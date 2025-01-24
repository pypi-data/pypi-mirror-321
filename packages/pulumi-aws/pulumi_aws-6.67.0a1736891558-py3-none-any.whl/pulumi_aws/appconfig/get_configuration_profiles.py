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
    'GetConfigurationProfilesResult',
    'AwaitableGetConfigurationProfilesResult',
    'get_configuration_profiles',
    'get_configuration_profiles_output',
]

@pulumi.output_type
class GetConfigurationProfilesResult:
    """
    A collection of values returned by getConfigurationProfiles.
    """
    def __init__(__self__, application_id=None, configuration_profile_ids=None, id=None):
        if application_id and not isinstance(application_id, str):
            raise TypeError("Expected argument 'application_id' to be a str")
        pulumi.set(__self__, "application_id", application_id)
        if configuration_profile_ids and not isinstance(configuration_profile_ids, list):
            raise TypeError("Expected argument 'configuration_profile_ids' to be a list")
        pulumi.set(__self__, "configuration_profile_ids", configuration_profile_ids)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> str:
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="configurationProfileIds")
    def configuration_profile_ids(self) -> Sequence[str]:
        """
        Set of Configuration Profile IDs associated with the AppConfig Application.
        """
        return pulumi.get(self, "configuration_profile_ids")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetConfigurationProfilesResult(GetConfigurationProfilesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigurationProfilesResult(
            application_id=self.application_id,
            configuration_profile_ids=self.configuration_profile_ids,
            id=self.id)


def get_configuration_profiles(application_id: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigurationProfilesResult:
    """
    Provides access to all Configuration Properties for an AppConfig Application. This will allow you to pass Configuration
    Profile IDs to another resource.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.appconfig.get_configuration_profiles(application_id="a1d3rpe")
    example_get_configuration_profile = {__key: aws.appconfig.get_configuration_profile(configuration_profile_id=__value,
        application_id=example_aws_appconfig_application["id"]) for __key, __value in example.configuration_profile_ids}
    ```


    :param str application_id: ID of the AppConfig Application.
    """
    __args__ = dict()
    __args__['applicationId'] = application_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:appconfig/getConfigurationProfiles:getConfigurationProfiles', __args__, opts=opts, typ=GetConfigurationProfilesResult).value

    return AwaitableGetConfigurationProfilesResult(
        application_id=pulumi.get(__ret__, 'application_id'),
        configuration_profile_ids=pulumi.get(__ret__, 'configuration_profile_ids'),
        id=pulumi.get(__ret__, 'id'))
def get_configuration_profiles_output(application_id: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetConfigurationProfilesResult]:
    """
    Provides access to all Configuration Properties for an AppConfig Application. This will allow you to pass Configuration
    Profile IDs to another resource.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.appconfig.get_configuration_profiles(application_id="a1d3rpe")
    example_get_configuration_profile = {__key: aws.appconfig.get_configuration_profile(configuration_profile_id=__value,
        application_id=example_aws_appconfig_application["id"]) for __key, __value in example.configuration_profile_ids}
    ```


    :param str application_id: ID of the AppConfig Application.
    """
    __args__ = dict()
    __args__['applicationId'] = application_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:appconfig/getConfigurationProfiles:getConfigurationProfiles', __args__, opts=opts, typ=GetConfigurationProfilesResult)
    return __ret__.apply(lambda __response__: GetConfigurationProfilesResult(
        application_id=pulumi.get(__response__, 'application_id'),
        configuration_profile_ids=pulumi.get(__response__, 'configuration_profile_ids'),
        id=pulumi.get(__response__, 'id')))
