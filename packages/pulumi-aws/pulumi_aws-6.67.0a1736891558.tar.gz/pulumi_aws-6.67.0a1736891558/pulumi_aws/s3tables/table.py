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

__all__ = ['TableArgs', 'Table']

@pulumi.input_type
class TableArgs:
    def __init__(__self__, *,
                 format: pulumi.Input[str],
                 namespace: pulumi.Input[str],
                 table_bucket_arn: pulumi.Input[str],
                 maintenance_configuration: Optional[pulumi.Input['TableMaintenanceConfigurationArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Table resource.
        :param pulumi.Input[str] format: Format of the table.
               Must be `ICEBERG`.
        :param pulumi.Input[str] namespace: Name of the namespace for this table.
               Must be between 1 and 255 characters in length.
               Can consist of lowercase letters, numbers, and underscores, and must begin and end with a lowercase letter or number.
        :param pulumi.Input[str] table_bucket_arn: ARN referencing the Table Bucket that contains this Namespace.
               
               The following argument is optional:
        :param pulumi.Input['TableMaintenanceConfigurationArgs'] maintenance_configuration: A single table bucket maintenance configuration block.
               See `maintenance_configuration` below
        :param pulumi.Input[str] name: Name of the table.
               Must be between 1 and 255 characters in length.
               Can consist of lowercase letters, numbers, and underscores, and must begin and end with a lowercase letter or number.
        """
        pulumi.set(__self__, "format", format)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "table_bucket_arn", table_bucket_arn)
        if maintenance_configuration is not None:
            pulumi.set(__self__, "maintenance_configuration", maintenance_configuration)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def format(self) -> pulumi.Input[str]:
        """
        Format of the table.
        Must be `ICEBERG`.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: pulumi.Input[str]):
        pulumi.set(self, "format", value)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[str]:
        """
        Name of the namespace for this table.
        Must be between 1 and 255 characters in length.
        Can consist of lowercase letters, numbers, and underscores, and must begin and end with a lowercase letter or number.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="tableBucketArn")
    def table_bucket_arn(self) -> pulumi.Input[str]:
        """
        ARN referencing the Table Bucket that contains this Namespace.

        The following argument is optional:
        """
        return pulumi.get(self, "table_bucket_arn")

    @table_bucket_arn.setter
    def table_bucket_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "table_bucket_arn", value)

    @property
    @pulumi.getter(name="maintenanceConfiguration")
    def maintenance_configuration(self) -> Optional[pulumi.Input['TableMaintenanceConfigurationArgs']]:
        """
        A single table bucket maintenance configuration block.
        See `maintenance_configuration` below
        """
        return pulumi.get(self, "maintenance_configuration")

    @maintenance_configuration.setter
    def maintenance_configuration(self, value: Optional[pulumi.Input['TableMaintenanceConfigurationArgs']]):
        pulumi.set(self, "maintenance_configuration", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the table.
        Must be between 1 and 255 characters in length.
        Can consist of lowercase letters, numbers, and underscores, and must begin and end with a lowercase letter or number.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _TableState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[str]] = None,
                 maintenance_configuration: Optional[pulumi.Input['TableMaintenanceConfigurationArgs']] = None,
                 metadata_location: Optional[pulumi.Input[str]] = None,
                 modified_at: Optional[pulumi.Input[str]] = None,
                 modified_by: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 owner_account_id: Optional[pulumi.Input[str]] = None,
                 table_bucket_arn: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 version_token: Optional[pulumi.Input[str]] = None,
                 warehouse_location: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Table resources.
        :param pulumi.Input[str] arn: ARN of the table.
        :param pulumi.Input[str] created_at: Date and time when the namespace was created.
        :param pulumi.Input[str] created_by: Account ID of the account that created the namespace.
        :param pulumi.Input[str] format: Format of the table.
               Must be `ICEBERG`.
        :param pulumi.Input['TableMaintenanceConfigurationArgs'] maintenance_configuration: A single table bucket maintenance configuration block.
               See `maintenance_configuration` below
        :param pulumi.Input[str] metadata_location: Location of table metadata.
        :param pulumi.Input[str] modified_at: Date and time when the namespace was last modified.
        :param pulumi.Input[str] modified_by: Account ID of the account that last modified the namespace.
        :param pulumi.Input[str] name: Name of the table.
               Must be between 1 and 255 characters in length.
               Can consist of lowercase letters, numbers, and underscores, and must begin and end with a lowercase letter or number.
        :param pulumi.Input[str] namespace: Name of the namespace for this table.
               Must be between 1 and 255 characters in length.
               Can consist of lowercase letters, numbers, and underscores, and must begin and end with a lowercase letter or number.
        :param pulumi.Input[str] owner_account_id: Account ID of the account that owns the namespace.
        :param pulumi.Input[str] table_bucket_arn: ARN referencing the Table Bucket that contains this Namespace.
               
               The following argument is optional:
        :param pulumi.Input[str] type: Type of the table.
               One of `customer` or `aws`.
        :param pulumi.Input[str] version_token: Identifier for the current version of table data.
        :param pulumi.Input[str] warehouse_location: S3 URI pointing to the S3 Bucket that contains the table data.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if format is not None:
            pulumi.set(__self__, "format", format)
        if maintenance_configuration is not None:
            pulumi.set(__self__, "maintenance_configuration", maintenance_configuration)
        if metadata_location is not None:
            pulumi.set(__self__, "metadata_location", metadata_location)
        if modified_at is not None:
            pulumi.set(__self__, "modified_at", modified_at)
        if modified_by is not None:
            pulumi.set(__self__, "modified_by", modified_by)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if owner_account_id is not None:
            pulumi.set(__self__, "owner_account_id", owner_account_id)
        if table_bucket_arn is not None:
            pulumi.set(__self__, "table_bucket_arn", table_bucket_arn)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if version_token is not None:
            pulumi.set(__self__, "version_token", version_token)
        if warehouse_location is not None:
            pulumi.set(__self__, "warehouse_location", warehouse_location)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the table.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Date and time when the namespace was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        Account ID of the account that created the namespace.
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[str]]:
        """
        Format of the table.
        Must be `ICEBERG`.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "format", value)

    @property
    @pulumi.getter(name="maintenanceConfiguration")
    def maintenance_configuration(self) -> Optional[pulumi.Input['TableMaintenanceConfigurationArgs']]:
        """
        A single table bucket maintenance configuration block.
        See `maintenance_configuration` below
        """
        return pulumi.get(self, "maintenance_configuration")

    @maintenance_configuration.setter
    def maintenance_configuration(self, value: Optional[pulumi.Input['TableMaintenanceConfigurationArgs']]):
        pulumi.set(self, "maintenance_configuration", value)

    @property
    @pulumi.getter(name="metadataLocation")
    def metadata_location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of table metadata.
        """
        return pulumi.get(self, "metadata_location")

    @metadata_location.setter
    def metadata_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metadata_location", value)

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> Optional[pulumi.Input[str]]:
        """
        Date and time when the namespace was last modified.
        """
        return pulumi.get(self, "modified_at")

    @modified_at.setter
    def modified_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "modified_at", value)

    @property
    @pulumi.getter(name="modifiedBy")
    def modified_by(self) -> Optional[pulumi.Input[str]]:
        """
        Account ID of the account that last modified the namespace.
        """
        return pulumi.get(self, "modified_by")

    @modified_by.setter
    def modified_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "modified_by", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the table.
        Must be between 1 and 255 characters in length.
        Can consist of lowercase letters, numbers, and underscores, and must begin and end with a lowercase letter or number.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the namespace for this table.
        Must be between 1 and 255 characters in length.
        Can consist of lowercase letters, numbers, and underscores, and must begin and end with a lowercase letter or number.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Account ID of the account that owns the namespace.
        """
        return pulumi.get(self, "owner_account_id")

    @owner_account_id.setter
    def owner_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner_account_id", value)

    @property
    @pulumi.getter(name="tableBucketArn")
    def table_bucket_arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN referencing the Table Bucket that contains this Namespace.

        The following argument is optional:
        """
        return pulumi.get(self, "table_bucket_arn")

    @table_bucket_arn.setter
    def table_bucket_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table_bucket_arn", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the table.
        One of `customer` or `aws`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="versionToken")
    def version_token(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier for the current version of table data.
        """
        return pulumi.get(self, "version_token")

    @version_token.setter
    def version_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_token", value)

    @property
    @pulumi.getter(name="warehouseLocation")
    def warehouse_location(self) -> Optional[pulumi.Input[str]]:
        """
        S3 URI pointing to the S3 Bucket that contains the table data.
        """
        return pulumi.get(self, "warehouse_location")

    @warehouse_location.setter
    def warehouse_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "warehouse_location", value)


class Table(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 format: Optional[pulumi.Input[str]] = None,
                 maintenance_configuration: Optional[pulumi.Input[Union['TableMaintenanceConfigurationArgs', 'TableMaintenanceConfigurationArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 table_bucket_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource for managing an Amazon S3 Tables Table.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_table_bucket = aws.s3tables.TableBucket("example", name="example-bucket")
        example_namespace = aws.s3tables.Namespace("example",
            namespace="example-namespace",
            table_bucket_arn=example_table_bucket.arn)
        example = aws.s3tables.Table("example",
            name="example-table",
            namespace=example_namespace.namespace,
            table_bucket_arn=example_namespace.table_bucket_arn,
            format="ICEBERG")
        ```

        ## Import

        Using `pulumi import`, import S3 Tables Table using the `table_bucket_arn`, the value of `namespace`, and the value of `name`, separated by a semicolon (`;`). For example:

        ```sh
        $ pulumi import aws:s3tables/table:Table example 'arn:aws:s3tables:us-west-2:123456789012:bucket/example-bucket;example-namespace;example-table'
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] format: Format of the table.
               Must be `ICEBERG`.
        :param pulumi.Input[Union['TableMaintenanceConfigurationArgs', 'TableMaintenanceConfigurationArgsDict']] maintenance_configuration: A single table bucket maintenance configuration block.
               See `maintenance_configuration` below
        :param pulumi.Input[str] name: Name of the table.
               Must be between 1 and 255 characters in length.
               Can consist of lowercase letters, numbers, and underscores, and must begin and end with a lowercase letter or number.
        :param pulumi.Input[str] namespace: Name of the namespace for this table.
               Must be between 1 and 255 characters in length.
               Can consist of lowercase letters, numbers, and underscores, and must begin and end with a lowercase letter or number.
        :param pulumi.Input[str] table_bucket_arn: ARN referencing the Table Bucket that contains this Namespace.
               
               The following argument is optional:
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing an Amazon S3 Tables Table.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_table_bucket = aws.s3tables.TableBucket("example", name="example-bucket")
        example_namespace = aws.s3tables.Namespace("example",
            namespace="example-namespace",
            table_bucket_arn=example_table_bucket.arn)
        example = aws.s3tables.Table("example",
            name="example-table",
            namespace=example_namespace.namespace,
            table_bucket_arn=example_namespace.table_bucket_arn,
            format="ICEBERG")
        ```

        ## Import

        Using `pulumi import`, import S3 Tables Table using the `table_bucket_arn`, the value of `namespace`, and the value of `name`, separated by a semicolon (`;`). For example:

        ```sh
        $ pulumi import aws:s3tables/table:Table example 'arn:aws:s3tables:us-west-2:123456789012:bucket/example-bucket;example-namespace;example-table'
        ```

        :param str resource_name: The name of the resource.
        :param TableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 format: Optional[pulumi.Input[str]] = None,
                 maintenance_configuration: Optional[pulumi.Input[Union['TableMaintenanceConfigurationArgs', 'TableMaintenanceConfigurationArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 table_bucket_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TableArgs.__new__(TableArgs)

            if format is None and not opts.urn:
                raise TypeError("Missing required property 'format'")
            __props__.__dict__["format"] = format
            __props__.__dict__["maintenance_configuration"] = maintenance_configuration
            __props__.__dict__["name"] = name
            if namespace is None and not opts.urn:
                raise TypeError("Missing required property 'namespace'")
            __props__.__dict__["namespace"] = namespace
            if table_bucket_arn is None and not opts.urn:
                raise TypeError("Missing required property 'table_bucket_arn'")
            __props__.__dict__["table_bucket_arn"] = table_bucket_arn
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["created_by"] = None
            __props__.__dict__["metadata_location"] = None
            __props__.__dict__["modified_at"] = None
            __props__.__dict__["modified_by"] = None
            __props__.__dict__["owner_account_id"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["version_token"] = None
            __props__.__dict__["warehouse_location"] = None
        super(Table, __self__).__init__(
            'aws:s3tables/table:Table',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            created_by: Optional[pulumi.Input[str]] = None,
            format: Optional[pulumi.Input[str]] = None,
            maintenance_configuration: Optional[pulumi.Input[Union['TableMaintenanceConfigurationArgs', 'TableMaintenanceConfigurationArgsDict']]] = None,
            metadata_location: Optional[pulumi.Input[str]] = None,
            modified_at: Optional[pulumi.Input[str]] = None,
            modified_by: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace: Optional[pulumi.Input[str]] = None,
            owner_account_id: Optional[pulumi.Input[str]] = None,
            table_bucket_arn: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            version_token: Optional[pulumi.Input[str]] = None,
            warehouse_location: Optional[pulumi.Input[str]] = None) -> 'Table':
        """
        Get an existing Table resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: ARN of the table.
        :param pulumi.Input[str] created_at: Date and time when the namespace was created.
        :param pulumi.Input[str] created_by: Account ID of the account that created the namespace.
        :param pulumi.Input[str] format: Format of the table.
               Must be `ICEBERG`.
        :param pulumi.Input[Union['TableMaintenanceConfigurationArgs', 'TableMaintenanceConfigurationArgsDict']] maintenance_configuration: A single table bucket maintenance configuration block.
               See `maintenance_configuration` below
        :param pulumi.Input[str] metadata_location: Location of table metadata.
        :param pulumi.Input[str] modified_at: Date and time when the namespace was last modified.
        :param pulumi.Input[str] modified_by: Account ID of the account that last modified the namespace.
        :param pulumi.Input[str] name: Name of the table.
               Must be between 1 and 255 characters in length.
               Can consist of lowercase letters, numbers, and underscores, and must begin and end with a lowercase letter or number.
        :param pulumi.Input[str] namespace: Name of the namespace for this table.
               Must be between 1 and 255 characters in length.
               Can consist of lowercase letters, numbers, and underscores, and must begin and end with a lowercase letter or number.
        :param pulumi.Input[str] owner_account_id: Account ID of the account that owns the namespace.
        :param pulumi.Input[str] table_bucket_arn: ARN referencing the Table Bucket that contains this Namespace.
               
               The following argument is optional:
        :param pulumi.Input[str] type: Type of the table.
               One of `customer` or `aws`.
        :param pulumi.Input[str] version_token: Identifier for the current version of table data.
        :param pulumi.Input[str] warehouse_location: S3 URI pointing to the S3 Bucket that contains the table data.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TableState.__new__(_TableState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["created_by"] = created_by
        __props__.__dict__["format"] = format
        __props__.__dict__["maintenance_configuration"] = maintenance_configuration
        __props__.__dict__["metadata_location"] = metadata_location
        __props__.__dict__["modified_at"] = modified_at
        __props__.__dict__["modified_by"] = modified_by
        __props__.__dict__["name"] = name
        __props__.__dict__["namespace"] = namespace
        __props__.__dict__["owner_account_id"] = owner_account_id
        __props__.__dict__["table_bucket_arn"] = table_bucket_arn
        __props__.__dict__["type"] = type
        __props__.__dict__["version_token"] = version_token
        __props__.__dict__["warehouse_location"] = warehouse_location
        return Table(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the table.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Date and time when the namespace was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        """
        Account ID of the account that created the namespace.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter
    def format(self) -> pulumi.Output[str]:
        """
        Format of the table.
        Must be `ICEBERG`.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter(name="maintenanceConfiguration")
    def maintenance_configuration(self) -> pulumi.Output['outputs.TableMaintenanceConfiguration']:
        """
        A single table bucket maintenance configuration block.
        See `maintenance_configuration` below
        """
        return pulumi.get(self, "maintenance_configuration")

    @property
    @pulumi.getter(name="metadataLocation")
    def metadata_location(self) -> pulumi.Output[str]:
        """
        Location of table metadata.
        """
        return pulumi.get(self, "metadata_location")

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> pulumi.Output[str]:
        """
        Date and time when the namespace was last modified.
        """
        return pulumi.get(self, "modified_at")

    @property
    @pulumi.getter(name="modifiedBy")
    def modified_by(self) -> pulumi.Output[str]:
        """
        Account ID of the account that last modified the namespace.
        """
        return pulumi.get(self, "modified_by")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the table.
        Must be between 1 and 255 characters in length.
        Can consist of lowercase letters, numbers, and underscores, and must begin and end with a lowercase letter or number.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[str]:
        """
        Name of the namespace for this table.
        Must be between 1 and 255 characters in length.
        Can consist of lowercase letters, numbers, and underscores, and must begin and end with a lowercase letter or number.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> pulumi.Output[str]:
        """
        Account ID of the account that owns the namespace.
        """
        return pulumi.get(self, "owner_account_id")

    @property
    @pulumi.getter(name="tableBucketArn")
    def table_bucket_arn(self) -> pulumi.Output[str]:
        """
        ARN referencing the Table Bucket that contains this Namespace.

        The following argument is optional:
        """
        return pulumi.get(self, "table_bucket_arn")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the table.
        One of `customer` or `aws`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="versionToken")
    def version_token(self) -> pulumi.Output[str]:
        """
        Identifier for the current version of table data.
        """
        return pulumi.get(self, "version_token")

    @property
    @pulumi.getter(name="warehouseLocation")
    def warehouse_location(self) -> pulumi.Output[str]:
        """
        S3 URI pointing to the S3 Bucket that contains the table data.
        """
        return pulumi.get(self, "warehouse_location")

