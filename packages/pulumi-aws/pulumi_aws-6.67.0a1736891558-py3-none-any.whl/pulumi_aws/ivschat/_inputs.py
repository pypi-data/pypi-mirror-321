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
    'LoggingConfigurationDestinationConfigurationArgs',
    'LoggingConfigurationDestinationConfigurationArgsDict',
    'LoggingConfigurationDestinationConfigurationCloudwatchLogsArgs',
    'LoggingConfigurationDestinationConfigurationCloudwatchLogsArgsDict',
    'LoggingConfigurationDestinationConfigurationFirehoseArgs',
    'LoggingConfigurationDestinationConfigurationFirehoseArgsDict',
    'LoggingConfigurationDestinationConfigurationS3Args',
    'LoggingConfigurationDestinationConfigurationS3ArgsDict',
    'RoomMessageReviewHandlerArgs',
    'RoomMessageReviewHandlerArgsDict',
]

MYPY = False

if not MYPY:
    class LoggingConfigurationDestinationConfigurationArgsDict(TypedDict):
        cloudwatch_logs: NotRequired[pulumi.Input['LoggingConfigurationDestinationConfigurationCloudwatchLogsArgsDict']]
        """
        An Amazon CloudWatch Logs destination configuration where chat activity will be logged.
        """
        firehose: NotRequired[pulumi.Input['LoggingConfigurationDestinationConfigurationFirehoseArgsDict']]
        """
        An Amazon Kinesis Data Firehose destination configuration where chat activity will be logged.
        """
        s3: NotRequired[pulumi.Input['LoggingConfigurationDestinationConfigurationS3ArgsDict']]
        """
        An Amazon S3 destination configuration where chat activity will be logged.
        """
elif False:
    LoggingConfigurationDestinationConfigurationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class LoggingConfigurationDestinationConfigurationArgs:
    def __init__(__self__, *,
                 cloudwatch_logs: Optional[pulumi.Input['LoggingConfigurationDestinationConfigurationCloudwatchLogsArgs']] = None,
                 firehose: Optional[pulumi.Input['LoggingConfigurationDestinationConfigurationFirehoseArgs']] = None,
                 s3: Optional[pulumi.Input['LoggingConfigurationDestinationConfigurationS3Args']] = None):
        """
        :param pulumi.Input['LoggingConfigurationDestinationConfigurationCloudwatchLogsArgs'] cloudwatch_logs: An Amazon CloudWatch Logs destination configuration where chat activity will be logged.
        :param pulumi.Input['LoggingConfigurationDestinationConfigurationFirehoseArgs'] firehose: An Amazon Kinesis Data Firehose destination configuration where chat activity will be logged.
        :param pulumi.Input['LoggingConfigurationDestinationConfigurationS3Args'] s3: An Amazon S3 destination configuration where chat activity will be logged.
        """
        if cloudwatch_logs is not None:
            pulumi.set(__self__, "cloudwatch_logs", cloudwatch_logs)
        if firehose is not None:
            pulumi.set(__self__, "firehose", firehose)
        if s3 is not None:
            pulumi.set(__self__, "s3", s3)

    @property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(self) -> Optional[pulumi.Input['LoggingConfigurationDestinationConfigurationCloudwatchLogsArgs']]:
        """
        An Amazon CloudWatch Logs destination configuration where chat activity will be logged.
        """
        return pulumi.get(self, "cloudwatch_logs")

    @cloudwatch_logs.setter
    def cloudwatch_logs(self, value: Optional[pulumi.Input['LoggingConfigurationDestinationConfigurationCloudwatchLogsArgs']]):
        pulumi.set(self, "cloudwatch_logs", value)

    @property
    @pulumi.getter
    def firehose(self) -> Optional[pulumi.Input['LoggingConfigurationDestinationConfigurationFirehoseArgs']]:
        """
        An Amazon Kinesis Data Firehose destination configuration where chat activity will be logged.
        """
        return pulumi.get(self, "firehose")

    @firehose.setter
    def firehose(self, value: Optional[pulumi.Input['LoggingConfigurationDestinationConfigurationFirehoseArgs']]):
        pulumi.set(self, "firehose", value)

    @property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input['LoggingConfigurationDestinationConfigurationS3Args']]:
        """
        An Amazon S3 destination configuration where chat activity will be logged.
        """
        return pulumi.get(self, "s3")

    @s3.setter
    def s3(self, value: Optional[pulumi.Input['LoggingConfigurationDestinationConfigurationS3Args']]):
        pulumi.set(self, "s3", value)


