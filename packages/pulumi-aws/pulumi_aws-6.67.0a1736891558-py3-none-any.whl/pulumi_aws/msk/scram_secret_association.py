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

__all__ = ['ScramSecretAssociationArgs', 'ScramSecretAssociation']

@pulumi.input_type
class ScramSecretAssociationArgs:
    def __init__(__self__, *,
                 cluster_arn: pulumi.Input[str],
                 secret_arn_lists: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        The set of arguments for constructing a ScramSecretAssociation resource.
        :param pulumi.Input[str] cluster_arn: Amazon Resource Name (ARN) of the MSK cluster.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] secret_arn_lists: List of AWS Secrets Manager secret ARNs.
        """
        pulumi.set(__self__, "cluster_arn", cluster_arn)
        pulumi.set(__self__, "secret_arn_lists", secret_arn_lists)

    @property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> pulumi.Input[str]:
        """
        Amazon Resource Name (ARN) of the MSK cluster.
        """
        return pulumi.get(self, "cluster_arn")

    @cluster_arn.setter
    def cluster_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_arn", value)

    @property
    @pulumi.getter(name="secretArnLists")
    def secret_arn_lists(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of AWS Secrets Manager secret ARNs.
        """
        return pulumi.get(self, "secret_arn_lists")

    @secret_arn_lists.setter
    def secret_arn_lists(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "secret_arn_lists", value)


