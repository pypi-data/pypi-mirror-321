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

__all__ = ['RolePoliciesExclusiveArgs', 'RolePoliciesExclusive']

@pulumi.input_type
class RolePoliciesExclusiveArgs:
    def __init__(__self__, *,
                 policy_names: pulumi.Input[Sequence[pulumi.Input[str]]],
                 role_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a RolePoliciesExclusive resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policy_names: A list of inline policy names to be assigned to the role. Policies attached to this role but not configured in this argument will be removed.
        :param pulumi.Input[str] role_name: IAM role name.
        """
        pulumi.set(__self__, "policy_names", policy_names)
        pulumi.set(__self__, "role_name", role_name)

    @property
    @pulumi.getter(name="policyNames")
    def policy_names(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of inline policy names to be assigned to the role. Policies attached to this role but not configured in this argument will be removed.
        """
        return pulumi.get(self, "policy_names")

    @policy_names.setter
    def policy_names(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "policy_names", value)

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Input[str]:
        """
        IAM role name.
        """
        return pulumi.get(self, "role_name")

    @role_name.setter
    def role_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_name", value)


@pulumi.input_type
class _RolePoliciesExclusiveState:
    def __init__(__self__, *,
                 policy_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RolePoliciesExclusive resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policy_names: A list of inline policy names to be assigned to the role. Policies attached to this role but not configured in this argument will be removed.
        :param pulumi.Input[str] role_name: IAM role name.
        """
        if policy_names is not None:
            pulumi.set(__self__, "policy_names", policy_names)
        if role_name is not None:
            pulumi.set(__self__, "role_name", role_name)

    @property
    @pulumi.getter(name="policyNames")
    def policy_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of inline policy names to be assigned to the role. Policies attached to this role but not configured in this argument will be removed.
        """
        return pulumi.get(self, "policy_names")

    @policy_names.setter
    def policy_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "policy_names", value)

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[pulumi.Input[str]]:
        """
        IAM role name.
        """
        return pulumi.get(self, "role_name")

    @role_name.setter
    def role_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_name", value)


class RolePoliciesExclusive(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        > **NOTE:**: To reliably detect drift between customer managed inline policies listed in this resource and actual policies attached to the role in the cloud, you currently need to run Pulumi with `pulumi up --refresh`. See [#4766](https://github.com/pulumi/pulumi-aws/issues/4766) for tracking making this work with regular `pulumi up` invocations.

        Resource for maintaining exclusive management of inline policies assigned to an AWS IAM (Identity & Access Management) role.

        !> This resource takes exclusive ownership over inline policies assigned to a role. This includes removal of inline policies which are not explicitly configured. To prevent persistent drift, ensure any `iam.RolePolicy` resources managed alongside this resource are included in the `policy_names` argument.

        > Destruction of this resource means Pulumi will no longer manage reconciliation of the configured inline policy assignments. It __will not__ delete the configured policies from the role.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.iam.RolePoliciesExclusive("example",
            role_name=example_aws_iam_role["name"],
            policy_names=[example_aws_iam_role_policy["name"]])
        ```

        ### Disallow Inline Policies

        To automatically remove any configured inline policies, set the `policy_names` argument to an empty list.

        > This will not __prevent__ inline policies from being assigned to a role via Pulumi (or any other interface). This resource enables bringing inline policy assignments into a configured state, however, this reconciliation happens only when `apply` is proactively run.

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.iam.RolePoliciesExclusive("example",
            role_name=example_aws_iam_role["name"],
            policy_names=[])
        ```

        ## Import

        Using `pulumi import`, import exclusive management of inline policy assignments using the `role_name`. For example:

        ```sh
        $ pulumi import aws:iam/rolePoliciesExclusive:RolePoliciesExclusive example MyRole
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policy_names: A list of inline policy names to be assigned to the role. Policies attached to this role but not configured in this argument will be removed.
        :param pulumi.Input[str] role_name: IAM role name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RolePoliciesExclusiveArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        > **NOTE:**: To reliably detect drift between customer managed inline policies listed in this resource and actual policies attached to the role in the cloud, you currently need to run Pulumi with `pulumi up --refresh`. See [#4766](https://github.com/pulumi/pulumi-aws/issues/4766) for tracking making this work with regular `pulumi up` invocations.

        Resource for maintaining exclusive management of inline policies assigned to an AWS IAM (Identity & Access Management) role.

        !> This resource takes exclusive ownership over inline policies assigned to a role. This includes removal of inline policies which are not explicitly configured. To prevent persistent drift, ensure any `iam.RolePolicy` resources managed alongside this resource are included in the `policy_names` argument.

        > Destruction of this resource means Pulumi will no longer manage reconciliation of the configured inline policy assignments. It __will not__ delete the configured policies from the role.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.iam.RolePoliciesExclusive("example",
            role_name=example_aws_iam_role["name"],
            policy_names=[example_aws_iam_role_policy["name"]])
        ```

        ### Disallow Inline Policies

        To automatically remove any configured inline policies, set the `policy_names` argument to an empty list.

        > This will not __prevent__ inline policies from being assigned to a role via Pulumi (or any other interface). This resource enables bringing inline policy assignments into a configured state, however, this reconciliation happens only when `apply` is proactively run.

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.iam.RolePoliciesExclusive("example",
            role_name=example_aws_iam_role["name"],
            policy_names=[])
        ```

        ## Import

        Using `pulumi import`, import exclusive management of inline policy assignments using the `role_name`. For example:

        ```sh
        $ pulumi import aws:iam/rolePoliciesExclusive:RolePoliciesExclusive example MyRole
        ```

        :param str resource_name: The name of the resource.
        :param RolePoliciesExclusiveArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RolePoliciesExclusiveArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RolePoliciesExclusiveArgs.__new__(RolePoliciesExclusiveArgs)

            if policy_names is None and not opts.urn:
                raise TypeError("Missing required property 'policy_names'")
            __props__.__dict__["policy_names"] = policy_names
            if role_name is None and not opts.urn:
                raise TypeError("Missing required property 'role_name'")
            __props__.__dict__["role_name"] = role_name
        super(RolePoliciesExclusive, __self__).__init__(
            'aws:iam/rolePoliciesExclusive:RolePoliciesExclusive',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            policy_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            role_name: Optional[pulumi.Input[str]] = None) -> 'RolePoliciesExclusive':
        """
        Get an existing RolePoliciesExclusive resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policy_names: A list of inline policy names to be assigned to the role. Policies attached to this role but not configured in this argument will be removed.
        :param pulumi.Input[str] role_name: IAM role name.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RolePoliciesExclusiveState.__new__(_RolePoliciesExclusiveState)

        __props__.__dict__["policy_names"] = policy_names
        __props__.__dict__["role_name"] = role_name
        return RolePoliciesExclusive(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="policyNames")
    def policy_names(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of inline policy names to be assigned to the role. Policies attached to this role but not configured in this argument will be removed.
        """
        return pulumi.get(self, "policy_names")

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Output[str]:
        """
        IAM role name.
        """
        return pulumi.get(self, "role_name")

