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
from ._enums import *

__all__ = ['ImageArgs', 'Image']

@pulumi.input_type
class ImageArgs:
    def __init__(__self__, *,
                 repository_url: pulumi.Input[str],
                 args: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 builder_version: Optional['BuilderVersion'] = None,
                 cache_from: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 context: Optional[pulumi.Input[str]] = None,
                 dockerfile: Optional[pulumi.Input[str]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 image_tag: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None,
                 registry_id: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Image resource.
        :param pulumi.Input[str] repository_url: Url of the repository
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] args: An optional map of named build-time argument variables to set during the Docker build.  This flag allows you to pass built-time variables that can be accessed like environment variables inside the `RUN` instruction.
        :param 'BuilderVersion' builder_version: The version of the Docker builder.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cache_from: Images to consider as cache sources
        :param pulumi.Input[str] context: Path to a directory to use for the Docker build context, usually the directory in which the Dockerfile resides (although dockerfile may be used to choose a custom location independent of this choice). If not specified, the context defaults to the current working directory; if a relative path is used, it is relative to the current working directory that Pulumi is evaluating.
        :param pulumi.Input[str] dockerfile: dockerfile may be used to override the default Dockerfile name and/or location.  By default, it is assumed to be a file named Dockerfile in the root of the build context.
        :param pulumi.Input[str] image_name: Custom name for the underlying Docker image resource. If omitted, the image tag assigned by the provider will be used
        :param pulumi.Input[str] image_tag: Custom image tag for the resulting docker image. If omitted a random string will be used
        :param pulumi.Input[str] platform: The architecture of the platform you want to build this image for, e.g. `linux/arm64`.
        :param pulumi.Input[str] registry_id: ID of the ECR registry in which to store the image.  If not provided, this will be inferred from the repository URL)
        :param pulumi.Input[str] target: The target of the dockerfile to build
        """
        pulumi.set(__self__, "repository_url", repository_url)
        if args is not None:
            pulumi.set(__self__, "args", args)
        if builder_version is not None:
            pulumi.set(__self__, "builder_version", builder_version)
        if cache_from is not None:
            pulumi.set(__self__, "cache_from", cache_from)
        if context is not None:
            pulumi.set(__self__, "context", context)
        if dockerfile is not None:
            pulumi.set(__self__, "dockerfile", dockerfile)
        if image_name is not None:
            pulumi.set(__self__, "image_name", image_name)
        if image_tag is not None:
            pulumi.set(__self__, "image_tag", image_tag)
        if platform is not None:
            pulumi.set(__self__, "platform", platform)
        if registry_id is not None:
            pulumi.set(__self__, "registry_id", registry_id)
        if target is not None:
            pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Input[str]:
        """
        Url of the repository
        """
        return pulumi.get(self, "repository_url")

    @repository_url.setter
    def repository_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "repository_url", value)

    @property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        An optional map of named build-time argument variables to set during the Docker build.  This flag allows you to pass built-time variables that can be accessed like environment variables inside the `RUN` instruction.
        """
        return pulumi.get(self, "args")

    @args.setter
    def args(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "args", value)

    @property
    @pulumi.getter(name="builderVersion")
    def builder_version(self) -> Optional['BuilderVersion']:
        """
        The version of the Docker builder.
        """
        return pulumi.get(self, "builder_version")

    @builder_version.setter
    def builder_version(self, value: Optional['BuilderVersion']):
        pulumi.set(self, "builder_version", value)

    @property
    @pulumi.getter(name="cacheFrom")
    def cache_from(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Images to consider as cache sources
        """
        return pulumi.get(self, "cache_from")

    @cache_from.setter
    def cache_from(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "cache_from", value)

    @property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[str]]:
        """
        Path to a directory to use for the Docker build context, usually the directory in which the Dockerfile resides (although dockerfile may be used to choose a custom location independent of this choice). If not specified, the context defaults to the current working directory; if a relative path is used, it is relative to the current working directory that Pulumi is evaluating.
        """
        return pulumi.get(self, "context")

    @context.setter
    def context(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "context", value)

    @property
    @pulumi.getter
    def dockerfile(self) -> Optional[pulumi.Input[str]]:
        """
        dockerfile may be used to override the default Dockerfile name and/or location.  By default, it is assumed to be a file named Dockerfile in the root of the build context.
        """
        return pulumi.get(self, "dockerfile")

    @dockerfile.setter
    def dockerfile(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dockerfile", value)

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[str]]:
        """
        Custom name for the underlying Docker image resource. If omitted, the image tag assigned by the provider will be used
        """
        return pulumi.get(self, "image_name")

    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_name", value)

    @property
    @pulumi.getter(name="imageTag")
    def image_tag(self) -> Optional[pulumi.Input[str]]:
        """
        Custom image tag for the resulting docker image. If omitted a random string will be used
        """
        return pulumi.get(self, "image_tag")

    @image_tag.setter
    def image_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_tag", value)

    @property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[str]]:
        """
        The architecture of the platform you want to build this image for, e.g. `linux/arm64`.
        """
        return pulumi.get(self, "platform")

    @platform.setter
    def platform(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "platform", value)

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the ECR registry in which to store the image.  If not provided, this will be inferred from the repository URL)
        """
        return pulumi.get(self, "registry_id")

    @registry_id.setter
    def registry_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registry_id", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        """
        The target of the dockerfile to build
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)