@pulumi.input_type
class _ScramSecretAssociationState:
    def __init__(__self__, *,
                 cluster_arn: Optional[pulumi.Input[str]] = None,
                 secret_arn_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering ScramSecretAssociation resources.
        :param pulumi.Input[str] cluster_arn: Amazon Resource Name (ARN) of the MSK cluster.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] secret_arn_lists: List of AWS Secrets Manager secret ARNs.
        """
        if cluster_arn is not None:
            pulumi.set(__self__, "cluster_arn", cluster_arn)
        if secret_arn_lists is not None:
            pulumi.set(__self__, "secret_arn_lists", secret_arn_lists)

    @property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of the MSK cluster.
        """
        return pulumi.get(self, "cluster_arn")

    @cluster_arn.setter
    def cluster_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_arn", value)

    @property
    @pulumi.getter(name="secretArnLists")
    def secret_arn_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of AWS Secrets Manager secret ARNs.
        """
        return pulumi.get(self, "secret_arn_lists")

    @secret_arn_lists.setter
    def secret_arn_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "secret_arn_lists", value)


class ScramSecretAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_arn: Optional[pulumi.Input[str]] = None,
                 secret_arn_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Associates SCRAM secrets stored in the Secrets Manager service with a Managed Streaming for Kafka (MSK) cluster.

        !> This resource takes exclusive ownership over SCRAM secrets associated with a cluster. This includes removal of SCRAM secrets which are not explicitly configured. To prevent persistent drift, ensure any `msk.SingleScramSecretAssociation` resources managed alongside this resource are included in the `secret_arn_list` argument.

        > **Note:** The following assumes the MSK cluster has SASL/SCRAM authentication enabled. See below for example usage or refer to the [Username/Password Authentication](https://docs.aws.amazon.com/msk/latest/developerguide/msk-password.html) section of the MSK Developer Guide for more details.

        To set up username and password authentication for a cluster, create an `secretsmanager.Secret` resource and associate
        a username and password with the secret with an `secretsmanager.SecretVersion` resource. When creating a secret for the cluster,
        the `name` must have the prefix `AmazonMSK_` and you must either use an existing custom AWS KMS key or create a new
        custom AWS KMS key for your secret with the `kms.Key` resource. It is important to note that a policy is required for the `secretsmanager.Secret`
        resource in order for Kafka to be able to read it. This policy is attached automatically when the `msk.ScramSecretAssociation` is used,
        however, this policy will not be in the state and as such, will present a diff on plan/apply. For that reason, you must use the `secretsmanager.SecretPolicy`
        resource](/docs/providers/aws/r/secretsmanager_secret_policy.html) as shown below in order to ensure that the state is in a clean state after the creation of secret and the association to the cluster.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        example_cluster = aws.msk.Cluster("example",
            cluster_name="example",
            client_authentication={
                "sasl": {
                    "scram": True,
                },
            })
        example_key = aws.kms.Key("example", description="Example Key for MSK Cluster Scram Secret Association")
        example_secret = aws.secretsmanager.Secret("example",
            name="AmazonMSK_example",
            kms_key_id=example_key.key_id)
        example_secret_version = aws.secretsmanager.SecretVersion("example",
            secret_id=example_secret.id,
            secret_string=json.dumps({
                "username": "user",
                "password": "pass",
            }))
        example_scram_secret_association = aws.msk.ScramSecretAssociation("example",
            cluster_arn=example_cluster.arn,
            secret_arn_lists=[example_secret.arn],
            opts = pulumi.ResourceOptions(depends_on=[example_secret_version]))
        example = aws.iam.get_policy_document_output(statements=[{
            "sid": "AWSKafkaResourcePolicy",
            "effect": "Allow",
            "principals": [{
                "type": "Service",
                "identifiers": ["kafka.amazonaws.com"],
            }],
            "actions": ["secretsmanager:getSecretValue"],
            "resources": [example_secret.arn],
        }])
        example_secret_policy = aws.secretsmanager.SecretPolicy("example",
            secret_arn=example_secret.arn,
            policy=example.json)
        ```

        ## Import

        Using `pulumi import`, import MSK SCRAM Secret Associations using the `id`. For example:

        ```sh
        $ pulumi import aws:msk/scramSecretAssociation:ScramSecretAssociation example arn:aws:kafka:us-west-2:123456789012:cluster/example/279c0212-d057-4dba-9aa9-1c4e5a25bfc7-3
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_arn: Amazon Resource Name (ARN) of the MSK cluster.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] secret_arn_lists: List of AWS Secrets Manager secret ARNs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScramSecretAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Associates SCRAM secrets stored in the Secrets Manager service with a Managed Streaming for Kafka (MSK) cluster.

        !> This resource takes exclusive ownership over SCRAM secrets associated with a cluster. This includes removal of SCRAM secrets which are not explicitly configured. To prevent persistent drift, ensure any `msk.SingleScramSecretAssociation` resources managed alongside this resource are included in the `secret_arn_list` argument.

        > **Note:** The following assumes the MSK cluster has SASL/SCRAM authentication enabled. See below for example usage or refer to the [Username/Password Authentication](https://docs.aws.amazon.com/msk/latest/developerguide/msk-password.html) section of the MSK Developer Guide for more details.

        To set up username and password authentication for a cluster, create an `secretsmanager.Secret` resource and associate
        a username and password with the secret with an `secretsmanager.SecretVersion` resource. When creating a secret for the cluster,
        the `name` must have the prefix `AmazonMSK_` and you must either use an existing custom AWS KMS key or create a new
        custom AWS KMS key for your secret with the `kms.Key` resource. It is important to note that a policy is required for the `secretsmanager.Secret`
        resource in order for Kafka to be able to read it. This policy is attached automatically when the `msk.ScramSecretAssociation` is used,
        however, this policy will not be in the state and as such, will present a diff on plan/apply. For that reason, you must use the `secretsmanager.SecretPolicy`
        resource](/docs/providers/aws/r/secretsmanager_secret_policy.html) as shown below in order to ensure that the state is in a clean state after the creation of secret and the association to the cluster.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        example_cluster = aws.msk.Cluster("example",
            cluster_name="example",
            client_authentication={
                "sasl": {
                    "scram": True,
                },
            })
        example_key = aws.kms.Key("example", description="Example Key for MSK Cluster Scram Secret Association")
        example_secret = aws.secretsmanager.Secret("example",
            name="AmazonMSK_example",
            kms_key_id=example_key.key_id)
        example_secret_version = aws.secretsmanager.SecretVersion("example",
            secret_id=example_secret.id,
            secret_string=json.dumps({
                "username": "user",
                "password": "pass",
            }))
        example_scram_secret_association = aws.msk.ScramSecretAssociation("example",
            cluster_arn=example_cluster.arn,
            secret_arn_lists=[example_secret.arn],
            opts = pulumi.ResourceOptions(depends_on=[example_secret_version]))
        example = aws.iam.get_policy_document_output(statements=[{
            "sid": "AWSKafkaResourcePolicy",
            "effect": "Allow",
            "principals": [{
                "type": "Service",
                "identifiers": ["kafka.amazonaws.com"],
            }],
            "actions": ["secretsmanager:getSecretValue"],
            "resources": [example_secret.arn],
        }])
        example_secret_policy = aws.secretsmanager.SecretPolicy("example",
            secret_arn=example_secret.arn,
            policy=example.json)
        ```

        ## Import

        Using `pulumi import`, import MSK SCRAM Secret Associations using the `id`. For example:

        ```sh
        $ pulumi import aws:msk/scramSecretAssociation:ScramSecretAssociation example arn:aws:kafka:us-west-2:123456789012:cluster/example/279c0212-d057-4dba-9aa9-1c4e5a25bfc7-3
        ```

        :param str resource_name: The name of the resource.
        :param ScramSecretAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScramSecretAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_arn: Optional[pulumi.Input[str]] = None,
                 secret_arn_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScramSecretAssociationArgs.__new__(ScramSecretAssociationArgs)

            if cluster_arn is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_arn'")
            __props__.__dict__["cluster_arn"] = cluster_arn
            if secret_arn_lists is None and not opts.urn:
                raise TypeError("Missing required property 'secret_arn_lists'")
            __props__.__dict__["secret_arn_lists"] = secret_arn_lists
        super(ScramSecretAssociation, __self__).__init__(
            'aws:msk/scramSecretAssociation:ScramSecretAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_arn: Optional[pulumi.Input[str]] = None,
            secret_arn_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'ScramSecretAssociation':
        """
        Get an existing ScramSecretAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_arn: Amazon Resource Name (ARN) of the MSK cluster.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] secret_arn_lists: List of AWS Secrets Manager secret ARNs.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ScramSecretAssociationState.__new__(_ScramSecretAssociationState)

        __props__.__dict__["cluster_arn"] = cluster_arn
        __props__.__dict__["secret_arn_lists"] = secret_arn_lists
        return ScramSecretAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the MSK cluster.
        """
        return pulumi.get(self, "cluster_arn")

    @property
    @pulumi.getter(name="secretArnLists")
    def secret_arn_lists(self) -> pulumi.Output[Sequence[str]]:
        """
        List of AWS Secrets Manager secret ARNs.
        """
        return pulumi.get(self, "secret_arn_lists")

