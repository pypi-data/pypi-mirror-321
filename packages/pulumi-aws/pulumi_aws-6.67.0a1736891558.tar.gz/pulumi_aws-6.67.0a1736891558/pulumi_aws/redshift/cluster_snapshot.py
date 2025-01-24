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

__all__ = ['ClusterSnapshotArgs', 'ClusterSnapshot']

@pulumi.input_type
class ClusterSnapshotArgs:
    def __init__(__self__, *,
                 cluster_identifier: pulumi.Input[str],
                 snapshot_identifier: pulumi.Input[str],
                 manual_snapshot_retention_period: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ClusterSnapshot resource.
        :param pulumi.Input[str] cluster_identifier: The cluster identifier for which you want a snapshot.
        :param pulumi.Input[str] snapshot_identifier: A unique identifier for the snapshot that you are requesting. This identifier must be unique for all snapshots within the Amazon Web Services account.
        :param pulumi.Input[int] manual_snapshot_retention_period: The number of days that a manual snapshot is retained. If the value is `-1`, the manual snapshot is retained indefinitely. Valid values are -1 and between `1` and `3653`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        pulumi.set(__self__, "cluster_identifier", cluster_identifier)
        pulumi.set(__self__, "snapshot_identifier", snapshot_identifier)
        if manual_snapshot_retention_period is not None:
            pulumi.set(__self__, "manual_snapshot_retention_period", manual_snapshot_retention_period)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Input[str]:
        """
        The cluster identifier for which you want a snapshot.
        """
        return pulumi.get(self, "cluster_identifier")

    @cluster_identifier.setter
    def cluster_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_identifier", value)

    @property
    @pulumi.getter(name="snapshotIdentifier")
    def snapshot_identifier(self) -> pulumi.Input[str]:
        """
        A unique identifier for the snapshot that you are requesting. This identifier must be unique for all snapshots within the Amazon Web Services account.
        """
        return pulumi.get(self, "snapshot_identifier")

    @snapshot_identifier.setter
    def snapshot_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "snapshot_identifier", value)

    @property
    @pulumi.getter(name="manualSnapshotRetentionPeriod")
    def manual_snapshot_retention_period(self) -> Optional[pulumi.Input[int]]:
        """
        The number of days that a manual snapshot is retained. If the value is `-1`, the manual snapshot is retained indefinitely. Valid values are -1 and between `1` and `3653`.
        """
        return pulumi.get(self, "manual_snapshot_retention_period")

    @manual_snapshot_retention_period.setter
    def manual_snapshot_retention_period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "manual_snapshot_retention_period", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ClusterSnapshotState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 cluster_identifier: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 manual_snapshot_retention_period: Optional[pulumi.Input[int]] = None,
                 owner_account: Optional[pulumi.Input[str]] = None,
                 snapshot_identifier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering ClusterSnapshot resources.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the snapshot.
        :param pulumi.Input[str] cluster_identifier: The cluster identifier for which you want a snapshot.
        :param pulumi.Input[str] kms_key_id: The Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.
        :param pulumi.Input[int] manual_snapshot_retention_period: The number of days that a manual snapshot is retained. If the value is `-1`, the manual snapshot is retained indefinitely. Valid values are -1 and between `1` and `3653`.
        :param pulumi.Input[str] owner_account: For manual snapshots, the Amazon Web Services account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.
        :param pulumi.Input[str] snapshot_identifier: A unique identifier for the snapshot that you are requesting. This identifier must be unique for all snapshots within the Amazon Web Services account.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if cluster_identifier is not None:
            pulumi.set(__self__, "cluster_identifier", cluster_identifier)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if manual_snapshot_retention_period is not None:
            pulumi.set(__self__, "manual_snapshot_retention_period", manual_snapshot_retention_period)
        if owner_account is not None:
            pulumi.set(__self__, "owner_account", owner_account)
        if snapshot_identifier is not None:
            pulumi.set(__self__, "snapshot_identifier", snapshot_identifier)
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
        Amazon Resource Name (ARN) of the snapshot.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The cluster identifier for which you want a snapshot.
        """
        return pulumi.get(self, "cluster_identifier")

    @cluster_identifier.setter
    def cluster_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_identifier", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="manualSnapshotRetentionPeriod")
    def manual_snapshot_retention_period(self) -> Optional[pulumi.Input[int]]:
        """
        The number of days that a manual snapshot is retained. If the value is `-1`, the manual snapshot is retained indefinitely. Valid values are -1 and between `1` and `3653`.
        """
        return pulumi.get(self, "manual_snapshot_retention_period")

    @manual_snapshot_retention_period.setter
    def manual_snapshot_retention_period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "manual_snapshot_retention_period", value)

    @property
    @pulumi.getter(name="ownerAccount")
    def owner_account(self) -> Optional[pulumi.Input[str]]:
        """
        For manual snapshots, the Amazon Web Services account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.
        """
        return pulumi.get(self, "owner_account")

    @owner_account.setter
    def owner_account(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner_account", value)

    @property
    @pulumi.getter(name="snapshotIdentifier")
    def snapshot_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        A unique identifier for the snapshot that you are requesting. This identifier must be unique for all snapshots within the Amazon Web Services account.
        """
        return pulumi.get(self, "snapshot_identifier")

    @snapshot_identifier.setter
    def snapshot_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "snapshot_identifier", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


