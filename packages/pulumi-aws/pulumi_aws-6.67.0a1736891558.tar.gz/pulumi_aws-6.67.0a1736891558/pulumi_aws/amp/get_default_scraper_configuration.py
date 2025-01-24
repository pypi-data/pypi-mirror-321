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
    'GetDefaultScraperConfigurationResult',
    'AwaitableGetDefaultScraperConfigurationResult',
    'get_default_scraper_configuration',
    'get_default_scraper_configuration_output',
]

@pulumi.output_type
class GetDefaultScraperConfigurationResult:
    """
    A collection of values returned by getDefaultScraperConfiguration.
    """
    def __init__(__self__, configuration=None, id=None):
        if configuration and not isinstance(configuration, str):
            raise TypeError("Expected argument 'configuration' to be a str")
        pulumi.set(__self__, "configuration", configuration)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def configuration(self) -> str:
        """
        The configuration file.
        """
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetDefaultScraperConfigurationResult(GetDefaultScraperConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDefaultScraperConfigurationResult(
            configuration=self.configuration,
            id=self.id)


def get_default_scraper_configuration(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDefaultScraperConfigurationResult:
    """
    Returns the default scraper configuration used when Amazon EKS creates a scraper for you.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.amp.get_default_scraper_configuration()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:amp/getDefaultScraperConfiguration:getDefaultScraperConfiguration', __args__, opts=opts, typ=GetDefaultScraperConfigurationResult).value

    return AwaitableGetDefaultScraperConfigurationResult(
        configuration=pulumi.get(__ret__, 'configuration'),
        id=pulumi.get(__ret__, 'id'))
def get_default_scraper_configuration_output(opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDefaultScraperConfigurationResult]:
    """
    Returns the default scraper configuration used when Amazon EKS creates a scraper for you.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.amp.get_default_scraper_configuration()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:amp/getDefaultScraperConfiguration:getDefaultScraperConfiguration', __args__, opts=opts, typ=GetDefaultScraperConfigurationResult)
    return __ret__.apply(lambda __response__: GetDefaultScraperConfigurationResult(
        configuration=pulumi.get(__response__, 'configuration'),
        id=pulumi.get(__response__, 'id')))
