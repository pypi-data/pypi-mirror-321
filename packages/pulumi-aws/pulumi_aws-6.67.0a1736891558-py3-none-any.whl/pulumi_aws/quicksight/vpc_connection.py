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

__all__ = ['VpcConnectionArgs', 'VpcConnection']

@pulumi.input_type
class VpcConnectionArgs:
    def __init__(__self__, *,
                 role_arn: pulumi.Input[str],
                 security_group_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 vpc_connection_id: pulumi.Input[str],
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 dns_resolvers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeouts: Optional[pulumi.Input['VpcConnectionTimeoutsArgs']] = None):
        """
        The set of arguments for constructing a VpcConnection resource.
        :param pulumi.Input[str] role_arn: The IAM role to associate with the VPC connection.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: A list of security group IDs for the VPC connection.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: A list of subnet IDs for the VPC connection.
               
               The following arguments are optional:
        :param pulumi.Input[str] vpc_connection_id: The ID of the VPC connection.
        :param pulumi.Input[str] aws_account_id: AWS account ID.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_resolvers: A list of IP addresses of DNS resolver endpoints for the VPC connection.
        :param pulumi.Input[str] name: The display name for the VPC connection.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        pulumi.set(__self__, "role_arn", role_arn)
        pulumi.set(__self__, "security_group_ids", security_group_ids)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        pulumi.set(__self__, "vpc_connection_id", vpc_connection_id)
        if aws_account_id is not None:
            pulumi.set(__self__, "aws_account_id", aws_account_id)
        if dns_resolvers is not None:
            pulumi.set(__self__, "dns_resolvers", dns_resolvers)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        The IAM role to associate with the VPC connection.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of security group IDs for the VPC connection.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of subnet IDs for the VPC connection.

        The following arguments are optional:
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="vpcConnectionId")
    def vpc_connection_id(self) -> pulumi.Input[str]:
        """
        The ID of the VPC connection.
        """
        return pulumi.get(self, "vpc_connection_id")

    @vpc_connection_id.setter
    def vpc_connection_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_connection_id", value)

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        AWS account ID.
        """
        return pulumi.get(self, "aws_account_id")

    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_account_id", value)

    @property
    @pulumi.getter(name="dnsResolvers")
    def dns_resolvers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of IP addresses of DNS resolver endpoints for the VPC connection.
        """
        return pulumi.get(self, "dns_resolvers")

    @dns_resolvers.setter
    def dns_resolvers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dns_resolvers", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name for the VPC connection.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['VpcConnectionTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['VpcConnectionTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


@pulumi.input_type
class _VpcConnectionState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 availability_status: Optional[pulumi.Input[str]] = None,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 dns_resolvers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeouts: Optional[pulumi.Input['VpcConnectionTimeoutsArgs']] = None,
                 vpc_connection_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VpcConnection resources.
        :param pulumi.Input[str] arn: ARN of the VPC connection.
        :param pulumi.Input[str] availability_status: The availability status of the VPC connection. Valid values are `AVAILABLE`, `UNAVAILABLE` or `PARTIALLY_AVAILABLE`.
        :param pulumi.Input[str] aws_account_id: AWS account ID.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_resolvers: A list of IP addresses of DNS resolver endpoints for the VPC connection.
        :param pulumi.Input[str] name: The display name for the VPC connection.
        :param pulumi.Input[str] role_arn: The IAM role to associate with the VPC connection.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: A list of security group IDs for the VPC connection.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: A list of subnet IDs for the VPC connection.
               
               The following arguments are optional:
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] vpc_connection_id: The ID of the VPC connection.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if availability_status is not None:
            pulumi.set(__self__, "availability_status", availability_status)
        if aws_account_id is not None:
            pulumi.set(__self__, "aws_account_id", aws_account_id)
        if dns_resolvers is not None:
            pulumi.set(__self__, "dns_resolvers", dns_resolvers)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
            pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)
        if vpc_connection_id is not None:
            pulumi.set(__self__, "vpc_connection_id", vpc_connection_id)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the VPC connection.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[pulumi.Input[str]]:
        """
        The availability status of the VPC connection. Valid values are `AVAILABLE`, `UNAVAILABLE` or `PARTIALLY_AVAILABLE`.
        """
        return pulumi.get(self, "availability_status")

    @availability_status.setter
    def availability_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_status", value)

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        AWS account ID.
        """
        return pulumi.get(self, "aws_account_id")

    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_account_id", value)

    @property
    @pulumi.getter(name="dnsResolvers")
    def dns_resolvers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of IP addresses of DNS resolver endpoints for the VPC connection.
        """
        return pulumi.get(self, "dns_resolvers")

    @dns_resolvers.setter
    def dns_resolvers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dns_resolvers", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name for the VPC connection.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The IAM role to associate with the VPC connection.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of security group IDs for the VPC connection.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of subnet IDs for the VPC connection.

        The following arguments are optional:
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    @_utilities.deprecated("""Please use `tags` instead.""")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['VpcConnectionTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['VpcConnectionTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)

    @property
    @pulumi.getter(name="vpcConnectionId")
    def vpc_connection_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the VPC connection.
        """
        return pulumi.get(self, "vpc_connection_id")

    @vpc_connection_id.setter
    def vpc_connection_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_connection_id", value)


class VpcConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 dns_resolvers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeouts: Optional[pulumi.Input[Union['VpcConnectionTimeoutsArgs', 'VpcConnectionTimeoutsArgsDict']]] = None,
                 vpc_connection_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource for managing an AWS QuickSight VPC Connection.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        vpc_connection_role = aws.iam.Role("vpc_connection_role",
            assume_role_policy=json.dumps({
                "Version": "2012-10-17",
                "Statement": [{
                    "Effect": "Allow",
                    "Action": "sts:AssumeRole",
                    "Principal": {
                        "Service": "quicksight.amazonaws.com",
                    },
                }],
            }),
            inline_policies=[{
                "name": "QuickSightVPCConnectionRolePolicy",
                "policy": json.dumps({
                    "Version": "2012-10-17",
                    "Statement": [{
                        "Effect": "Allow",
                        "Action": [
                            "ec2:CreateNetworkInterface",
                            "ec2:ModifyNetworkInterfaceAttribute",
                            "ec2:DeleteNetworkInterface",
                            "ec2:DescribeSubnets",
                            "ec2:DescribeSecurityGroups",
                        ],
                        "Resource": ["*"],
                    }],
                }),
            }])
        example = aws.quicksight.VpcConnection("example",
            vpc_connection_id="example-connection-id",
            name="Example Connection",
            role_arn=vpc_connection_role.arn,
            security_group_ids=["sg-00000000000000000"],
            subnet_ids=[
                "subnet-00000000000000000",
                "subnet-00000000000000001",
            ])
        ```

        ## Import

        Using `pulumi import`, import QuickSight VPC connection using the AWS account ID and VPC connection ID separated by commas (`,`). For example:

        ```sh
        $ pulumi import aws:quicksight/vpcConnection:VpcConnection example 123456789012,example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] aws_account_id: AWS account ID.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_resolvers: A list of IP addresses of DNS resolver endpoints for the VPC connection.
        :param pulumi.Input[str] name: The display name for the VPC connection.
        :param pulumi.Input[str] role_arn: The IAM role to associate with the VPC connection.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: A list of security group IDs for the VPC connection.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: A list of subnet IDs for the VPC connection.
               
               The following arguments are optional:
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] vpc_connection_id: The ID of the VPC connection.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpcConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing an AWS QuickSight VPC Connection.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        vpc_connection_role = aws.iam.Role("vpc_connection_role",
            assume_role_policy=json.dumps({
                "Version": "2012-10-17",
                "Statement": [{
                    "Effect": "Allow",
                    "Action": "sts:AssumeRole",
                    "Principal": {
                        "Service": "quicksight.amazonaws.com",
                    },
                }],
            }),
            inline_policies=[{
                "name": "QuickSightVPCConnectionRolePolicy",
                "policy": json.dumps({
                    "Version": "2012-10-17",
                    "Statement": [{
                        "Effect": "Allow",
                        "Action": [
                            "ec2:CreateNetworkInterface",
                            "ec2:ModifyNetworkInterfaceAttribute",
                            "ec2:DeleteNetworkInterface",
                            "ec2:DescribeSubnets",
                            "ec2:DescribeSecurityGroups",
                        ],
                        "Resource": ["*"],
                    }],
                }),
            }])
        example = aws.quicksight.VpcConnection("example",
            vpc_connection_id="example-connection-id",
            name="Example Connection",
            role_arn=vpc_connection_role.arn,
            security_group_ids=["sg-00000000000000000"],
            subnet_ids=[
                "subnet-00000000000000000",
                "subnet-00000000000000001",
            ])
        ```

        ## Import

        Using `pulumi import`, import QuickSight VPC connection using the AWS account ID and VPC connection ID separated by commas (`,`). For example:

        ```sh
        $ pulumi import aws:quicksight/vpcConnection:VpcConnection example 123456789012,example
        ```

        :param str resource_name: The name of the resource.
        :param VpcConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpcConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 dns_resolvers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeouts: Optional[pulumi.Input[Union['VpcConnectionTimeoutsArgs', 'VpcConnectionTimeoutsArgsDict']]] = None,
                 vpc_connection_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpcConnectionArgs.__new__(VpcConnectionArgs)

            __props__.__dict__["aws_account_id"] = aws_account_id
            __props__.__dict__["dns_resolvers"] = dns_resolvers
            __props__.__dict__["name"] = name
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            if security_group_ids is None and not opts.urn:
                raise TypeError("Missing required property 'security_group_ids'")
            __props__.__dict__["security_group_ids"] = security_group_ids
            if subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_ids'")
            __props__.__dict__["subnet_ids"] = subnet_ids
            __props__.__dict__["tags"] = tags
            __props__.__dict__["timeouts"] = timeouts
            if vpc_connection_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_connection_id'")
            __props__.__dict__["vpc_connection_id"] = vpc_connection_id
            __props__.__dict__["arn"] = None
            __props__.__dict__["availability_status"] = None
            __props__.__dict__["tags_all"] = None
        super(VpcConnection, __self__).__init__(
            'aws:quicksight/vpcConnection:VpcConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            availability_status: Optional[pulumi.Input[str]] = None,
            aws_account_id: Optional[pulumi.Input[str]] = None,
            dns_resolvers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            role_arn: Optional[pulumi.Input[str]] = None,
            security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            timeouts: Optional[pulumi.Input[Union['VpcConnectionTimeoutsArgs', 'VpcConnectionTimeoutsArgsDict']]] = None,
            vpc_connection_id: Optional[pulumi.Input[str]] = None) -> 'VpcConnection':
        """
        Get an existing VpcConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: ARN of the VPC connection.
        :param pulumi.Input[str] availability_status: The availability status of the VPC connection. Valid values are `AVAILABLE`, `UNAVAILABLE` or `PARTIALLY_AVAILABLE`.
        :param pulumi.Input[str] aws_account_id: AWS account ID.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_resolvers: A list of IP addresses of DNS resolver endpoints for the VPC connection.
        :param pulumi.Input[str] name: The display name for the VPC connection.
        :param pulumi.Input[str] role_arn: The IAM role to associate with the VPC connection.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: A list of security group IDs for the VPC connection.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: A list of subnet IDs for the VPC connection.
               
               The following arguments are optional:
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] vpc_connection_id: The ID of the VPC connection.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VpcConnectionState.__new__(_VpcConnectionState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["availability_status"] = availability_status
        __props__.__dict__["aws_account_id"] = aws_account_id
        __props__.__dict__["dns_resolvers"] = dns_resolvers
        __props__.__dict__["name"] = name
        __props__.__dict__["role_arn"] = role_arn
        __props__.__dict__["security_group_ids"] = security_group_ids
        __props__.__dict__["subnet_ids"] = subnet_ids
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["timeouts"] = timeouts
        __props__.__dict__["vpc_connection_id"] = vpc_connection_id
        return VpcConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the VPC connection.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> pulumi.Output[str]:
        """
        The availability status of the VPC connection. Valid values are `AVAILABLE`, `UNAVAILABLE` or `PARTIALLY_AVAILABLE`.
        """
        return pulumi.get(self, "availability_status")

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[str]:
        """
        AWS account ID.
        """
        return pulumi.get(self, "aws_account_id")

    @property
    @pulumi.getter(name="dnsResolvers")
    def dns_resolvers(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of IP addresses of DNS resolver endpoints for the VPC connection.
        """
        return pulumi.get(self, "dns_resolvers")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The display name for the VPC connection.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        The IAM role to associate with the VPC connection.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of security group IDs for the VPC connection.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of subnet IDs for the VPC connection.

        The following arguments are optional:
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    @_utilities.deprecated("""Please use `tags` instead.""")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional['outputs.VpcConnectionTimeouts']]:
        return pulumi.get(self, "timeouts")

    @property
    @pulumi.getter(name="vpcConnectionId")
    def vpc_connection_id(self) -> pulumi.Output[str]:
        """
        The ID of the VPC connection.
        """
        return pulumi.get(self, "vpc_connection_id")

