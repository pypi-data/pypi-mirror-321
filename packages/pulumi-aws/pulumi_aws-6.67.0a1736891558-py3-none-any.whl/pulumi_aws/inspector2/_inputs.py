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

__all__ = [
    'OrganizationConfigurationAutoEnableArgs',
    'OrganizationConfigurationAutoEnableArgsDict',
]

MYPY = False

if not MYPY:
    class OrganizationConfigurationAutoEnableArgsDict(TypedDict):
        ec2: pulumi.Input[bool]
        """
        Whether Amazon EC2 scans are automatically enabled for new members of your Amazon Inspector organization.
        """
        ecr: pulumi.Input[bool]
        """
        Whether Amazon ECR scans are automatically enabled for new members of your Amazon Inspector organization.
        """
        lambda_: NotRequired[pulumi.Input[bool]]
        """
        Whether Lambda Function scans are automatically enabled for new members of your Amazon Inspector organization.
        """
        lambda_code: NotRequired[pulumi.Input[bool]]
        """
        Whether AWS Lambda code scans are automatically enabled for new members of your Amazon Inspector organization. **Note:** Lambda code scanning requires Lambda standard scanning to be activated. Consequently, if you are setting this argument to `true`, you must also set the `lambda` argument to `true`. See [Scanning AWS Lambda functions with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html#lambda-code-scans) for more information.
        """
elif False:
    OrganizationConfigurationAutoEnableArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class OrganizationConfigurationAutoEnableArgs:
    def __init__(__self__, *,
                 ec2: pulumi.Input[bool],
                 ecr: pulumi.Input[bool],
                 lambda_: Optional[pulumi.Input[bool]] = None,
                 lambda_code: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[bool] ec2: Whether Amazon EC2 scans are automatically enabled for new members of your Amazon Inspector organization.
        :param pulumi.Input[bool] ecr: Whether Amazon ECR scans are automatically enabled for new members of your Amazon Inspector organization.
        :param pulumi.Input[bool] lambda_: Whether Lambda Function scans are automatically enabled for new members of your Amazon Inspector organization.
        :param pulumi.Input[bool] lambda_code: Whether AWS Lambda code scans are automatically enabled for new members of your Amazon Inspector organization. **Note:** Lambda code scanning requires Lambda standard scanning to be activated. Consequently, if you are setting this argument to `true`, you must also set the `lambda` argument to `true`. See [Scanning AWS Lambda functions with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html#lambda-code-scans) for more information.
        """
        pulumi.set(__self__, "ec2", ec2)
        pulumi.set(__self__, "ecr", ecr)
        if lambda_ is not None:
            pulumi.set(__self__, "lambda_", lambda_)
        if lambda_code is not None:
            pulumi.set(__self__, "lambda_code", lambda_code)

    @property
    @pulumi.getter
    def ec2(self) -> pulumi.Input[bool]:
        """
        Whether Amazon EC2 scans are automatically enabled for new members of your Amazon Inspector organization.
        """
        return pulumi.get(self, "ec2")

    @ec2.setter
    def ec2(self, value: pulumi.Input[bool]):
        pulumi.set(self, "ec2", value)

    @property
    @pulumi.getter
    def ecr(self) -> pulumi.Input[bool]:
        """
        Whether Amazon ECR scans are automatically enabled for new members of your Amazon Inspector organization.
        """
        return pulumi.get(self, "ecr")

    @ecr.setter
    def ecr(self, value: pulumi.Input[bool]):
        pulumi.set(self, "ecr", value)

    @property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether Lambda Function scans are automatically enabled for new members of your Amazon Inspector organization.
        """
        return pulumi.get(self, "lambda_")

    @lambda_.setter
    def lambda_(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "lambda_", value)

    @property
    @pulumi.getter(name="lambdaCode")
    def lambda_code(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether AWS Lambda code scans are automatically enabled for new members of your Amazon Inspector organization. **Note:** Lambda code scanning requires Lambda standard scanning to be activated. Consequently, if you are setting this argument to `true`, you must also set the `lambda` argument to `true`. See [Scanning AWS Lambda functions with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html#lambda-code-scans) for more information.
        """
        return pulumi.get(self, "lambda_code")

    @lambda_code.setter
    def lambda_code(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "lambda_code", value)


