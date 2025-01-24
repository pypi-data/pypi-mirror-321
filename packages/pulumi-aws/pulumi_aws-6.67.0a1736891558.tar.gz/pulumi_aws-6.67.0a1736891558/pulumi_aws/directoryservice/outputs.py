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
    'DirectoryConnectSettings',
    'DirectoryVpcSettings',
    'ServiceRegionVpcSettings',
    'SharedDirectoryTarget',
    'GetDirectoryConnectSettingResult',
    'GetDirectoryRadiusSettingResult',
    'GetDirectoryVpcSettingResult',
]

@pulumi.output_type
class DirectoryConnectSettings(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "customerDnsIps":
            suggest = "customer_dns_ips"
        elif key == "customerUsername":
            suggest = "customer_username"
        elif key == "subnetIds":
            suggest = "subnet_ids"
        elif key == "vpcId":
            suggest = "vpc_id"
        elif key == "availabilityZones":
            suggest = "availability_zones"
        elif key == "connectIps":
            suggest = "connect_ips"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DirectoryConnectSettings. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DirectoryConnectSettings.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DirectoryConnectSettings.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 customer_dns_ips: Sequence[str],
                 customer_username: str,
                 subnet_ids: Sequence[str],
                 vpc_id: str,
                 availability_zones: Optional[Sequence[str]] = None,
                 connect_ips: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] customer_dns_ips: The DNS IP addresses of the domain to connect to.
        :param str customer_username: The username corresponding to the password provided.
        :param Sequence[str] subnet_ids: The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).
        :param str vpc_id: The identifier of the VPC that the directory is in.
        :param Sequence[str] connect_ips: The IP addresses of the AD Connector servers.
        """
        pulumi.set(__self__, "customer_dns_ips", customer_dns_ips)
        pulumi.set(__self__, "customer_username", customer_username)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        pulumi.set(__self__, "vpc_id", vpc_id)
        if availability_zones is not None:
            pulumi.set(__self__, "availability_zones", availability_zones)
        if connect_ips is not None:
            pulumi.set(__self__, "connect_ips", connect_ips)

    @property
    @pulumi.getter(name="customerDnsIps")
    def customer_dns_ips(self) -> Sequence[str]:
        """
        The DNS IP addresses of the domain to connect to.
        """
        return pulumi.get(self, "customer_dns_ips")

    @property
    @pulumi.getter(name="customerUsername")
    def customer_username(self) -> str:
        """
        The username corresponding to the password provided.
        """
        return pulumi.get(self, "customer_username")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[str]:
        """
        The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        The identifier of the VPC that the directory is in.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter(name="connectIps")
    def connect_ips(self) -> Optional[Sequence[str]]:
        """
        The IP addresses of the AD Connector servers.
        """
        return pulumi.get(self, "connect_ips")


@pulumi.output_type
class DirectoryVpcSettings(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subnetIds":
            suggest = "subnet_ids"
        elif key == "vpcId":
            suggest = "vpc_id"
        elif key == "availabilityZones":
            suggest = "availability_zones"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DirectoryVpcSettings. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DirectoryVpcSettings.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DirectoryVpcSettings.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 subnet_ids: Sequence[str],
                 vpc_id: str,
                 availability_zones: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] subnet_ids: The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).
        :param str vpc_id: The identifier of the VPC that the directory is in.
        """
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        pulumi.set(__self__, "vpc_id", vpc_id)
        if availability_zones is not None:
            pulumi.set(__self__, "availability_zones", availability_zones)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[str]:
        """
        The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        The identifier of the VPC that the directory is in.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "availability_zones")


@pulumi.output_type
class ServiceRegionVpcSettings(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subnetIds":
            suggest = "subnet_ids"
        elif key == "vpcId":
            suggest = "vpc_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceRegionVpcSettings. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceRegionVpcSettings.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceRegionVpcSettings.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 subnet_ids: Sequence[str],
                 vpc_id: str):
        """
        :param Sequence[str] subnet_ids: The identifiers of the subnets for the directory servers.
        :param str vpc_id: The identifier of the VPC in which to create the directory.
        """
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[str]:
        """
        The identifiers of the subnets for the directory servers.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        The identifier of the VPC in which to create the directory.
        """
        return pulumi.get(self, "vpc_id")


