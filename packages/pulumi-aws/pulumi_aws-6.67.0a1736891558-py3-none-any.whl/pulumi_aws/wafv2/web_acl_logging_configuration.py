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

__all__ = ['WebAclLoggingConfigurationArgs', 'WebAclLoggingConfiguration']

@pulumi.input_type
class WebAclLoggingConfigurationArgs:
    def __init__(__self__, *,
                 log_destination_configs: pulumi.Input[Sequence[pulumi.Input[str]]],
                 resource_arn: pulumi.Input[str],
                 logging_filter: Optional[pulumi.Input['WebAclLoggingConfigurationLoggingFilterArgs']] = None,
                 redacted_fields: Optional[pulumi.Input[Sequence[pulumi.Input['WebAclLoggingConfigurationRedactedFieldArgs']]]] = None):
        """
        The set of arguments for constructing a WebAclLoggingConfiguration resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] log_destination_configs: Configuration block that allows you to associate Amazon Kinesis Data Firehose, Cloudwatch Log log group, or S3 bucket Amazon Resource Names (ARNs) with the web ACL. **Note:** data firehose, log group, or bucket name **must** be prefixed with `aws-waf-logs-`, e.g. `aws-waf-logs-example-firehose`, `aws-waf-logs-example-log-group`, or `aws-waf-logs-example-bucket`.
        :param pulumi.Input[str] resource_arn: Amazon Resource Name (ARN) of the web ACL that you want to associate with `log_destination_configs`.
        :param pulumi.Input['WebAclLoggingConfigurationLoggingFilterArgs'] logging_filter: Configuration block that specifies which web requests are kept in the logs and which are dropped. It allows filtering based on the rule action and the web request labels applied by matching rules during web ACL evaluation. For more details, refer to the Logging Filter section below.
        :param pulumi.Input[Sequence[pulumi.Input['WebAclLoggingConfigurationRedactedFieldArgs']]] redacted_fields: Configuration for parts of the request that you want to keep out of the logs. Up to 100 `redacted_fields` blocks are supported. See Redacted Fields below for more details.
        """
        pulumi.set(__self__, "log_destination_configs", log_destination_configs)
        pulumi.set(__self__, "resource_arn", resource_arn)
        if logging_filter is not None:
            pulumi.set(__self__, "logging_filter", logging_filter)
        if redacted_fields is not None:
            pulumi.set(__self__, "redacted_fields", redacted_fields)

    @property
    @pulumi.getter(name="logDestinationConfigs")
    def log_destination_configs(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Configuration block that allows you to associate Amazon Kinesis Data Firehose, Cloudwatch Log log group, or S3 bucket Amazon Resource Names (ARNs) with the web ACL. **Note:** data firehose, log group, or bucket name **must** be prefixed with `aws-waf-logs-`, e.g. `aws-waf-logs-example-firehose`, `aws-waf-logs-example-log-group`, or `aws-waf-logs-example-bucket`.
        """
        return pulumi.get(self, "log_destination_configs")

    @log_destination_configs.setter
    def log_destination_configs(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "log_destination_configs", value)

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[str]:
        """
        Amazon Resource Name (ARN) of the web ACL that you want to associate with `log_destination_configs`.
        """
        return pulumi.get(self, "resource_arn")

    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_arn", value)

    @property
    @pulumi.getter(name="loggingFilter")
    def logging_filter(self) -> Optional[pulumi.Input['WebAclLoggingConfigurationLoggingFilterArgs']]:
        """
        Configuration block that specifies which web requests are kept in the logs and which are dropped. It allows filtering based on the rule action and the web request labels applied by matching rules during web ACL evaluation. For more details, refer to the Logging Filter section below.
        """
        return pulumi.get(self, "logging_filter")

    @logging_filter.setter
    def logging_filter(self, value: Optional[pulumi.Input['WebAclLoggingConfigurationLoggingFilterArgs']]):
        pulumi.set(self, "logging_filter", value)

    @property
    @pulumi.getter(name="redactedFields")
    def redacted_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WebAclLoggingConfigurationRedactedFieldArgs']]]]:
        """
        Configuration for parts of the request that you want to keep out of the logs. Up to 100 `redacted_fields` blocks are supported. See Redacted Fields below for more details.
        """
        return pulumi.get(self, "redacted_fields")

    @redacted_fields.setter
    def redacted_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WebAclLoggingConfigurationRedactedFieldArgs']]]]):
        pulumi.set(self, "redacted_fields", value)


@pulumi.input_type
class _WebAclLoggingConfigurationState:
    def __init__(__self__, *,
                 log_destination_configs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 logging_filter: Optional[pulumi.Input['WebAclLoggingConfigurationLoggingFilterArgs']] = None,
                 redacted_fields: Optional[pulumi.Input[Sequence[pulumi.Input['WebAclLoggingConfigurationRedactedFieldArgs']]]] = None,
                 resource_arn: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WebAclLoggingConfiguration resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] log_destination_configs: Configuration block that allows you to associate Amazon Kinesis Data Firehose, Cloudwatch Log log group, or S3 bucket Amazon Resource Names (ARNs) with the web ACL. **Note:** data firehose, log group, or bucket name **must** be prefixed with `aws-waf-logs-`, e.g. `aws-waf-logs-example-firehose`, `aws-waf-logs-example-log-group`, or `aws-waf-logs-example-bucket`.
        :param pulumi.Input['WebAclLoggingConfigurationLoggingFilterArgs'] logging_filter: Configuration block that specifies which web requests are kept in the logs and which are dropped. It allows filtering based on the rule action and the web request labels applied by matching rules during web ACL evaluation. For more details, refer to the Logging Filter section below.
        :param pulumi.Input[Sequence[pulumi.Input['WebAclLoggingConfigurationRedactedFieldArgs']]] redacted_fields: Configuration for parts of the request that you want to keep out of the logs. Up to 100 `redacted_fields` blocks are supported. See Redacted Fields below for more details.
        :param pulumi.Input[str] resource_arn: Amazon Resource Name (ARN) of the web ACL that you want to associate with `log_destination_configs`.
        """
        if log_destination_configs is not None:
            pulumi.set(__self__, "log_destination_configs", log_destination_configs)
        if logging_filter is not None:
            pulumi.set(__self__, "logging_filter", logging_filter)
        if redacted_fields is not None:
            pulumi.set(__self__, "redacted_fields", redacted_fields)
        if resource_arn is not None:
            pulumi.set(__self__, "resource_arn", resource_arn)

    @property
    @pulumi.getter(name="logDestinationConfigs")
    def log_destination_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Configuration block that allows you to associate Amazon Kinesis Data Firehose, Cloudwatch Log log group, or S3 bucket Amazon Resource Names (ARNs) with the web ACL. **Note:** data firehose, log group, or bucket name **must** be prefixed with `aws-waf-logs-`, e.g. `aws-waf-logs-example-firehose`, `aws-waf-logs-example-log-group`, or `aws-waf-logs-example-bucket`.
        """
        return pulumi.get(self, "log_destination_configs")

    @log_destination_configs.setter
    def log_destination_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "log_destination_configs", value)

    @property
    @pulumi.getter(name="loggingFilter")
    def logging_filter(self) -> Optional[pulumi.Input['WebAclLoggingConfigurationLoggingFilterArgs']]:
        """
        Configuration block that specifies which web requests are kept in the logs and which are dropped. It allows filtering based on the rule action and the web request labels applied by matching rules during web ACL evaluation. For more details, refer to the Logging Filter section below.
        """
        return pulumi.get(self, "logging_filter")

    @logging_filter.setter
    def logging_filter(self, value: Optional[pulumi.Input['WebAclLoggingConfigurationLoggingFilterArgs']]):
        pulumi.set(self, "logging_filter", value)

    @property
    @pulumi.getter(name="redactedFields")
    def redacted_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WebAclLoggingConfigurationRedactedFieldArgs']]]]:
        """
        Configuration for parts of the request that you want to keep out of the logs. Up to 100 `redacted_fields` blocks are supported. See Redacted Fields below for more details.
        """
        return pulumi.get(self, "redacted_fields")

    @redacted_fields.setter
    def redacted_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WebAclLoggingConfigurationRedactedFieldArgs']]]]):
        pulumi.set(self, "redacted_fields", value)

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of the web ACL that you want to associate with `log_destination_configs`.
        """
        return pulumi.get(self, "resource_arn")

    @resource_arn.setter
    def resource_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_arn", value)


class WebAclLoggingConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 log_destination_configs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 logging_filter: Optional[pulumi.Input[Union['WebAclLoggingConfigurationLoggingFilterArgs', 'WebAclLoggingConfigurationLoggingFilterArgsDict']]] = None,
                 redacted_fields: Optional[pulumi.Input[Sequence[pulumi.Input[Union['WebAclLoggingConfigurationRedactedFieldArgs', 'WebAclLoggingConfigurationRedactedFieldArgsDict']]]]] = None,
                 resource_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource creates a WAFv2 Web ACL Logging Configuration.

        !> **WARNING:** When logging from a WAFv2 Web ACL to a CloudWatch Log Group, the WAFv2 service tries to create or update a generic Log Resource Policy named `AWSWAF-LOGS`. However, if there are a large number of Web ACLs or if the account frequently creates and deletes Web ACLs, this policy may exceed the maximum policy size. As a result, this resource type will fail to be created. More details about this issue can be found in this issue. To prevent this issue, you can manage a specific resource policy. Please refer to the example below for managing a CloudWatch Log Group with a managed CloudWatch Log Resource Policy.

        ## Example Usage

        ### With Redacted Fields

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.wafv2.WebAclLoggingConfiguration("example",
            log_destination_configs=[example_aws_kinesis_firehose_delivery_stream["arn"]],
            resource_arn=example_aws_wafv2_web_acl["arn"],
            redacted_fields=[{
                "single_header": {
                    "name": "user-agent",
                },
            }])
        ```

        ### With Logging Filter

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.wafv2.WebAclLoggingConfiguration("example",
            log_destination_configs=[example_aws_kinesis_firehose_delivery_stream["arn"]],
            resource_arn=example_aws_wafv2_web_acl["arn"],
            logging_filter={
                "default_behavior": "KEEP",
                "filters": [
                    {
                        "behavior": "DROP",
                        "conditions": [
                            {
                                "action_condition": {
                                    "action": "COUNT",
                                },
                            },
                            {
                                "label_name_condition": {
                                    "label_name": "awswaf:111122223333:rulegroup:testRules:LabelNameZ",
                                },
                            },
                        ],
                        "requirement": "MEETS_ALL",
                    },
                    {
                        "behavior": "KEEP",
                        "conditions": [{
                            "action_condition": {
                                "action": "ALLOW",
                            },
                        }],
                        "requirement": "MEETS_ANY",
                    },
                ],
            })
        ```

        ## Import

        Using `pulumi import`, import WAFv2 Web ACL Logging Configurations using the ARN of the WAFv2 Web ACL. For example:

        ```sh
        $ pulumi import aws:wafv2/webAclLoggingConfiguration:WebAclLoggingConfiguration example arn:aws:wafv2:us-west-2:123456789012:regional/webacl/test-logs/a1b2c3d4-5678-90ab-cdef
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] log_destination_configs: Configuration block that allows you to associate Amazon Kinesis Data Firehose, Cloudwatch Log log group, or S3 bucket Amazon Resource Names (ARNs) with the web ACL. **Note:** data firehose, log group, or bucket name **must** be prefixed with `aws-waf-logs-`, e.g. `aws-waf-logs-example-firehose`, `aws-waf-logs-example-log-group`, or `aws-waf-logs-example-bucket`.
        :param pulumi.Input[Union['WebAclLoggingConfigurationLoggingFilterArgs', 'WebAclLoggingConfigurationLoggingFilterArgsDict']] logging_filter: Configuration block that specifies which web requests are kept in the logs and which are dropped. It allows filtering based on the rule action and the web request labels applied by matching rules during web ACL evaluation. For more details, refer to the Logging Filter section below.
        :param pulumi.Input[Sequence[pulumi.Input[Union['WebAclLoggingConfigurationRedactedFieldArgs', 'WebAclLoggingConfigurationRedactedFieldArgsDict']]]] redacted_fields: Configuration for parts of the request that you want to keep out of the logs. Up to 100 `redacted_fields` blocks are supported. See Redacted Fields below for more details.
        :param pulumi.Input[str] resource_arn: Amazon Resource Name (ARN) of the web ACL that you want to associate with `log_destination_configs`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebAclLoggingConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource creates a WAFv2 Web ACL Logging Configuration.

        !> **WARNING:** When logging from a WAFv2 Web ACL to a CloudWatch Log Group, the WAFv2 service tries to create or update a generic Log Resource Policy named `AWSWAF-LOGS`. However, if there are a large number of Web ACLs or if the account frequently creates and deletes Web ACLs, this policy may exceed the maximum policy size. As a result, this resource type will fail to be created. More details about this issue can be found in this issue. To prevent this issue, you can manage a specific resource policy. Please refer to the example below for managing a CloudWatch Log Group with a managed CloudWatch Log Resource Policy.

        ## Example Usage

        ### With Redacted Fields

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.wafv2.WebAclLoggingConfiguration("example",
            log_destination_configs=[example_aws_kinesis_firehose_delivery_stream["arn"]],
            resource_arn=example_aws_wafv2_web_acl["arn"],
            redacted_fields=[{
                "single_header": {
                    "name": "user-agent",
                },
            }])
        ```

        ### With Logging Filter

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.wafv2.WebAclLoggingConfiguration("example",
            log_destination_configs=[example_aws_kinesis_firehose_delivery_stream["arn"]],
            resource_arn=example_aws_wafv2_web_acl["arn"],
            logging_filter={
                "default_behavior": "KEEP",
                "filters": [
                    {
                        "behavior": "DROP",
                        "conditions": [
                            {
                                "action_condition": {
                                    "action": "COUNT",
                                },
                            },
                            {
                                "label_name_condition": {
                                    "label_name": "awswaf:111122223333:rulegroup:testRules:LabelNameZ",
                                },
                            },
                        ],
                        "requirement": "MEETS_ALL",
                    },
                    {
                        "behavior": "KEEP",
                        "conditions": [{
                            "action_condition": {
                                "action": "ALLOW",
                            },
                        }],
                        "requirement": "MEETS_ANY",
                    },
                ],
            })
        ```

        ## Import

        Using `pulumi import`, import WAFv2 Web ACL Logging Configurations using the ARN of the WAFv2 Web ACL. For example:

        ```sh
        $ pulumi import aws:wafv2/webAclLoggingConfiguration:WebAclLoggingConfiguration example arn:aws:wafv2:us-west-2:123456789012:regional/webacl/test-logs/a1b2c3d4-5678-90ab-cdef
        ```

        :param str resource_name: The name of the resource.
        :param WebAclLoggingConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebAclLoggingConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 log_destination_configs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 logging_filter: Optional[pulumi.Input[Union['WebAclLoggingConfigurationLoggingFilterArgs', 'WebAclLoggingConfigurationLoggingFilterArgsDict']]] = None,
                 redacted_fields: Optional[pulumi.Input[Sequence[pulumi.Input[Union['WebAclLoggingConfigurationRedactedFieldArgs', 'WebAclLoggingConfigurationRedactedFieldArgsDict']]]]] = None,
                 resource_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WebAclLoggingConfigurationArgs.__new__(WebAclLoggingConfigurationArgs)

            if log_destination_configs is None and not opts.urn:
                raise TypeError("Missing required property 'log_destination_configs'")
            __props__.__dict__["log_destination_configs"] = log_destination_configs
            __props__.__dict__["logging_filter"] = logging_filter
            __props__.__dict__["redacted_fields"] = redacted_fields
            if resource_arn is None and not opts.urn:
                raise TypeError("Missing required property 'resource_arn'")
            __props__.__dict__["resource_arn"] = resource_arn
        super(WebAclLoggingConfiguration, __self__).__init__(
            'aws:wafv2/webAclLoggingConfiguration:WebAclLoggingConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            log_destination_configs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            logging_filter: Optional[pulumi.Input[Union['WebAclLoggingConfigurationLoggingFilterArgs', 'WebAclLoggingConfigurationLoggingFilterArgsDict']]] = None,
            redacted_fields: Optional[pulumi.Input[Sequence[pulumi.Input[Union['WebAclLoggingConfigurationRedactedFieldArgs', 'WebAclLoggingConfigurationRedactedFieldArgsDict']]]]] = None,
            resource_arn: Optional[pulumi.Input[str]] = None) -> 'WebAclLoggingConfiguration':
        """
        Get an existing WebAclLoggingConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] log_destination_configs: Configuration block that allows you to associate Amazon Kinesis Data Firehose, Cloudwatch Log log group, or S3 bucket Amazon Resource Names (ARNs) with the web ACL. **Note:** data firehose, log group, or bucket name **must** be prefixed with `aws-waf-logs-`, e.g. `aws-waf-logs-example-firehose`, `aws-waf-logs-example-log-group`, or `aws-waf-logs-example-bucket`.
        :param pulumi.Input[Union['WebAclLoggingConfigurationLoggingFilterArgs', 'WebAclLoggingConfigurationLoggingFilterArgsDict']] logging_filter: Configuration block that specifies which web requests are kept in the logs and which are dropped. It allows filtering based on the rule action and the web request labels applied by matching rules during web ACL evaluation. For more details, refer to the Logging Filter section below.
        :param pulumi.Input[Sequence[pulumi.Input[Union['WebAclLoggingConfigurationRedactedFieldArgs', 'WebAclLoggingConfigurationRedactedFieldArgsDict']]]] redacted_fields: Configuration for parts of the request that you want to keep out of the logs. Up to 100 `redacted_fields` blocks are supported. See Redacted Fields below for more details.
        :param pulumi.Input[str] resource_arn: Amazon Resource Name (ARN) of the web ACL that you want to associate with `log_destination_configs`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WebAclLoggingConfigurationState.__new__(_WebAclLoggingConfigurationState)

        __props__.__dict__["log_destination_configs"] = log_destination_configs
        __props__.__dict__["logging_filter"] = logging_filter
        __props__.__dict__["redacted_fields"] = redacted_fields
        __props__.__dict__["resource_arn"] = resource_arn
        return WebAclLoggingConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="logDestinationConfigs")
    def log_destination_configs(self) -> pulumi.Output[Sequence[str]]:
        """
        Configuration block that allows you to associate Amazon Kinesis Data Firehose, Cloudwatch Log log group, or S3 bucket Amazon Resource Names (ARNs) with the web ACL. **Note:** data firehose, log group, or bucket name **must** be prefixed with `aws-waf-logs-`, e.g. `aws-waf-logs-example-firehose`, `aws-waf-logs-example-log-group`, or `aws-waf-logs-example-bucket`.
        """
        return pulumi.get(self, "log_destination_configs")

    @property
    @pulumi.getter(name="loggingFilter")
    def logging_filter(self) -> pulumi.Output[Optional['outputs.WebAclLoggingConfigurationLoggingFilter']]:
        """
        Configuration block that specifies which web requests are kept in the logs and which are dropped. It allows filtering based on the rule action and the web request labels applied by matching rules during web ACL evaluation. For more details, refer to the Logging Filter section below.
        """
        return pulumi.get(self, "logging_filter")

    @property
    @pulumi.getter(name="redactedFields")
    def redacted_fields(self) -> pulumi.Output[Optional[Sequence['outputs.WebAclLoggingConfigurationRedactedField']]]:
        """
        Configuration for parts of the request that you want to keep out of the logs. Up to 100 `redacted_fields` blocks are supported. See Redacted Fields below for more details.
        """
        return pulumi.get(self, "redacted_fields")

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the web ACL that you want to associate with `log_destination_configs`.
        """
        return pulumi.get(self, "resource_arn")

