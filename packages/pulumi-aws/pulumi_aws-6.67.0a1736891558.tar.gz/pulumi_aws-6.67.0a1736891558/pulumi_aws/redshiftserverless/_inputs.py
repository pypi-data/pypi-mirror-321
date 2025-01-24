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
    'EndpointAccessVpcEndpointArgs',
    'EndpointAccessVpcEndpointArgsDict',
    'EndpointAccessVpcEndpointNetworkInterfaceArgs',
    'EndpointAccessVpcEndpointNetworkInterfaceArgsDict',
    'WorkgroupConfigParameterArgs',
    'WorkgroupConfigParameterArgsDict',
    'WorkgroupEndpointArgs',
    'WorkgroupEndpointArgsDict',
    'WorkgroupEndpointVpcEndpointArgs',
    'WorkgroupEndpointVpcEndpointArgsDict',
    'WorkgroupEndpointVpcEndpointNetworkInterfaceArgs',
    'WorkgroupEndpointVpcEndpointNetworkInterfaceArgsDict',
]

MYPY = False

if not MYPY:
    class EndpointAccessVpcEndpointArgsDict(TypedDict):
        network_interfaces: NotRequired[pulumi.Input[Sequence[pulumi.Input['EndpointAccessVpcEndpointNetworkInterfaceArgsDict']]]]
        """
        The network interfaces of the endpoint.. See `Network Interface` below.
        """
        vpc_endpoint_id: NotRequired[pulumi.Input[str]]
        """
        The DNS address of the VPC endpoint.
        """
        vpc_id: NotRequired[pulumi.Input[str]]
        """
        The port that Amazon Redshift Serverless listens on.
        """