@pulumi.output_type
class SharedDirectoryTarget(dict):
    def __init__(__self__, *,
                 id: str,
                 type: Optional[str] = None):
        """
        :param str id: Identifier of the directory consumer account.
        :param str type: Type of identifier to be used in the `id` field. Valid value is `ACCOUNT`. Default is `ACCOUNT`.
        """
        pulumi.set(__self__, "id", id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Identifier of the directory consumer account.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Type of identifier to be used in the `id` field. Valid value is `ACCOUNT`. Default is `ACCOUNT`.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetDirectoryConnectSettingResult(dict):
    def __init__(__self__, *,
                 availability_zones: Sequence[str],
                 connect_ips: Sequence[str],
                 customer_dns_ips: Sequence[str],
                 customer_username: str,
                 subnet_ids: Sequence[str],
                 vpc_id: str):
        """
        :param Sequence[str] connect_ips: IP addresses of the AD Connector servers.
        :param Sequence[str] customer_dns_ips: DNS IP addresses of the domain to connect to.
        :param str customer_username: Username corresponding to the password provided.
        :param Sequence[str] subnet_ids: Identifiers of the subnets for the connector servers (2 subnets in 2 different AZs).
        :param str vpc_id: ID of the VPC that the connector is in.
        """
        pulumi.set(__self__, "availability_zones", availability_zones)
        pulumi.set(__self__, "connect_ips", connect_ips)
        pulumi.set(__self__, "customer_dns_ips", customer_dns_ips)
        pulumi.set(__self__, "customer_username", customer_username)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[str]:
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter(name="connectIps")
    def connect_ips(self) -> Sequence[str]:
        """
        IP addresses of the AD Connector servers.
        """
        return pulumi.get(self, "connect_ips")

    @property
    @pulumi.getter(name="customerDnsIps")
    def customer_dns_ips(self) -> Sequence[str]:
        """
        DNS IP addresses of the domain to connect to.
        """
        return pulumi.get(self, "customer_dns_ips")

    @property
    @pulumi.getter(name="customerUsername")
    def customer_username(self) -> str:
        """
        Username corresponding to the password provided.
        """
        return pulumi.get(self, "customer_username")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[str]:
        """
        Identifiers of the subnets for the connector servers (2 subnets in 2 different AZs).
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        ID of the VPC that the connector is in.
        """
        return pulumi.get(self, "vpc_id")


@pulumi.output_type
class GetDirectoryRadiusSettingResult(dict):
    def __init__(__self__, *,
                 authentication_protocol: str,
                 display_label: str,
                 radius_port: int,
                 radius_retries: int,
                 radius_servers: Sequence[str],
                 radius_timeout: int,
                 use_same_username: bool):
        """
        :param str authentication_protocol: The protocol specified for your RADIUS endpoints.
        :param str display_label: Display label.
        :param int radius_port: Port that your RADIUS server is using for communications.
        :param int radius_retries: Maximum number of times that communication with the RADIUS server is attempted.
        :param Sequence[str] radius_servers: Set of strings that contains the fully qualified domain name (FQDN) or IP addresses of the RADIUS server endpoints, or the FQDN or IP addresses of your RADIUS server load balancer.
        :param int radius_timeout: Amount of time, in seconds, to wait for the RADIUS server to respond.
        :param bool use_same_username: Not currently used.
        """
        pulumi.set(__self__, "authentication_protocol", authentication_protocol)
        pulumi.set(__self__, "display_label", display_label)
        pulumi.set(__self__, "radius_port", radius_port)
        pulumi.set(__self__, "radius_retries", radius_retries)
        pulumi.set(__self__, "radius_servers", radius_servers)
        pulumi.set(__self__, "radius_timeout", radius_timeout)
        pulumi.set(__self__, "use_same_username", use_same_username)

    @property
    @pulumi.getter(name="authenticationProtocol")
    def authentication_protocol(self) -> str:
        """
        The protocol specified for your RADIUS endpoints.
        """
        return pulumi.get(self, "authentication_protocol")

    @property
    @pulumi.getter(name="displayLabel")
    def display_label(self) -> str:
        """
        Display label.
        """
        return pulumi.get(self, "display_label")

    @property
    @pulumi.getter(name="radiusPort")
    def radius_port(self) -> int:
        """
        Port that your RADIUS server is using for communications.
        """
        return pulumi.get(self, "radius_port")

    @property
    @pulumi.getter(name="radiusRetries")
    def radius_retries(self) -> int:
        """
        Maximum number of times that communication with the RADIUS server is attempted.
        """
        return pulumi.get(self, "radius_retries")

    @property
    @pulumi.getter(name="radiusServers")
    def radius_servers(self) -> Sequence[str]:
        """
        Set of strings that contains the fully qualified domain name (FQDN) or IP addresses of the RADIUS server endpoints, or the FQDN or IP addresses of your RADIUS server load balancer.
        """
        return pulumi.get(self, "radius_servers")

    @property
    @pulumi.getter(name="radiusTimeout")
    def radius_timeout(self) -> int:
        """
        Amount of time, in seconds, to wait for the RADIUS server to respond.
        """
        return pulumi.get(self, "radius_timeout")

    @property
    @pulumi.getter(name="useSameUsername")
    def use_same_username(self) -> bool:
        """
        Not currently used.
        """
        return pulumi.get(self, "use_same_username")


@pulumi.output_type
class GetDirectoryVpcSettingResult(dict):
    def __init__(__self__, *,
                 availability_zones: Sequence[str],
                 subnet_ids: Sequence[str],
                 vpc_id: str):
        """
        :param Sequence[str] subnet_ids: Identifiers of the subnets for the connector servers (2 subnets in 2 different AZs).
        :param str vpc_id: ID of the VPC that the connector is in.
        """
        pulumi.set(__self__, "availability_zones", availability_zones)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[str]:
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[str]:
        """
        Identifiers of the subnets for the connector servers (2 subnets in 2 different AZs).
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        ID of the VPC that the connector is in.
        """
        return pulumi.get(self, "vpc_id")


