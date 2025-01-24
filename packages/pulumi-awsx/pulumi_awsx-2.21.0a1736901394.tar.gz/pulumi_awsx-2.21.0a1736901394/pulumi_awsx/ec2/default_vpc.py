# coding=utf-8
# *** WARNING: this file was generated by pulumi-gen-awsx. ***
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

__all__ = ['DefaultVpcArgs', 'DefaultVpc']

@pulumi.input_type
class DefaultVpcArgs:
    def __init__(__self__):
        """
        The set of arguments for constructing a DefaultVpc resource.
        """
        pass


class DefaultVpc(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 __props__=None):
        """
        Pseudo resource representing the default VPC and associated subnets for an account and region. This does not create any resources. This will be replaced with `getDefaultVpc` in the future.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DefaultVpcArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Pseudo resource representing the default VPC and associated subnets for an account and region. This does not create any resources. This will be replaced with `getDefaultVpc` in the future.

        :param str resource_name: The name of the resource.
        :param DefaultVpcArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DefaultVpcArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DefaultVpcArgs.__new__(DefaultVpcArgs)

            __props__.__dict__["private_subnet_ids"] = None
            __props__.__dict__["public_subnet_ids"] = None
            __props__.__dict__["vpc_id"] = None
        super(DefaultVpc, __self__).__init__(
            'awsx:ec2:DefaultVpc',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="privateSubnetIds")
    def private_subnet_ids(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "private_subnet_ids")

    @property
    @pulumi.getter(name="publicSubnetIds")
    def public_subnet_ids(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "public_subnet_ids")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        The VPC ID for the default VPC
        """
        return pulumi.get(self, "vpc_id")

