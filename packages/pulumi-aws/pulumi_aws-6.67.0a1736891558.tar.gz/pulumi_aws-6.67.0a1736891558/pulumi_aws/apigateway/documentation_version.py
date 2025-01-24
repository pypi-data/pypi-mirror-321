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

__all__ = ['DocumentationVersionArgs', 'DocumentationVersion']

@pulumi.input_type
class DocumentationVersionArgs:
    def __init__(__self__, *,
                 rest_api_id: pulumi.Input[str],
                 version: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DocumentationVersion resource.
        :param pulumi.Input[str] rest_api_id: ID of the associated Rest API
        :param pulumi.Input[str] version: Version identifier of the API documentation snapshot.
        :param pulumi.Input[str] description: Description of the API documentation version.
        """
        pulumi.set(__self__, "rest_api_id", rest_api_id)
        pulumi.set(__self__, "version", version)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> pulumi.Input[str]:
        """
        ID of the associated Rest API
        """
        return pulumi.get(self, "rest_api_id")

    @rest_api_id.setter
    def rest_api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "rest_api_id", value)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Input[str]:
        """
        Version identifier of the API documentation snapshot.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[str]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the API documentation version.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class _DocumentationVersionState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 rest_api_id: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DocumentationVersion resources.
        :param pulumi.Input[str] description: Description of the API documentation version.
        :param pulumi.Input[str] rest_api_id: ID of the associated Rest API
        :param pulumi.Input[str] version: Version identifier of the API documentation snapshot.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if rest_api_id is not None:
            pulumi.set(__self__, "rest_api_id", rest_api_id)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the API documentation version.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the associated Rest API
        """
        return pulumi.get(self, "rest_api_id")

    @rest_api_id.setter
    def rest_api_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rest_api_id", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Version identifier of the API documentation snapshot.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class DocumentationVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 rest_api_id: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource to manage an API Gateway Documentation Version.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_rest_api = aws.apigateway.RestApi("example", name="example_api")
        example_documentation_part = aws.apigateway.DocumentationPart("example",
            location={
                "type": "API",
            },
            properties="{\\"description\\":\\"Example\\"}",
            rest_api_id=example_rest_api.id)
        example = aws.apigateway.DocumentationVersion("example",
            version="example_version",
            rest_api_id=example_rest_api.id,
            description="Example description",
            opts = pulumi.ResourceOptions(depends_on=[example_documentation_part]))
        ```

        ## Import

        Using `pulumi import`, import API Gateway documentation versions using `REST-API-ID/VERSION`. For example:

        ```sh
        $ pulumi import aws:apigateway/documentationVersion:DocumentationVersion example 5i4e1ko720/example-version
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the API documentation version.
        :param pulumi.Input[str] rest_api_id: ID of the associated Rest API
        :param pulumi.Input[str] version: Version identifier of the API documentation snapshot.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DocumentationVersionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to manage an API Gateway Documentation Version.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_rest_api = aws.apigateway.RestApi("example", name="example_api")
        example_documentation_part = aws.apigateway.DocumentationPart("example",
            location={
                "type": "API",
            },
            properties="{\\"description\\":\\"Example\\"}",
            rest_api_id=example_rest_api.id)
        example = aws.apigateway.DocumentationVersion("example",
            version="example_version",
            rest_api_id=example_rest_api.id,
            description="Example description",
            opts = pulumi.ResourceOptions(depends_on=[example_documentation_part]))
        ```

        ## Import

        Using `pulumi import`, import API Gateway documentation versions using `REST-API-ID/VERSION`. For example:

        ```sh
        $ pulumi import aws:apigateway/documentationVersion:DocumentationVersion example 5i4e1ko720/example-version
        ```

        :param str resource_name: The name of the resource.
        :param DocumentationVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DocumentationVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 rest_api_id: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DocumentationVersionArgs.__new__(DocumentationVersionArgs)

            __props__.__dict__["description"] = description
            if rest_api_id is None and not opts.urn:
                raise TypeError("Missing required property 'rest_api_id'")
            __props__.__dict__["rest_api_id"] = rest_api_id
            if version is None and not opts.urn:
                raise TypeError("Missing required property 'version'")
            __props__.__dict__["version"] = version
        super(DocumentationVersion, __self__).__init__(
            'aws:apigateway/documentationVersion:DocumentationVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            rest_api_id: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'DocumentationVersion':
        """
        Get an existing DocumentationVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the API documentation version.
        :param pulumi.Input[str] rest_api_id: ID of the associated Rest API
        :param pulumi.Input[str] version: Version identifier of the API documentation snapshot.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DocumentationVersionState.__new__(_DocumentationVersionState)

        __props__.__dict__["description"] = description
        __props__.__dict__["rest_api_id"] = rest_api_id
        __props__.__dict__["version"] = version
        return DocumentationVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the API documentation version.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> pulumi.Output[str]:
        """
        ID of the associated Rest API
        """
        return pulumi.get(self, "rest_api_id")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Version identifier of the API documentation snapshot.
        """
        return pulumi.get(self, "version")

