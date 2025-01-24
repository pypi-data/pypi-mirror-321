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

__all__ = ['AgentKnowledgeBaseArgs', 'AgentKnowledgeBase']

@pulumi.input_type
class AgentKnowledgeBaseArgs:
    def __init__(__self__, *,
                 role_arn: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 knowledge_base_configuration: Optional[pulumi.Input['AgentKnowledgeBaseKnowledgeBaseConfigurationArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage_configuration: Optional[pulumi.Input['AgentKnowledgeBaseStorageConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeouts: Optional[pulumi.Input['AgentKnowledgeBaseTimeoutsArgs']] = None):
        """
        The set of arguments for constructing a AgentKnowledgeBase resource.
        :param pulumi.Input[str] role_arn: ARN of the IAM role with permissions to invoke API operations on the knowledge base.
        :param pulumi.Input[str] description: Description of the knowledge base.
        :param pulumi.Input['AgentKnowledgeBaseKnowledgeBaseConfigurationArgs'] knowledge_base_configuration: Details about the embeddings configuration of the knowledge base. See `knowledge_base_configuration` block for details.
        :param pulumi.Input[str] name: Name of the knowledge base.
        :param pulumi.Input['AgentKnowledgeBaseStorageConfigurationArgs'] storage_configuration: Details about the storage configuration of the knowledge base. See `storage_configuration` block for details.
               
               The following arguments are optional:
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags assigned to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        pulumi.set(__self__, "role_arn", role_arn)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if knowledge_base_configuration is not None:
            pulumi.set(__self__, "knowledge_base_configuration", knowledge_base_configuration)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if storage_configuration is not None:
            pulumi.set(__self__, "storage_configuration", storage_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        ARN of the IAM role with permissions to invoke API operations on the knowledge base.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the knowledge base.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="knowledgeBaseConfiguration")
    def knowledge_base_configuration(self) -> Optional[pulumi.Input['AgentKnowledgeBaseKnowledgeBaseConfigurationArgs']]:
        """
        Details about the embeddings configuration of the knowledge base. See `knowledge_base_configuration` block for details.
        """
        return pulumi.get(self, "knowledge_base_configuration")

    @knowledge_base_configuration.setter
    def knowledge_base_configuration(self, value: Optional[pulumi.Input['AgentKnowledgeBaseKnowledgeBaseConfigurationArgs']]):
        pulumi.set(self, "knowledge_base_configuration", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the knowledge base.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="storageConfiguration")
    def storage_configuration(self) -> Optional[pulumi.Input['AgentKnowledgeBaseStorageConfigurationArgs']]:
        """
        Details about the storage configuration of the knowledge base. See `storage_configuration` block for details.

        The following arguments are optional:
        """
        return pulumi.get(self, "storage_configuration")

    @storage_configuration.setter
    def storage_configuration(self, value: Optional[pulumi.Input['AgentKnowledgeBaseStorageConfigurationArgs']]):
        pulumi.set(self, "storage_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of tags assigned to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['AgentKnowledgeBaseTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['AgentKnowledgeBaseTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


@pulumi.input_type
class _AgentKnowledgeBaseState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 failure_reasons: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 knowledge_base_configuration: Optional[pulumi.Input['AgentKnowledgeBaseKnowledgeBaseConfigurationArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 storage_configuration: Optional[pulumi.Input['AgentKnowledgeBaseStorageConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeouts: Optional[pulumi.Input['AgentKnowledgeBaseTimeoutsArgs']] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AgentKnowledgeBase resources.
        :param pulumi.Input[str] arn: ARN of the knowledge base.
        :param pulumi.Input[str] created_at: Time at which the knowledge base was created.
        :param pulumi.Input[str] description: Description of the knowledge base.
        :param pulumi.Input['AgentKnowledgeBaseKnowledgeBaseConfigurationArgs'] knowledge_base_configuration: Details about the embeddings configuration of the knowledge base. See `knowledge_base_configuration` block for details.
        :param pulumi.Input[str] name: Name of the knowledge base.
        :param pulumi.Input[str] role_arn: ARN of the IAM role with permissions to invoke API operations on the knowledge base.
        :param pulumi.Input['AgentKnowledgeBaseStorageConfigurationArgs'] storage_configuration: Details about the storage configuration of the knowledge base. See `storage_configuration` block for details.
               
               The following arguments are optional:
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags assigned to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] updated_at: Time at which the knowledge base was last updated.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if failure_reasons is not None:
            pulumi.set(__self__, "failure_reasons", failure_reasons)
        if knowledge_base_configuration is not None:
            pulumi.set(__self__, "knowledge_base_configuration", knowledge_base_configuration)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)
        if storage_configuration is not None:
            pulumi.set(__self__, "storage_configuration", storage_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
            pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the knowledge base.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Time at which the knowledge base was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the knowledge base.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="failureReasons")
    def failure_reasons(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "failure_reasons")

    @failure_reasons.setter
    def failure_reasons(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "failure_reasons", value)

    @property
    @pulumi.getter(name="knowledgeBaseConfiguration")
    def knowledge_base_configuration(self) -> Optional[pulumi.Input['AgentKnowledgeBaseKnowledgeBaseConfigurationArgs']]:
        """
        Details about the embeddings configuration of the knowledge base. See `knowledge_base_configuration` block for details.
        """
        return pulumi.get(self, "knowledge_base_configuration")

    @knowledge_base_configuration.setter
    def knowledge_base_configuration(self, value: Optional[pulumi.Input['AgentKnowledgeBaseKnowledgeBaseConfigurationArgs']]):
        pulumi.set(self, "knowledge_base_configuration", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the knowledge base.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the IAM role with permissions to invoke API operations on the knowledge base.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="storageConfiguration")
    def storage_configuration(self) -> Optional[pulumi.Input['AgentKnowledgeBaseStorageConfigurationArgs']]:
        """
        Details about the storage configuration of the knowledge base. See `storage_configuration` block for details.

        The following arguments are optional:
        """
        return pulumi.get(self, "storage_configuration")

    @storage_configuration.setter
    def storage_configuration(self, value: Optional[pulumi.Input['AgentKnowledgeBaseStorageConfigurationArgs']]):
        pulumi.set(self, "storage_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of tags assigned to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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
    def timeouts(self) -> Optional[pulumi.Input['AgentKnowledgeBaseTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['AgentKnowledgeBaseTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        Time at which the knowledge base was last updated.
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)


class AgentKnowledgeBase(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 knowledge_base_configuration: Optional[pulumi.Input[Union['AgentKnowledgeBaseKnowledgeBaseConfigurationArgs', 'AgentKnowledgeBaseKnowledgeBaseConfigurationArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 storage_configuration: Optional[pulumi.Input[Union['AgentKnowledgeBaseStorageConfigurationArgs', 'AgentKnowledgeBaseStorageConfigurationArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeouts: Optional[pulumi.Input[Union['AgentKnowledgeBaseTimeoutsArgs', 'AgentKnowledgeBaseTimeoutsArgsDict']]] = None,
                 __props__=None):
        """
        Resource for managing an AWS Agents for Amazon Bedrock Knowledge Base.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.bedrock.AgentKnowledgeBase("example",
            name="example",
            role_arn=example_aws_iam_role["arn"],
            knowledge_base_configuration={
                "vector_knowledge_base_configuration": {
                    "embedding_model_arn": "arn:aws:bedrock:us-west-2::foundation-model/amazon.titan-embed-text-v1",
                },
                "type": "VECTOR",
            },
            storage_configuration={
                "type": "OPENSEARCH_SERVERLESS",
                "opensearch_serverless_configuration": {
                    "collection_arn": "arn:aws:aoss:us-west-2:123456789012:collection/142bezjddq707i5stcrf",
                    "vector_index_name": "bedrock-knowledge-base-default-index",
                    "field_mapping": {
                        "vector_field": "bedrock-knowledge-base-default-vector",
                        "text_field": "AMAZON_BEDROCK_TEXT_CHUNK",
                        "metadata_field": "AMAZON_BEDROCK_METADATA",
                    },
                },
            })
        ```

        ## Import

        Using `pulumi import`, import Agents for Amazon Bedrock Knowledge Base using the knowledge base ID. For example:

        ```sh
        $ pulumi import aws:bedrock/agentKnowledgeBase:AgentKnowledgeBase example EMDPPAYPZI
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the knowledge base.
        :param pulumi.Input[Union['AgentKnowledgeBaseKnowledgeBaseConfigurationArgs', 'AgentKnowledgeBaseKnowledgeBaseConfigurationArgsDict']] knowledge_base_configuration: Details about the embeddings configuration of the knowledge base. See `knowledge_base_configuration` block for details.
        :param pulumi.Input[str] name: Name of the knowledge base.
        :param pulumi.Input[str] role_arn: ARN of the IAM role with permissions to invoke API operations on the knowledge base.
        :param pulumi.Input[Union['AgentKnowledgeBaseStorageConfigurationArgs', 'AgentKnowledgeBaseStorageConfigurationArgsDict']] storage_configuration: Details about the storage configuration of the knowledge base. See `storage_configuration` block for details.
               
               The following arguments are optional:
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags assigned to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AgentKnowledgeBaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing an AWS Agents for Amazon Bedrock Knowledge Base.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.bedrock.AgentKnowledgeBase("example",
            name="example",
            role_arn=example_aws_iam_role["arn"],
            knowledge_base_configuration={
                "vector_knowledge_base_configuration": {
                    "embedding_model_arn": "arn:aws:bedrock:us-west-2::foundation-model/amazon.titan-embed-text-v1",
                },
                "type": "VECTOR",
            },
            storage_configuration={
                "type": "OPENSEARCH_SERVERLESS",
                "opensearch_serverless_configuration": {
                    "collection_arn": "arn:aws:aoss:us-west-2:123456789012:collection/142bezjddq707i5stcrf",
                    "vector_index_name": "bedrock-knowledge-base-default-index",
                    "field_mapping": {
                        "vector_field": "bedrock-knowledge-base-default-vector",
                        "text_field": "AMAZON_BEDROCK_TEXT_CHUNK",
                        "metadata_field": "AMAZON_BEDROCK_METADATA",
                    },
                },
            })
        ```

        ## Import

        Using `pulumi import`, import Agents for Amazon Bedrock Knowledge Base using the knowledge base ID. For example:

        ```sh
        $ pulumi import aws:bedrock/agentKnowledgeBase:AgentKnowledgeBase example EMDPPAYPZI
        ```

        :param str resource_name: The name of the resource.
        :param AgentKnowledgeBaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AgentKnowledgeBaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 knowledge_base_configuration: Optional[pulumi.Input[Union['AgentKnowledgeBaseKnowledgeBaseConfigurationArgs', 'AgentKnowledgeBaseKnowledgeBaseConfigurationArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 storage_configuration: Optional[pulumi.Input[Union['AgentKnowledgeBaseStorageConfigurationArgs', 'AgentKnowledgeBaseStorageConfigurationArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeouts: Optional[pulumi.Input[Union['AgentKnowledgeBaseTimeoutsArgs', 'AgentKnowledgeBaseTimeoutsArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AgentKnowledgeBaseArgs.__new__(AgentKnowledgeBaseArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["knowledge_base_configuration"] = knowledge_base_configuration
            __props__.__dict__["name"] = name
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["storage_configuration"] = storage_configuration
            __props__.__dict__["tags"] = tags
            __props__.__dict__["timeouts"] = timeouts
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["failure_reasons"] = None
            __props__.__dict__["tags_all"] = None
            __props__.__dict__["updated_at"] = None
        super(AgentKnowledgeBase, __self__).__init__(
            'aws:bedrock/agentKnowledgeBase:AgentKnowledgeBase',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            failure_reasons: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            knowledge_base_configuration: Optional[pulumi.Input[Union['AgentKnowledgeBaseKnowledgeBaseConfigurationArgs', 'AgentKnowledgeBaseKnowledgeBaseConfigurationArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            role_arn: Optional[pulumi.Input[str]] = None,
            storage_configuration: Optional[pulumi.Input[Union['AgentKnowledgeBaseStorageConfigurationArgs', 'AgentKnowledgeBaseStorageConfigurationArgsDict']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            timeouts: Optional[pulumi.Input[Union['AgentKnowledgeBaseTimeoutsArgs', 'AgentKnowledgeBaseTimeoutsArgsDict']]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'AgentKnowledgeBase':
        """
        Get an existing AgentKnowledgeBase resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: ARN of the knowledge base.
        :param pulumi.Input[str] created_at: Time at which the knowledge base was created.
        :param pulumi.Input[str] description: Description of the knowledge base.
        :param pulumi.Input[Union['AgentKnowledgeBaseKnowledgeBaseConfigurationArgs', 'AgentKnowledgeBaseKnowledgeBaseConfigurationArgsDict']] knowledge_base_configuration: Details about the embeddings configuration of the knowledge base. See `knowledge_base_configuration` block for details.
        :param pulumi.Input[str] name: Name of the knowledge base.
        :param pulumi.Input[str] role_arn: ARN of the IAM role with permissions to invoke API operations on the knowledge base.
        :param pulumi.Input[Union['AgentKnowledgeBaseStorageConfigurationArgs', 'AgentKnowledgeBaseStorageConfigurationArgsDict']] storage_configuration: Details about the storage configuration of the knowledge base. See `storage_configuration` block for details.
               
               The following arguments are optional:
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags assigned to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] updated_at: Time at which the knowledge base was last updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AgentKnowledgeBaseState.__new__(_AgentKnowledgeBaseState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["description"] = description
        __props__.__dict__["failure_reasons"] = failure_reasons
        __props__.__dict__["knowledge_base_configuration"] = knowledge_base_configuration
        __props__.__dict__["name"] = name
        __props__.__dict__["role_arn"] = role_arn
        __props__.__dict__["storage_configuration"] = storage_configuration
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["timeouts"] = timeouts
        __props__.__dict__["updated_at"] = updated_at
        return AgentKnowledgeBase(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the knowledge base.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Time at which the knowledge base was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the knowledge base.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="failureReasons")
    def failure_reasons(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "failure_reasons")

    @property
    @pulumi.getter(name="knowledgeBaseConfiguration")
    def knowledge_base_configuration(self) -> pulumi.Output[Optional['outputs.AgentKnowledgeBaseKnowledgeBaseConfiguration']]:
        """
        Details about the embeddings configuration of the knowledge base. See `knowledge_base_configuration` block for details.
        """
        return pulumi.get(self, "knowledge_base_configuration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the knowledge base.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        ARN of the IAM role with permissions to invoke API operations on the knowledge base.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="storageConfiguration")
    def storage_configuration(self) -> pulumi.Output[Optional['outputs.AgentKnowledgeBaseStorageConfiguration']]:
        """
        Details about the storage configuration of the knowledge base. See `storage_configuration` block for details.

        The following arguments are optional:
        """
        return pulumi.get(self, "storage_configuration")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Map of tags assigned to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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
    def timeouts(self) -> pulumi.Output[Optional['outputs.AgentKnowledgeBaseTimeouts']]:
        return pulumi.get(self, "timeouts")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Time at which the knowledge base was last updated.
        """
        return pulumi.get(self, "updated_at")

