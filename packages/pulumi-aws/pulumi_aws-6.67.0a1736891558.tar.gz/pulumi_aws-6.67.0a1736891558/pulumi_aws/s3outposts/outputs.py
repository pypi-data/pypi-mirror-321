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
    'EndpointNetworkInterface',
]

@pulumi.output_type
class EndpointNetworkInterface(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "networkInterfaceId":
            suggest = "network_interface_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EndpointNetworkInterface. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EndpointNetworkInterface.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EndpointNetworkInterface.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 network_interface_id: Optional[str] = None):
        """
        :param str network_interface_id: Identifier of the Elastic Network Interface (ENI).
        """
        if network_interface_id is not None:
            pulumi.set(__self__, "network_interface_id", network_interface_id)

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[str]:
        """
        Identifier of the Elastic Network Interface (ENI).
        """
        return pulumi.get(self, "network_interface_id")


