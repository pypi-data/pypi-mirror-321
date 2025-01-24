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

__all__ = ['ConditionalForwaderArgs', 'ConditionalForwader']

@pulumi.input_type
class ConditionalForwaderArgs:
    def __init__(__self__, *,
                 directory_id: pulumi.Input[str],
                 dns_ips: pulumi.Input[Sequence[pulumi.Input[str]]],
                 remote_domain_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a ConditionalForwader resource.
        :param pulumi.Input[str] directory_id: ID of directory.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_ips: A list of forwarder IP addresses.
        :param pulumi.Input[str] remote_domain_name: The fully qualified domain name of the remote domain for which forwarders will be used.
        """
        pulumi.set(__self__, "directory_id", directory_id)
        pulumi.set(__self__, "dns_ips", dns_ips)
        pulumi.set(__self__, "remote_domain_name", remote_domain_name)

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Input[str]:
        """
        ID of directory.
        """
        return pulumi.get(self, "directory_id")

    @directory_id.setter
    def directory_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "directory_id", value)

    @property
    @pulumi.getter(name="dnsIps")
    def dns_ips(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of forwarder IP addresses.
        """
        return pulumi.get(self, "dns_ips")

    @dns_ips.setter
    def dns_ips(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "dns_ips", value)

    @property
    @pulumi.getter(name="remoteDomainName")
    def remote_domain_name(self) -> pulumi.Input[str]:
        """
        The fully qualified domain name of the remote domain for which forwarders will be used.
        """
        return pulumi.get(self, "remote_domain_name")

    @remote_domain_name.setter
    def remote_domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "remote_domain_name", value)


@pulumi.input_type
class _ConditionalForwaderState:
    def __init__(__self__, *,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 dns_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 remote_domain_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ConditionalForwader resources.
        :param pulumi.Input[str] directory_id: ID of directory.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_ips: A list of forwarder IP addresses.
        :param pulumi.Input[str] remote_domain_name: The fully qualified domain name of the remote domain for which forwarders will be used.
        """
        if directory_id is not None:
            pulumi.set(__self__, "directory_id", directory_id)
        if dns_ips is not None:
            pulumi.set(__self__, "dns_ips", dns_ips)
        if remote_domain_name is not None:
            pulumi.set(__self__, "remote_domain_name", remote_domain_name)

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of directory.
        """
        return pulumi.get(self, "directory_id")

    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory_id", value)

    @property
    @pulumi.getter(name="dnsIps")
    def dns_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of forwarder IP addresses.
        """
        return pulumi.get(self, "dns_ips")

    @dns_ips.setter
    def dns_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dns_ips", value)

    @property
    @pulumi.getter(name="remoteDomainName")
    def remote_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The fully qualified domain name of the remote domain for which forwarders will be used.
        """
        return pulumi.get(self, "remote_domain_name")

    @remote_domain_name.setter
    def remote_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remote_domain_name", value)


class ConditionalForwader(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 dns_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 remote_domain_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a conditional forwarder for managed Microsoft AD in AWS Directory Service.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.directoryservice.ConditionalForwader("example",
            directory_id=ad["id"],
            remote_domain_name="example.com",
            dns_ips=[
                "8.8.8.8",
                "8.8.4.4",
            ])
        ```

        ## Import

        Using `pulumi import`, import conditional forwarders using the directory id and remote_domain_name. For example:

        ```sh
        $ pulumi import aws:directoryservice/conditionalForwader:ConditionalForwader example d-1234567890:example.com
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] directory_id: ID of directory.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_ips: A list of forwarder IP addresses.
        :param pulumi.Input[str] remote_domain_name: The fully qualified domain name of the remote domain for which forwarders will be used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConditionalForwaderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a conditional forwarder for managed Microsoft AD in AWS Directory Service.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.directoryservice.ConditionalForwader("example",
            directory_id=ad["id"],
            remote_domain_name="example.com",
            dns_ips=[
                "8.8.8.8",
                "8.8.4.4",
            ])
        ```

        ## Import

        Using `pulumi import`, import conditional forwarders using the directory id and remote_domain_name. For example:

        ```sh
        $ pulumi import aws:directoryservice/conditionalForwader:ConditionalForwader example d-1234567890:example.com
        ```

        :param str resource_name: The name of the resource.
        :param ConditionalForwaderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConditionalForwaderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 dns_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 remote_domain_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConditionalForwaderArgs.__new__(ConditionalForwaderArgs)

            if directory_id is None and not opts.urn:
                raise TypeError("Missing required property 'directory_id'")
            __props__.__dict__["directory_id"] = directory_id
            if dns_ips is None and not opts.urn:
                raise TypeError("Missing required property 'dns_ips'")
            __props__.__dict__["dns_ips"] = dns_ips
            if remote_domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'remote_domain_name'")
            __props__.__dict__["remote_domain_name"] = remote_domain_name
        super(ConditionalForwader, __self__).__init__(
            'aws:directoryservice/conditionalForwader:ConditionalForwader',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            directory_id: Optional[pulumi.Input[str]] = None,
            dns_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            remote_domain_name: Optional[pulumi.Input[str]] = None) -> 'ConditionalForwader':
        """
        Get an existing ConditionalForwader resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] directory_id: ID of directory.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_ips: A list of forwarder IP addresses.
        :param pulumi.Input[str] remote_domain_name: The fully qualified domain name of the remote domain for which forwarders will be used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConditionalForwaderState.__new__(_ConditionalForwaderState)

        __props__.__dict__["directory_id"] = directory_id
        __props__.__dict__["dns_ips"] = dns_ips
        __props__.__dict__["remote_domain_name"] = remote_domain_name
        return ConditionalForwader(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Output[str]:
        """
        ID of directory.
        """
        return pulumi.get(self, "directory_id")

    @property
    @pulumi.getter(name="dnsIps")
    def dns_ips(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of forwarder IP addresses.
        """
        return pulumi.get(self, "dns_ips")

    @property
    @pulumi.getter(name="remoteDomainName")
    def remote_domain_name(self) -> pulumi.Output[str]:
        """
        The fully qualified domain name of the remote domain for which forwarders will be used.
        """
        return pulumi.get(self, "remote_domain_name")

