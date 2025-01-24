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

__all__ = ['RegexPatternSetArgs', 'RegexPatternSet']

@pulumi.input_type
class RegexPatternSetArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 regex_pattern_strings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a RegexPatternSet resource.
        :param pulumi.Input[str] name: The name or description of the Regex Pattern Set.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regex_pattern_strings: A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if regex_pattern_strings is not None:
            pulumi.set(__self__, "regex_pattern_strings", regex_pattern_strings)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name or description of the Regex Pattern Set.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="regexPatternStrings")
    def regex_pattern_strings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.
        """
        return pulumi.get(self, "regex_pattern_strings")

    @regex_pattern_strings.setter
    def regex_pattern_strings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "regex_pattern_strings", value)


@pulumi.input_type
class _RegexPatternSetState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 regex_pattern_strings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering RegexPatternSet resources.
        :param pulumi.Input[str] name: The name or description of the Regex Pattern Set.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regex_pattern_strings: A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if regex_pattern_strings is not None:
            pulumi.set(__self__, "regex_pattern_strings", regex_pattern_strings)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name or description of the Regex Pattern Set.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="regexPatternStrings")
    def regex_pattern_strings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.
        """
        return pulumi.get(self, "regex_pattern_strings")

    @regex_pattern_strings.setter
    def regex_pattern_strings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "regex_pattern_strings", value)


class RegexPatternSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regex_pattern_strings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a WAF Regional Regex Pattern Set Resource

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.wafregional.RegexPatternSet("example",
            name="example",
            regex_pattern_strings=[
                "one",
                "two",
            ])
        ```

        ## Import

        Using `pulumi import`, import WAF Regional Regex Pattern Set using the id. For example:

        ```sh
        $ pulumi import aws:wafregional/regexPatternSet:RegexPatternSet example a1b2c3d4-d5f6-7777-8888-9999aaaabbbbcccc
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name or description of the Regex Pattern Set.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regex_pattern_strings: A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[RegexPatternSetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a WAF Regional Regex Pattern Set Resource

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.wafregional.RegexPatternSet("example",
            name="example",
            regex_pattern_strings=[
                "one",
                "two",
            ])
        ```

        ## Import

        Using `pulumi import`, import WAF Regional Regex Pattern Set using the id. For example:

        ```sh
        $ pulumi import aws:wafregional/regexPatternSet:RegexPatternSet example a1b2c3d4-d5f6-7777-8888-9999aaaabbbbcccc
        ```

        :param str resource_name: The name of the resource.
        :param RegexPatternSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegexPatternSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regex_pattern_strings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RegexPatternSetArgs.__new__(RegexPatternSetArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["regex_pattern_strings"] = regex_pattern_strings
        super(RegexPatternSet, __self__).__init__(
            'aws:wafregional/regexPatternSet:RegexPatternSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            regex_pattern_strings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'RegexPatternSet':
        """
        Get an existing RegexPatternSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name or description of the Regex Pattern Set.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regex_pattern_strings: A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RegexPatternSetState.__new__(_RegexPatternSetState)

        __props__.__dict__["name"] = name
        __props__.__dict__["regex_pattern_strings"] = regex_pattern_strings
        return RegexPatternSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name or description of the Regex Pattern Set.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="regexPatternStrings")
    def regex_pattern_strings(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.
        """
        return pulumi.get(self, "regex_pattern_strings")