if not MYPY:
    class LoggingConfigurationDestinationConfigurationCloudwatchLogsArgsDict(TypedDict):
        log_group_name: pulumi.Input[str]
        """
        Name of the Amazon Cloudwatch Logs destination where chat activity will be logged.
        """
elif False:
    LoggingConfigurationDestinationConfigurationCloudwatchLogsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class LoggingConfigurationDestinationConfigurationCloudwatchLogsArgs:
    def __init__(__self__, *,
                 log_group_name: pulumi.Input[str]):
        """
        :param pulumi.Input[str] log_group_name: Name of the Amazon Cloudwatch Logs destination where chat activity will be logged.
        """
        pulumi.set(__self__, "log_group_name", log_group_name)

    @property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Amazon Cloudwatch Logs destination where chat activity will be logged.
        """
        return pulumi.get(self, "log_group_name")

    @log_group_name.setter
    def log_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "log_group_name", value)


if not MYPY:
    class LoggingConfigurationDestinationConfigurationFirehoseArgsDict(TypedDict):
        delivery_stream_name: pulumi.Input[str]
        """
        Name of the Amazon Kinesis Firehose delivery stream where chat activity will be logged.
        """
elif False:
    LoggingConfigurationDestinationConfigurationFirehoseArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class LoggingConfigurationDestinationConfigurationFirehoseArgs:
    def __init__(__self__, *,
                 delivery_stream_name: pulumi.Input[str]):
        """
        :param pulumi.Input[str] delivery_stream_name: Name of the Amazon Kinesis Firehose delivery stream where chat activity will be logged.
        """
        pulumi.set(__self__, "delivery_stream_name", delivery_stream_name)

    @property
    @pulumi.getter(name="deliveryStreamName")
    def delivery_stream_name(self) -> pulumi.Input[str]:
        """
        Name of the Amazon Kinesis Firehose delivery stream where chat activity will be logged.
        """
        return pulumi.get(self, "delivery_stream_name")

    @delivery_stream_name.setter
    def delivery_stream_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "delivery_stream_name", value)


if not MYPY:
    class LoggingConfigurationDestinationConfigurationS3ArgsDict(TypedDict):
        bucket_name: pulumi.Input[str]
        """
        Name of the Amazon S3 bucket where chat activity will be logged.

        The following arguments are optional:
        """
elif False:
    LoggingConfigurationDestinationConfigurationS3ArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class LoggingConfigurationDestinationConfigurationS3Args:
    def __init__(__self__, *,
                 bucket_name: pulumi.Input[str]):
        """
        :param pulumi.Input[str] bucket_name: Name of the Amazon S3 bucket where chat activity will be logged.
               
               The following arguments are optional:
        """
        pulumi.set(__self__, "bucket_name", bucket_name)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[str]:
        """
        Name of the Amazon S3 bucket where chat activity will be logged.

        The following arguments are optional:
        """
        return pulumi.get(self, "bucket_name")

    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket_name", value)


if not MYPY:
    class RoomMessageReviewHandlerArgsDict(TypedDict):
        fallback_result: NotRequired[pulumi.Input[str]]
        """
        The fallback behavior (whether the message
        is allowed or denied) if the handler does not return a valid response,
        encounters an error, or times out. Valid values: `ALLOW`, `DENY`.
        """
        uri: NotRequired[pulumi.Input[str]]
        """
        ARN of the lambda message review handler function.
        """
elif False:
    RoomMessageReviewHandlerArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class RoomMessageReviewHandlerArgs:
    def __init__(__self__, *,
                 fallback_result: Optional[pulumi.Input[str]] = None,
                 uri: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] fallback_result: The fallback behavior (whether the message
               is allowed or denied) if the handler does not return a valid response,
               encounters an error, or times out. Valid values: `ALLOW`, `DENY`.
        :param pulumi.Input[str] uri: ARN of the lambda message review handler function.
        """
        if fallback_result is not None:
            pulumi.set(__self__, "fallback_result", fallback_result)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter(name="fallbackResult")
    def fallback_result(self) -> Optional[pulumi.Input[str]]:
        """
        The fallback behavior (whether the message
        is allowed or denied) if the handler does not return a valid response,
        encounters an error, or times out. Valid values: `ALLOW`, `DENY`.
        """
        return pulumi.get(self, "fallback_result")

    @fallback_result.setter
    def fallback_result(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fallback_result", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the lambda message review handler function.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)


