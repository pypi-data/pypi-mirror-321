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
    'GetContainerRecipeResult',
    'AwaitableGetContainerRecipeResult',
    'get_container_recipe',
    'get_container_recipe_output',
]

@pulumi.output_type
class GetContainerRecipeResult:
    """
    A collection of values returned by getContainerRecipe.
    """
    def __init__(__self__, arn=None, components=None, container_type=None, date_created=None, description=None, dockerfile_template_data=None, encrypted=None, id=None, instance_configurations=None, kms_key_id=None, name=None, owner=None, parent_image=None, platform=None, tags=None, target_repositories=None, version=None, working_directory=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if components and not isinstance(components, list):
            raise TypeError("Expected argument 'components' to be a list")
        pulumi.set(__self__, "components", components)
        if container_type and not isinstance(container_type, str):
            raise TypeError("Expected argument 'container_type' to be a str")
        pulumi.set(__self__, "container_type", container_type)
        if date_created and not isinstance(date_created, str):
            raise TypeError("Expected argument 'date_created' to be a str")
        pulumi.set(__self__, "date_created", date_created)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if dockerfile_template_data and not isinstance(dockerfile_template_data, str):
            raise TypeError("Expected argument 'dockerfile_template_data' to be a str")
        pulumi.set(__self__, "dockerfile_template_data", dockerfile_template_data)
        if encrypted and not isinstance(encrypted, bool):
            raise TypeError("Expected argument 'encrypted' to be a bool")
        pulumi.set(__self__, "encrypted", encrypted)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_configurations and not isinstance(instance_configurations, list):
            raise TypeError("Expected argument 'instance_configurations' to be a list")
        pulumi.set(__self__, "instance_configurations", instance_configurations)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if owner and not isinstance(owner, str):
            raise TypeError("Expected argument 'owner' to be a str")
        pulumi.set(__self__, "owner", owner)
        if parent_image and not isinstance(parent_image, str):
            raise TypeError("Expected argument 'parent_image' to be a str")
        pulumi.set(__self__, "parent_image", parent_image)
        if platform and not isinstance(platform, str):
            raise TypeError("Expected argument 'platform' to be a str")
        pulumi.set(__self__, "platform", platform)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if target_repositories and not isinstance(target_repositories, list):
            raise TypeError("Expected argument 'target_repositories' to be a list")
        pulumi.set(__self__, "target_repositories", target_repositories)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)
        if working_directory and not isinstance(working_directory, str):
            raise TypeError("Expected argument 'working_directory' to be a str")
        pulumi.set(__self__, "working_directory", working_directory)

    @property
    @pulumi.getter
    def arn(self) -> str:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def components(self) -> Sequence['outputs.GetContainerRecipeComponentResult']:
        """
        List of objects with components for the container recipe.
        """
        return pulumi.get(self, "components")

    @property
    @pulumi.getter(name="containerType")
    def container_type(self) -> str:
        """
        Type of the container.
        """
        return pulumi.get(self, "container_type")

    @property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> str:
        """
        Date the container recipe was created.
        """
        return pulumi.get(self, "date_created")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the container recipe.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dockerfileTemplateData")
    def dockerfile_template_data(self) -> str:
        """
        Dockerfile template used to build the image.
        """
        return pulumi.get(self, "dockerfile_template_data")

    @property
    @pulumi.getter
    def encrypted(self) -> bool:
        """
        Whether to encrypt the volume. Defaults to unset, which is the value inherited from the parent image.
        """
        return pulumi.get(self, "encrypted")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceConfigurations")
    def instance_configurations(self) -> Sequence['outputs.GetContainerRecipeInstanceConfigurationResult']:
        """
        List of objects with instance configurations for building and testing container images.
        """
        return pulumi.get(self, "instance_configurations")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> str:
        """
        KMS key used to encrypt the container image.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the container recipe.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> str:
        """
        Owner of the container recipe.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="parentImage")
    def parent_image(self) -> str:
        """
        Base image for the container recipe.
        """
        return pulumi.get(self, "parent_image")

    @property
    @pulumi.getter
    def platform(self) -> str:
        """
        Platform of the container recipe.
        """
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Key-value map of resource tags for the container recipe.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetRepositories")
    def target_repositories(self) -> Sequence['outputs.GetContainerRecipeTargetRepositoryResult']:
        """
        Destination repository for the container image.
        """
        return pulumi.get(self, "target_repositories")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Version of the container recipe.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="workingDirectory")
    def working_directory(self) -> str:
        """
        Working directory used during build and test workflows.
        """
        return pulumi.get(self, "working_directory")


