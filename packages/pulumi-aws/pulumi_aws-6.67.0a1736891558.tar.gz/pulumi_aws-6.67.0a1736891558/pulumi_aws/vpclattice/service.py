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

__all__ = ['ServiceArgs', 'Service']

@pulumi.input_type
class ServiceArgs:
    def __init__(__self__, *,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 custom_domain_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Service resource.
        :param pulumi.Input[str] auth_type: Type of IAM policy. Either `NONE` or `AWS_IAM`.
        :param pulumi.Input[str] certificate_arn: Amazon Resource Name (ARN) of the certificate.
        :param pulumi.Input[str] custom_domain_name: Custom domain name of the service.
        :param pulumi.Input[str] name: Name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.Must be between 3 and 40 characters in length.
               
               The following arguments are optional:
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value mapping of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        if auth_type is not None:
            pulumi.set(__self__, "auth_type", auth_type)
        if certificate_arn is not None:
            pulumi.set(__self__, "certificate_arn", certificate_arn)
        if custom_domain_name is not None:
            pulumi.set(__self__, "custom_domain_name", custom_domain_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of IAM policy. Either `NONE` or `AWS_IAM`.
        """
        return pulumi.get(self, "auth_type")

    @auth_type.setter
    def auth_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_type", value)

    @property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of the certificate.
        """
        return pulumi.get(self, "certificate_arn")

    @certificate_arn.setter
    def certificate_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_arn", value)

    @property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Custom domain name of the service.
        """
        return pulumi.get(self, "custom_domain_name")

    @custom_domain_name.setter
    def custom_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_domain_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.Must be between 3 and 40 characters in length.

        The following arguments are optional:
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value mapping of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ServiceState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 custom_domain_name: Optional[pulumi.Input[str]] = None,
                 dns_entries: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceDnsEntryArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Service resources.
        :param pulumi.Input[str] arn: ARN of the service.
        :param pulumi.Input[str] auth_type: Type of IAM policy. Either `NONE` or `AWS_IAM`.
        :param pulumi.Input[str] certificate_arn: Amazon Resource Name (ARN) of the certificate.
        :param pulumi.Input[str] custom_domain_name: Custom domain name of the service.
        :param pulumi.Input[Sequence[pulumi.Input['ServiceDnsEntryArgs']]] dns_entries: DNS name of the service.
        :param pulumi.Input[str] name: Name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.Must be between 3 and 40 characters in length.
               
               The following arguments are optional:
        :param pulumi.Input[str] status: Status of the service.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value mapping of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if auth_type is not None:
            pulumi.set(__self__, "auth_type", auth_type)
        if certificate_arn is not None:
            pulumi.set(__self__, "certificate_arn", certificate_arn)
        if custom_domain_name is not None:
            pulumi.set(__self__, "custom_domain_name", custom_domain_name)
        if dns_entries is not None:
            pulumi.set(__self__, "dns_entries", dns_entries)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
            pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the service.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of IAM policy. Either `NONE` or `AWS_IAM`.
        """
        return pulumi.get(self, "auth_type")

    @auth_type.setter
    def auth_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_type", value)

    @property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of the certificate.
        """
        return pulumi.get(self, "certificate_arn")

    @certificate_arn.setter
    def certificate_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_arn", value)

    @property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Custom domain name of the service.
        """
        return pulumi.get(self, "custom_domain_name")

    @custom_domain_name.setter
    def custom_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_domain_name", value)

    @property
    @pulumi.getter(name="dnsEntries")
    def dns_entries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceDnsEntryArgs']]]]:
        """
        DNS name of the service.
        """
        return pulumi.get(self, "dns_entries")

    @dns_entries.setter
    def dns_entries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceDnsEntryArgs']]]]):
        pulumi.set(self, "dns_entries", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.Must be between 3 and 40 characters in length.

        The following arguments are optional:
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the service.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value mapping of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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
        Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


class Service(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 custom_domain_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Resource for managing an AWS VPC Lattice Service.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.vpclattice.Service("example",
            name="example",
            auth_type="AWS_IAM",
            custom_domain_name="example.com")
        ```

        ## Import

        Using `pulumi import`, import VPC Lattice Service using the `id`. For example:

        ```sh
        $ pulumi import aws:vpclattice/service:Service example svc-06728e2357ea55f8a
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_type: Type of IAM policy. Either `NONE` or `AWS_IAM`.
        :param pulumi.Input[str] certificate_arn: Amazon Resource Name (ARN) of the certificate.
        :param pulumi.Input[str] custom_domain_name: Custom domain name of the service.
        :param pulumi.Input[str] name: Name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.Must be between 3 and 40 characters in length.
               
               The following arguments are optional:
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value mapping of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ServiceArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing an AWS VPC Lattice Service.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.vpclattice.Service("example",
            name="example",
            auth_type="AWS_IAM",
            custom_domain_name="example.com")
        ```

        ## Import

        Using `pulumi import`, import VPC Lattice Service using the `id`. For example:

        ```sh
        $ pulumi import aws:vpclattice/service:Service example svc-06728e2357ea55f8a
        ```

        :param str resource_name: The name of the resource.
        :param ServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 custom_domain_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceArgs.__new__(ServiceArgs)

            __props__.__dict__["auth_type"] = auth_type
            __props__.__dict__["certificate_arn"] = certificate_arn
            __props__.__dict__["custom_domain_name"] = custom_domain_name
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["dns_entries"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["tags_all"] = None
        super(Service, __self__).__init__(
            'aws:vpclattice/service:Service',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            auth_type: Optional[pulumi.Input[str]] = None,
            certificate_arn: Optional[pulumi.Input[str]] = None,
            custom_domain_name: Optional[pulumi.Input[str]] = None,
            dns_entries: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ServiceDnsEntryArgs', 'ServiceDnsEntryArgsDict']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Service':
        """
        Get an existing Service resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: ARN of the service.
        :param pulumi.Input[str] auth_type: Type of IAM policy. Either `NONE` or `AWS_IAM`.
        :param pulumi.Input[str] certificate_arn: Amazon Resource Name (ARN) of the certificate.
        :param pulumi.Input[str] custom_domain_name: Custom domain name of the service.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ServiceDnsEntryArgs', 'ServiceDnsEntryArgsDict']]]] dns_entries: DNS name of the service.
        :param pulumi.Input[str] name: Name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.Must be between 3 and 40 characters in length.
               
               The following arguments are optional:
        :param pulumi.Input[str] status: Status of the service.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value mapping of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServiceState.__new__(_ServiceState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["auth_type"] = auth_type
        __props__.__dict__["certificate_arn"] = certificate_arn
        __props__.__dict__["custom_domain_name"] = custom_domain_name
        __props__.__dict__["dns_entries"] = dns_entries
        __props__.__dict__["name"] = name
        __props__.__dict__["status"] = status
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return Service(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the service.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Output[str]:
        """
        Type of IAM policy. Either `NONE` or `AWS_IAM`.
        """
        return pulumi.get(self, "auth_type")

    @property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> pulumi.Output[Optional[str]]:
        """
        Amazon Resource Name (ARN) of the certificate.
        """
        return pulumi.get(self, "certificate_arn")

    @property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> pulumi.Output[Optional[str]]:
        """
        Custom domain name of the service.
        """
        return pulumi.get(self, "custom_domain_name")

    @property
    @pulumi.getter(name="dnsEntries")
    def dns_entries(self) -> pulumi.Output[Sequence['outputs.ServiceDnsEntry']]:
        """
        DNS name of the service.
        """
        return pulumi.get(self, "dns_entries")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.Must be between 3 and 40 characters in length.

        The following arguments are optional:
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the service.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value mapping of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    @_utilities.deprecated("""Please use `tags` instead.""")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