class ClusterSnapshot(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_identifier: Optional[pulumi.Input[str]] = None,
                 manual_snapshot_retention_period: Optional[pulumi.Input[int]] = None,
                 snapshot_identifier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Creates a Redshift cluster snapshot

        ## Import

        Using `pulumi import`, import Redshift Cluster Snapshots using `snapshot_identifier`. For example:

        ```sh
        $ pulumi import aws:redshift/clusterSnapshot:ClusterSnapshot test example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_identifier: The cluster identifier for which you want a snapshot.
        :param pulumi.Input[int] manual_snapshot_retention_period: The number of days that a manual snapshot is retained. If the value is `-1`, the manual snapshot is retained indefinitely. Valid values are -1 and between `1` and `3653`.
        :param pulumi.Input[str] snapshot_identifier: A unique identifier for the snapshot that you are requesting. This identifier must be unique for all snapshots within the Amazon Web Services account.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterSnapshotArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a Redshift cluster snapshot

        ## Import

        Using `pulumi import`, import Redshift Cluster Snapshots using `snapshot_identifier`. For example:

        ```sh
        $ pulumi import aws:redshift/clusterSnapshot:ClusterSnapshot test example
        ```

        :param str resource_name: The name of the resource.
        :param ClusterSnapshotArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterSnapshotArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_identifier: Optional[pulumi.Input[str]] = None,
                 manual_snapshot_retention_period: Optional[pulumi.Input[int]] = None,
                 snapshot_identifier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterSnapshotArgs.__new__(ClusterSnapshotArgs)

            if cluster_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_identifier'")
            __props__.__dict__["cluster_identifier"] = cluster_identifier
            __props__.__dict__["manual_snapshot_retention_period"] = manual_snapshot_retention_period
            if snapshot_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'snapshot_identifier'")
            __props__.__dict__["snapshot_identifier"] = snapshot_identifier
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["kms_key_id"] = None
            __props__.__dict__["owner_account"] = None
            __props__.__dict__["tags_all"] = None
        super(ClusterSnapshot, __self__).__init__(
            'aws:redshift/clusterSnapshot:ClusterSnapshot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            cluster_identifier: Optional[pulumi.Input[str]] = None,
            kms_key_id: Optional[pulumi.Input[str]] = None,
            manual_snapshot_retention_period: Optional[pulumi.Input[int]] = None,
            owner_account: Optional[pulumi.Input[str]] = None,
            snapshot_identifier: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'ClusterSnapshot':
        """
        Get an existing ClusterSnapshot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the snapshot.
        :param pulumi.Input[str] cluster_identifier: The cluster identifier for which you want a snapshot.
        :param pulumi.Input[str] kms_key_id: The Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.
        :param pulumi.Input[int] manual_snapshot_retention_period: The number of days that a manual snapshot is retained. If the value is `-1`, the manual snapshot is retained indefinitely. Valid values are -1 and between `1` and `3653`.
        :param pulumi.Input[str] owner_account: For manual snapshots, the Amazon Web Services account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.
        :param pulumi.Input[str] snapshot_identifier: A unique identifier for the snapshot that you are requesting. This identifier must be unique for all snapshots within the Amazon Web Services account.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ClusterSnapshotState.__new__(_ClusterSnapshotState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["cluster_identifier"] = cluster_identifier
        __props__.__dict__["kms_key_id"] = kms_key_id
        __props__.__dict__["manual_snapshot_retention_period"] = manual_snapshot_retention_period
        __props__.__dict__["owner_account"] = owner_account
        __props__.__dict__["snapshot_identifier"] = snapshot_identifier
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return ClusterSnapshot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the snapshot.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Output[str]:
        """
        The cluster identifier for which you want a snapshot.
        """
        return pulumi.get(self, "cluster_identifier")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[str]:
        """
        The Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="manualSnapshotRetentionPeriod")
    def manual_snapshot_retention_period(self) -> pulumi.Output[Optional[int]]:
        """
        The number of days that a manual snapshot is retained. If the value is `-1`, the manual snapshot is retained indefinitely. Valid values are -1 and between `1` and `3653`.
        """
        return pulumi.get(self, "manual_snapshot_retention_period")

    @property
    @pulumi.getter(name="ownerAccount")
    def owner_account(self) -> pulumi.Output[str]:
        """
        For manual snapshots, the Amazon Web Services account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.
        """
        return pulumi.get(self, "owner_account")

    @property
    @pulumi.getter(name="snapshotIdentifier")
    def snapshot_identifier(self) -> pulumi.Output[str]:
        """
        A unique identifier for the snapshot that you are requesting. This identifier must be unique for all snapshots within the Amazon Web Services account.
        """
        return pulumi.get(self, "snapshot_identifier")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    @_utilities.deprecated("""Please use `tags` instead.""")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

