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

__all__ = [
    'GetLogDataProtectionPolicyDocumentResult',
    'AwaitableGetLogDataProtectionPolicyDocumentResult',
    'get_log_data_protection_policy_document',
    'get_log_data_protection_policy_document_output',
]

@pulumi.output_type
class GetLogDataProtectionPolicyDocumentResult:
    """
    A collection of values returned by getLogDataProtectionPolicyDocument.
    """
    def __init__(__self__, description=None, id=None, json=None, name=None, statements=None, version=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if json and not isinstance(json, str):
            raise TypeError("Expected argument 'json' to be a str")
        pulumi.set(__self__, "json", json)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if statements and not isinstance(statements, list):
            raise TypeError("Expected argument 'statements' to be a list")
        pulumi.set(__self__, "statements", statements)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def json(self) -> str:
        """
        Standard JSON policy document rendered based on the arguments above.
        """
        return pulumi.get(self, "json")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def statements(self) -> Sequence['outputs.GetLogDataProtectionPolicyDocumentStatementResult']:
        return pulumi.get(self, "statements")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        return pulumi.get(self, "version")


class AwaitableGetLogDataProtectionPolicyDocumentResult(GetLogDataProtectionPolicyDocumentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLogDataProtectionPolicyDocumentResult(
            description=self.description,
            id=self.id,
            json=self.json,
            name=self.name,
            statements=self.statements,
            version=self.version)


def get_log_data_protection_policy_document(description: Optional[str] = None,
                                            name: Optional[str] = None,
                                            statements: Optional[Sequence[Union['GetLogDataProtectionPolicyDocumentStatementArgs', 'GetLogDataProtectionPolicyDocumentStatementArgsDict']]] = None,
                                            version: Optional[str] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLogDataProtectionPolicyDocumentResult:
    """
    Generates a CloudWatch Log Group Data Protection Policy document in JSON format for use with the `cloudwatch.LogDataProtectionPolicy` resource.

    > For more information about data protection policies, see the [Help protect sensitive log data with masking](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.cloudwatch.get_log_data_protection_policy_document(name="Example",
        statements=[
            {
                "sid": "Audit",
                "data_identifiers": [
                    "arn:aws:dataprotection::aws:data-identifier/EmailAddress",
                    "arn:aws:dataprotection::aws:data-identifier/DriversLicense-US",
                ],
                "operation": {
                    "audit": {
                        "findings_destination": {
                            "cloudwatch_logs": {
                                "log_group": audit["name"],
                            },
                            "firehose": {
                                "delivery_stream": audit_aws_kinesis_firehose_delivery_stream["name"],
                            },
                            "s3": {
                                "bucket": audit_aws_s3_bucket["bucket"],
                            },
                        },
                    },
                },
            },
            {
                "sid": "Deidentify",
                "data_identifiers": [
                    "arn:aws:dataprotection::aws:data-identifier/EmailAddress",
                    "arn:aws:dataprotection::aws:data-identifier/DriversLicense-US",
                ],
                "operation": {
                    "deidentify": {
                        "mask_config": {},
                    },
                },
            },
        ])
    example_log_data_protection_policy = aws.cloudwatch.LogDataProtectionPolicy("example",
        log_group_name=example_aws_cloudwatch_log_group["name"],
        policy_document=example.json)
    ```


    :param str name: The name of the data protection policy document.
    :param Sequence[Union['GetLogDataProtectionPolicyDocumentStatementArgs', 'GetLogDataProtectionPolicyDocumentStatementArgsDict']] statements: Configures the data protection policy.
           
           > There must be exactly two statements: the first with an `audit` operation, and the second with a `deidentify` operation.
           
           The following arguments are optional:
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['name'] = name
    __args__['statements'] = statements
    __args__['version'] = version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:cloudwatch/getLogDataProtectionPolicyDocument:getLogDataProtectionPolicyDocument', __args__, opts=opts, typ=GetLogDataProtectionPolicyDocumentResult).value

    return AwaitableGetLogDataProtectionPolicyDocumentResult(
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        json=pulumi.get(__ret__, 'json'),
        name=pulumi.get(__ret__, 'name'),
        statements=pulumi.get(__ret__, 'statements'),
        version=pulumi.get(__ret__, 'version'))
def get_log_data_protection_policy_document_output(description: Optional[pulumi.Input[Optional[str]]] = None,
                                                   name: Optional[pulumi.Input[str]] = None,
                                                   statements: Optional[pulumi.Input[Sequence[Union['GetLogDataProtectionPolicyDocumentStatementArgs', 'GetLogDataProtectionPolicyDocumentStatementArgsDict']]]] = None,
                                                   version: Optional[pulumi.Input[Optional[str]]] = None,
                                                   opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetLogDataProtectionPolicyDocumentResult]:
    """
    Generates a CloudWatch Log Group Data Protection Policy document in JSON format for use with the `cloudwatch.LogDataProtectionPolicy` resource.

    > For more information about data protection policies, see the [Help protect sensitive log data with masking](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.cloudwatch.get_log_data_protection_policy_document(name="Example",
        statements=[
            {
                "sid": "Audit",
                "data_identifiers": [
                    "arn:aws:dataprotection::aws:data-identifier/EmailAddress",
                    "arn:aws:dataprotection::aws:data-identifier/DriversLicense-US",
                ],
                "operation": {
                    "audit": {
                        "findings_destination": {
                            "cloudwatch_logs": {
                                "log_group": audit["name"],
                            },
                            "firehose": {
                                "delivery_stream": audit_aws_kinesis_firehose_delivery_stream["name"],
                            },
                            "s3": {
                                "bucket": audit_aws_s3_bucket["bucket"],
                            },
                        },
                    },
                },
            },
            {
                "sid": "Deidentify",
                "data_identifiers": [
                    "arn:aws:dataprotection::aws:data-identifier/EmailAddress",
                    "arn:aws:dataprotection::aws:data-identifier/DriversLicense-US",
                ],
                "operation": {
                    "deidentify": {
                        "mask_config": {},
                    },
                },
            },
        ])
    example_log_data_protection_policy = aws.cloudwatch.LogDataProtectionPolicy("example",
        log_group_name=example_aws_cloudwatch_log_group["name"],
        policy_document=example.json)
    ```


    :param str name: The name of the data protection policy document.
    :param Sequence[Union['GetLogDataProtectionPolicyDocumentStatementArgs', 'GetLogDataProtectionPolicyDocumentStatementArgsDict']] statements: Configures the data protection policy.
           
           > There must be exactly two statements: the first with an `audit` operation, and the second with a `deidentify` operation.
           
           The following arguments are optional:
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['name'] = name
    __args__['statements'] = statements
    __args__['version'] = version
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:cloudwatch/getLogDataProtectionPolicyDocument:getLogDataProtectionPolicyDocument', __args__, opts=opts, typ=GetLogDataProtectionPolicyDocumentResult)
    return __ret__.apply(lambda __response__: GetLogDataProtectionPolicyDocumentResult(
        description=pulumi.get(__response__, 'description'),
        id=pulumi.get(__response__, 'id'),
        json=pulumi.get(__response__, 'json'),
        name=pulumi.get(__response__, 'name'),
        statements=pulumi.get(__response__, 'statements'),
        version=pulumi.get(__response__, 'version')))
