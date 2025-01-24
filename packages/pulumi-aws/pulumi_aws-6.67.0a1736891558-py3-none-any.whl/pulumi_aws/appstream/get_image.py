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
    'GetImageResult',
    'AwaitableGetImageResult',
    'get_image',
    'get_image_output',
]

@pulumi.output_type
class GetImageResult:
    """
    A collection of values returned by getImage.
    """
    def __init__(__self__, applications=None, appstream_agent_version=None, arn=None, base_image_arn=None, created_time=None, description=None, display_name=None, id=None, image_builder_name=None, image_builder_supported=None, image_permissions=None, most_recent=None, name=None, name_regex=None, platform=None, public_base_image_released_date=None, state=None, state_change_reasons=None, type=None):
        if applications and not isinstance(applications, list):
            raise TypeError("Expected argument 'applications' to be a list")
        pulumi.set(__self__, "applications", applications)
        if appstream_agent_version and not isinstance(appstream_agent_version, str):
            raise TypeError("Expected argument 'appstream_agent_version' to be a str")
        pulumi.set(__self__, "appstream_agent_version", appstream_agent_version)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if base_image_arn and not isinstance(base_image_arn, str):
            raise TypeError("Expected argument 'base_image_arn' to be a str")
        pulumi.set(__self__, "base_image_arn", base_image_arn)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_builder_name and not isinstance(image_builder_name, str):
            raise TypeError("Expected argument 'image_builder_name' to be a str")
        pulumi.set(__self__, "image_builder_name", image_builder_name)
        if image_builder_supported and not isinstance(image_builder_supported, bool):
            raise TypeError("Expected argument 'image_builder_supported' to be a bool")
        pulumi.set(__self__, "image_builder_supported", image_builder_supported)
        if image_permissions and not isinstance(image_permissions, list):
            raise TypeError("Expected argument 'image_permissions' to be a list")
        pulumi.set(__self__, "image_permissions", image_permissions)
        if most_recent and not isinstance(most_recent, bool):
            raise TypeError("Expected argument 'most_recent' to be a bool")
        pulumi.set(__self__, "most_recent", most_recent)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if platform and not isinstance(platform, str):
            raise TypeError("Expected argument 'platform' to be a str")
        pulumi.set(__self__, "platform", platform)
        if public_base_image_released_date and not isinstance(public_base_image_released_date, str):
            raise TypeError("Expected argument 'public_base_image_released_date' to be a str")
        pulumi.set(__self__, "public_base_image_released_date", public_base_image_released_date)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if state_change_reasons and not isinstance(state_change_reasons, list):
            raise TypeError("Expected argument 'state_change_reasons' to be a list")
        pulumi.set(__self__, "state_change_reasons", state_change_reasons)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def applications(self) -> Sequence['outputs.GetImageApplicationResult']:
        return pulumi.get(self, "applications")

    @property
    @pulumi.getter(name="appstreamAgentVersion")
    def appstream_agent_version(self) -> str:
        """
        Version of the AppStream 2.0 agent to use for instances that are launched from this image. Has a maximum length of 100 characters.
        """
        return pulumi.get(self, "appstream_agent_version")

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the image.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="baseImageArn")
    def base_image_arn(self) -> str:
        """
        ARN of the image from which the image was created.
        """
        return pulumi.get(self, "base_image_arn")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> str:
        """
        Time at which this image was created.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of image.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Image name to display.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageBuilderName")
    def image_builder_name(self) -> str:
        """
        The name of the image builder that was used to created the private image. If the image is sharedthen the value is null.
        """
        return pulumi.get(self, "image_builder_name")

    @property
    @pulumi.getter(name="imageBuilderSupported")
    def image_builder_supported(self) -> bool:
        """
        Boolean to indicate whether an image builder can be launched from this image.
        * `image error` - Resource error object that describes the error containing the following:
        """
        return pulumi.get(self, "image_builder_supported")

    @property
    @pulumi.getter(name="imagePermissions")
    def image_permissions(self) -> Sequence['outputs.GetImageImagePermissionResult']:
        """
        List of strings describing the image permissions containing the following:
        """
        return pulumi.get(self, "image_permissions")

    @property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[bool]:
        return pulumi.get(self, "most_recent")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def platform(self) -> str:
        """
        Operating system platform of the image. Values will be from: WINDOWS | WINDOWS_SERVER_2016 | WINDOWS_SERVER_2019 | WINDOWS_SERVER_2022 | AMAZON_LINUX2
        """
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter(name="publicBaseImageReleasedDate")
    def public_base_image_released_date(self) -> str:
        return pulumi.get(self, "public_base_image_released_date")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Current state of image. Image starts in PENDING state which changes to AVAILABLE if creation passes and FAILED if it fails. Values will be from: PENDING | AVAILABLE | FAILED | COPYING | DELETING | CREATING | IMPORTING.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateChangeReasons")
    def state_change_reasons(self) -> Sequence['outputs.GetImageStateChangeReasonResult']:
        return pulumi.get(self, "state_change_reasons")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")


class AwaitableGetImageResult(GetImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImageResult(
            applications=self.applications,
            appstream_agent_version=self.appstream_agent_version,
            arn=self.arn,
            base_image_arn=self.base_image_arn,
            created_time=self.created_time,
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            image_builder_name=self.image_builder_name,
            image_builder_supported=self.image_builder_supported,
            image_permissions=self.image_permissions,
            most_recent=self.most_recent,
            name=self.name,
            name_regex=self.name_regex,
            platform=self.platform,
            public_base_image_released_date=self.public_base_image_released_date,
            state=self.state,
            state_change_reasons=self.state_change_reasons,
            type=self.type)


def get_image(arn: Optional[str] = None,
              most_recent: Optional[bool] = None,
              name: Optional[str] = None,
              name_regex: Optional[str] = None,
              type: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetImageResult:
    """
    Data source for managing an AWS AppStream 2.0 Image.


    :param str arn: Arn of the image being searched for. Cannot be used with name_regex or name.
    :param bool most_recent: Boolean that if it is set to true and there are multiple images returned the most recent will be returned. If it is set to false and there are multiple images return the datasource will error.
    :param str name: Name of the image being searched for. Cannot be used with name_regex or arn.
    :param str name_regex: Regular expression name of the image being searched for. Cannot be used with arn or name.
    :param str type: The type of image which must be (PUBLIC, PRIVATE, or SHARED).
    """
    __args__ = dict()
    __args__['arn'] = arn
    __args__['mostRecent'] = most_recent
    __args__['name'] = name
    __args__['nameRegex'] = name_regex
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:appstream/getImage:getImage', __args__, opts=opts, typ=GetImageResult).value

    return AwaitableGetImageResult(
        applications=pulumi.get(__ret__, 'applications'),
        appstream_agent_version=pulumi.get(__ret__, 'appstream_agent_version'),
        arn=pulumi.get(__ret__, 'arn'),
        base_image_arn=pulumi.get(__ret__, 'base_image_arn'),
        created_time=pulumi.get(__ret__, 'created_time'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        image_builder_name=pulumi.get(__ret__, 'image_builder_name'),
        image_builder_supported=pulumi.get(__ret__, 'image_builder_supported'),
        image_permissions=pulumi.get(__ret__, 'image_permissions'),
        most_recent=pulumi.get(__ret__, 'most_recent'),
        name=pulumi.get(__ret__, 'name'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        platform=pulumi.get(__ret__, 'platform'),
        public_base_image_released_date=pulumi.get(__ret__, 'public_base_image_released_date'),
        state=pulumi.get(__ret__, 'state'),
        state_change_reasons=pulumi.get(__ret__, 'state_change_reasons'),
        type=pulumi.get(__ret__, 'type'))
def get_image_output(arn: Optional[pulumi.Input[Optional[str]]] = None,
                     most_recent: Optional[pulumi.Input[Optional[bool]]] = None,
                     name: Optional[pulumi.Input[Optional[str]]] = None,
                     name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                     type: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetImageResult]:
    """
    Data source for managing an AWS AppStream 2.0 Image.


    :param str arn: Arn of the image being searched for. Cannot be used with name_regex or name.
    :param bool most_recent: Boolean that if it is set to true and there are multiple images returned the most recent will be returned. If it is set to false and there are multiple images return the datasource will error.
    :param str name: Name of the image being searched for. Cannot be used with name_regex or arn.
    :param str name_regex: Regular expression name of the image being searched for. Cannot be used with arn or name.
    :param str type: The type of image which must be (PUBLIC, PRIVATE, or SHARED).
    """
    __args__ = dict()
    __args__['arn'] = arn
    __args__['mostRecent'] = most_recent
    __args__['name'] = name
    __args__['nameRegex'] = name_regex
    __args__['type'] = type
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:appstream/getImage:getImage', __args__, opts=opts, typ=GetImageResult)
    return __ret__.apply(lambda __response__: GetImageResult(
        applications=pulumi.get(__response__, 'applications'),
        appstream_agent_version=pulumi.get(__response__, 'appstream_agent_version'),
        arn=pulumi.get(__response__, 'arn'),
        base_image_arn=pulumi.get(__response__, 'base_image_arn'),
        created_time=pulumi.get(__response__, 'created_time'),
        description=pulumi.get(__response__, 'description'),
        display_name=pulumi.get(__response__, 'display_name'),
        id=pulumi.get(__response__, 'id'),
        image_builder_name=pulumi.get(__response__, 'image_builder_name'),
        image_builder_supported=pulumi.get(__response__, 'image_builder_supported'),
        image_permissions=pulumi.get(__response__, 'image_permissions'),
        most_recent=pulumi.get(__response__, 'most_recent'),
        name=pulumi.get(__response__, 'name'),
        name_regex=pulumi.get(__response__, 'name_regex'),
        platform=pulumi.get(__response__, 'platform'),
        public_base_image_released_date=pulumi.get(__response__, 'public_base_image_released_date'),
        state=pulumi.get(__response__, 'state'),
        state_change_reasons=pulumi.get(__response__, 'state_change_reasons'),
        type=pulumi.get(__response__, 'type')))
