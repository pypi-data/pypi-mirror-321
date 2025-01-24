r'''
# cdk-mentor

This library acts as a mentor to AWS CDK users, providing guidance and suggestions for better infrastructure coding practices. Inspired by [cfn_nag](https://github.com/stelligent/cfn_nag).

![Stability: Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

[![View on Construct Hub](https://constructs.dev/badge?package=cdk-mentor)](https://constructs.dev/packages/cdk-mentor)

## Overview Image

![cdk-mentor-demo](images/cdk-mentor-demo.gif)

This library uses Aspects and is executed during the prepare phase.

![phase](images/cdk-mentor-phase.png)

## Introduction

```bash
% npm install -D cdk-mentor
```

```python
import * as cdk from 'aws-cdk-lib';
import * as sns from 'aws-cdk-lib/aws-sns';
import { TestStack } from '../lib/test-stack';
import { CdkMentor } from 'cdk-mentor';

const app = new cdk.App();
const stack = new TestStack(app, 'TestStack');
cdk.Aspects.of(app).add(new CdkMentor());
```

```python
import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as sns from 'aws-cdk-lib/aws-sns';

export class TestStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    new sns.Topic(this, 'testTopic'); // Construct ID is NOT PascalCase
  }
}
```

```bash
% npx cdk synth -q
[Error at /TestStack/testTopic/Resource] [ERR:001]: Construct ID "testTopic"should be defined in PascalCase.
Found errors
```

## Available Rules

* Recommends PascalCase for Construct IDs
* Avoid `Stack` or `Construct` in Construct IDs
* Detecte strong cross-stack references
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import constructs as _constructs_77d1e7e8


@jsii.implements(_aws_cdk_ceddda9d.IAspect)
class CdkMentor(metaclass=jsii.JSIIMeta, jsii_type="cdk-mentor.CdkMentor"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="visit")
    def visit(self, node: _constructs_77d1e7e8.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__045805137e837d4f428049a0f8490560c47783f8eb5c2da947c2ec960726b5a2)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


__all__ = [
    "CdkMentor",
]

publication.publish()

def _typecheckingstub__045805137e837d4f428049a0f8490560c47783f8eb5c2da947c2ec960726b5a2(
    node: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass
