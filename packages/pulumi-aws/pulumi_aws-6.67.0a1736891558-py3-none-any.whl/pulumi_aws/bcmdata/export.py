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

__all__ = ['ExportArgs', 'Export']

@pulumi.input_type
class ExportArgs:
    def __init__(__self__, *,
                 export: Optional[pulumi.Input['ExportExportArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeouts: Optional[pulumi.Input['ExportTimeoutsArgs']] = None):
        """
        The set of arguments for constructing a Export resource.
        :param pulumi.Input['ExportExportArgs'] export: The details of the export, including data query, name, description, and destination configuration.  See the `export` argument reference below.
        """
        if export is not None:
            pulumi.set(__self__, "export", export)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter
    def export(self) -> Optional[pulumi.Input['ExportExportArgs']]:
        """
        The details of the export, including data query, name, description, and destination configuration.  See the `export` argument reference below.
        """
        return pulumi.get(self, "export")

    @export.setter
    def export(self, value: Optional[pulumi.Input['ExportExportArgs']]):
        pulumi.set(self, "export", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['ExportTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['ExportTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


@pulumi.input_type
class _ExportState:
    def __init__(__self__, *,
                 export: Optional[pulumi.Input['ExportExportArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeouts: Optional[pulumi.Input['ExportTimeoutsArgs']] = None):
        """
        Input properties used for looking up and filtering Export resources.
        :param pulumi.Input['ExportExportArgs'] export: The details of the export, including data query, name, description, and destination configuration.  See the `export` argument reference below.
        """
        if export is not None:
            pulumi.set(__self__, "export", export)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
            pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter
    def export(self) -> Optional[pulumi.Input['ExportExportArgs']]:
        """
        The details of the export, including data query, name, description, and destination configuration.  See the `export` argument reference below.
        """
        return pulumi.get(self, "export")

    @export.setter
    def export(self, value: Optional[pulumi.Input['ExportExportArgs']]):
        pulumi.set(self, "export", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    @_utilities.deprecated("""Please use `tags` instead.""")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['ExportTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['ExportTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


class Export(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 export: Optional[pulumi.Input[Union['ExportExportArgs', 'ExportExportArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeouts: Optional[pulumi.Input[Union['ExportTimeoutsArgs', 'ExportTimeoutsArgsDict']]] = None,
                 __props__=None):
        """
        Resource for managing an AWS BCM Data Exports Export.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.bcmdata.Export("test", export={
            "name": "testexample",
            "data_queries": [{
                "query_statement": "SELECT identity_line_item_id, identity_time_interval, line_item_product_code,line_item_unblended_cost FROM COST_AND_USAGE_REPORT",
                "table_configurations": {
                    "COST_AND_USAGE_REPORT": {
                        "TIME_GRANULARITY": "HOURLY",
                        "INCLUDE_RESOURCES": "FALSE",
                        "INCLUDE_MANUAL_DISCOUNT_COMPATIBILITY": "FALSE",
                        "INCLUDE_SPLIT_COST_ALLOCATION_DATA": "FALSE",
                    },
                },
            }],
            "destination_configurations": [{
                "s3_destinations": [{
                    "s3_bucket": test_aws_s3_bucket["bucket"],
                    "s3_prefix": test_aws_s3_bucket["bucketPrefix"],
                    "s3_region": test_aws_s3_bucket["region"],
                    "s3_output_configurations": [{
                        "overwrite": "OVERWRITE_REPORT",
                        "format": "TEXT_OR_CSV",
                        "compression": "GZIP",
                        "output_type": "CUSTOM",
                    }],
                }],
            }],
            "refresh_cadences": [{
                "frequency": "SYNCHRONOUS",
            }],
        })
        ```

        ## Import

        Using `pulumi import`, import BCM Data Exports Export using the export ARN. For example:

        ```sh
        $ pulumi import aws:bcmdata/export:Export example arn:aws:bcm-data-exports:us-east-1:123456789012:export/CostUsageReport-9f1c75f3-f982-4d9a-b936-1e7ecab814b7
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ExportExportArgs', 'ExportExportArgsDict']] export: The details of the export, including data query, name, description, and destination configuration.  See the `export` argument reference below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ExportArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing an AWS BCM Data Exports Export.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.bcmdata.Export("test", export={
            "name": "testexample",
            "data_queries": [{
                "query_statement": "SELECT identity_line_item_id, identity_time_interval, line_item_product_code,line_item_unblended_cost FROM COST_AND_USAGE_REPORT",
                "table_configurations": {
                    "COST_AND_USAGE_REPORT": {
                        "TIME_GRANULARITY": "HOURLY",
                        "INCLUDE_RESOURCES": "FALSE",
                        "INCLUDE_MANUAL_DISCOUNT_COMPATIBILITY": "FALSE",
                        "INCLUDE_SPLIT_COST_ALLOCATION_DATA": "FALSE",
                    },
                },
            }],
            "destination_configurations": [{
                "s3_destinations": [{
                    "s3_bucket": test_aws_s3_bucket["bucket"],
                    "s3_prefix": test_aws_s3_bucket["bucketPrefix"],
                    "s3_region": test_aws_s3_bucket["region"],
                    "s3_output_configurations": [{
                        "overwrite": "OVERWRITE_REPORT",
                        "format": "TEXT_OR_CSV",
                        "compression": "GZIP",
                        "output_type": "CUSTOM",
                    }],
                }],
            }],
            "refresh_cadences": [{
                "frequency": "SYNCHRONOUS",
            }],
        })
        ```

        ## Import

        Using `pulumi import`, import BCM Data Exports Export using the export ARN. For example:

        ```sh
        $ pulumi import aws:bcmdata/export:Export example arn:aws:bcm-data-exports:us-east-1:123456789012:export/CostUsageReport-9f1c75f3-f982-4d9a-b936-1e7ecab814b7
        ```

        :param str resource_name: The name of the resource.
        :param ExportArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExportArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 export: Optional[pulumi.Input[Union['ExportExportArgs', 'ExportExportArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeouts: Optional[pulumi.Input[Union['ExportTimeoutsArgs', 'ExportTimeoutsArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExportArgs.__new__(ExportArgs)

            __props__.__dict__["export"] = export
            __props__.__dict__["tags"] = tags
            __props__.__dict__["timeouts"] = timeouts
            __props__.__dict__["tags_all"] = None
        super(Export, __self__).__init__(
            'aws:bcmdata/export:Export',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            export: Optional[pulumi.Input[Union['ExportExportArgs', 'ExportExportArgsDict']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            timeouts: Optional[pulumi.Input[Union['ExportTimeoutsArgs', 'ExportTimeoutsArgsDict']]] = None) -> 'Export':
        """
        Get an existing Export resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ExportExportArgs', 'ExportExportArgsDict']] export: The details of the export, including data query, name, description, and destination configuration.  See the `export` argument reference below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ExportState.__new__(_ExportState)

        __props__.__dict__["export"] = export
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["timeouts"] = timeouts
        return Export(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def export(self) -> pulumi.Output[Optional['outputs.ExportExport']]:
        """
        The details of the export, including data query, name, description, and destination configuration.  See the `export` argument reference below.
        """
        return pulumi.get(self, "export")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    @_utilities.deprecated("""Please use `tags` instead.""")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional['outputs.ExportTimeouts']]:
        return pulumi.get(self, "timeouts")

