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

__all__ = [
    'OrganizationAccount',
    'OrganizationNonMasterAccount',
    'OrganizationRoot',
    'OrganizationRootPolicyType',
    'OrganizationalUnitAccount',
    'GetDelegatedAdministratorsDelegatedAdministratorResult',
    'GetDelegatedServicesDelegatedServiceResult',
    'GetOrganizationAccountResult',
    'GetOrganizationNonMasterAccountResult',
    'GetOrganizationRootResult',
    'GetOrganizationRootPolicyTypeResult',
    'GetOrganizationalUnitChildAccountsAccountResult',
    'GetOrganizationalUnitDescendantAccountsAccountResult',
    'GetOrganizationalUnitDescendantOrganizationalUnitsChildrenResult',
    'GetOrganizationalUnitsChildResult',
]

@pulumi.output_type
class OrganizationAccount(dict):
    def __init__(__self__, *,
                 arn: Optional[str] = None,
                 email: Optional[str] = None,
                 id: Optional[str] = None,
                 name: Optional[str] = None,
                 status: Optional[str] = None):
        """
        :param str arn: ARN of the root
        :param str email: Email of the account
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param str status: The status of the policy type as it relates to the associated root
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> Optional[str]:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class OrganizationNonMasterAccount(dict):
    def __init__(__self__, *,
                 arn: Optional[str] = None,
                 email: Optional[str] = None,
                 id: Optional[str] = None,
                 name: Optional[str] = None,
                 status: Optional[str] = None):
        """
        :param str arn: ARN of the root
        :param str email: Email of the account
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param str status: The status of the policy type as it relates to the associated root
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> Optional[str]:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class OrganizationRoot(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "policyTypes":
            suggest = "policy_types"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OrganizationRoot. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OrganizationRoot.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OrganizationRoot.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 arn: Optional[str] = None,
                 id: Optional[str] = None,
                 name: Optional[str] = None,
                 policy_types: Optional[Sequence['outputs.OrganizationRootPolicyType']] = None):
        """
        :param str arn: ARN of the root
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param Sequence['OrganizationRootPolicyTypeArgs'] policy_types: List of policy types enabled for this root. All elements have these attributes:
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy_types is not None:
            pulumi.set(__self__, "policy_types", policy_types)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyTypes")
    def policy_types(self) -> Optional[Sequence['outputs.OrganizationRootPolicyType']]:
        """
        List of policy types enabled for this root. All elements have these attributes:
        """
        return pulumi.get(self, "policy_types")


@pulumi.output_type
class OrganizationRootPolicyType(dict):
    def __init__(__self__, *,
                 status: Optional[str] = None,
                 type: Optional[str] = None):
        """
        :param str status: The status of the policy type as it relates to the associated root
        """
        if status is not None:
            pulumi.set(__self__, "status", status)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")


@pulumi.output_type
class OrganizationalUnitAccount(dict):
    def __init__(__self__, *,
                 arn: Optional[str] = None,
                 email: Optional[str] = None,
                 id: Optional[str] = None,
                 name: Optional[str] = None):
        """
        :param str arn: ARN of the organizational unit
        :param str email: Email of the account
        :param str id: Identifier of the organization unit
        :param str name: The name for the organizational unit
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        ARN of the organizational unit
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> Optional[str]:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Identifier of the organization unit
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name for the organizational unit
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetDelegatedAdministratorsDelegatedAdministratorResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 delegation_enabled_date: str,
                 email: str,
                 id: str,
                 joined_method: str,
                 joined_timestamp: str,
                 name: str,
                 status: str):
        """
        :param str arn: The ARN of the delegated administrator's account.
        :param str delegation_enabled_date: The date when the account was made a delegated administrator.
        :param str email: The email address that is associated with the delegated administrator's AWS account.
        :param str id: The unique identifier (ID) of the delegated administrator's account.
        :param str joined_method: The method by which the delegated administrator's account joined the organization.
        :param str joined_timestamp: The date when the delegated administrator's account became a part of the organization.
        :param str name: The friendly name of the delegated administrator's account.
        :param str status: The status of the delegated administrator's account in the organization.
        """
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "delegation_enabled_date", delegation_enabled_date)
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "joined_method", joined_method)
        pulumi.set(__self__, "joined_timestamp", joined_timestamp)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The ARN of the delegated administrator's account.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="delegationEnabledDate")
    def delegation_enabled_date(self) -> str:
        """
        The date when the account was made a delegated administrator.
        """
        return pulumi.get(self, "delegation_enabled_date")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The email address that is associated with the delegated administrator's AWS account.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique identifier (ID) of the delegated administrator's account.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="joinedMethod")
    def joined_method(self) -> str:
        """
        The method by which the delegated administrator's account joined the organization.
        """
        return pulumi.get(self, "joined_method")

    @property
    @pulumi.getter(name="joinedTimestamp")
    def joined_timestamp(self) -> str:
        """
        The date when the delegated administrator's account became a part of the organization.
        """
        return pulumi.get(self, "joined_timestamp")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The friendly name of the delegated administrator's account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the delegated administrator's account in the organization.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetDelegatedServicesDelegatedServiceResult(dict):
    def __init__(__self__, *,
                 delegation_enabled_date: str,
                 service_principal: str):
        """
        :param str delegation_enabled_date: The date that the account became a delegated administrator for this service.
        :param str service_principal: The name of an AWS service that can request an operation for the specified service.
        """
        pulumi.set(__self__, "delegation_enabled_date", delegation_enabled_date)
        pulumi.set(__self__, "service_principal", service_principal)

    @property
    @pulumi.getter(name="delegationEnabledDate")
    def delegation_enabled_date(self) -> str:
        """
        The date that the account became a delegated administrator for this service.
        """
        return pulumi.get(self, "delegation_enabled_date")

    @property
    @pulumi.getter(name="servicePrincipal")
    def service_principal(self) -> str:
        """
        The name of an AWS service that can request an operation for the specified service.
        """
        return pulumi.get(self, "service_principal")


