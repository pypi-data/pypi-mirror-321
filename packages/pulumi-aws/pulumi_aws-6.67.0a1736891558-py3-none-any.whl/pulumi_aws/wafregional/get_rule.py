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
    'GetRuleResult',
    'AwaitableGetRuleResult',
    'get_rule',
    'get_rule_output',
]

@pulumi.output_type
class GetRuleResult:
    """
    A collection of values returned by getRule.
    """
    def __init__(__self__, id=None, name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


class AwaitableGetRuleResult(GetRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRuleResult(
            id=self.id,
            name=self.name)


def get_rule(name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRuleResult:
    """
    `wafregional.Rule` Retrieves a WAF Regional Rule Resource Id.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.wafregional.get_rule(name="tfWAFRegionalRule")
    ```


    :param str name: Name of the WAF Regional rule.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:wafregional/getRule:getRule', __args__, opts=opts, typ=GetRuleResult).value

    return AwaitableGetRuleResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'))
def get_rule_output(name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetRuleResult]:
    """
    `wafregional.Rule` Retrieves a WAF Regional Rule Resource Id.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.wafregional.get_rule(name="tfWAFRegionalRule")
    ```


    :param str name: Name of the WAF Regional rule.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:wafregional/getRule:getRule', __args__, opts=opts, typ=GetRuleResult)
    return __ret__.apply(lambda __response__: GetRuleResult(
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name')))
