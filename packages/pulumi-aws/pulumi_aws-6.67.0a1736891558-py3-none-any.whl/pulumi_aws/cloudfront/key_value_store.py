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

__all__ = ['KeyValueStoreArgs', 'KeyValueStore']

@pulumi.input_type
class KeyValueStoreArgs:
    def __init__(__self__, *,
                 comment: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input['KeyValueStoreTimeoutsArgs']] = None):
        """
        The set of arguments for constructing a KeyValueStore resource.
        :param pulumi.Input[str] comment: Comment.
        :param pulumi.Input[str] name: Unique name for your CloudFront KeyValueStore.
               
               The following arguments are optional:
        """
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Comment.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique name for your CloudFront KeyValueStore.

        The following arguments are optional:
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['KeyValueStoreTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['KeyValueStoreTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


@pulumi.input_type
class _KeyValueStoreState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 last_modified_time: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input['KeyValueStoreTimeoutsArgs']] = None):
        """
        Input properties used for looking up and filtering KeyValueStore resources.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) identifying your CloudFront KeyValueStore.
        :param pulumi.Input[str] comment: Comment.
        :param pulumi.Input[str] etag: ETag hash of the KeyValueStore.
        :param pulumi.Input[str] name: Unique name for your CloudFront KeyValueStore.
               
               The following arguments are optional:
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if last_modified_time is not None:
            pulumi.set(__self__, "last_modified_time", last_modified_time)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) identifying your CloudFront KeyValueStore.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Comment.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        ETag hash of the KeyValueStore.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "last_modified_time")

    @last_modified_time.setter
    def last_modified_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified_time", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique name for your CloudFront KeyValueStore.

        The following arguments are optional:
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['KeyValueStoreTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['KeyValueStoreTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


class KeyValueStore(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input[Union['KeyValueStoreTimeoutsArgs', 'KeyValueStoreTimeoutsArgsDict']]] = None,
                 __props__=None):
        """
        Resource for managing an AWS CloudFront Key Value Store.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.cloudfront.KeyValueStore("example",
            name="ExampleKeyValueStore",
            comment="This is an example key value store")
        ```

        ## Import

        Using `pulumi import`, import CloudFront Key Value Store using the `name`. For example:

        ```sh
        $ pulumi import aws:cloudfront/keyValueStore:KeyValueStore example example_store
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] comment: Comment.
        :param pulumi.Input[str] name: Unique name for your CloudFront KeyValueStore.
               
               The following arguments are optional:
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[KeyValueStoreArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing an AWS CloudFront Key Value Store.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.cloudfront.KeyValueStore("example",
            name="ExampleKeyValueStore",
            comment="This is an example key value store")
        ```

        ## Import

        Using `pulumi import`, import CloudFront Key Value Store using the `name`. For example:

        ```sh
        $ pulumi import aws:cloudfront/keyValueStore:KeyValueStore example example_store
        ```

        :param str resource_name: The name of the resource.
        :param KeyValueStoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KeyValueStoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input[Union['KeyValueStoreTimeoutsArgs', 'KeyValueStoreTimeoutsArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KeyValueStoreArgs.__new__(KeyValueStoreArgs)

            __props__.__dict__["comment"] = comment
            __props__.__dict__["name"] = name
            __props__.__dict__["timeouts"] = timeouts
            __props__.__dict__["arn"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["last_modified_time"] = None
        super(KeyValueStore, __self__).__init__(
            'aws:cloudfront/keyValueStore:KeyValueStore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            comment: Optional[pulumi.Input[str]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            last_modified_time: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            timeouts: Optional[pulumi.Input[Union['KeyValueStoreTimeoutsArgs', 'KeyValueStoreTimeoutsArgsDict']]] = None) -> 'KeyValueStore':
        """
        Get an existing KeyValueStore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) identifying your CloudFront KeyValueStore.
        :param pulumi.Input[str] comment: Comment.
        :param pulumi.Input[str] etag: ETag hash of the KeyValueStore.
        :param pulumi.Input[str] name: Unique name for your CloudFront KeyValueStore.
               
               The following arguments are optional:
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KeyValueStoreState.__new__(_KeyValueStoreState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["comment"] = comment
        __props__.__dict__["etag"] = etag
        __props__.__dict__["last_modified_time"] = last_modified_time
        __props__.__dict__["name"] = name
        __props__.__dict__["timeouts"] = timeouts
        return KeyValueStore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) identifying your CloudFront KeyValueStore.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        Comment.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        ETag hash of the KeyValueStore.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Unique name for your CloudFront KeyValueStore.

        The following arguments are optional:
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional['outputs.KeyValueStoreTimeouts']]:
        return pulumi.get(self, "timeouts")

