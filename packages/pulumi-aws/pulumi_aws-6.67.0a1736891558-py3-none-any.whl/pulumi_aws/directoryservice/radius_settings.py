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

__all__ = ['RadiusSettingsArgs', 'RadiusSettings']

@pulumi.input_type
class RadiusSettingsArgs:
    def __init__(__self__, *,
                 authentication_protocol: pulumi.Input[str],
                 directory_id: pulumi.Input[str],
                 display_label: pulumi.Input[str],
                 radius_port: pulumi.Input[int],
                 radius_retries: pulumi.Input[int],
                 radius_servers: pulumi.Input[Sequence[pulumi.Input[str]]],
                 radius_timeout: pulumi.Input[int],
                 shared_secret: pulumi.Input[str],
                 use_same_username: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a RadiusSettings resource.
        :param pulumi.Input[str] authentication_protocol: The protocol specified for your RADIUS endpoints. Valid values: `PAP`, `CHAP`, `MS-CHAPv1`, `MS-CHAPv2`.
        :param pulumi.Input[str] directory_id: The identifier of the directory for which you want to manager RADIUS settings.
        :param pulumi.Input[str] display_label: Display label.
        :param pulumi.Input[int] radius_port: The port that your RADIUS server is using for communications. Your self-managed network must allow inbound traffic over this port from the AWS Directory Service servers.
        :param pulumi.Input[int] radius_retries: The maximum number of times that communication with the RADIUS server is attempted. Minimum value of `0`. Maximum value of `10`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] radius_servers: An array of strings that contains the fully qualified domain name (FQDN) or IP addresses of the RADIUS server endpoints, or the FQDN or IP addresses of your RADIUS server load balancer.
        :param pulumi.Input[int] radius_timeout: The amount of time, in seconds, to wait for the RADIUS server to respond. Minimum value of `1`. Maximum value of `50`.
        :param pulumi.Input[str] shared_secret: Required for enabling RADIUS on the directory.
        :param pulumi.Input[bool] use_same_username: Not currently used.
        """
        pulumi.set(__self__, "authentication_protocol", authentication_protocol)
        pulumi.set(__self__, "directory_id", directory_id)
        pulumi.set(__self__, "display_label", display_label)
        pulumi.set(__self__, "radius_port", radius_port)
        pulumi.set(__self__, "radius_retries", radius_retries)
        pulumi.set(__self__, "radius_servers", radius_servers)
        pulumi.set(__self__, "radius_timeout", radius_timeout)
        pulumi.set(__self__, "shared_secret", shared_secret)
        if use_same_username is not None:
            pulumi.set(__self__, "use_same_username", use_same_username)

    @property
    @pulumi.getter(name="authenticationProtocol")
    def authentication_protocol(self) -> pulumi.Input[str]:
        """
        The protocol specified for your RADIUS endpoints. Valid values: `PAP`, `CHAP`, `MS-CHAPv1`, `MS-CHAPv2`.
        """
        return pulumi.get(self, "authentication_protocol")

    @authentication_protocol.setter
    def authentication_protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "authentication_protocol", value)

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Input[str]:
        """
        The identifier of the directory for which you want to manager RADIUS settings.
        """
        return pulumi.get(self, "directory_id")

    @directory_id.setter
    def directory_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "directory_id", value)

    @property
    @pulumi.getter(name="displayLabel")
    def display_label(self) -> pulumi.Input[str]:
        """
        Display label.
        """
        return pulumi.get(self, "display_label")

    @display_label.setter
    def display_label(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_label", value)

    @property
    @pulumi.getter(name="radiusPort")
    def radius_port(self) -> pulumi.Input[int]:
        """
        The port that your RADIUS server is using for communications. Your self-managed network must allow inbound traffic over this port from the AWS Directory Service servers.
        """
        return pulumi.get(self, "radius_port")

    @radius_port.setter
    def radius_port(self, value: pulumi.Input[int]):
        pulumi.set(self, "radius_port", value)

    @property
    @pulumi.getter(name="radiusRetries")
    def radius_retries(self) -> pulumi.Input[int]:
        """
        The maximum number of times that communication with the RADIUS server is attempted. Minimum value of `0`. Maximum value of `10`.
        """
        return pulumi.get(self, "radius_retries")

    @radius_retries.setter
    def radius_retries(self, value: pulumi.Input[int]):
        pulumi.set(self, "radius_retries", value)

    @property
    @pulumi.getter(name="radiusServers")
    def radius_servers(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        An array of strings that contains the fully qualified domain name (FQDN) or IP addresses of the RADIUS server endpoints, or the FQDN or IP addresses of your RADIUS server load balancer.
        """
        return pulumi.get(self, "radius_servers")

    @radius_servers.setter
    def radius_servers(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "radius_servers", value)

    @property
    @pulumi.getter(name="radiusTimeout")
    def radius_timeout(self) -> pulumi.Input[int]:
        """
        The amount of time, in seconds, to wait for the RADIUS server to respond. Minimum value of `1`. Maximum value of `50`.
        """
        return pulumi.get(self, "radius_timeout")

    @radius_timeout.setter
    def radius_timeout(self, value: pulumi.Input[int]):
        pulumi.set(self, "radius_timeout", value)

    @property
    @pulumi.getter(name="sharedSecret")
    def shared_secret(self) -> pulumi.Input[str]:
        """
        Required for enabling RADIUS on the directory.
        """
        return pulumi.get(self, "shared_secret")

    @shared_secret.setter
    def shared_secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "shared_secret", value)

    @property
    @pulumi.getter(name="useSameUsername")
    def use_same_username(self) -> Optional[pulumi.Input[bool]]:
        """
        Not currently used.
        """
        return pulumi.get(self, "use_same_username")

    @use_same_username.setter
    def use_same_username(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_same_username", value)


@pulumi.input_type
class _RadiusSettingsState:
    def __init__(__self__, *,
                 authentication_protocol: Optional[pulumi.Input[str]] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 display_label: Optional[pulumi.Input[str]] = None,
                 radius_port: Optional[pulumi.Input[int]] = None,
                 radius_retries: Optional[pulumi.Input[int]] = None,
                 radius_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 radius_timeout: Optional[pulumi.Input[int]] = None,
                 shared_secret: Optional[pulumi.Input[str]] = None,
                 use_same_username: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering RadiusSettings resources.
        :param pulumi.Input[str] authentication_protocol: The protocol specified for your RADIUS endpoints. Valid values: `PAP`, `CHAP`, `MS-CHAPv1`, `MS-CHAPv2`.
        :param pulumi.Input[str] directory_id: The identifier of the directory for which you want to manager RADIUS settings.
        :param pulumi.Input[str] display_label: Display label.
        :param pulumi.Input[int] radius_port: The port that your RADIUS server is using for communications. Your self-managed network must allow inbound traffic over this port from the AWS Directory Service servers.
        :param pulumi.Input[int] radius_retries: The maximum number of times that communication with the RADIUS server is attempted. Minimum value of `0`. Maximum value of `10`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] radius_servers: An array of strings that contains the fully qualified domain name (FQDN) or IP addresses of the RADIUS server endpoints, or the FQDN or IP addresses of your RADIUS server load balancer.
        :param pulumi.Input[int] radius_timeout: The amount of time, in seconds, to wait for the RADIUS server to respond. Minimum value of `1`. Maximum value of `50`.
        :param pulumi.Input[str] shared_secret: Required for enabling RADIUS on the directory.
        :param pulumi.Input[bool] use_same_username: Not currently used.
        """
        if authentication_protocol is not None:
            pulumi.set(__self__, "authentication_protocol", authentication_protocol)
        if directory_id is not None:
            pulumi.set(__self__, "directory_id", directory_id)
        if display_label is not None:
            pulumi.set(__self__, "display_label", display_label)
        if radius_port is not None:
            pulumi.set(__self__, "radius_port", radius_port)
        if radius_retries is not None:
            pulumi.set(__self__, "radius_retries", radius_retries)
        if radius_servers is not None:
            pulumi.set(__self__, "radius_servers", radius_servers)
        if radius_timeout is not None:
            pulumi.set(__self__, "radius_timeout", radius_timeout)
        if shared_secret is not None:
            pulumi.set(__self__, "shared_secret", shared_secret)
        if use_same_username is not None:
            pulumi.set(__self__, "use_same_username", use_same_username)

    @property
    @pulumi.getter(name="authenticationProtocol")
    def authentication_protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The protocol specified for your RADIUS endpoints. Valid values: `PAP`, `CHAP`, `MS-CHAPv1`, `MS-CHAPv2`.
        """
        return pulumi.get(self, "authentication_protocol")

    @authentication_protocol.setter
    def authentication_protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication_protocol", value)

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the directory for which you want to manager RADIUS settings.
        """
        return pulumi.get(self, "directory_id")

    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory_id", value)

    @property
    @pulumi.getter(name="displayLabel")
    def display_label(self) -> Optional[pulumi.Input[str]]:
        """
        Display label.
        """
        return pulumi.get(self, "display_label")

    @display_label.setter
    def display_label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_label", value)

    @property
    @pulumi.getter(name="radiusPort")
    def radius_port(self) -> Optional[pulumi.Input[int]]:
        """
        The port that your RADIUS server is using for communications. Your self-managed network must allow inbound traffic over this port from the AWS Directory Service servers.
        """
        return pulumi.get(self, "radius_port")

    @radius_port.setter
    def radius_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "radius_port", value)

    @property
    @pulumi.getter(name="radiusRetries")
    def radius_retries(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of times that communication with the RADIUS server is attempted. Minimum value of `0`. Maximum value of `10`.
        """
        return pulumi.get(self, "radius_retries")

    @radius_retries.setter
    def radius_retries(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "radius_retries", value)

    @property
    @pulumi.getter(name="radiusServers")
    def radius_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array of strings that contains the fully qualified domain name (FQDN) or IP addresses of the RADIUS server endpoints, or the FQDN or IP addresses of your RADIUS server load balancer.
        """
        return pulumi.get(self, "radius_servers")

    @radius_servers.setter
    def radius_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "radius_servers", value)

    @property
    @pulumi.getter(name="radiusTimeout")
    def radius_timeout(self) -> Optional[pulumi.Input[int]]:
        """
        The amount of time, in seconds, to wait for the RADIUS server to respond. Minimum value of `1`. Maximum value of `50`.
        """
        return pulumi.get(self, "radius_timeout")

    @radius_timeout.setter
    def radius_timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "radius_timeout", value)

    @property
    @pulumi.getter(name="sharedSecret")
    def shared_secret(self) -> Optional[pulumi.Input[str]]:
        """
        Required for enabling RADIUS on the directory.
        """
        return pulumi.get(self, "shared_secret")

    @shared_secret.setter
    def shared_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shared_secret", value)

    @property
    @pulumi.getter(name="useSameUsername")
    def use_same_username(self) -> Optional[pulumi.Input[bool]]:
        """
        Not currently used.
        """
        return pulumi.get(self, "use_same_username")

    @use_same_username.setter
    def use_same_username(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_same_username", value)


class RadiusSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_protocol: Optional[pulumi.Input[str]] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 display_label: Optional[pulumi.Input[str]] = None,
                 radius_port: Optional[pulumi.Input[int]] = None,
                 radius_retries: Optional[pulumi.Input[int]] = None,
                 radius_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 radius_timeout: Optional[pulumi.Input[int]] = None,
                 shared_secret: Optional[pulumi.Input[str]] = None,
                 use_same_username: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Manages a directory's multi-factor authentication (MFA) using a Remote Authentication Dial In User Service (RADIUS) server.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.directoryservice.RadiusSettings("example",
            directory_id=example_aws_directory_service_directory["id"],
            authentication_protocol="PAP",
            display_label="example",
            radius_port=1812,
            radius_retries=4,
            radius_servers=["10.0.1.5"],
            radius_timeout=1,
            shared_secret="12345678")
        ```

        ## Import

        Using `pulumi import`, import RADIUS settings using the directory ID. For example:

        ```sh
        $ pulumi import aws:directoryservice/radiusSettings:RadiusSettings example d-926724cf57
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication_protocol: The protocol specified for your RADIUS endpoints. Valid values: `PAP`, `CHAP`, `MS-CHAPv1`, `MS-CHAPv2`.
        :param pulumi.Input[str] directory_id: The identifier of the directory for which you want to manager RADIUS settings.
        :param pulumi.Input[str] display_label: Display label.
        :param pulumi.Input[int] radius_port: The port that your RADIUS server is using for communications. Your self-managed network must allow inbound traffic over this port from the AWS Directory Service servers.
        :param pulumi.Input[int] radius_retries: The maximum number of times that communication with the RADIUS server is attempted. Minimum value of `0`. Maximum value of `10`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] radius_servers: An array of strings that contains the fully qualified domain name (FQDN) or IP addresses of the RADIUS server endpoints, or the FQDN or IP addresses of your RADIUS server load balancer.
        :param pulumi.Input[int] radius_timeout: The amount of time, in seconds, to wait for the RADIUS server to respond. Minimum value of `1`. Maximum value of `50`.
        :param pulumi.Input[str] shared_secret: Required for enabling RADIUS on the directory.
        :param pulumi.Input[bool] use_same_username: Not currently used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RadiusSettingsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a directory's multi-factor authentication (MFA) using a Remote Authentication Dial In User Service (RADIUS) server.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.directoryservice.RadiusSettings("example",
            directory_id=example_aws_directory_service_directory["id"],
            authentication_protocol="PAP",
            display_label="example",
            radius_port=1812,
            radius_retries=4,
            radius_servers=["10.0.1.5"],
            radius_timeout=1,
            shared_secret="12345678")
        ```

        ## Import

        Using `pulumi import`, import RADIUS settings using the directory ID. For example:

        ```sh
        $ pulumi import aws:directoryservice/radiusSettings:RadiusSettings example d-926724cf57
        ```

        :param str resource_name: The name of the resource.
        :param RadiusSettingsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RadiusSettingsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_protocol: Optional[pulumi.Input[str]] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 display_label: Optional[pulumi.Input[str]] = None,
                 radius_port: Optional[pulumi.Input[int]] = None,
                 radius_retries: Optional[pulumi.Input[int]] = None,
                 radius_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 radius_timeout: Optional[pulumi.Input[int]] = None,
                 shared_secret: Optional[pulumi.Input[str]] = None,
                 use_same_username: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RadiusSettingsArgs.__new__(RadiusSettingsArgs)

            if authentication_protocol is None and not opts.urn:
                raise TypeError("Missing required property 'authentication_protocol'")
            __props__.__dict__["authentication_protocol"] = authentication_protocol
            if directory_id is None and not opts.urn:
                raise TypeError("Missing required property 'directory_id'")
            __props__.__dict__["directory_id"] = directory_id
            if display_label is None and not opts.urn:
                raise TypeError("Missing required property 'display_label'")
            __props__.__dict__["display_label"] = display_label
            if radius_port is None and not opts.urn:
                raise TypeError("Missing required property 'radius_port'")
            __props__.__dict__["radius_port"] = radius_port
            if radius_retries is None and not opts.urn:
                raise TypeError("Missing required property 'radius_retries'")
            __props__.__dict__["radius_retries"] = radius_retries
            if radius_servers is None and not opts.urn:
                raise TypeError("Missing required property 'radius_servers'")
            __props__.__dict__["radius_servers"] = radius_servers
            if radius_timeout is None and not opts.urn:
                raise TypeError("Missing required property 'radius_timeout'")
            __props__.__dict__["radius_timeout"] = radius_timeout
            if shared_secret is None and not opts.urn:
                raise TypeError("Missing required property 'shared_secret'")
            __props__.__dict__["shared_secret"] = None if shared_secret is None else pulumi.Output.secret(shared_secret)
            __props__.__dict__["use_same_username"] = use_same_username
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["sharedSecret"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(RadiusSettings, __self__).__init__(
            'aws:directoryservice/radiusSettings:RadiusSettings',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authentication_protocol: Optional[pulumi.Input[str]] = None,
            directory_id: Optional[pulumi.Input[str]] = None,
            display_label: Optional[pulumi.Input[str]] = None,
            radius_port: Optional[pulumi.Input[int]] = None,
            radius_retries: Optional[pulumi.Input[int]] = None,
            radius_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            radius_timeout: Optional[pulumi.Input[int]] = None,
            shared_secret: Optional[pulumi.Input[str]] = None,
            use_same_username: Optional[pulumi.Input[bool]] = None) -> 'RadiusSettings':
        """
        Get an existing RadiusSettings resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication_protocol: The protocol specified for your RADIUS endpoints. Valid values: `PAP`, `CHAP`, `MS-CHAPv1`, `MS-CHAPv2`.
        :param pulumi.Input[str] directory_id: The identifier of the directory for which you want to manager RADIUS settings.
        :param pulumi.Input[str] display_label: Display label.
        :param pulumi.Input[int] radius_port: The port that your RADIUS server is using for communications. Your self-managed network must allow inbound traffic over this port from the AWS Directory Service servers.
        :param pulumi.Input[int] radius_retries: The maximum number of times that communication with the RADIUS server is attempted. Minimum value of `0`. Maximum value of `10`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] radius_servers: An array of strings that contains the fully qualified domain name (FQDN) or IP addresses of the RADIUS server endpoints, or the FQDN or IP addresses of your RADIUS server load balancer.
        :param pulumi.Input[int] radius_timeout: The amount of time, in seconds, to wait for the RADIUS server to respond. Minimum value of `1`. Maximum value of `50`.
        :param pulumi.Input[str] shared_secret: Required for enabling RADIUS on the directory.
        :param pulumi.Input[bool] use_same_username: Not currently used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RadiusSettingsState.__new__(_RadiusSettingsState)

        __props__.__dict__["authentication_protocol"] = authentication_protocol
        __props__.__dict__["directory_id"] = directory_id
        __props__.__dict__["display_label"] = display_label
        __props__.__dict__["radius_port"] = radius_port
        __props__.__dict__["radius_retries"] = radius_retries
        __props__.__dict__["radius_servers"] = radius_servers
        __props__.__dict__["radius_timeout"] = radius_timeout
        __props__.__dict__["shared_secret"] = shared_secret
        __props__.__dict__["use_same_username"] = use_same_username
        return RadiusSettings(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authenticationProtocol")
    def authentication_protocol(self) -> pulumi.Output[str]:
        """
        The protocol specified for your RADIUS endpoints. Valid values: `PAP`, `CHAP`, `MS-CHAPv1`, `MS-CHAPv2`.
        """
        return pulumi.get(self, "authentication_protocol")

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Output[str]:
        """
        The identifier of the directory for which you want to manager RADIUS settings.
        """
        return pulumi.get(self, "directory_id")

    @property
    @pulumi.getter(name="displayLabel")
    def display_label(self) -> pulumi.Output[str]:
        """
        Display label.
        """
        return pulumi.get(self, "display_label")

    @property
    @pulumi.getter(name="radiusPort")
    def radius_port(self) -> pulumi.Output[int]:
        """
        The port that your RADIUS server is using for communications. Your self-managed network must allow inbound traffic over this port from the AWS Directory Service servers.
        """
        return pulumi.get(self, "radius_port")

    @property
    @pulumi.getter(name="radiusRetries")
    def radius_retries(self) -> pulumi.Output[int]:
        """
        The maximum number of times that communication with the RADIUS server is attempted. Minimum value of `0`. Maximum value of `10`.
        """
        return pulumi.get(self, "radius_retries")

    @property
    @pulumi.getter(name="radiusServers")
    def radius_servers(self) -> pulumi.Output[Sequence[str]]:
        """
        An array of strings that contains the fully qualified domain name (FQDN) or IP addresses of the RADIUS server endpoints, or the FQDN or IP addresses of your RADIUS server load balancer.
        """
        return pulumi.get(self, "radius_servers")

    @property
    @pulumi.getter(name="radiusTimeout")
    def radius_timeout(self) -> pulumi.Output[int]:
        """
        The amount of time, in seconds, to wait for the RADIUS server to respond. Minimum value of `1`. Maximum value of `50`.
        """
        return pulumi.get(self, "radius_timeout")

    @property
    @pulumi.getter(name="sharedSecret")
    def shared_secret(self) -> pulumi.Output[str]:
        """
        Required for enabling RADIUS on the directory.
        """
        return pulumi.get(self, "shared_secret")

    @property
    @pulumi.getter(name="useSameUsername")
    def use_same_username(self) -> pulumi.Output[Optional[bool]]:
        """
        Not currently used.
        """
        return pulumi.get(self, "use_same_username")

