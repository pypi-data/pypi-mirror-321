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
    'FileSystemAssociationCacheAttributesArgs',
    'FileSystemAssociationCacheAttributesArgsDict',
    'GatewayGatewayNetworkInterfaceArgs',
    'GatewayGatewayNetworkInterfaceArgsDict',
    'GatewayMaintenanceStartTimeArgs',
    'GatewayMaintenanceStartTimeArgsDict',
    'GatewaySmbActiveDirectorySettingsArgs',
    'GatewaySmbActiveDirectorySettingsArgsDict',
    'NfsFileShareCacheAttributesArgs',
    'NfsFileShareCacheAttributesArgsDict',
    'NfsFileShareNfsFileShareDefaultsArgs',
    'NfsFileShareNfsFileShareDefaultsArgsDict',
    'SmbFileShareCacheAttributesArgs',
    'SmbFileShareCacheAttributesArgsDict',
]

MYPY = False

if not MYPY:
    class FileSystemAssociationCacheAttributesArgsDict(TypedDict):
        cache_stale_timeout_in_seconds: NotRequired[pulumi.Input[int]]
        """
        Refreshes a file share's cache by using Time To Live (TTL).
        TTL is the length of time since the last refresh after which access to the directory would cause the file gateway
        to first refresh that directory's contents from the Amazon S3 bucket. Valid Values: `0` or `300` to `2592000` seconds (5 minutes to 30 days). Defaults to `0`
        """
elif False:
    FileSystemAssociationCacheAttributesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class FileSystemAssociationCacheAttributesArgs:
    def __init__(__self__, *,
                 cache_stale_timeout_in_seconds: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] cache_stale_timeout_in_seconds: Refreshes a file share's cache by using Time To Live (TTL).
               TTL is the length of time since the last refresh after which access to the directory would cause the file gateway
               to first refresh that directory's contents from the Amazon S3 bucket. Valid Values: `0` or `300` to `2592000` seconds (5 minutes to 30 days). Defaults to `0`
        """
        if cache_stale_timeout_in_seconds is not None:
            pulumi.set(__self__, "cache_stale_timeout_in_seconds", cache_stale_timeout_in_seconds)

    @property
    @pulumi.getter(name="cacheStaleTimeoutInSeconds")
    def cache_stale_timeout_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Refreshes a file share's cache by using Time To Live (TTL).
        TTL is the length of time since the last refresh after which access to the directory would cause the file gateway
        to first refresh that directory's contents from the Amazon S3 bucket. Valid Values: `0` or `300` to `2592000` seconds (5 minutes to 30 days). Defaults to `0`
        """
        return pulumi.get(self, "cache_stale_timeout_in_seconds")

    @cache_stale_timeout_in_seconds.setter
    def cache_stale_timeout_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cache_stale_timeout_in_seconds", value)


if not MYPY:
    class GatewayGatewayNetworkInterfaceArgsDict(TypedDict):
        ipv4_address: NotRequired[pulumi.Input[str]]
        """
        The Internet Protocol version 4 (IPv4) address of the interface.
        """