elif False:
    EndpointAccessVpcEndpointArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class EndpointAccessVpcEndpointArgs:
    def __init__(__self__, *,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input['EndpointAccessVpcEndpointNetworkInterfaceArgs']]]] = None,
                 vpc_endpoint_id: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input['EndpointAccessVpcEndpointNetworkInterfaceArgs']]] network_interfaces: The network interfaces of the endpoint.. See `Network Interface` below.
        :param pulumi.Input[str] vpc_endpoint_id: The DNS address of the VPC endpoint.
        :param pulumi.Input[str] vpc_id: The port that Amazon Redshift Serverless listens on.
        """
        if network_interfaces is not None:
            pulumi.set(__self__, "network_interfaces", network_interfaces)
        if vpc_endpoint_id is not None:
            pulumi.set(__self__, "vpc_endpoint_id", vpc_endpoint_id)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EndpointAccessVpcEndpointNetworkInterfaceArgs']]]]:
        """
        The network interfaces of the endpoint.. See `Network Interface` below.
        """
        return pulumi.get(self, "network_interfaces")

    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EndpointAccessVpcEndpointNetworkInterfaceArgs']]]]):
        pulumi.set(self, "network_interfaces", value)

    @property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[str]]:
        """
        The DNS address of the VPC endpoint.
        """
        return pulumi.get(self, "vpc_endpoint_id")

    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_endpoint_id", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        The port that Amazon Redshift Serverless listens on.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


if not MYPY:
    class EndpointAccessVpcEndpointNetworkInterfaceArgsDict(TypedDict):
        availability_zone: NotRequired[pulumi.Input[str]]
        """
        The availability Zone.
        """
        network_interface_id: NotRequired[pulumi.Input[str]]
        """
        The unique identifier of the network interface.
        """
        private_ip_address: NotRequired[pulumi.Input[str]]
        """
        The IPv4 address of the network interface within the subnet.
        """
        subnet_id: NotRequired[pulumi.Input[str]]
        """
        The unique identifier of the subnet.
        """
elif False:
    EndpointAccessVpcEndpointNetworkInterfaceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class EndpointAccessVpcEndpointNetworkInterfaceArgs:
    def __init__(__self__, *,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 private_ip_address: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] availability_zone: The availability Zone.
        :param pulumi.Input[str] network_interface_id: The unique identifier of the network interface.
        :param pulumi.Input[str] private_ip_address: The IPv4 address of the network interface within the subnet.
        :param pulumi.Input[str] subnet_id: The unique identifier of the subnet.
        """
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if network_interface_id is not None:
            pulumi.set(__self__, "network_interface_id", network_interface_id)
        if private_ip_address is not None:
            pulumi.set(__self__, "private_ip_address", private_ip_address)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The availability Zone.
        """
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier of the network interface.
        """
        return pulumi.get(self, "network_interface_id")

    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_interface_id", value)

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 address of the network interface within the subnet.
        """
        return pulumi.get(self, "private_ip_address")

    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_ip_address", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier of the subnet.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)


if not MYPY:
    class WorkgroupConfigParameterArgsDict(TypedDict):
        parameter_key: pulumi.Input[str]
        """
        The key of the parameter. The options are `auto_mv`, `datestyle`, `enable_case_sensitive_identifier`, `enable_user_activity_logging`, `query_group`, `search_path`, `require_ssl`, `use_fips_ssl`, and [query monitoring metrics](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless) that let you define performance boundaries: `max_query_cpu_time`, `max_query_blocks_read`, `max_scan_row_count`, `max_query_execution_time`, `max_query_queue_time`, `max_query_cpu_usage_percent`, `max_query_temp_blocks_to_disk`, `max_join_row_count` and `max_nested_loop_join_row_count`.
        """
        parameter_value: pulumi.Input[str]
        """
        The value of the parameter to set.
        """
elif False:
    WorkgroupConfigParameterArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WorkgroupConfigParameterArgs:
    def __init__(__self__, *,
                 parameter_key: pulumi.Input[str],
                 parameter_value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] parameter_key: The key of the parameter. The options are `auto_mv`, `datestyle`, `enable_case_sensitive_identifier`, `enable_user_activity_logging`, `query_group`, `search_path`, `require_ssl`, `use_fips_ssl`, and [query monitoring metrics](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless) that let you define performance boundaries: `max_query_cpu_time`, `max_query_blocks_read`, `max_scan_row_count`, `max_query_execution_time`, `max_query_queue_time`, `max_query_cpu_usage_percent`, `max_query_temp_blocks_to_disk`, `max_join_row_count` and `max_nested_loop_join_row_count`.
        :param pulumi.Input[str] parameter_value: The value of the parameter to set.
        """
        pulumi.set(__self__, "parameter_key", parameter_key)
        pulumi.set(__self__, "parameter_value", parameter_value)

    @property
    @pulumi.getter(name="parameterKey")
    def parameter_key(self) -> pulumi.Input[str]:
        """
        The key of the parameter. The options are `auto_mv`, `datestyle`, `enable_case_sensitive_identifier`, `enable_user_activity_logging`, `query_group`, `search_path`, `require_ssl`, `use_fips_ssl`, and [query monitoring metrics](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless) that let you define performance boundaries: `max_query_cpu_time`, `max_query_blocks_read`, `max_scan_row_count`, `max_query_execution_time`, `max_query_queue_time`, `max_query_cpu_usage_percent`, `max_query_temp_blocks_to_disk`, `max_join_row_count` and `max_nested_loop_join_row_count`.
        """
        return pulumi.get(self, "parameter_key")

    @parameter_key.setter
    def parameter_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "parameter_key", value)

    @property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> pulumi.Input[str]:
        """
        The value of the parameter to set.
        """
        return pulumi.get(self, "parameter_value")

    @parameter_value.setter
    def parameter_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "parameter_value", value)


if not MYPY:
    class WorkgroupEndpointArgsDict(TypedDict):
        address: NotRequired[pulumi.Input[str]]
        """
        The DNS address of the VPC endpoint.
        """
        port: NotRequired[pulumi.Input[int]]
        """
        The port number on which the cluster accepts incoming connections.
        """
        vpc_endpoints: NotRequired[pulumi.Input[Sequence[pulumi.Input['WorkgroupEndpointVpcEndpointArgsDict']]]]
        """
        The VPC endpoint or the Redshift Serverless workgroup. See `VPC Endpoint` below.
        """
