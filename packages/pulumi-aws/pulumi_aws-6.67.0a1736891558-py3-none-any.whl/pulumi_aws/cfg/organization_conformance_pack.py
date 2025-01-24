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

__all__ = ['OrganizationConformancePackArgs', 'OrganizationConformancePack']

@pulumi.input_type
class OrganizationConformancePackArgs:
    def __init__(__self__, *,
                 delivery_s3_bucket: Optional[pulumi.Input[str]] = None,
                 delivery_s3_key_prefix: Optional[pulumi.Input[str]] = None,
                 excluded_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 input_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationConformancePackInputParameterArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 template_body: Optional[pulumi.Input[str]] = None,
                 template_s3_uri: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OrganizationConformancePack resource.
        :param pulumi.Input[str] delivery_s3_bucket: Amazon S3 bucket where AWS Config stores conformance pack templates. Delivery bucket must begin with `awsconfigconforms` prefix. Maximum length of 63.
        :param pulumi.Input[str] delivery_s3_key_prefix: The prefix for the Amazon S3 bucket. Maximum length of 1024.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] excluded_accounts: Set of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack. Maximum of 1000 accounts.
        :param pulumi.Input[Sequence[pulumi.Input['OrganizationConformancePackInputParameterArgs']]] input_parameters: Set of configuration blocks describing input parameters passed to the conformance pack template. Documented below. When configured, the parameters must also be included in the `template_body` or in the template stored in Amazon S3 if using `template_s3_uri`.
        :param pulumi.Input[str] name: The name of the organization conformance pack. Must begin with a letter and contain from 1 to 128 alphanumeric characters and hyphens.
        :param pulumi.Input[str] template_body: A string containing full conformance pack template body. Maximum length of 51200. Drift detection is not possible with this argument.
        :param pulumi.Input[str] template_s3_uri: Location of file, e.g., `s3://bucketname/prefix`, containing the template body. The uri must point to the conformance pack template that is located in an Amazon S3 bucket in the same region as the conformance pack. Maximum length of 1024. Drift detection is not possible with this argument.
        """
        if delivery_s3_bucket is not None:
            pulumi.set(__self__, "delivery_s3_bucket", delivery_s3_bucket)
        if delivery_s3_key_prefix is not None:
            pulumi.set(__self__, "delivery_s3_key_prefix", delivery_s3_key_prefix)
        if excluded_accounts is not None:
            pulumi.set(__self__, "excluded_accounts", excluded_accounts)
        if input_parameters is not None:
            pulumi.set(__self__, "input_parameters", input_parameters)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if template_body is not None:
            pulumi.set(__self__, "template_body", template_body)
        if template_s3_uri is not None:
            pulumi.set(__self__, "template_s3_uri", template_s3_uri)

    @property
    @pulumi.getter(name="deliveryS3Bucket")
    def delivery_s3_bucket(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon S3 bucket where AWS Config stores conformance pack templates. Delivery bucket must begin with `awsconfigconforms` prefix. Maximum length of 63.
        """
        return pulumi.get(self, "delivery_s3_bucket")

    @delivery_s3_bucket.setter
    def delivery_s3_bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delivery_s3_bucket", value)

    @property
    @pulumi.getter(name="deliveryS3KeyPrefix")
    def delivery_s3_key_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The prefix for the Amazon S3 bucket. Maximum length of 1024.
        """
        return pulumi.get(self, "delivery_s3_key_prefix")

    @delivery_s3_key_prefix.setter
    def delivery_s3_key_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delivery_s3_key_prefix", value)

    @property
    @pulumi.getter(name="excludedAccounts")
    def excluded_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Set of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack. Maximum of 1000 accounts.
        """
        return pulumi.get(self, "excluded_accounts")

    @excluded_accounts.setter
    def excluded_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "excluded_accounts", value)

    @property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationConformancePackInputParameterArgs']]]]:
        """
        Set of configuration blocks describing input parameters passed to the conformance pack template. Documented below. When configured, the parameters must also be included in the `template_body` or in the template stored in Amazon S3 if using `template_s3_uri`.
        """
        return pulumi.get(self, "input_parameters")

    @input_parameters.setter
    def input_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationConformancePackInputParameterArgs']]]]):
        pulumi.set(self, "input_parameters", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the organization conformance pack. Must begin with a letter and contain from 1 to 128 alphanumeric characters and hyphens.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> Optional[pulumi.Input[str]]:
        """
        A string containing full conformance pack template body. Maximum length of 51200. Drift detection is not possible with this argument.
        """
        return pulumi.get(self, "template_body")

    @template_body.setter
    def template_body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_body", value)

    @property
    @pulumi.getter(name="templateS3Uri")
    def template_s3_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Location of file, e.g., `s3://bucketname/prefix`, containing the template body. The uri must point to the conformance pack template that is located in an Amazon S3 bucket in the same region as the conformance pack. Maximum length of 1024. Drift detection is not possible with this argument.
        """
        return pulumi.get(self, "template_s3_uri")

    @template_s3_uri.setter
    def template_s3_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_s3_uri", value)


@pulumi.input_type
class _OrganizationConformancePackState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 delivery_s3_bucket: Optional[pulumi.Input[str]] = None,
                 delivery_s3_key_prefix: Optional[pulumi.Input[str]] = None,
                 excluded_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 input_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationConformancePackInputParameterArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 template_body: Optional[pulumi.Input[str]] = None,
                 template_s3_uri: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering OrganizationConformancePack resources.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the organization conformance pack.
        :param pulumi.Input[str] delivery_s3_bucket: Amazon S3 bucket where AWS Config stores conformance pack templates. Delivery bucket must begin with `awsconfigconforms` prefix. Maximum length of 63.
        :param pulumi.Input[str] delivery_s3_key_prefix: The prefix for the Amazon S3 bucket. Maximum length of 1024.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] excluded_accounts: Set of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack. Maximum of 1000 accounts.
        :param pulumi.Input[Sequence[pulumi.Input['OrganizationConformancePackInputParameterArgs']]] input_parameters: Set of configuration blocks describing input parameters passed to the conformance pack template. Documented below. When configured, the parameters must also be included in the `template_body` or in the template stored in Amazon S3 if using `template_s3_uri`.
        :param pulumi.Input[str] name: The name of the organization conformance pack. Must begin with a letter and contain from 1 to 128 alphanumeric characters and hyphens.
        :param pulumi.Input[str] template_body: A string containing full conformance pack template body. Maximum length of 51200. Drift detection is not possible with this argument.
        :param pulumi.Input[str] template_s3_uri: Location of file, e.g., `s3://bucketname/prefix`, containing the template body. The uri must point to the conformance pack template that is located in an Amazon S3 bucket in the same region as the conformance pack. Maximum length of 1024. Drift detection is not possible with this argument.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if delivery_s3_bucket is not None:
            pulumi.set(__self__, "delivery_s3_bucket", delivery_s3_bucket)
        if delivery_s3_key_prefix is not None:
            pulumi.set(__self__, "delivery_s3_key_prefix", delivery_s3_key_prefix)
        if excluded_accounts is not None:
            pulumi.set(__self__, "excluded_accounts", excluded_accounts)
        if input_parameters is not None:
            pulumi.set(__self__, "input_parameters", input_parameters)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if template_body is not None:
            pulumi.set(__self__, "template_body", template_body)
        if template_s3_uri is not None:
            pulumi.set(__self__, "template_s3_uri", template_s3_uri)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of the organization conformance pack.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="deliveryS3Bucket")
    def delivery_s3_bucket(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon S3 bucket where AWS Config stores conformance pack templates. Delivery bucket must begin with `awsconfigconforms` prefix. Maximum length of 63.
        """
        return pulumi.get(self, "delivery_s3_bucket")

    @delivery_s3_bucket.setter
    def delivery_s3_bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delivery_s3_bucket", value)

    @property
    @pulumi.getter(name="deliveryS3KeyPrefix")
    def delivery_s3_key_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The prefix for the Amazon S3 bucket. Maximum length of 1024.
        """
        return pulumi.get(self, "delivery_s3_key_prefix")

    @delivery_s3_key_prefix.setter
    def delivery_s3_key_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delivery_s3_key_prefix", value)

    @property
    @pulumi.getter(name="excludedAccounts")
    def excluded_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Set of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack. Maximum of 1000 accounts.
        """
        return pulumi.get(self, "excluded_accounts")

    @excluded_accounts.setter
    def excluded_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "excluded_accounts", value)

    @property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationConformancePackInputParameterArgs']]]]:
        """
        Set of configuration blocks describing input parameters passed to the conformance pack template. Documented below. When configured, the parameters must also be included in the `template_body` or in the template stored in Amazon S3 if using `template_s3_uri`.
        """
        return pulumi.get(self, "input_parameters")

    @input_parameters.setter
    def input_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationConformancePackInputParameterArgs']]]]):
        pulumi.set(self, "input_parameters", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the organization conformance pack. Must begin with a letter and contain from 1 to 128 alphanumeric characters and hyphens.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> Optional[pulumi.Input[str]]:
        """
        A string containing full conformance pack template body. Maximum length of 51200. Drift detection is not possible with this argument.
        """
        return pulumi.get(self, "template_body")

    @template_body.setter
    def template_body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_body", value)

    @property
    @pulumi.getter(name="templateS3Uri")
    def template_s3_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Location of file, e.g., `s3://bucketname/prefix`, containing the template body. The uri must point to the conformance pack template that is located in an Amazon S3 bucket in the same region as the conformance pack. Maximum length of 1024. Drift detection is not possible with this argument.
        """
        return pulumi.get(self, "template_s3_uri")

    @template_s3_uri.setter
    def template_s3_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_s3_uri", value)


class OrganizationConformancePack(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delivery_s3_bucket: Optional[pulumi.Input[str]] = None,
                 delivery_s3_key_prefix: Optional[pulumi.Input[str]] = None,
                 excluded_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 input_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['OrganizationConformancePackInputParameterArgs', 'OrganizationConformancePackInputParameterArgsDict']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 template_body: Optional[pulumi.Input[str]] = None,
                 template_s3_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Config Organization Conformance Pack. More information can be found in the [Managing Conformance Packs Across all Accounts in Your Organization](https://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-organization-apis.html) and [AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html) documentation. Example conformance pack templates may be found in the [AWS Config Rules Repository](https://github.com/awslabs/aws-config-rules/tree/master/aws-config-conformance-packs).

        > **NOTE:** This resource must be created in the Organization master account or a delegated administrator account, and the Organization must have all features enabled. Every Organization account except those configured in the `excluded_accounts` argument must have a Configuration Recorder with proper IAM permissions before the Organization Conformance Pack will successfully create or update. See also the `cfg.Recorder` resource.

        ## Example Usage

        ### Using Template Body

        ```python
        import pulumi
        import pulumi_aws as aws

        example_organization = aws.organizations.Organization("example",
            aws_service_access_principals=["config-multiaccountsetup.amazonaws.com"],
            feature_set="ALL")
        example = aws.cfg.OrganizationConformancePack("example",
            name="example",
            input_parameters=[{
                "parameter_name": "AccessKeysRotatedParameterMaxAccessKeyAge",
                "parameter_value": "90",
            }],
            template_body=\"\"\"Parameters:
          AccessKeysRotatedParameterMaxAccessKeyAge:
            Type: String
        Resources:
          IAMPasswordPolicy:
            Properties:
              ConfigRuleName: IAMPasswordPolicy
              Source:
                Owner: AWS
                SourceIdentifier: IAM_PASSWORD_POLICY
            Type: AWS::Config::ConfigRule
        \"\"\",
            opts = pulumi.ResourceOptions(depends_on=[
                    example_aws_config_configuration_recorder,
                    example_organization,
                ]))
        ```

        ### Using Template S3 URI

        ```python
        import pulumi
        import pulumi_aws as aws

        example_organization = aws.organizations.Organization("example",
            aws_service_access_principals=["config-multiaccountsetup.amazonaws.com"],
            feature_set="ALL")
        example_bucket_v2 = aws.s3.BucketV2("example", bucket="example")
        example_bucket_objectv2 = aws.s3.BucketObjectv2("example",
            bucket=example_bucket_v2.id,
            key="example-key",
            content=\"\"\"Resources:
          IAMPasswordPolicy:
            Properties:
              ConfigRuleName: IAMPasswordPolicy
              Source:
                Owner: AWS
                SourceIdentifier: IAM_PASSWORD_POLICY
            Type: AWS::Config::ConfigRule
        \"\"\")
        example = aws.cfg.OrganizationConformancePack("example",
            name="example",
            template_s3_uri=pulumi.Output.all(
                bucket=example_bucket_v2.bucket,
                key=example_bucket_objectv2.key
        ).apply(lambda resolved_outputs: f"s3://{resolved_outputs['bucket']}/{resolved_outputs['key']}")
        ,
            opts = pulumi.ResourceOptions(depends_on=[
                    example_aws_config_configuration_recorder,
                    example_organization,
                ]))
        ```

        ## Import

        Using `pulumi import`, import Config Organization Conformance Packs using the `name`. For example:

        ```sh
        $ pulumi import aws:cfg/organizationConformancePack:OrganizationConformancePack example example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] delivery_s3_bucket: Amazon S3 bucket where AWS Config stores conformance pack templates. Delivery bucket must begin with `awsconfigconforms` prefix. Maximum length of 63.
        :param pulumi.Input[str] delivery_s3_key_prefix: The prefix for the Amazon S3 bucket. Maximum length of 1024.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] excluded_accounts: Set of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack. Maximum of 1000 accounts.
        :param pulumi.Input[Sequence[pulumi.Input[Union['OrganizationConformancePackInputParameterArgs', 'OrganizationConformancePackInputParameterArgsDict']]]] input_parameters: Set of configuration blocks describing input parameters passed to the conformance pack template. Documented below. When configured, the parameters must also be included in the `template_body` or in the template stored in Amazon S3 if using `template_s3_uri`.
        :param pulumi.Input[str] name: The name of the organization conformance pack. Must begin with a letter and contain from 1 to 128 alphanumeric characters and hyphens.
        :param pulumi.Input[str] template_body: A string containing full conformance pack template body. Maximum length of 51200. Drift detection is not possible with this argument.
        :param pulumi.Input[str] template_s3_uri: Location of file, e.g., `s3://bucketname/prefix`, containing the template body. The uri must point to the conformance pack template that is located in an Amazon S3 bucket in the same region as the conformance pack. Maximum length of 1024. Drift detection is not possible with this argument.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[OrganizationConformancePackArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Config Organization Conformance Pack. More information can be found in the [Managing Conformance Packs Across all Accounts in Your Organization](https://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-organization-apis.html) and [AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html) documentation. Example conformance pack templates may be found in the [AWS Config Rules Repository](https://github.com/awslabs/aws-config-rules/tree/master/aws-config-conformance-packs).

        > **NOTE:** This resource must be created in the Organization master account or a delegated administrator account, and the Organization must have all features enabled. Every Organization account except those configured in the `excluded_accounts` argument must have a Configuration Recorder with proper IAM permissions before the Organization Conformance Pack will successfully create or update. See also the `cfg.Recorder` resource.

        ## Example Usage

        ### Using Template Body

        ```python
        import pulumi
        import pulumi_aws as aws

        example_organization = aws.organizations.Organization("example",
            aws_service_access_principals=["config-multiaccountsetup.amazonaws.com"],
            feature_set="ALL")
        example = aws.cfg.OrganizationConformancePack("example",
            name="example",
            input_parameters=[{
                "parameter_name": "AccessKeysRotatedParameterMaxAccessKeyAge",
                "parameter_value": "90",
            }],
            template_body=\"\"\"Parameters:
          AccessKeysRotatedParameterMaxAccessKeyAge:
            Type: String
        Resources:
          IAMPasswordPolicy:
            Properties:
              ConfigRuleName: IAMPasswordPolicy
              Source:
                Owner: AWS
                SourceIdentifier: IAM_PASSWORD_POLICY
            Type: AWS::Config::ConfigRule
        \"\"\",
            opts = pulumi.ResourceOptions(depends_on=[
                    example_aws_config_configuration_recorder,
                    example_organization,
                ]))
        ```

        ### Using Template S3 URI

        ```python
        import pulumi
        import pulumi_aws as aws

        example_organization = aws.organizations.Organization("example",
            aws_service_access_principals=["config-multiaccountsetup.amazonaws.com"],
            feature_set="ALL")
        example_bucket_v2 = aws.s3.BucketV2("example", bucket="example")
        example_bucket_objectv2 = aws.s3.BucketObjectv2("example",
            bucket=example_bucket_v2.id,
            key="example-key",
            content=\"\"\"Resources:
          IAMPasswordPolicy:
            Properties:
              ConfigRuleName: IAMPasswordPolicy
              Source:
                Owner: AWS
                SourceIdentifier: IAM_PASSWORD_POLICY
            Type: AWS::Config::ConfigRule
        \"\"\")
        example = aws.cfg.OrganizationConformancePack("example",
            name="example",
            template_s3_uri=pulumi.Output.all(
                bucket=example_bucket_v2.bucket,
                key=example_bucket_objectv2.key
        ).apply(lambda resolved_outputs: f"s3://{resolved_outputs['bucket']}/{resolved_outputs['key']}")
        ,
            opts = pulumi.ResourceOptions(depends_on=[
                    example_aws_config_configuration_recorder,
                    example_organization,
                ]))
        ```

        ## Import

        Using `pulumi import`, import Config Organization Conformance Packs using the `name`. For example:

        ```sh
        $ pulumi import aws:cfg/organizationConformancePack:OrganizationConformancePack example example
        ```

        :param str resource_name: The name of the resource.
        :param OrganizationConformancePackArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationConformancePackArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delivery_s3_bucket: Optional[pulumi.Input[str]] = None,
                 delivery_s3_key_prefix: Optional[pulumi.Input[str]] = None,
                 excluded_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 input_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['OrganizationConformancePackInputParameterArgs', 'OrganizationConformancePackInputParameterArgsDict']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 template_body: Optional[pulumi.Input[str]] = None,
                 template_s3_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OrganizationConformancePackArgs.__new__(OrganizationConformancePackArgs)

            __props__.__dict__["delivery_s3_bucket"] = delivery_s3_bucket
            __props__.__dict__["delivery_s3_key_prefix"] = delivery_s3_key_prefix
            __props__.__dict__["excluded_accounts"] = excluded_accounts
            __props__.__dict__["input_parameters"] = input_parameters
            __props__.__dict__["name"] = name
            __props__.__dict__["template_body"] = template_body
            __props__.__dict__["template_s3_uri"] = template_s3_uri
            __props__.__dict__["arn"] = None
        super(OrganizationConformancePack, __self__).__init__(
            'aws:cfg/organizationConformancePack:OrganizationConformancePack',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            delivery_s3_bucket: Optional[pulumi.Input[str]] = None,
            delivery_s3_key_prefix: Optional[pulumi.Input[str]] = None,
            excluded_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            input_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['OrganizationConformancePackInputParameterArgs', 'OrganizationConformancePackInputParameterArgsDict']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            template_body: Optional[pulumi.Input[str]] = None,
            template_s3_uri: Optional[pulumi.Input[str]] = None) -> 'OrganizationConformancePack':
        """
        Get an existing OrganizationConformancePack resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the organization conformance pack.
        :param pulumi.Input[str] delivery_s3_bucket: Amazon S3 bucket where AWS Config stores conformance pack templates. Delivery bucket must begin with `awsconfigconforms` prefix. Maximum length of 63.
        :param pulumi.Input[str] delivery_s3_key_prefix: The prefix for the Amazon S3 bucket. Maximum length of 1024.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] excluded_accounts: Set of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack. Maximum of 1000 accounts.
        :param pulumi.Input[Sequence[pulumi.Input[Union['OrganizationConformancePackInputParameterArgs', 'OrganizationConformancePackInputParameterArgsDict']]]] input_parameters: Set of configuration blocks describing input parameters passed to the conformance pack template. Documented below. When configured, the parameters must also be included in the `template_body` or in the template stored in Amazon S3 if using `template_s3_uri`.
        :param pulumi.Input[str] name: The name of the organization conformance pack. Must begin with a letter and contain from 1 to 128 alphanumeric characters and hyphens.
        :param pulumi.Input[str] template_body: A string containing full conformance pack template body. Maximum length of 51200. Drift detection is not possible with this argument.
        :param pulumi.Input[str] template_s3_uri: Location of file, e.g., `s3://bucketname/prefix`, containing the template body. The uri must point to the conformance pack template that is located in an Amazon S3 bucket in the same region as the conformance pack. Maximum length of 1024. Drift detection is not possible with this argument.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OrganizationConformancePackState.__new__(_OrganizationConformancePackState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["delivery_s3_bucket"] = delivery_s3_bucket
        __props__.__dict__["delivery_s3_key_prefix"] = delivery_s3_key_prefix
        __props__.__dict__["excluded_accounts"] = excluded_accounts
        __props__.__dict__["input_parameters"] = input_parameters
        __props__.__dict__["name"] = name
        __props__.__dict__["template_body"] = template_body
        __props__.__dict__["template_s3_uri"] = template_s3_uri
        return OrganizationConformancePack(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the organization conformance pack.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="deliveryS3Bucket")
    def delivery_s3_bucket(self) -> pulumi.Output[Optional[str]]:
        """
        Amazon S3 bucket where AWS Config stores conformance pack templates. Delivery bucket must begin with `awsconfigconforms` prefix. Maximum length of 63.
        """
        return pulumi.get(self, "delivery_s3_bucket")

    @property
    @pulumi.getter(name="deliveryS3KeyPrefix")
    def delivery_s3_key_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        The prefix for the Amazon S3 bucket. Maximum length of 1024.
        """
        return pulumi.get(self, "delivery_s3_key_prefix")

    @property
    @pulumi.getter(name="excludedAccounts")
    def excluded_accounts(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Set of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack. Maximum of 1000 accounts.
        """
        return pulumi.get(self, "excluded_accounts")

    @property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> pulumi.Output[Optional[Sequence['outputs.OrganizationConformancePackInputParameter']]]:
        """
        Set of configuration blocks describing input parameters passed to the conformance pack template. Documented below. When configured, the parameters must also be included in the `template_body` or in the template stored in Amazon S3 if using `template_s3_uri`.
        """
        return pulumi.get(self, "input_parameters")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the organization conformance pack. Must begin with a letter and contain from 1 to 128 alphanumeric characters and hyphens.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> pulumi.Output[Optional[str]]:
        """
        A string containing full conformance pack template body. Maximum length of 51200. Drift detection is not possible with this argument.
        """
        return pulumi.get(self, "template_body")

    @property
    @pulumi.getter(name="templateS3Uri")
    def template_s3_uri(self) -> pulumi.Output[Optional[str]]:
        """
        Location of file, e.g., `s3://bucketname/prefix`, containing the template body. The uri must point to the conformance pack template that is located in an Amazon S3 bucket in the same region as the conformance pack. Maximum length of 1024. Drift detection is not possible with this argument.
        """
        return pulumi.get(self, "template_s3_uri")