elif False:
    GatewayGatewayNetworkInterfaceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GatewayGatewayNetworkInterfaceArgs:
    def __init__(__self__, *,
                 ipv4_address: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] ipv4_address: The Internet Protocol version 4 (IPv4) address of the interface.
        """
        if ipv4_address is not None:
            pulumi.set(__self__, "ipv4_address", ipv4_address)

    @property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> Optional[pulumi.Input[str]]:
        """
        The Internet Protocol version 4 (IPv4) address of the interface.
        """
        return pulumi.get(self, "ipv4_address")

    @ipv4_address.setter
    def ipv4_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv4_address", value)


if not MYPY:
    class GatewayMaintenanceStartTimeArgsDict(TypedDict):
        hour_of_day: pulumi.Input[int]
        """
        The hour component of the maintenance start time represented as _hh_, where _hh_ is the hour (00 to 23). The hour of the day is in the time zone of the gateway.
        """
        day_of_month: NotRequired[pulumi.Input[str]]
        """
        The day of the month component of the maintenance start time represented as an ordinal number from 1 to 28, where 1 represents the first day of the month and 28 represents the last day of the month.
        """
        day_of_week: NotRequired[pulumi.Input[str]]
        """
        The day of the week component of the maintenance start time week represented as an ordinal number from 0 to 6, where 0 represents Sunday and 6 Saturday.
        """
        minute_of_hour: NotRequired[pulumi.Input[int]]
        """
        The minute component of the maintenance start time represented as _mm_, where _mm_ is the minute (00 to 59). The minute of the hour is in the time zone of the gateway.
        """
elif False:
    GatewayMaintenanceStartTimeArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GatewayMaintenanceStartTimeArgs:
    def __init__(__self__, *,
                 hour_of_day: pulumi.Input[int],
                 day_of_month: Optional[pulumi.Input[str]] = None,
                 day_of_week: Optional[pulumi.Input[str]] = None,
                 minute_of_hour: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] hour_of_day: The hour component of the maintenance start time represented as _hh_, where _hh_ is the hour (00 to 23). The hour of the day is in the time zone of the gateway.
        :param pulumi.Input[str] day_of_month: The day of the month component of the maintenance start time represented as an ordinal number from 1 to 28, where 1 represents the first day of the month and 28 represents the last day of the month.
        :param pulumi.Input[str] day_of_week: The day of the week component of the maintenance start time week represented as an ordinal number from 0 to 6, where 0 represents Sunday and 6 Saturday.
        :param pulumi.Input[int] minute_of_hour: The minute component of the maintenance start time represented as _mm_, where _mm_ is the minute (00 to 59). The minute of the hour is in the time zone of the gateway.
        """
        pulumi.set(__self__, "hour_of_day", hour_of_day)
        if day_of_month is not None:
            pulumi.set(__self__, "day_of_month", day_of_month)
        if day_of_week is not None:
            pulumi.set(__self__, "day_of_week", day_of_week)
        if minute_of_hour is not None:
            pulumi.set(__self__, "minute_of_hour", minute_of_hour)

    @property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> pulumi.Input[int]:
        """
        The hour component of the maintenance start time represented as _hh_, where _hh_ is the hour (00 to 23). The hour of the day is in the time zone of the gateway.
        """
        return pulumi.get(self, "hour_of_day")

    @hour_of_day.setter
    def hour_of_day(self, value: pulumi.Input[int]):
        pulumi.set(self, "hour_of_day", value)

    @property
    @pulumi.getter(name="dayOfMonth")
    def day_of_month(self) -> Optional[pulumi.Input[str]]:
        """
        The day of the month component of the maintenance start time represented as an ordinal number from 1 to 28, where 1 represents the first day of the month and 28 represents the last day of the month.
        """
        return pulumi.get(self, "day_of_month")

    @day_of_month.setter
    def day_of_month(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "day_of_month", value)

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[pulumi.Input[str]]:
        """
        The day of the week component of the maintenance start time week represented as an ordinal number from 0 to 6, where 0 represents Sunday and 6 Saturday.
        """
        return pulumi.get(self, "day_of_week")

    @day_of_week.setter
    def day_of_week(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "day_of_week", value)

    @property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> Optional[pulumi.Input[int]]:
        """
        The minute component of the maintenance start time represented as _mm_, where _mm_ is the minute (00 to 59). The minute of the hour is in the time zone of the gateway.
        """
        return pulumi.get(self, "minute_of_hour")

    @minute_of_hour.setter
    def minute_of_hour(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "minute_of_hour", value)


