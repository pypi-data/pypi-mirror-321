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

__all__ = ['HostedZoneDnsSecArgs', 'HostedZoneDnsSec']

@pulumi.input_type
class HostedZoneDnsSecArgs:
    def __init__(__self__, *,
                 hosted_zone_id: pulumi.Input[str],
                 signing_status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a HostedZoneDnsSec resource.
        :param pulumi.Input[str] hosted_zone_id: Identifier of the Route 53 Hosted Zone.
               
               The following arguments are optional:
        :param pulumi.Input[str] signing_status: Hosted Zone signing status. Valid values: `SIGNING`, `NOT_SIGNING`. Defaults to `SIGNING`.
        """
        pulumi.set(__self__, "hosted_zone_id", hosted_zone_id)
        if signing_status is not None:
            pulumi.set(__self__, "signing_status", signing_status)

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Input[str]:
        """
        Identifier of the Route 53 Hosted Zone.

        The following arguments are optional:
        """
        return pulumi.get(self, "hosted_zone_id")

    @hosted_zone_id.setter
    def hosted_zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "hosted_zone_id", value)

    @property
    @pulumi.getter(name="signingStatus")
    def signing_status(self) -> Optional[pulumi.Input[str]]:
        """
        Hosted Zone signing status. Valid values: `SIGNING`, `NOT_SIGNING`. Defaults to `SIGNING`.
        """
        return pulumi.get(self, "signing_status")

    @signing_status.setter
    def signing_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "signing_status", value)


@pulumi.input_type
class _HostedZoneDnsSecState:
    def __init__(__self__, *,
                 hosted_zone_id: Optional[pulumi.Input[str]] = None,
                 signing_status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering HostedZoneDnsSec resources.
        :param pulumi.Input[str] hosted_zone_id: Identifier of the Route 53 Hosted Zone.
               
               The following arguments are optional:
        :param pulumi.Input[str] signing_status: Hosted Zone signing status. Valid values: `SIGNING`, `NOT_SIGNING`. Defaults to `SIGNING`.
        """
        if hosted_zone_id is not None:
            pulumi.set(__self__, "hosted_zone_id", hosted_zone_id)
        if signing_status is not None:
            pulumi.set(__self__, "signing_status", signing_status)

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the Route 53 Hosted Zone.

        The following arguments are optional:
        """
        return pulumi.get(self, "hosted_zone_id")

    @hosted_zone_id.setter
    def hosted_zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hosted_zone_id", value)

    @property
    @pulumi.getter(name="signingStatus")
    def signing_status(self) -> Optional[pulumi.Input[str]]:
        """
        Hosted Zone signing status. Valid values: `SIGNING`, `NOT_SIGNING`. Defaults to `SIGNING`.
        """
        return pulumi.get(self, "signing_status")

    @signing_status.setter
    def signing_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "signing_status", value)


class HostedZoneDnsSec(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hosted_zone_id: Optional[pulumi.Input[str]] = None,
                 signing_status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages Route 53 Hosted Zone Domain Name System Security Extensions (DNSSEC). For more information about managing DNSSEC in Route 53, see the [Route 53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec.html).

        !> **WARNING:** If you disable DNSSEC signing for your hosted zone before the DNS changes have propagated, your domain could become unavailable on the internet. When you remove the DS records, you must wait until the longest TTL for the DS records that you remove has expired before you complete the step to disable DNSSEC signing. Please refer to the [Route 53 Developer Guide - Disable DNSSEC](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-disable.html) for a detailed breakdown on the steps required to disable DNSSEC safely for a hosted zone.

        > **Note:** Route53 hosted zones are global resources, and as such any `kms.Key` that you use as part of a signing key needs to be located in the `us-east-1` region. In the example below, the main AWS provider declaration is for `us-east-1`, however if you are provisioning your AWS resources in a different region, you will need to specify a provider alias and use that attached to the `kms.Key` resource as described in the provider alias documentation.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        current = aws.get_caller_identity()
        example = aws.kms.Key("example",
            customer_master_key_spec="ECC_NIST_P256",
            deletion_window_in_days=7,
            key_usage="SIGN_VERIFY",
            policy=json.dumps({
                "Statement": [
                    {
                        "Action": [
                            "kms:DescribeKey",
                            "kms:GetPublicKey",
                            "kms:Sign",
                            "kms:Verify",
                        ],
                        "Effect": "Allow",
                        "Principal": {
                            "Service": "dnssec-route53.amazonaws.com",
                        },
                        "Resource": "*",
                        "Sid": "Allow Route 53 DNSSEC Service",
                    },
                    {
                        "Action": "kms:*",
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": f"arn:aws:iam::{current.account_id}:root",
                        },
                        "Resource": "*",
                        "Sid": "Enable IAM User Permissions",
                    },
                ],
                "Version": "2012-10-17",
            }))
        example_zone = aws.route53.Zone("example", name="example.com")
        example_key_signing_key = aws.route53.KeySigningKey("example",
            hosted_zone_id=example_zone.id,
            key_management_service_arn=example.arn,
            name="example")
        example_hosted_zone_dns_sec = aws.route53.HostedZoneDnsSec("example", hosted_zone_id=example_key_signing_key.hosted_zone_id,
        opts = pulumi.ResourceOptions(depends_on=[example_key_signing_key]))
        ```

        ## Import

        Using `pulumi import`, import `aws_route53_hosted_zone_dnssec` resources using the Route 53 Hosted Zone identifier. For example:

        ```sh
        $ pulumi import aws:route53/hostedZoneDnsSec:HostedZoneDnsSec example Z1D633PJN98FT9
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hosted_zone_id: Identifier of the Route 53 Hosted Zone.
               
               The following arguments are optional:
        :param pulumi.Input[str] signing_status: Hosted Zone signing status. Valid values: `SIGNING`, `NOT_SIGNING`. Defaults to `SIGNING`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HostedZoneDnsSecArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages Route 53 Hosted Zone Domain Name System Security Extensions (DNSSEC). For more information about managing DNSSEC in Route 53, see the [Route 53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec.html).

        !> **WARNING:** If you disable DNSSEC signing for your hosted zone before the DNS changes have propagated, your domain could become unavailable on the internet. When you remove the DS records, you must wait until the longest TTL for the DS records that you remove has expired before you complete the step to disable DNSSEC signing. Please refer to the [Route 53 Developer Guide - Disable DNSSEC](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-disable.html) for a detailed breakdown on the steps required to disable DNSSEC safely for a hosted zone.

        > **Note:** Route53 hosted zones are global resources, and as such any `kms.Key` that you use as part of a signing key needs to be located in the `us-east-1` region. In the example below, the main AWS provider declaration is for `us-east-1`, however if you are provisioning your AWS resources in a different region, you will need to specify a provider alias and use that attached to the `kms.Key` resource as described in the provider alias documentation.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        current = aws.get_caller_identity()
        example = aws.kms.Key("example",
            customer_master_key_spec="ECC_NIST_P256",
            deletion_window_in_days=7,
            key_usage="SIGN_VERIFY",
            policy=json.dumps({
                "Statement": [
                    {
                        "Action": [
                            "kms:DescribeKey",
                            "kms:GetPublicKey",
                            "kms:Sign",
                            "kms:Verify",
                        ],
                        "Effect": "Allow",
                        "Principal": {
                            "Service": "dnssec-route53.amazonaws.com",
                        },
                        "Resource": "*",
                        "Sid": "Allow Route 53 DNSSEC Service",
                    },
                    {
                        "Action": "kms:*",
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": f"arn:aws:iam::{current.account_id}:root",
                        },
                        "Resource": "*",
                        "Sid": "Enable IAM User Permissions",
                    },
                ],
                "Version": "2012-10-17",
            }))
        example_zone = aws.route53.Zone("example", name="example.com")
        example_key_signing_key = aws.route53.KeySigningKey("example",
            hosted_zone_id=example_zone.id,
            key_management_service_arn=example.arn,
            name="example")
        example_hosted_zone_dns_sec = aws.route53.HostedZoneDnsSec("example", hosted_zone_id=example_key_signing_key.hosted_zone_id,
        opts = pulumi.ResourceOptions(depends_on=[example_key_signing_key]))
        ```

        ## Import

        Using `pulumi import`, import `aws_route53_hosted_zone_dnssec` resources using the Route 53 Hosted Zone identifier. For example:

        ```sh
        $ pulumi import aws:route53/hostedZoneDnsSec:HostedZoneDnsSec example Z1D633PJN98FT9
        ```

        :param str resource_name: The name of the resource.
        :param HostedZoneDnsSecArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HostedZoneDnsSecArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hosted_zone_id: Optional[pulumi.Input[str]] = None,
                 signing_status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HostedZoneDnsSecArgs.__new__(HostedZoneDnsSecArgs)

            if hosted_zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'hosted_zone_id'")
            __props__.__dict__["hosted_zone_id"] = hosted_zone_id
            __props__.__dict__["signing_status"] = signing_status
        super(HostedZoneDnsSec, __self__).__init__(
            'aws:route53/hostedZoneDnsSec:HostedZoneDnsSec',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            hosted_zone_id: Optional[pulumi.Input[str]] = None,
            signing_status: Optional[pulumi.Input[str]] = None) -> 'HostedZoneDnsSec':
        """
        Get an existing HostedZoneDnsSec resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hosted_zone_id: Identifier of the Route 53 Hosted Zone.
               
               The following arguments are optional:
        :param pulumi.Input[str] signing_status: Hosted Zone signing status. Valid values: `SIGNING`, `NOT_SIGNING`. Defaults to `SIGNING`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HostedZoneDnsSecState.__new__(_HostedZoneDnsSecState)

        __props__.__dict__["hosted_zone_id"] = hosted_zone_id
        __props__.__dict__["signing_status"] = signing_status
        return HostedZoneDnsSec(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Output[str]:
        """
        Identifier of the Route 53 Hosted Zone.

        The following arguments are optional:
        """
        return pulumi.get(self, "hosted_zone_id")

    @property
    @pulumi.getter(name="signingStatus")
    def signing_status(self) -> pulumi.Output[Optional[str]]:
        """
        Hosted Zone signing status. Valid values: `SIGNING`, `NOT_SIGNING`. Defaults to `SIGNING`.
        """
        return pulumi.get(self, "signing_status")

