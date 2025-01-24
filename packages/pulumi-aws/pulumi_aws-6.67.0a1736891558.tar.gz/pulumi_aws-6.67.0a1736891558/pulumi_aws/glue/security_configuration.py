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

__all__ = ['SecurityConfigurationArgs', 'SecurityConfiguration']

@pulumi.input_type
class SecurityConfigurationArgs:
    def __init__(__self__, *,
                 encryption_configuration: pulumi.Input['SecurityConfigurationEncryptionConfigurationArgs'],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SecurityConfiguration resource.
        :param pulumi.Input['SecurityConfigurationEncryptionConfigurationArgs'] encryption_configuration: Configuration block containing encryption configuration. Detailed below.
        :param pulumi.Input[str] name: Name of the security configuration.
        """
        pulumi.set(__self__, "encryption_configuration", encryption_configuration)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> pulumi.Input['SecurityConfigurationEncryptionConfigurationArgs']:
        """
        Configuration block containing encryption configuration. Detailed below.
        """
        return pulumi.get(self, "encryption_configuration")

    @encryption_configuration.setter
    def encryption_configuration(self, value: pulumi.Input['SecurityConfigurationEncryptionConfigurationArgs']):
        pulumi.set(self, "encryption_configuration", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the security configuration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _SecurityConfigurationState:
    def __init__(__self__, *,
                 encryption_configuration: Optional[pulumi.Input['SecurityConfigurationEncryptionConfigurationArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SecurityConfiguration resources.
        :param pulumi.Input['SecurityConfigurationEncryptionConfigurationArgs'] encryption_configuration: Configuration block containing encryption configuration. Detailed below.
        :param pulumi.Input[str] name: Name of the security configuration.
        """
        if encryption_configuration is not None:
            pulumi.set(__self__, "encryption_configuration", encryption_configuration)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input['SecurityConfigurationEncryptionConfigurationArgs']]:
        """
        Configuration block containing encryption configuration. Detailed below.
        """
        return pulumi.get(self, "encryption_configuration")

    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input['SecurityConfigurationEncryptionConfigurationArgs']]):
        pulumi.set(self, "encryption_configuration", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the security configuration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class SecurityConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encryption_configuration: Optional[pulumi.Input[Union['SecurityConfigurationEncryptionConfigurationArgs', 'SecurityConfigurationEncryptionConfigurationArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Glue Security Configuration.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.SecurityConfiguration("example",
            name="example",
            encryption_configuration={
                "cloudwatch_encryption": {
                    "cloudwatch_encryption_mode": "DISABLED",
                },
                "job_bookmarks_encryption": {
                    "job_bookmarks_encryption_mode": "DISABLED",
                },
                "s3_encryption": {
                    "kms_key_arn": example_aws_kms_key["arn"],
                    "s3_encryption_mode": "SSE-KMS",
                },
            })
        ```

        ## Import

        Using `pulumi import`, import Glue Security Configurations using `name`. For example:

        ```sh
        $ pulumi import aws:glue/securityConfiguration:SecurityConfiguration example example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['SecurityConfigurationEncryptionConfigurationArgs', 'SecurityConfigurationEncryptionConfigurationArgsDict']] encryption_configuration: Configuration block containing encryption configuration. Detailed below.
        :param pulumi.Input[str] name: Name of the security configuration.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Glue Security Configuration.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.SecurityConfiguration("example",
            name="example",
            encryption_configuration={
                "cloudwatch_encryption": {
                    "cloudwatch_encryption_mode": "DISABLED",
                },
                "job_bookmarks_encryption": {
                    "job_bookmarks_encryption_mode": "DISABLED",
                },
                "s3_encryption": {
                    "kms_key_arn": example_aws_kms_key["arn"],
                    "s3_encryption_mode": "SSE-KMS",
                },
            })
        ```

        ## Import

        Using `pulumi import`, import Glue Security Configurations using `name`. For example:

        ```sh
        $ pulumi import aws:glue/securityConfiguration:SecurityConfiguration example example
        ```

        :param str resource_name: The name of the resource.
        :param SecurityConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encryption_configuration: Optional[pulumi.Input[Union['SecurityConfigurationEncryptionConfigurationArgs', 'SecurityConfigurationEncryptionConfigurationArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecurityConfigurationArgs.__new__(SecurityConfigurationArgs)

            if encryption_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'encryption_configuration'")
            __props__.__dict__["encryption_configuration"] = encryption_configuration
            __props__.__dict__["name"] = name
        super(SecurityConfiguration, __self__).__init__(
            'aws:glue/securityConfiguration:SecurityConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            encryption_configuration: Optional[pulumi.Input[Union['SecurityConfigurationEncryptionConfigurationArgs', 'SecurityConfigurationEncryptionConfigurationArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'SecurityConfiguration':
        """
        Get an existing SecurityConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['SecurityConfigurationEncryptionConfigurationArgs', 'SecurityConfigurationEncryptionConfigurationArgsDict']] encryption_configuration: Configuration block containing encryption configuration. Detailed below.
        :param pulumi.Input[str] name: Name of the security configuration.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SecurityConfigurationState.__new__(_SecurityConfigurationState)

        __props__.__dict__["encryption_configuration"] = encryption_configuration
        __props__.__dict__["name"] = name
        return SecurityConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> pulumi.Output['outputs.SecurityConfigurationEncryptionConfiguration']:
        """
        Configuration block containing encryption configuration. Detailed below.
        """
        return pulumi.get(self, "encryption_configuration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the security configuration.
        """
        return pulumi.get(self, "name")