if not MYPY:
    class GatewaySmbActiveDirectorySettingsArgsDict(TypedDict):
        domain_name: pulumi.Input[str]
        """
        The name of the domain that you want the gateway to join.
        """
        password: pulumi.Input[str]
        """
        The password of the user who has permission to add the gateway to the Active Directory domain.
        """
        username: pulumi.Input[str]
        """
        The user name of user who has permission to add the gateway to the Active Directory domain.
        """
        active_directory_status: NotRequired[pulumi.Input[str]]
        domain_controllers: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        List of IPv4 addresses, NetBIOS names, or host names of your domain server.
        If you need to specify the port number include it after the colon (“:”). For example, `mydc.mydomain.com:389`.
        """
        organizational_unit: NotRequired[pulumi.Input[str]]
        """
        The organizational unit (OU) is a container in an Active Directory that can hold users, groups,
        computers, and other OUs and this parameter specifies the OU that the gateway will join within the AD domain.
        """
        timeout_in_seconds: NotRequired[pulumi.Input[int]]
        """
        Specifies the time in seconds, in which the JoinDomain operation must complete. The default is `20` seconds.
        """
elif False:
    GatewaySmbActiveDirectorySettingsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GatewaySmbActiveDirectorySettingsArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 password: pulumi.Input[str],
                 username: pulumi.Input[str],
                 active_directory_status: Optional[pulumi.Input[str]] = None,
                 domain_controllers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 organizational_unit: Optional[pulumi.Input[str]] = None,
                 timeout_in_seconds: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] domain_name: The name of the domain that you want the gateway to join.
        :param pulumi.Input[str] password: The password of the user who has permission to add the gateway to the Active Directory domain.
        :param pulumi.Input[str] username: The user name of user who has permission to add the gateway to the Active Directory domain.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domain_controllers: List of IPv4 addresses, NetBIOS names, or host names of your domain server.
               If you need to specify the port number include it after the colon (“:”). For example, `mydc.mydomain.com:389`.
        :param pulumi.Input[str] organizational_unit: The organizational unit (OU) is a container in an Active Directory that can hold users, groups,
               computers, and other OUs and this parameter specifies the OU that the gateway will join within the AD domain.
        :param pulumi.Input[int] timeout_in_seconds: Specifies the time in seconds, in which the JoinDomain operation must complete. The default is `20` seconds.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)
        if active_directory_status is not None:
            pulumi.set(__self__, "active_directory_status", active_directory_status)
        if domain_controllers is not None:
            pulumi.set(__self__, "domain_controllers", domain_controllers)
        if organizational_unit is not None:
            pulumi.set(__self__, "organizational_unit", organizational_unit)
        if timeout_in_seconds is not None:
            pulumi.set(__self__, "timeout_in_seconds", timeout_in_seconds)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The name of the domain that you want the gateway to join.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        The password of the user who has permission to add the gateway to the Active Directory domain.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        The user name of user who has permission to add the gateway to the Active Directory domain.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter(name="activeDirectoryStatus")
    def active_directory_status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "active_directory_status")

    @active_directory_status.setter
    def active_directory_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "active_directory_status", value)

    @property
    @pulumi.getter(name="domainControllers")
    def domain_controllers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of IPv4 addresses, NetBIOS names, or host names of your domain server.
        If you need to specify the port number include it after the colon (“:”). For example, `mydc.mydomain.com:389`.
        """
        return pulumi.get(self, "domain_controllers")

    @domain_controllers.setter
    def domain_controllers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "domain_controllers", value)

    @property
    @pulumi.getter(name="organizationalUnit")
    def organizational_unit(self) -> Optional[pulumi.Input[str]]:
        """
        The organizational unit (OU) is a container in an Active Directory that can hold users, groups,
        computers, and other OUs and this parameter specifies the OU that the gateway will join within the AD domain.
        """
        return pulumi.get(self, "organizational_unit")

    @organizational_unit.setter
    def organizational_unit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organizational_unit", value)

    @property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the time in seconds, in which the JoinDomain operation must complete. The default is `20` seconds.
        """
        return pulumi.get(self, "timeout_in_seconds")

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout_in_seconds", value)


if not MYPY:
    class NfsFileShareCacheAttributesArgsDict(TypedDict):
        cache_stale_timeout_in_seconds: NotRequired[pulumi.Input[int]]
        """
        Refreshes a file share's cache by using Time To Live (TTL).
        TTL is the length of time since the last refresh after which access to the directory would cause the file gateway
        to first refresh that directory's contents from the Amazon S3 bucket. Valid Values: 300 to 2,592,000 seconds (5 minutes to 30 days)
        """
elif False:
    NfsFileShareCacheAttributesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class NfsFileShareCacheAttributesArgs:
    def __init__(__self__, *,
                 cache_stale_timeout_in_seconds: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] cache_stale_timeout_in_seconds: Refreshes a file share's cache by using Time To Live (TTL).
               TTL is the length of time since the last refresh after which access to the directory would cause the file gateway
               to first refresh that directory's contents from the Amazon S3 bucket. Valid Values: 300 to 2,592,000 seconds (5 minutes to 30 days)
        """
        if cache_stale_timeout_in_seconds is not None:
            pulumi.set(__self__, "cache_stale_timeout_in_seconds", cache_stale_timeout_in_seconds)

    @property
    @pulumi.getter(name="cacheStaleTimeoutInSeconds")
    def cache_stale_timeout_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Refreshes a file share's cache by using Time To Live (TTL).
        TTL is the length of time since the last refresh after which access to the directory would cause the file gateway
        to first refresh that directory's contents from the Amazon S3 bucket. Valid Values: 300 to 2,592,000 seconds (5 minutes to 30 days)
        """
        return pulumi.get(self, "cache_stale_timeout_in_seconds")

    @cache_stale_timeout_in_seconds.setter
    def cache_stale_timeout_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cache_stale_timeout_in_seconds", value)


if not MYPY:
    class NfsFileShareNfsFileShareDefaultsArgsDict(TypedDict):
        directory_mode: NotRequired[pulumi.Input[str]]
        """
        The Unix directory mode in the string form "nnnn". Defaults to `"0777"`.
        """
        file_mode: NotRequired[pulumi.Input[str]]
        """
        The Unix file mode in the string form "nnnn". Defaults to `"0666"`.
        """
        group_id: NotRequired[pulumi.Input[str]]
        """
        The default group ID for the file share (unless the files have another group ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
        """
        owner_id: NotRequired[pulumi.Input[str]]
        """
        The default owner ID for the file share (unless the files have another owner ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
        """
elif False:
    NfsFileShareNfsFileShareDefaultsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class NfsFileShareNfsFileShareDefaultsArgs:
    def __init__(__self__, *,
                 directory_mode: Optional[pulumi.Input[str]] = None,
                 file_mode: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 owner_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] directory_mode: The Unix directory mode in the string form "nnnn". Defaults to `"0777"`.
        :param pulumi.Input[str] file_mode: The Unix file mode in the string form "nnnn". Defaults to `"0666"`.
        :param pulumi.Input[str] group_id: The default group ID for the file share (unless the files have another group ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
        :param pulumi.Input[str] owner_id: The default owner ID for the file share (unless the files have another owner ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
        """
        if directory_mode is not None:
            pulumi.set(__self__, "directory_mode", directory_mode)
        if file_mode is not None:
            pulumi.set(__self__, "file_mode", file_mode)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if owner_id is not None:
            pulumi.set(__self__, "owner_id", owner_id)

    @property
    @pulumi.getter(name="directoryMode")
    def directory_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The Unix directory mode in the string form "nnnn". Defaults to `"0777"`.
        """
        return pulumi.get(self, "directory_mode")

    @directory_mode.setter
    def directory_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory_mode", value)

    @property
    @pulumi.getter(name="fileMode")
    def file_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The Unix file mode in the string form "nnnn". Defaults to `"0666"`.
        """
        return pulumi.get(self, "file_mode")

    @file_mode.setter
    def file_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_mode", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The default group ID for the file share (unless the files have another group ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[str]]:
        """
        The default owner ID for the file share (unless the files have another owner ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
        """
        return pulumi.get(self, "owner_id")

    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner_id", value)


if not MYPY:
    class SmbFileShareCacheAttributesArgsDict(TypedDict):
        cache_stale_timeout_in_seconds: NotRequired[pulumi.Input[int]]
        """
        Refreshes a file share's cache by using Time To Live (TTL).
        TTL is the length of time since the last refresh after which access to the directory would cause the file gateway
        to first refresh that directory's contents from the Amazon S3 bucket. Valid Values: 300 to 2,592,000 seconds (5 minutes to 30 days)
        """
elif False:
    SmbFileShareCacheAttributesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SmbFileShareCacheAttributesArgs:
    def __init__(__self__, *,
                 cache_stale_timeout_in_seconds: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] cache_stale_timeout_in_seconds: Refreshes a file share's cache by using Time To Live (TTL).
               TTL is the length of time since the last refresh after which access to the directory would cause the file gateway
               to first refresh that directory's contents from the Amazon S3 bucket. Valid Values: 300 to 2,592,000 seconds (5 minutes to 30 days)
        """
        if cache_stale_timeout_in_seconds is not None:
            pulumi.set(__self__, "cache_stale_timeout_in_seconds", cache_stale_timeout_in_seconds)

    @property
    @pulumi.getter(name="cacheStaleTimeoutInSeconds")
    def cache_stale_timeout_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Refreshes a file share's cache by using Time To Live (TTL).
        TTL is the length of time since the last refresh after which access to the directory would cause the file gateway
        to first refresh that directory's contents from the Amazon S3 bucket. Valid Values: 300 to 2,592,000 seconds (5 minutes to 30 days)
        """
        return pulumi.get(self, "cache_stale_timeout_in_seconds")

    @cache_stale_timeout_in_seconds.setter
    def cache_stale_timeout_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cache_stale_timeout_in_seconds", value)


