#!/usr/bin/env python3
from aws_cdk import core

from cdk_app.cdk_app_stack import HelloCdkStack

app = core.App()
HelloCdkStack(app, "CdkTestAppCICDContainer")
app.synth()
