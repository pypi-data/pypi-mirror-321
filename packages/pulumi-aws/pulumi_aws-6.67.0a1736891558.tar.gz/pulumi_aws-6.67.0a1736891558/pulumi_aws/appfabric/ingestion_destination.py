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

__all__ = ['IngestionDestinationArgs', 'IngestionDestination']

@pulumi.input_type
class IngestionDestinationArgs:
    def __init__(__self__, *,
                 app_bundle_arn: pulumi.Input[str],
                 ingestion_arn: pulumi.Input[str],
                 destination_configuration: Optional[pulumi.Input['IngestionDestinationDestinationConfigurationArgs']] = None,
                 processing_configuration: Optional[pulumi.Input['IngestionDestinationProcessingConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeouts: Optional[pulumi.Input['IngestionDestinationTimeoutsArgs']] = None):
        """
        The set of arguments for constructing a IngestionDestination resource.
        :param pulumi.Input[str] app_bundle_arn: The Amazon Resource Name (ARN) of the app bundle to use for the request.
        :param pulumi.Input[str] ingestion_arn: The Amazon Resource Name (ARN) of the ingestion to use for the request.
        :param pulumi.Input['IngestionDestinationDestinationConfigurationArgs'] destination_configuration: Contains information about the destination of ingested data.
        :param pulumi.Input['IngestionDestinationProcessingConfigurationArgs'] processing_configuration: Contains information about how ingested data is processed.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        pulumi.set(__self__, "app_bundle_arn", app_bundle_arn)
        pulumi.set(__self__, "ingestion_arn", ingestion_arn)
        if destination_configuration is not None:
            pulumi.set(__self__, "destination_configuration", destination_configuration)
        if processing_configuration is not None:
            pulumi.set(__self__, "processing_configuration", processing_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter(name="appBundleArn")
    def app_bundle_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the app bundle to use for the request.
        """
        return pulumi.get(self, "app_bundle_arn")

    @app_bundle_arn.setter
    def app_bundle_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_bundle_arn", value)

    @property
    @pulumi.getter(name="ingestionArn")
    def ingestion_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the ingestion to use for the request.
        """
        return pulumi.get(self, "ingestion_arn")

    @ingestion_arn.setter
    def ingestion_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "ingestion_arn", value)

    @property
    @pulumi.getter(name="destinationConfiguration")
    def destination_configuration(self) -> Optional[pulumi.Input['IngestionDestinationDestinationConfigurationArgs']]:
        """
        Contains information about the destination of ingested data.
        """
        return pulumi.get(self, "destination_configuration")

    @destination_configuration.setter
    def destination_configuration(self, value: Optional[pulumi.Input['IngestionDestinationDestinationConfigurationArgs']]):
        pulumi.set(self, "destination_configuration", value)

    @property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(self) -> Optional[pulumi.Input['IngestionDestinationProcessingConfigurationArgs']]:
        """
        Contains information about how ingested data is processed.
        """
        return pulumi.get(self, "processing_configuration")

    @processing_configuration.setter
    def processing_configuration(self, value: Optional[pulumi.Input['IngestionDestinationProcessingConfigurationArgs']]):
        pulumi.set(self, "processing_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['IngestionDestinationTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['IngestionDestinationTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


@pulumi.input_type
class _IngestionDestinationState:
    def __init__(__self__, *,
                 app_bundle_arn: Optional[pulumi.Input[str]] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 destination_configuration: Optional[pulumi.Input['IngestionDestinationDestinationConfigurationArgs']] = None,
                 ingestion_arn: Optional[pulumi.Input[str]] = None,
                 processing_configuration: Optional[pulumi.Input['IngestionDestinationProcessingConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeouts: Optional[pulumi.Input['IngestionDestinationTimeoutsArgs']] = None):
        """
        Input properties used for looking up and filtering IngestionDestination resources.
        :param pulumi.Input[str] app_bundle_arn: The Amazon Resource Name (ARN) of the app bundle to use for the request.
        :param pulumi.Input[str] arn: ARN of the Ingestion Destination.
        :param pulumi.Input['IngestionDestinationDestinationConfigurationArgs'] destination_configuration: Contains information about the destination of ingested data.
        :param pulumi.Input[str] ingestion_arn: The Amazon Resource Name (ARN) of the ingestion to use for the request.
        :param pulumi.Input['IngestionDestinationProcessingConfigurationArgs'] processing_configuration: Contains information about how ingested data is processed.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        if app_bundle_arn is not None:
            pulumi.set(__self__, "app_bundle_arn", app_bundle_arn)
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if destination_configuration is not None:
            pulumi.set(__self__, "destination_configuration", destination_configuration)
        if ingestion_arn is not None:
            pulumi.set(__self__, "ingestion_arn", ingestion_arn)
        if processing_configuration is not None:
            pulumi.set(__self__, "processing_configuration", processing_configuration)
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
    @pulumi.getter(name="appBundleArn")
    def app_bundle_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the app bundle to use for the request.
        """
        return pulumi.get(self, "app_bundle_arn")

    @app_bundle_arn.setter
    def app_bundle_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_bundle_arn", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the Ingestion Destination.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="destinationConfiguration")
    def destination_configuration(self) -> Optional[pulumi.Input['IngestionDestinationDestinationConfigurationArgs']]:
        """
        Contains information about the destination of ingested data.
        """
        return pulumi.get(self, "destination_configuration")

    @destination_configuration.setter
    def destination_configuration(self, value: Optional[pulumi.Input['IngestionDestinationDestinationConfigurationArgs']]):
        pulumi.set(self, "destination_configuration", value)

    @property
    @pulumi.getter(name="ingestionArn")
    def ingestion_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the ingestion to use for the request.
        """
        return pulumi.get(self, "ingestion_arn")

    @ingestion_arn.setter
    def ingestion_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ingestion_arn", value)

    @property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(self) -> Optional[pulumi.Input['IngestionDestinationProcessingConfigurationArgs']]:
        """
        Contains information about how ingested data is processed.
        """
        return pulumi.get(self, "processing_configuration")

    @processing_configuration.setter
    def processing_configuration(self, value: Optional[pulumi.Input['IngestionDestinationProcessingConfigurationArgs']]):
        pulumi.set(self, "processing_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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
        Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['IngestionDestinationTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['IngestionDestinationTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


class IngestionDestination(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_bundle_arn: Optional[pulumi.Input[str]] = None,
                 destination_configuration: Optional[pulumi.Input[Union['IngestionDestinationDestinationConfigurationArgs', 'IngestionDestinationDestinationConfigurationArgsDict']]] = None,
                 ingestion_arn: Optional[pulumi.Input[str]] = None,
                 processing_configuration: Optional[pulumi.Input[Union['IngestionDestinationProcessingConfigurationArgs', 'IngestionDestinationProcessingConfigurationArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeouts: Optional[pulumi.Input[Union['IngestionDestinationTimeoutsArgs', 'IngestionDestinationTimeoutsArgsDict']]] = None,
                 __props__=None):
        """
        Resource for managing an AWS AppFabric Ingestion Destination.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.appfabric.IngestionDestination("example",
            app_bundle_arn=example_aws_appfabric_app_bundle["arn"],
            ingestion_arn=example_aws_appfabric_ingestion["arn"],
            processing_configuration={
                "audit_log": {
                    "format": "json",
                    "schema": "raw",
                },
            },
            destination_configuration={
                "audit_log": {
                    "destination": {
                        "s3_bucket": {
                            "bucket_name": example_aws_s3_bucket["bucket"],
                        },
                    },
                },
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_bundle_arn: The Amazon Resource Name (ARN) of the app bundle to use for the request.
        :param pulumi.Input[Union['IngestionDestinationDestinationConfigurationArgs', 'IngestionDestinationDestinationConfigurationArgsDict']] destination_configuration: Contains information about the destination of ingested data.
        :param pulumi.Input[str] ingestion_arn: The Amazon Resource Name (ARN) of the ingestion to use for the request.
        :param pulumi.Input[Union['IngestionDestinationProcessingConfigurationArgs', 'IngestionDestinationProcessingConfigurationArgsDict']] processing_configuration: Contains information about how ingested data is processed.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IngestionDestinationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing an AWS AppFabric Ingestion Destination.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.appfabric.IngestionDestination("example",
            app_bundle_arn=example_aws_appfabric_app_bundle["arn"],
            ingestion_arn=example_aws_appfabric_ingestion["arn"],
            processing_configuration={
                "audit_log": {
                    "format": "json",
                    "schema": "raw",
                },
            },
            destination_configuration={
                "audit_log": {
                    "destination": {
                        "s3_bucket": {
                            "bucket_name": example_aws_s3_bucket["bucket"],
                        },
                    },
                },
            })
        ```

        :param str resource_name: The name of the resource.
        :param IngestionDestinationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IngestionDestinationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_bundle_arn: Optional[pulumi.Input[str]] = None,
                 destination_configuration: Optional[pulumi.Input[Union['IngestionDestinationDestinationConfigurationArgs', 'IngestionDestinationDestinationConfigurationArgsDict']]] = None,
                 ingestion_arn: Optional[pulumi.Input[str]] = None,
                 processing_configuration: Optional[pulumi.Input[Union['IngestionDestinationProcessingConfigurationArgs', 'IngestionDestinationProcessingConfigurationArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeouts: Optional[pulumi.Input[Union['IngestionDestinationTimeoutsArgs', 'IngestionDestinationTimeoutsArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IngestionDestinationArgs.__new__(IngestionDestinationArgs)

            if app_bundle_arn is None and not opts.urn:
                raise TypeError("Missing required property 'app_bundle_arn'")
            __props__.__dict__["app_bundle_arn"] = app_bundle_arn
            __props__.__dict__["destination_configuration"] = destination_configuration
            if ingestion_arn is None and not opts.urn:
                raise TypeError("Missing required property 'ingestion_arn'")
            __props__.__dict__["ingestion_arn"] = ingestion_arn
            __props__.__dict__["processing_configuration"] = processing_configuration
            __props__.__dict__["tags"] = tags
            __props__.__dict__["timeouts"] = timeouts
            __props__.__dict__["arn"] = None
            __props__.__dict__["tags_all"] = None
        super(IngestionDestination, __self__).__init__(
            'aws:appfabric/ingestionDestination:IngestionDestination',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_bundle_arn: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            destination_configuration: Optional[pulumi.Input[Union['IngestionDestinationDestinationConfigurationArgs', 'IngestionDestinationDestinationConfigurationArgsDict']]] = None,
            ingestion_arn: Optional[pulumi.Input[str]] = None,
            processing_configuration: Optional[pulumi.Input[Union['IngestionDestinationProcessingConfigurationArgs', 'IngestionDestinationProcessingConfigurationArgsDict']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            timeouts: Optional[pulumi.Input[Union['IngestionDestinationTimeoutsArgs', 'IngestionDestinationTimeoutsArgsDict']]] = None) -> 'IngestionDestination':
        """
        Get an existing IngestionDestination resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_bundle_arn: The Amazon Resource Name (ARN) of the app bundle to use for the request.
        :param pulumi.Input[str] arn: ARN of the Ingestion Destination.
        :param pulumi.Input[Union['IngestionDestinationDestinationConfigurationArgs', 'IngestionDestinationDestinationConfigurationArgsDict']] destination_configuration: Contains information about the destination of ingested data.
        :param pulumi.Input[str] ingestion_arn: The Amazon Resource Name (ARN) of the ingestion to use for the request.
        :param pulumi.Input[Union['IngestionDestinationProcessingConfigurationArgs', 'IngestionDestinationProcessingConfigurationArgsDict']] processing_configuration: Contains information about how ingested data is processed.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IngestionDestinationState.__new__(_IngestionDestinationState)

        __props__.__dict__["app_bundle_arn"] = app_bundle_arn
        __props__.__dict__["arn"] = arn
        __props__.__dict__["destination_configuration"] = destination_configuration
        __props__.__dict__["ingestion_arn"] = ingestion_arn
        __props__.__dict__["processing_configuration"] = processing_configuration
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["timeouts"] = timeouts
        return IngestionDestination(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appBundleArn")
    def app_bundle_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the app bundle to use for the request.
        """
        return pulumi.get(self, "app_bundle_arn")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the Ingestion Destination.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="destinationConfiguration")
    def destination_configuration(self) -> pulumi.Output[Optional['outputs.IngestionDestinationDestinationConfiguration']]:
        """
        Contains information about the destination of ingested data.
        """
        return pulumi.get(self, "destination_configuration")

    @property
    @pulumi.getter(name="ingestionArn")
    def ingestion_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the ingestion to use for the request.
        """
        return pulumi.get(self, "ingestion_arn")

    @property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(self) -> pulumi.Output[Optional['outputs.IngestionDestinationProcessingConfiguration']]:
        """
        Contains information about how ingested data is processed.
        """
        return pulumi.get(self, "processing_configuration")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    @_utilities.deprecated("""Please use `tags` instead.""")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional['outputs.IngestionDestinationTimeouts']]:
        return pulumi.get(self, "timeouts")