class Image(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 args: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 builder_version: Optional['BuilderVersion'] = None,
                 cache_from: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 context: Optional[pulumi.Input[str]] = None,
                 dockerfile: Optional[pulumi.Input[str]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 image_tag: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None,
                 registry_id: Optional[pulumi.Input[str]] = None,
                 repository_url: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Builds a docker image and pushes to the ECR repository

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] args: An optional map of named build-time argument variables to set during the Docker build.  This flag allows you to pass built-time variables that can be accessed like environment variables inside the `RUN` instruction.
        :param 'BuilderVersion' builder_version: The version of the Docker builder.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cache_from: Images to consider as cache sources
        :param pulumi.Input[str] context: Path to a directory to use for the Docker build context, usually the directory in which the Dockerfile resides (although dockerfile may be used to choose a custom location independent of this choice). If not specified, the context defaults to the current working directory; if a relative path is used, it is relative to the current working directory that Pulumi is evaluating.
        :param pulumi.Input[str] dockerfile: dockerfile may be used to override the default Dockerfile name and/or location.  By default, it is assumed to be a file named Dockerfile in the root of the build context.
        :param pulumi.Input[str] image_name: Custom name for the underlying Docker image resource. If omitted, the image tag assigned by the provider will be used
        :param pulumi.Input[str] image_tag: Custom image tag for the resulting docker image. If omitted a random string will be used
        :param pulumi.Input[str] platform: The architecture of the platform you want to build this image for, e.g. `linux/arm64`.
        :param pulumi.Input[str] registry_id: ID of the ECR registry in which to store the image.  If not provided, this will be inferred from the repository URL)
        :param pulumi.Input[str] repository_url: Url of the repository
        :param pulumi.Input[str] target: The target of the dockerfile to build
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ImageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Builds a docker image and pushes to the ECR repository

        :param str resource_name: The name of the resource.
        :param ImageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ImageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 args: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 builder_version: Optional['BuilderVersion'] = None,
                 cache_from: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 context: Optional[pulumi.Input[str]] = None,
                 dockerfile: Optional[pulumi.Input[str]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 image_tag: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None,
                 registry_id: Optional[pulumi.Input[str]] = None,
                 repository_url: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ImageArgs.__new__(ImageArgs)

            __props__.__dict__["args"] = args
            __props__.__dict__["builder_version"] = builder_version
            __props__.__dict__["cache_from"] = cache_from
            __props__.__dict__["context"] = context
            __props__.__dict__["dockerfile"] = dockerfile
            __props__.__dict__["image_name"] = image_name
            __props__.__dict__["image_tag"] = image_tag
            __props__.__dict__["platform"] = platform
            __props__.__dict__["registry_id"] = registry_id
            if repository_url is None and not opts.urn:
                raise TypeError("Missing required property 'repository_url'")
            __props__.__dict__["repository_url"] = repository_url
            __props__.__dict__["target"] = target
            __props__.__dict__["image_uri"] = None
        super(Image, __self__).__init__(
            'awsx:ecr:Image',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> pulumi.Output[str]:
        """
        Unique identifier of the pushed image
        """
        return pulumi.get(self, "image_uri")

