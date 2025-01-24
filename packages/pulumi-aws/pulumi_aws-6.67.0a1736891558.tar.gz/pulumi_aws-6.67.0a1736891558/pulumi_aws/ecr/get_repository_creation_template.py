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
    'GetRepositoryCreationTemplateResult',
    'AwaitableGetRepositoryCreationTemplateResult',
    'get_repository_creation_template',
    'get_repository_creation_template_output',
]

@pulumi.output_type
class GetRepositoryCreationTemplateResult:
    """
    A collection of values returned by getRepositoryCreationTemplate.
    """
    def __init__(__self__, applied_fors=None, custom_role_arn=None, description=None, encryption_configurations=None, id=None, image_tag_mutability=None, lifecycle_policy=None, prefix=None, registry_id=None, repository_policy=None, resource_tags=None):
        if applied_fors and not isinstance(applied_fors, list):
            raise TypeError("Expected argument 'applied_fors' to be a list")
        pulumi.set(__self__, "applied_fors", applied_fors)
        if custom_role_arn and not isinstance(custom_role_arn, str):
            raise TypeError("Expected argument 'custom_role_arn' to be a str")
        pulumi.set(__self__, "custom_role_arn", custom_role_arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if encryption_configurations and not isinstance(encryption_configurations, list):
            raise TypeError("Expected argument 'encryption_configurations' to be a list")
        pulumi.set(__self__, "encryption_configurations", encryption_configurations)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_tag_mutability and not isinstance(image_tag_mutability, str):
            raise TypeError("Expected argument 'image_tag_mutability' to be a str")
        pulumi.set(__self__, "image_tag_mutability", image_tag_mutability)
        if lifecycle_policy and not isinstance(lifecycle_policy, str):
            raise TypeError("Expected argument 'lifecycle_policy' to be a str")
        pulumi.set(__self__, "lifecycle_policy", lifecycle_policy)
        if prefix and not isinstance(prefix, str):
            raise TypeError("Expected argument 'prefix' to be a str")
        pulumi.set(__self__, "prefix", prefix)
        if registry_id and not isinstance(registry_id, str):
            raise TypeError("Expected argument 'registry_id' to be a str")
        pulumi.set(__self__, "registry_id", registry_id)
        if repository_policy and not isinstance(repository_policy, str):
            raise TypeError("Expected argument 'repository_policy' to be a str")
        pulumi.set(__self__, "repository_policy", repository_policy)
        if resource_tags and not isinstance(resource_tags, dict):
            raise TypeError("Expected argument 'resource_tags' to be a dict")
        pulumi.set(__self__, "resource_tags", resource_tags)

    @property
    @pulumi.getter(name="appliedFors")
    def applied_fors(self) -> Sequence[str]:
        """
        Which features this template applies to. Contains one or more of `PULL_THROUGH_CACHE` or `REPLICATION`.
        """
        return pulumi.get(self, "applied_fors")

    @property
    @pulumi.getter(name="customRoleArn")
    def custom_role_arn(self) -> str:
        """
        The ARN of the custom role used for repository creation.
        """
        return pulumi.get(self, "custom_role_arn")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description for this template.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(self) -> Sequence['outputs.GetRepositoryCreationTemplateEncryptionConfigurationResult']:
        """
        Encryption configuration for any created repositories. See Encryption Configuration below.
        """
        return pulumi.get(self, "encryption_configurations")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageTagMutability")
    def image_tag_mutability(self) -> str:
        """
        The tag mutability setting for any created repositories.
        """
        return pulumi.get(self, "image_tag_mutability")

    @property
    @pulumi.getter(name="lifecyclePolicy")
    def lifecycle_policy(self) -> str:
        """
        The lifecycle policy document to apply to any created repositories.
        """
        return pulumi.get(self, "lifecycle_policy")

    @property
    @pulumi.getter
    def prefix(self) -> str:
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> str:
        """
        The registry ID the repository creation template applies to.
        """
        return pulumi.get(self, "registry_id")

    @property
    @pulumi.getter(name="repositoryPolicy")
    def repository_policy(self) -> str:
        """
        The registry policy document to apply to any created repositories.
        """
        return pulumi.get(self, "repository_policy")

    @property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Mapping[str, str]:
        """
        A map of tags to assign to any created repositories.
        """
        return pulumi.get(self, "resource_tags")


class AwaitableGetRepositoryCreationTemplateResult(GetRepositoryCreationTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRepositoryCreationTemplateResult(
            applied_fors=self.applied_fors,
            custom_role_arn=self.custom_role_arn,
            description=self.description,
            encryption_configurations=self.encryption_configurations,
            id=self.id,
            image_tag_mutability=self.image_tag_mutability,
            lifecycle_policy=self.lifecycle_policy,
            prefix=self.prefix,
            registry_id=self.registry_id,
            repository_policy=self.repository_policy,
            resource_tags=self.resource_tags)


def get_repository_creation_template(prefix: Optional[str] = None,
                                     resource_tags: Optional[Mapping[str, str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRepositoryCreationTemplateResult:
    """
    The ECR Repository Creation Template data source allows the template details to be retrieved for a Repository Creation Template.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ecr.get_repository_creation_template(prefix="example")
    ```


    :param str prefix: The repository name prefix that the template matches against.
    :param Mapping[str, str] resource_tags: A map of tags to assign to any created repositories.
    """
    __args__ = dict()
    __args__['prefix'] = prefix
    __args__['resourceTags'] = resource_tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:ecr/getRepositoryCreationTemplate:getRepositoryCreationTemplate', __args__, opts=opts, typ=GetRepositoryCreationTemplateResult).value

    return AwaitableGetRepositoryCreationTemplateResult(
        applied_fors=pulumi.get(__ret__, 'applied_fors'),
        custom_role_arn=pulumi.get(__ret__, 'custom_role_arn'),
        description=pulumi.get(__ret__, 'description'),
        encryption_configurations=pulumi.get(__ret__, 'encryption_configurations'),
        id=pulumi.get(__ret__, 'id'),
        image_tag_mutability=pulumi.get(__ret__, 'image_tag_mutability'),
        lifecycle_policy=pulumi.get(__ret__, 'lifecycle_policy'),
        prefix=pulumi.get(__ret__, 'prefix'),
        registry_id=pulumi.get(__ret__, 'registry_id'),
        repository_policy=pulumi.get(__ret__, 'repository_policy'),
        resource_tags=pulumi.get(__ret__, 'resource_tags'))
def get_repository_creation_template_output(prefix: Optional[pulumi.Input[str]] = None,
                                            resource_tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                            opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetRepositoryCreationTemplateResult]:
    """
    The ECR Repository Creation Template data source allows the template details to be retrieved for a Repository Creation Template.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ecr.get_repository_creation_template(prefix="example")
    ```


    :param str prefix: The repository name prefix that the template matches against.
    :param Mapping[str, str] resource_tags: A map of tags to assign to any created repositories.
    """
    __args__ = dict()
    __args__['prefix'] = prefix
    __args__['resourceTags'] = resource_tags
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:ecr/getRepositoryCreationTemplate:getRepositoryCreationTemplate', __args__, opts=opts, typ=GetRepositoryCreationTemplateResult)
    return __ret__.apply(lambda __response__: GetRepositoryCreationTemplateResult(
        applied_fors=pulumi.get(__response__, 'applied_fors'),
        custom_role_arn=pulumi.get(__response__, 'custom_role_arn'),
        description=pulumi.get(__response__, 'description'),
        encryption_configurations=pulumi.get(__response__, 'encryption_configurations'),
        id=pulumi.get(__response__, 'id'),
        image_tag_mutability=pulumi.get(__response__, 'image_tag_mutability'),
        lifecycle_policy=pulumi.get(__response__, 'lifecycle_policy'),
        prefix=pulumi.get(__response__, 'prefix'),
        registry_id=pulumi.get(__response__, 'registry_id'),
        repository_policy=pulumi.get(__response__, 'repository_policy'),
        resource_tags=pulumi.get(__response__, 'resource_tags')))
