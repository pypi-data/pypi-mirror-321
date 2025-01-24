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
    'GetBucketPolicyResult',
    'AwaitableGetBucketPolicyResult',
    'get_bucket_policy',
    'get_bucket_policy_output',
]

@pulumi.output_type
class GetBucketPolicyResult:
    """
    A collection of values returned by getBucketPolicy.
    """
    def __init__(__self__, bucket=None, id=None, policy=None):
        if bucket and not isinstance(bucket, str):
            raise TypeError("Expected argument 'bucket' to be a str")
        pulumi.set(__self__, "bucket", bucket)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if policy and not isinstance(policy, str):
            raise TypeError("Expected argument 'policy' to be a str")
        pulumi.set(__self__, "policy", policy)

    @property
    @pulumi.getter
    def bucket(self) -> str:
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def policy(self) -> str:
        """
        IAM bucket policy.
        """
        return pulumi.get(self, "policy")


class AwaitableGetBucketPolicyResult(GetBucketPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBucketPolicyResult(
            bucket=self.bucket,
            id=self.id,
            policy=self.policy)


def get_bucket_policy(bucket: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBucketPolicyResult:
    """
    The bucket policy data source returns IAM policy of an S3 bucket.

    ## Example Usage

    The following example retrieves IAM policy of a specified S3 bucket.

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.s3.get_bucket_policy(bucket="example-bucket-name")
    pulumi.export("foo", example.policy)
    ```


    :param str bucket: Bucket name.
    """
    __args__ = dict()
    __args__['bucket'] = bucket
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:s3/getBucketPolicy:getBucketPolicy', __args__, opts=opts, typ=GetBucketPolicyResult).value

    return AwaitableGetBucketPolicyResult(
        bucket=pulumi.get(__ret__, 'bucket'),
        id=pulumi.get(__ret__, 'id'),
        policy=pulumi.get(__ret__, 'policy'))
def get_bucket_policy_output(bucket: Optional[pulumi.Input[str]] = None,
                             opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetBucketPolicyResult]:
    """
    The bucket policy data source returns IAM policy of an S3 bucket.

    ## Example Usage

    The following example retrieves IAM policy of a specified S3 bucket.

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.s3.get_bucket_policy(bucket="example-bucket-name")
    pulumi.export("foo", example.policy)
    ```


    :param str bucket: Bucket name.
    """
    __args__ = dict()
    __args__['bucket'] = bucket
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:s3/getBucketPolicy:getBucketPolicy', __args__, opts=opts, typ=GetBucketPolicyResult)
    return __ret__.apply(lambda __response__: GetBucketPolicyResult(
        bucket=pulumi.get(__response__, 'bucket'),
        id=pulumi.get(__response__, 'id'),
        policy=pulumi.get(__response__, 'policy')))