elif False:
    WorkgroupEndpointArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WorkgroupEndpointArgs:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 vpc_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input['WorkgroupEndpointVpcEndpointArgs']]]] = None):
        """
        :param pulumi.Input[str] address: The DNS address of the VPC endpoint.
        :param pulumi.Input[int] port: The port number on which the cluster accepts incoming connections.
        :param pulumi.Input[Sequence[pulumi.Input['WorkgroupEndpointVpcEndpointArgs']]] vpc_endpoints: The VPC endpoint or the Redshift Serverless workgroup. See `VPC Endpoint` below.
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if vpc_endpoints is not None:
            pulumi.set(__self__, "vpc_endpoints", vpc_endpoints)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[str]]:
        """
        The DNS address of the VPC endpoint.
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        The port number on which the cluster accepts incoming connections.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="vpcEndpoints")
    def vpc_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkgroupEndpointVpcEndpointArgs']]]]:
        """
        The VPC endpoint or the Redshift Serverless workgroup. See `VPC Endpoint` below.
        """
        return pulumi.get(self, "vpc_endpoints")

    @vpc_endpoints.setter
    def vpc_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkgroupEndpointVpcEndpointArgs']]]]):
        pulumi.set(self, "vpc_endpoints", value)


if not MYPY:
    class WorkgroupEndpointVpcEndpointArgsDict(TypedDict):
        network_interfaces: NotRequired[pulumi.Input[Sequence[pulumi.Input['WorkgroupEndpointVpcEndpointNetworkInterfaceArgsDict']]]]
        """
        The network interfaces of the endpoint.. See `Network Interface` below.
        """
        vpc_endpoint_id: NotRequired[pulumi.Input[str]]
        """
        The DNS address of the VPC endpoint.
        """
        vpc_id: NotRequired[pulumi.Input[str]]
        """
        The port that Amazon Redshift Serverless listens on.
        """
elif False:
    WorkgroupEndpointVpcEndpointArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WorkgroupEndpointVpcEndpointArgs:
    def __init__(__self__, *,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input['WorkgroupEndpointVpcEndpointNetworkInterfaceArgs']]]] = None,
                 vpc_endpoint_id: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input['WorkgroupEndpointVpcEndpointNetworkInterfaceArgs']]] network_interfaces: The network interfaces of the endpoint.. See `Network Interface` below.
        :param pulumi.Input[str] vpc_endpoint_id: The DNS address of the VPC endpoint.
        :param pulumi.Input[str] vpc_id: The port that Amazon Redshift Serverless listens on.
        """
        if network_interfaces is not None:
            pulumi.set(__self__, "network_interfaces", network_interfaces)
        if vpc_endpoint_id is not None:
            pulumi.set(__self__, "vpc_endpoint_id", vpc_endpoint_id)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkgroupEndpointVpcEndpointNetworkInterfaceArgs']]]]:
        """
        The network interfaces of the endpoint.. See `Network Interface` below.
        """
        return pulumi.get(self, "network_interfaces")

    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkgroupEndpointVpcEndpointNetworkInterfaceArgs']]]]):
        pulumi.set(self, "network_interfaces", value)

    @property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[str]]:
        """
        The DNS address of the VPC endpoint.
        """
        return pulumi.get(self, "vpc_endpoint_id")

    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_endpoint_id", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        The port that Amazon Redshift Serverless listens on.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


if not MYPY:
    class WorkgroupEndpointVpcEndpointNetworkInterfaceArgsDict(TypedDict):
        availability_zone: NotRequired[pulumi.Input[str]]
        """
        The availability Zone.
        """
        network_interface_id: NotRequired[pulumi.Input[str]]
        """
        The unique identifier of the network interface.
        """
        private_ip_address: NotRequired[pulumi.Input[str]]
        """
        The IPv4 address of the network interface within the subnet.
        """
        subnet_id: NotRequired[pulumi.Input[str]]
        """
        The unique identifier of the subnet.
        """
elif False:
    WorkgroupEndpointVpcEndpointNetworkInterfaceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WorkgroupEndpointVpcEndpointNetworkInterfaceArgs:
    def __init__(__self__, *,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 private_ip_address: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] availability_zone: The availability Zone.
        :param pulumi.Input[str] network_interface_id: The unique identifier of the network interface.
        :param pulumi.Input[str] private_ip_address: The IPv4 address of the network interface within the subnet.
        :param pulumi.Input[str] subnet_id: The unique identifier of the subnet.
        """
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if network_interface_id is not None:
            pulumi.set(__self__, "network_interface_id", network_interface_id)
        if private_ip_address is not None:
            pulumi.set(__self__, "private_ip_address", private_ip_address)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The availability Zone.
        """
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier of the network interface.
        """
        return pulumi.get(self, "network_interface_id")

    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_interface_id", value)

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 address of the network interface within the subnet.
        """
        return pulumi.get(self, "private_ip_address")

    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_ip_address", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier of the subnet.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)


