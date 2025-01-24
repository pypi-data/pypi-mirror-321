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
    'KeyKeyAttributesArgs',
    'KeyKeyAttributesArgsDict',
    'KeyKeyAttributesKeyModesOfUseArgs',
    'KeyKeyAttributesKeyModesOfUseArgsDict',
    'KeyTimeoutsArgs',
    'KeyTimeoutsArgsDict',
]

MYPY = False

if not MYPY:
    class KeyKeyAttributesArgsDict(TypedDict):
        key_algorithm: pulumi.Input[str]
        """
        Key algorithm to be use during creation of an AWS Payment Cryptography key.
        """
        key_class: pulumi.Input[str]
        """
        Type of AWS Payment Cryptography key to create.
        """
        key_usage: pulumi.Input[str]
        """
        Cryptographic usage of an AWS Payment Cryptography key as defined in section A.5.2 of the TR-31 spec.
        """
        key_modes_of_use: NotRequired[pulumi.Input['KeyKeyAttributesKeyModesOfUseArgsDict']]
        """
        List of cryptographic operations that you can perform using the key.
        """
elif False:
    KeyKeyAttributesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class KeyKeyAttributesArgs:
    def __init__(__self__, *,
                 key_algorithm: pulumi.Input[str],
                 key_class: pulumi.Input[str],
                 key_usage: pulumi.Input[str],
                 key_modes_of_use: Optional[pulumi.Input['KeyKeyAttributesKeyModesOfUseArgs']] = None):
        """
        :param pulumi.Input[str] key_algorithm: Key algorithm to be use during creation of an AWS Payment Cryptography key.
        :param pulumi.Input[str] key_class: Type of AWS Payment Cryptography key to create.
        :param pulumi.Input[str] key_usage: Cryptographic usage of an AWS Payment Cryptography key as defined in section A.5.2 of the TR-31 spec.
        :param pulumi.Input['KeyKeyAttributesKeyModesOfUseArgs'] key_modes_of_use: List of cryptographic operations that you can perform using the key.
        """
        pulumi.set(__self__, "key_algorithm", key_algorithm)
        pulumi.set(__self__, "key_class", key_class)
        pulumi.set(__self__, "key_usage", key_usage)
        if key_modes_of_use is not None:
            pulumi.set(__self__, "key_modes_of_use", key_modes_of_use)

    @property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> pulumi.Input[str]:
        """
        Key algorithm to be use during creation of an AWS Payment Cryptography key.
        """
        return pulumi.get(self, "key_algorithm")

    @key_algorithm.setter
    def key_algorithm(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_algorithm", value)

    @property
    @pulumi.getter(name="keyClass")
    def key_class(self) -> pulumi.Input[str]:
        """
        Type of AWS Payment Cryptography key to create.
        """
        return pulumi.get(self, "key_class")

    @key_class.setter
    def key_class(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_class", value)

    @property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> pulumi.Input[str]:
        """
        Cryptographic usage of an AWS Payment Cryptography key as defined in section A.5.2 of the TR-31 spec.
        """
        return pulumi.get(self, "key_usage")

    @key_usage.setter
    def key_usage(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_usage", value)

    @property
    @pulumi.getter(name="keyModesOfUse")
    def key_modes_of_use(self) -> Optional[pulumi.Input['KeyKeyAttributesKeyModesOfUseArgs']]:
        """
        List of cryptographic operations that you can perform using the key.
        """
        return pulumi.get(self, "key_modes_of_use")

    @key_modes_of_use.setter
    def key_modes_of_use(self, value: Optional[pulumi.Input['KeyKeyAttributesKeyModesOfUseArgs']]):
        pulumi.set(self, "key_modes_of_use", value)


if not MYPY:
    class KeyKeyAttributesKeyModesOfUseArgsDict(TypedDict):
        decrypt: NotRequired[pulumi.Input[bool]]
        """
        Whether an AWS Payment Cryptography key can be used to decrypt data.
        """
        derive_key: NotRequired[pulumi.Input[bool]]
        """
        Whether an AWS Payment Cryptography key can be used to derive new keys.
        """
        encrypt: NotRequired[pulumi.Input[bool]]
        """
        Whether an AWS Payment Cryptography key can be used to encrypt data.
        """
        generate: NotRequired[pulumi.Input[bool]]
        """
        Whether an AWS Payment Cryptography key can be used to generate and verify other card and PIN verification keys.
        """
        no_restrictions: NotRequired[pulumi.Input[bool]]
        """
        Whether an AWS Payment Cryptography key has no special restrictions other than the restrictions implied by KeyUsage.
        """
        sign: NotRequired[pulumi.Input[bool]]
        """
        Whether an AWS Payment Cryptography key can be used for signing.
        """
        unwrap: NotRequired[pulumi.Input[bool]]
        """
        Whether an AWS Payment Cryptography key can be used to unwrap other keys.
        """
        verify: NotRequired[pulumi.Input[bool]]
        """
        Whether an AWS Payment Cryptography key can be used to verify signatures.
        """
        wrap: NotRequired[pulumi.Input[bool]]
        """
        Whether an AWS Payment Cryptography key can be used to wrap other keys.
        """
elif False:
    KeyKeyAttributesKeyModesOfUseArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class KeyKeyAttributesKeyModesOfUseArgs:
    def __init__(__self__, *,
                 decrypt: Optional[pulumi.Input[bool]] = None,
                 derive_key: Optional[pulumi.Input[bool]] = None,
                 encrypt: Optional[pulumi.Input[bool]] = None,
                 generate: Optional[pulumi.Input[bool]] = None,
                 no_restrictions: Optional[pulumi.Input[bool]] = None,
                 sign: Optional[pulumi.Input[bool]] = None,
                 unwrap: Optional[pulumi.Input[bool]] = None,
                 verify: Optional[pulumi.Input[bool]] = None,
                 wrap: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[bool] decrypt: Whether an AWS Payment Cryptography key can be used to decrypt data.
        :param pulumi.Input[bool] derive_key: Whether an AWS Payment Cryptography key can be used to derive new keys.
        :param pulumi.Input[bool] encrypt: Whether an AWS Payment Cryptography key can be used to encrypt data.
        :param pulumi.Input[bool] generate: Whether an AWS Payment Cryptography key can be used to generate and verify other card and PIN verification keys.
        :param pulumi.Input[bool] no_restrictions: Whether an AWS Payment Cryptography key has no special restrictions other than the restrictions implied by KeyUsage.
        :param pulumi.Input[bool] sign: Whether an AWS Payment Cryptography key can be used for signing.
        :param pulumi.Input[bool] unwrap: Whether an AWS Payment Cryptography key can be used to unwrap other keys.
        :param pulumi.Input[bool] verify: Whether an AWS Payment Cryptography key can be used to verify signatures.
        :param pulumi.Input[bool] wrap: Whether an AWS Payment Cryptography key can be used to wrap other keys.
        """
        if decrypt is not None:
            pulumi.set(__self__, "decrypt", decrypt)
        if derive_key is not None:
            pulumi.set(__self__, "derive_key", derive_key)
        if encrypt is not None:
            pulumi.set(__self__, "encrypt", encrypt)
        if generate is not None:
            pulumi.set(__self__, "generate", generate)
        if no_restrictions is not None:
            pulumi.set(__self__, "no_restrictions", no_restrictions)
        if sign is not None:
            pulumi.set(__self__, "sign", sign)
        if unwrap is not None:
            pulumi.set(__self__, "unwrap", unwrap)
        if verify is not None:
            pulumi.set(__self__, "verify", verify)
        if wrap is not None:
            pulumi.set(__self__, "wrap", wrap)

    @property
    @pulumi.getter
    def decrypt(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether an AWS Payment Cryptography key can be used to decrypt data.
        """
        return pulumi.get(self, "decrypt")

    @decrypt.setter
    def decrypt(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "decrypt", value)

    @property
    @pulumi.getter(name="deriveKey")
    def derive_key(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether an AWS Payment Cryptography key can be used to derive new keys.
        """
        return pulumi.get(self, "derive_key")

    @derive_key.setter
    def derive_key(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "derive_key", value)

    @property
    @pulumi.getter
    def encrypt(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether an AWS Payment Cryptography key can be used to encrypt data.
        """
        return pulumi.get(self, "encrypt")

    @encrypt.setter
    def encrypt(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "encrypt", value)

    @property
    @pulumi.getter
    def generate(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether an AWS Payment Cryptography key can be used to generate and verify other card and PIN verification keys.
        """
        return pulumi.get(self, "generate")

    @generate.setter
    def generate(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "generate", value)

    @property
    @pulumi.getter(name="noRestrictions")
    def no_restrictions(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether an AWS Payment Cryptography key has no special restrictions other than the restrictions implied by KeyUsage.
        """
        return pulumi.get(self, "no_restrictions")

    @no_restrictions.setter
    def no_restrictions(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "no_restrictions", value)

    @property
    @pulumi.getter
    def sign(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether an AWS Payment Cryptography key can be used for signing.
        """
        return pulumi.get(self, "sign")

    @sign.setter
    def sign(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sign", value)

    @property
    @pulumi.getter
    def unwrap(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether an AWS Payment Cryptography key can be used to unwrap other keys.
        """
        return pulumi.get(self, "unwrap")

    @unwrap.setter
    def unwrap(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "unwrap", value)

    @property
    @pulumi.getter
    def verify(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether an AWS Payment Cryptography key can be used to verify signatures.
        """
        return pulumi.get(self, "verify")

    @verify.setter
    def verify(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "verify", value)

    @property
    @pulumi.getter
    def wrap(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether an AWS Payment Cryptography key can be used to wrap other keys.
        """
        return pulumi.get(self, "wrap")

    @wrap.setter
    def wrap(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "wrap", value)


if not MYPY:
    class KeyTimeoutsArgsDict(TypedDict):
        create: NotRequired[pulumi.Input[str]]
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        delete: NotRequired[pulumi.Input[str]]
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Setting a timeout for a Delete operation is only applicable if changes are saved into state before the destroy operation occurs.
        """
        update: NotRequired[pulumi.Input[str]]
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
elif False:
    KeyTimeoutsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class KeyTimeoutsArgs:
    def __init__(__self__, *,
                 create: Optional[pulumi.Input[str]] = None,
                 delete: Optional[pulumi.Input[str]] = None,
                 update: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] create: A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        :param pulumi.Input[str] delete: A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Setting a timeout for a Delete operation is only applicable if changes are saved into state before the destroy operation occurs.
        :param pulumi.Input[str] update: A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        if create is not None:
            pulumi.set(__self__, "create", create)
        if delete is not None:
            pulumi.set(__self__, "delete", delete)
        if update is not None:
            pulumi.set(__self__, "update", update)

    @property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[str]]:
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        return pulumi.get(self, "create")

    @create.setter
    def create(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create", value)

    @property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[str]]:
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Setting a timeout for a Delete operation is only applicable if changes are saved into state before the destroy operation occurs.
        """
        return pulumi.get(self, "delete")

    @delete.setter
    def delete(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delete", value)

    @property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[str]]:
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        return pulumi.get(self, "update")

    @update.setter
    def update(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update", value)


