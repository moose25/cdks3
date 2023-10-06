#!/usr/bin/env python3
from constructs import Construct
from aws_cdk import App, Stack

from cdk_app.cdk_app_stack import HelloCdkStack

app = App()
HelloCdkStack(app, "CdkTestAppCICDContainer")
app.synth()