@pulumi.output_type
class GetOrganizationAccountResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 email: str,
                 id: str,
                 name: str,
                 status: str):
        """
        :param str arn: ARN of the root
        :param str email: Email of the account
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param str status: The status of the policy type as it relates to the associated root
        """
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetOrganizationNonMasterAccountResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 email: str,
                 id: str,
                 name: str,
                 status: str):
        """
        :param str arn: ARN of the root
        :param str email: Email of the account
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param str status: The status of the policy type as it relates to the associated root
        """
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetOrganizationRootResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 id: str,
                 name: str,
                 policy_types: Sequence['outputs.GetOrganizationRootPolicyTypeResult']):
        """
        :param str arn: ARN of the root
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param Sequence['GetOrganizationRootPolicyTypeArgs'] policy_types: List of policy types enabled for this root. All elements have these attributes:
        """
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "policy_types", policy_types)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyTypes")
    def policy_types(self) -> Sequence['outputs.GetOrganizationRootPolicyTypeResult']:
        """
        List of policy types enabled for this root. All elements have these attributes:
        """
        return pulumi.get(self, "policy_types")


@pulumi.output_type
class GetOrganizationRootPolicyTypeResult(dict):
    def __init__(__self__, *,
                 status: str,
                 type: str):
        """
        :param str status: The status of the policy type as it relates to the associated root
        """
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


@pulumi.output_type
class GetOrganizationalUnitChildAccountsAccountResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 email: str,
                 id: str,
                 name: str,
                 status: str):
        """
        :param str arn: The Amazon Resource Name (ARN) of the account.
        :param str email: The email address associated with the AWS account.
        :param str id: Parent identifier of the organizational units.
        :param str name: The friendly name of the account.
        :param str status: The status of the account in the organization.
        """
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the account.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The email address associated with the AWS account.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Parent identifier of the organizational units.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The friendly name of the account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the account in the organization.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetOrganizationalUnitDescendantAccountsAccountResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 email: str,
                 id: str,
                 name: str,
                 status: str):
        """
        :param str arn: The Amazon Resource Name (ARN) of the account.
        :param str email: The email address associated with the AWS account.
        :param str id: Parent identifier of the organizational units.
        :param str name: The friendly name of the account.
        :param str status: The status of the account in the organization.
        """
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the account.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The email address associated with the AWS account.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Parent identifier of the organizational units.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The friendly name of the account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the account in the organization.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetOrganizationalUnitDescendantOrganizationalUnitsChildrenResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 id: str,
                 name: str):
        """
        :param str arn: ARN of the organizational unit
        :param str id: Parent identifier of the organizational units.
        :param str name: Name of the organizational unit
        """
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the organizational unit
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Parent identifier of the organizational units.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the organizational unit
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetOrganizationalUnitsChildResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 id: str,
                 name: str):
        """
        :param str arn: ARN of the organizational unit
        :param str id: Parent identifier of the organizational units.
        :param str name: Name of the organizational unit
        """
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the organizational unit
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Parent identifier of the organizational units.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the organizational unit
        """
        return pulumi.get(self, "name")