class AwaitableGetContainerRecipeResult(GetContainerRecipeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerRecipeResult(
            arn=self.arn,
            components=self.components,
            container_type=self.container_type,
            date_created=self.date_created,
            description=self.description,
            dockerfile_template_data=self.dockerfile_template_data,
            encrypted=self.encrypted,
            id=self.id,
            instance_configurations=self.instance_configurations,
            kms_key_id=self.kms_key_id,
            name=self.name,
            owner=self.owner,
            parent_image=self.parent_image,
            platform=self.platform,
            tags=self.tags,
            target_repositories=self.target_repositories,
            version=self.version,
            working_directory=self.working_directory)


def get_container_recipe(arn: Optional[str] = None,
                         tags: Optional[Mapping[str, str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContainerRecipeResult:
    """
    Provides details about an Image builder Container Recipe.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.imagebuilder.get_container_recipe(arn="arn:aws:imagebuilder:us-east-1:aws:container-recipe/example/1.0.0")
    ```


    :param str arn: ARN of the container recipe.
    :param Mapping[str, str] tags: Key-value map of resource tags for the container recipe.
    """
    __args__ = dict()
    __args__['arn'] = arn
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:imagebuilder/getContainerRecipe:getContainerRecipe', __args__, opts=opts, typ=GetContainerRecipeResult).value

    return AwaitableGetContainerRecipeResult(
        arn=pulumi.get(__ret__, 'arn'),
        components=pulumi.get(__ret__, 'components'),
        container_type=pulumi.get(__ret__, 'container_type'),
        date_created=pulumi.get(__ret__, 'date_created'),
        description=pulumi.get(__ret__, 'description'),
        dockerfile_template_data=pulumi.get(__ret__, 'dockerfile_template_data'),
        encrypted=pulumi.get(__ret__, 'encrypted'),
        id=pulumi.get(__ret__, 'id'),
        instance_configurations=pulumi.get(__ret__, 'instance_configurations'),
        kms_key_id=pulumi.get(__ret__, 'kms_key_id'),
        name=pulumi.get(__ret__, 'name'),
        owner=pulumi.get(__ret__, 'owner'),
        parent_image=pulumi.get(__ret__, 'parent_image'),
        platform=pulumi.get(__ret__, 'platform'),
        tags=pulumi.get(__ret__, 'tags'),
        target_repositories=pulumi.get(__ret__, 'target_repositories'),
        version=pulumi.get(__ret__, 'version'),
        working_directory=pulumi.get(__ret__, 'working_directory'))
def get_container_recipe_output(arn: Optional[pulumi.Input[str]] = None,
                                tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetContainerRecipeResult]:
    """
    Provides details about an Image builder Container Recipe.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.imagebuilder.get_container_recipe(arn="arn:aws:imagebuilder:us-east-1:aws:container-recipe/example/1.0.0")
    ```


    :param str arn: ARN of the container recipe.
    :param Mapping[str, str] tags: Key-value map of resource tags for the container recipe.
    """
    __args__ = dict()
    __args__['arn'] = arn
    __args__['tags'] = tags
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:imagebuilder/getContainerRecipe:getContainerRecipe', __args__, opts=opts, typ=GetContainerRecipeResult)
    return __ret__.apply(lambda __response__: GetContainerRecipeResult(
        arn=pulumi.get(__response__, 'arn'),
        components=pulumi.get(__response__, 'components'),
        container_type=pulumi.get(__response__, 'container_type'),
        date_created=pulumi.get(__response__, 'date_created'),
        description=pulumi.get(__response__, 'description'),
        dockerfile_template_data=pulumi.get(__response__, 'dockerfile_template_data'),
        encrypted=pulumi.get(__response__, 'encrypted'),
        id=pulumi.get(__response__, 'id'),
        instance_configurations=pulumi.get(__response__, 'instance_configurations'),
        kms_key_id=pulumi.get(__response__, 'kms_key_id'),
        name=pulumi.get(__response__, 'name'),
        owner=pulumi.get(__response__, 'owner'),
        parent_image=pulumi.get(__response__, 'parent_image'),
        platform=pulumi.get(__response__, 'platform'),
        tags=pulumi.get(__response__, 'tags'),
        target_repositories=pulumi.get(__response__, 'target_repositories'),
        version=pulumi.get(__response__, 'version'),
        working_directory=pulumi.get(__response__, 'working_directory')))
