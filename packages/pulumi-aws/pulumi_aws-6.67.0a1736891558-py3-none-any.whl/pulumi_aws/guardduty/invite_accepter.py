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

__all__ = ['InviteAccepterArgs', 'InviteAccepter']

@pulumi.input_type
class InviteAccepterArgs:
    def __init__(__self__, *,
                 detector_id: pulumi.Input[str],
                 master_account_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a InviteAccepter resource.
        :param pulumi.Input[str] detector_id: The detector ID of the member GuardDuty account.
        :param pulumi.Input[str] master_account_id: AWS account ID for primary account.
        """
        pulumi.set(__self__, "detector_id", detector_id)
        pulumi.set(__self__, "master_account_id", master_account_id)

    @property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Input[str]:
        """
        The detector ID of the member GuardDuty account.
        """
        return pulumi.get(self, "detector_id")

    @detector_id.setter
    def detector_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "detector_id", value)

    @property
    @pulumi.getter(name="masterAccountId")
    def master_account_id(self) -> pulumi.Input[str]:
        """
        AWS account ID for primary account.
        """
        return pulumi.get(self, "master_account_id")

    @master_account_id.setter
    def master_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "master_account_id", value)


@pulumi.input_type
class _InviteAccepterState:
    def __init__(__self__, *,
                 detector_id: Optional[pulumi.Input[str]] = None,
                 master_account_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering InviteAccepter resources.
        :param pulumi.Input[str] detector_id: The detector ID of the member GuardDuty account.
        :param pulumi.Input[str] master_account_id: AWS account ID for primary account.
        """
        if detector_id is not None:
            pulumi.set(__self__, "detector_id", detector_id)
        if master_account_id is not None:
            pulumi.set(__self__, "master_account_id", master_account_id)

    @property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> Optional[pulumi.Input[str]]:
        """
        The detector ID of the member GuardDuty account.
        """
        return pulumi.get(self, "detector_id")

    @detector_id.setter
    def detector_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "detector_id", value)

    @property
    @pulumi.getter(name="masterAccountId")
    def master_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        AWS account ID for primary account.
        """
        return pulumi.get(self, "master_account_id")

    @master_account_id.setter
    def master_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "master_account_id", value)


class InviteAccepter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 detector_id: Optional[pulumi.Input[str]] = None,
                 master_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource to accept a pending GuardDuty invite on creation, ensure the detector has the correct primary account on read, and disassociate with the primary account upon removal.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        primary = aws.guardduty.Detector("primary")
        member_detector = aws.guardduty.Detector("member")
        member_member = aws.guardduty.Member("member",
            account_id=member_detector.account_id,
            detector_id=primary.id,
            email="required@example.com",
            invite=True)
        member = aws.guardduty.InviteAccepter("member",
            detector_id=member_detector.id,
            master_account_id=primary.account_id,
            opts = pulumi.ResourceOptions(depends_on=[member_member]))
        ```

        ## Import

        Using `pulumi import`, import `aws_guardduty_invite_accepter` using the member GuardDuty detector ID. For example:

        ```sh
        $ pulumi import aws:guardduty/inviteAccepter:InviteAccepter member 00b00fd5aecc0ab60a708659477e9617
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] detector_id: The detector ID of the member GuardDuty account.
        :param pulumi.Input[str] master_account_id: AWS account ID for primary account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InviteAccepterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to accept a pending GuardDuty invite on creation, ensure the detector has the correct primary account on read, and disassociate with the primary account upon removal.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        primary = aws.guardduty.Detector("primary")
        member_detector = aws.guardduty.Detector("member")
        member_member = aws.guardduty.Member("member",
            account_id=member_detector.account_id,
            detector_id=primary.id,
            email="required@example.com",
            invite=True)
        member = aws.guardduty.InviteAccepter("member",
            detector_id=member_detector.id,
            master_account_id=primary.account_id,
            opts = pulumi.ResourceOptions(depends_on=[member_member]))
        ```

        ## Import

        Using `pulumi import`, import `aws_guardduty_invite_accepter` using the member GuardDuty detector ID. For example:

        ```sh
        $ pulumi import aws:guardduty/inviteAccepter:InviteAccepter member 00b00fd5aecc0ab60a708659477e9617
        ```

        :param str resource_name: The name of the resource.
        :param InviteAccepterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InviteAccepterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 detector_id: Optional[pulumi.Input[str]] = None,
                 master_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InviteAccepterArgs.__new__(InviteAccepterArgs)

            if detector_id is None and not opts.urn:
                raise TypeError("Missing required property 'detector_id'")
            __props__.__dict__["detector_id"] = detector_id
            if master_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'master_account_id'")
            __props__.__dict__["master_account_id"] = master_account_id
        super(InviteAccepter, __self__).__init__(
            'aws:guardduty/inviteAccepter:InviteAccepter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            detector_id: Optional[pulumi.Input[str]] = None,
            master_account_id: Optional[pulumi.Input[str]] = None) -> 'InviteAccepter':
        """
        Get an existing InviteAccepter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] detector_id: The detector ID of the member GuardDuty account.
        :param pulumi.Input[str] master_account_id: AWS account ID for primary account.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InviteAccepterState.__new__(_InviteAccepterState)

        __props__.__dict__["detector_id"] = detector_id
        __props__.__dict__["master_account_id"] = master_account_id
        return InviteAccepter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Output[str]:
        """
        The detector ID of the member GuardDuty account.
        """
        return pulumi.get(self, "detector_id")

    @property
    @pulumi.getter(name="masterAccountId")
    def master_account_id(self) -> pulumi.Output[str]:
        """
        AWS account ID for primary account.
        """
        return pulumi.get(self, "master_account_id")

