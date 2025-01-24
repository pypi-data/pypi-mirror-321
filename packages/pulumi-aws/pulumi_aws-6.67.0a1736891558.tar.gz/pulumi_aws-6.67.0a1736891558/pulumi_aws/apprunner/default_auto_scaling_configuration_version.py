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

__all__ = ['DefaultAutoScalingConfigurationVersionArgs', 'DefaultAutoScalingConfigurationVersion']

@pulumi.input_type
class DefaultAutoScalingConfigurationVersionArgs:
    def __init__(__self__, *,
                 auto_scaling_configuration_arn: pulumi.Input[str]):
        """
        The set of arguments for constructing a DefaultAutoScalingConfigurationVersion resource.
        :param pulumi.Input[str] auto_scaling_configuration_arn: The ARN of the App Runner auto scaling configuration that you want to set as the default.
        """
        pulumi.set(__self__, "auto_scaling_configuration_arn", auto_scaling_configuration_arn)

    @property
    @pulumi.getter(name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the App Runner auto scaling configuration that you want to set as the default.
        """
        return pulumi.get(self, "auto_scaling_configuration_arn")

    @auto_scaling_configuration_arn.setter
    def auto_scaling_configuration_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "auto_scaling_configuration_arn", value)


@pulumi.input_type
class _DefaultAutoScalingConfigurationVersionState:
    def __init__(__self__, *,
                 auto_scaling_configuration_arn: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DefaultAutoScalingConfigurationVersion resources.
        :param pulumi.Input[str] auto_scaling_configuration_arn: The ARN of the App Runner auto scaling configuration that you want to set as the default.
        """
        if auto_scaling_configuration_arn is not None:
            pulumi.set(__self__, "auto_scaling_configuration_arn", auto_scaling_configuration_arn)

    @property
    @pulumi.getter(name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the App Runner auto scaling configuration that you want to set as the default.
        """
        return pulumi.get(self, "auto_scaling_configuration_arn")

    @auto_scaling_configuration_arn.setter
    def auto_scaling_configuration_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auto_scaling_configuration_arn", value)


class DefaultAutoScalingConfigurationVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_scaling_configuration_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages the default App Runner auto scaling configuration.
        When creating or updating this resource the existing default auto scaling configuration will be set to non-default automatically.
        When creating or updating this resource the configuration is automatically assigned as the default to the new services you create in the future. The new default designation doesn't affect the associations that were previously set for existing services.
        Each account can have only one default auto scaling configuration per Region.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apprunner.AutoScalingConfigurationVersion("example",
            auto_scaling_configuration_name="example",
            max_concurrency=50,
            max_size=10,
            min_size=2)
        example_default_auto_scaling_configuration_version = aws.apprunner.DefaultAutoScalingConfigurationVersion("example", auto_scaling_configuration_arn=example.arn)
        ```

        ## Import

        Using `pulumi import`, import App Runner default auto scaling configurations using the current Region. For example:

        ```sh
        $ pulumi import aws:apprunner/defaultAutoScalingConfigurationVersion:DefaultAutoScalingConfigurationVersion example us-west-2
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auto_scaling_configuration_arn: The ARN of the App Runner auto scaling configuration that you want to set as the default.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DefaultAutoScalingConfigurationVersionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages the default App Runner auto scaling configuration.
        When creating or updating this resource the existing default auto scaling configuration will be set to non-default automatically.
        When creating or updating this resource the configuration is automatically assigned as the default to the new services you create in the future. The new default designation doesn't affect the associations that were previously set for existing services.
        Each account can have only one default auto scaling configuration per Region.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apprunner.AutoScalingConfigurationVersion("example",
            auto_scaling_configuration_name="example",
            max_concurrency=50,
            max_size=10,
            min_size=2)
        example_default_auto_scaling_configuration_version = aws.apprunner.DefaultAutoScalingConfigurationVersion("example", auto_scaling_configuration_arn=example.arn)
        ```

        ## Import

        Using `pulumi import`, import App Runner default auto scaling configurations using the current Region. For example:

        ```sh
        $ pulumi import aws:apprunner/defaultAutoScalingConfigurationVersion:DefaultAutoScalingConfigurationVersion example us-west-2
        ```

        :param str resource_name: The name of the resource.
        :param DefaultAutoScalingConfigurationVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DefaultAutoScalingConfigurationVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_scaling_configuration_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DefaultAutoScalingConfigurationVersionArgs.__new__(DefaultAutoScalingConfigurationVersionArgs)

            if auto_scaling_configuration_arn is None and not opts.urn:
                raise TypeError("Missing required property 'auto_scaling_configuration_arn'")
            __props__.__dict__["auto_scaling_configuration_arn"] = auto_scaling_configuration_arn
        super(DefaultAutoScalingConfigurationVersion, __self__).__init__(
            'aws:apprunner/defaultAutoScalingConfigurationVersion:DefaultAutoScalingConfigurationVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auto_scaling_configuration_arn: Optional[pulumi.Input[str]] = None) -> 'DefaultAutoScalingConfigurationVersion':
        """
        Get an existing DefaultAutoScalingConfigurationVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auto_scaling_configuration_arn: The ARN of the App Runner auto scaling configuration that you want to set as the default.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DefaultAutoScalingConfigurationVersionState.__new__(_DefaultAutoScalingConfigurationVersionState)

        __props__.__dict__["auto_scaling_configuration_arn"] = auto_scaling_configuration_arn
        return DefaultAutoScalingConfigurationVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the App Runner auto scaling configuration that you want to set as the default.
        """
        return pulumi.get(self, "auto_scaling_configuration_arn")

