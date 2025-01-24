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
    'GetResponseHeadersPolicyResult',
    'AwaitableGetResponseHeadersPolicyResult',
    'get_response_headers_policy',
    'get_response_headers_policy_output',
]

@pulumi.output_type
class GetResponseHeadersPolicyResult:
    """
    A collection of values returned by getResponseHeadersPolicy.
    """
    def __init__(__self__, comment=None, cors_configs=None, custom_headers_configs=None, etag=None, id=None, name=None, remove_headers_configs=None, security_headers_configs=None, server_timing_headers_configs=None):
        if comment and not isinstance(comment, str):
            raise TypeError("Expected argument 'comment' to be a str")
        pulumi.set(__self__, "comment", comment)
        if cors_configs and not isinstance(cors_configs, list):
            raise TypeError("Expected argument 'cors_configs' to be a list")
        pulumi.set(__self__, "cors_configs", cors_configs)
        if custom_headers_configs and not isinstance(custom_headers_configs, list):
            raise TypeError("Expected argument 'custom_headers_configs' to be a list")
        pulumi.set(__self__, "custom_headers_configs", custom_headers_configs)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if remove_headers_configs and not isinstance(remove_headers_configs, list):
            raise TypeError("Expected argument 'remove_headers_configs' to be a list")
        pulumi.set(__self__, "remove_headers_configs", remove_headers_configs)
        if security_headers_configs and not isinstance(security_headers_configs, list):
            raise TypeError("Expected argument 'security_headers_configs' to be a list")
        pulumi.set(__self__, "security_headers_configs", security_headers_configs)
        if server_timing_headers_configs and not isinstance(server_timing_headers_configs, list):
            raise TypeError("Expected argument 'server_timing_headers_configs' to be a list")
        pulumi.set(__self__, "server_timing_headers_configs", server_timing_headers_configs)

    @property
    @pulumi.getter
    def comment(self) -> str:
        """
        Comment to describe the response headers policy. The comment cannot be longer than 128 characters.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="corsConfigs")
    def cors_configs(self) -> Sequence['outputs.GetResponseHeadersPolicyCorsConfigResult']:
        """
        Configuration for a set of HTTP response headers that are used for Cross-Origin Resource Sharing (CORS). See Cors Config for more information.
        """
        return pulumi.get(self, "cors_configs")

    @property
    @pulumi.getter(name="customHeadersConfigs")
    def custom_headers_configs(self) -> Sequence['outputs.GetResponseHeadersPolicyCustomHeadersConfigResult']:
        """
        Object that contains an attribute `items` that contains a list of Custom Headers. See Custom Header for more information.
        """
        return pulumi.get(self, "custom_headers_configs")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Current version of the response headers policy.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="removeHeadersConfigs")
    def remove_headers_configs(self) -> Sequence['outputs.GetResponseHeadersPolicyRemoveHeadersConfigResult']:
        """
        Object that contains an attribute `items` that contains a list of Remove Headers. See Remove Header for more information.
        """
        return pulumi.get(self, "remove_headers_configs")

    @property
    @pulumi.getter(name="securityHeadersConfigs")
    def security_headers_configs(self) -> Sequence['outputs.GetResponseHeadersPolicySecurityHeadersConfigResult']:
        """
        A configuration for a set of security-related HTTP response headers. See Security Headers Config for more information.
        """
        return pulumi.get(self, "security_headers_configs")

    @property
    @pulumi.getter(name="serverTimingHeadersConfigs")
    def server_timing_headers_configs(self) -> Sequence['outputs.GetResponseHeadersPolicyServerTimingHeadersConfigResult']:
        """
        (Optional) Configuration for enabling the Server-Timing header in HTTP responses sent from CloudFront. See Server Timing Headers Config for more information.
        """
        return pulumi.get(self, "server_timing_headers_configs")


class AwaitableGetResponseHeadersPolicyResult(GetResponseHeadersPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResponseHeadersPolicyResult(
            comment=self.comment,
            cors_configs=self.cors_configs,
            custom_headers_configs=self.custom_headers_configs,
            etag=self.etag,
            id=self.id,
            name=self.name,
            remove_headers_configs=self.remove_headers_configs,
            security_headers_configs=self.security_headers_configs,
            server_timing_headers_configs=self.server_timing_headers_configs)


def get_response_headers_policy(id: Optional[str] = None,
                                name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResponseHeadersPolicyResult:
    """
    Use this data source to retrieve information about a CloudFront cache policy.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.cloudfront.get_response_headers_policy(name="example-policy")
    ```

    ### AWS-Managed Policies

    AWS managed response header policy names are prefixed with `Managed-`:

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.cloudfront.get_response_headers_policy(name="Managed-SimpleCORS")
    ```


    :param str id: Identifier for the response headers policy.
    :param str name: Unique name to identify the response headers policy.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:cloudfront/getResponseHeadersPolicy:getResponseHeadersPolicy', __args__, opts=opts, typ=GetResponseHeadersPolicyResult).value

    return AwaitableGetResponseHeadersPolicyResult(
        comment=pulumi.get(__ret__, 'comment'),
        cors_configs=pulumi.get(__ret__, 'cors_configs'),
        custom_headers_configs=pulumi.get(__ret__, 'custom_headers_configs'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        remove_headers_configs=pulumi.get(__ret__, 'remove_headers_configs'),
        security_headers_configs=pulumi.get(__ret__, 'security_headers_configs'),
        server_timing_headers_configs=pulumi.get(__ret__, 'server_timing_headers_configs'))
def get_response_headers_policy_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                                       name: Optional[pulumi.Input[Optional[str]]] = None,
                                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetResponseHeadersPolicyResult]:
    """
    Use this data source to retrieve information about a CloudFront cache policy.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.cloudfront.get_response_headers_policy(name="example-policy")
    ```

    ### AWS-Managed Policies

    AWS managed response header policy names are prefixed with `Managed-`:

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.cloudfront.get_response_headers_policy(name="Managed-SimpleCORS")
    ```


    :param str id: Identifier for the response headers policy.
    :param str name: Unique name to identify the response headers policy.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:cloudfront/getResponseHeadersPolicy:getResponseHeadersPolicy', __args__, opts=opts, typ=GetResponseHeadersPolicyResult)
    return __ret__.apply(lambda __response__: GetResponseHeadersPolicyResult(
        comment=pulumi.get(__response__, 'comment'),
        cors_configs=pulumi.get(__response__, 'cors_configs'),
        custom_headers_configs=pulumi.get(__response__, 'custom_headers_configs'),
        etag=pulumi.get(__response__, 'etag'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        remove_headers_configs=pulumi.get(__response__, 'remove_headers_configs'),
        security_headers_configs=pulumi.get(__response__, 'security_headers_configs'),
        server_timing_headers_configs=pulumi.get(__response__, 'server_timing_headers_configs')))
